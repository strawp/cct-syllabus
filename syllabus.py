#!/env/python

import re, json, argparse, sys

infile = 'crest-cct-technical-syllabus-v2.2.md'

data = {
  'meta': {},
  'structure': {}
}

frontmatter = False
topic = ''
skill = ''
linenum = 0
debug = False
skillmeta = False

with open( infile, 'r' ) as f:
  for line in f.read().splitlines():
    linenum+=1
    if debug: print( '"' + line + '"' )

    # Is this a frontmatter block?
    if linenum == 1 and line == '---':
      frontmatter = True
      if debug: print('Frontmatter started')
      continue

    # Handle frontmatter
    if frontmatter:
      
      # End frontmatter
      if line == '---':
        frontmatter = False
        if debug: print('Frontmatter ended')
        continue

      # Parse the actual variable
      m = re.search(r'^([^:]+) *: *(.+)',line)
      if m:
        data['meta'][m.group(1)] = m.group(2)
        if debug: print('Frontmatter variable')
        continue

    # Topic change
    m = re.search(r'^## Appendix (.+)', line)
    if m:
      topic = m.group(1)
      skill = ''
      if debug: print(topic) 
      data['structure'][topic] = {}
      continue

    if topic == '': continue
    
    # Skill change
    m = re.search(r'^### ([A-Z][0-9]+):? (.+)', line)
    if m:
      skillmeta = True
      skill = m.group(1) + ': ' + m.group(2)
      if debug: print(topic, skill)
      data['structure'][topic][skill] = {'details':'','how_examined':{},'notes':'','meta':{}}
      continue

    if skill == '': continue

    # Skill metadata
    m = re.search(r'^ ?- ([a-z_0-9]+):([a-z0-9_, ]+)$', line, re.I)
    if m and skillmeta:
      if m.group(1) in ['ICE','ACE']:
        k = 'how_examined'
      else:
        k = 'meta'
      if ',' in m.group(2): v = [x.strip() for x in m.group(2).split(',')]
      else: v = m.group(2).strip()
      data['structure'][topic][skill][k][m.group(1).lower()] = v
      continue

    if len(line.strip()) > 0: skillmeta = False

    # Details
    m = re.search(r'^> *(.*)', line)
    if m:
      data['structure'][topic][skill]['details'] += '\n' + m.group(1)
      continue

    # Anything else is revision notes added in
    if topic != '' and skill != '':
      data['structure'][topic][skill]['notes'] += line + '\n'

topicletters = [x[0] for x in data['structure'].keys()]

parser = argparse.ArgumentParser(
  description="A CLI front end for the CREST CCT Syllabus",
  epilog="You can also use the name of any metadata field as an argument and these will be used to regex match against items with that value.\n\n e.g. if you have ` - confidence: 3` as one metadata field, that item will be returned if you pass `--confidence \"[2-4]\"` as a command line argument."
)
parser.add_argument("-a", "--app", help="Show CCT App skills relevant to MC and/or P")
parser.add_argument("-i", "--inf", help="Show CCT Inf skills relevant to MC and/or P")
parser.add_argument('-S', '--topic', choices=topicletters, help='Restrict results to this section only')
parser.add_argument('-f', '--format', default='md', choices=['md','json'], help='Output results in this format')
parser.add_argument('-t', '--titlesonly', action='store_true', help='Output only the skill titles')
parser.add_argument('-s', "--search", help="Search for text")

def metaname(astr):
  if astr.startswith('--'):
    astr = astr[2:]
  astr = astr.replace('-','_')
  return astr

args, extras = parser.parse_known_args()

# Search terms for metadata
meta = {metaname(k):v for k,v in zip(extras[::2],extras[1::2])}

if not args.app and not args.inf:
  args.app = 'MC,P'
  args.inf = 'MC,P'

if args.app:
  app_measure = [x.strip().upper() for x in args.app.split(',')]
else:
  app_measure = []

if args.inf:
  inf_measure = [x.strip().upper() for x in args.inf.split(',')]
else:
  inf_measure = []

results = {}

# Filter down data based on args
for topicname, topic in data['structure'].items():
  for skillname, skill in topic.items():

    # Filter on exam measurement
    if len([v for v in app_measure if v in skill['how_examined']['ace']]) == 0 and len([v for v in inf_measure if v in skill['how_examined']['ice']]) == 0:
      continue

    # Filter on search term in name and details
    if args.search:
      if args.search.lower() not in skillname.lower() and args.search.lower() not in skill['details'].lower(): 
        continue

    # Regex search against metadata
    if len(meta) > 0:
      ok = True
      for k,v in meta.items():
        k = k.lower()
        if k not in skill['meta'] or not re.search( v, skill['meta'][k], re.I ):
          ok = False
      if not ok: continue

    # Add in the topic section name
    if topicname not in results:
      results[topicname] = {}
    results[topicname][skillname] = skill

# Output results
data['structure'] = results

# JSON format
if args.format == 'json':
  print(json.dumps(data, indent=4))

# Markdown format
elif args.format == 'md':

  if not args.titlesonly:
  
    # Frontmatter
    print('---')
    for k,v in data['meta'].items():
      print(k + ': ' + v )
    print('search: ' + str( args.search ) )
    print('app: ' + ', '.join(app_measure))
    print('inf: ' + ', '.join(inf_measure))
    print('---')
    print('')
    print('[TOC]')
    print('')


  for topicname, topic in results.items():
    print('## ' + topicname + '\n')
    
    for skillname, skill in topic.items():
      print('### ' + skillname + '\n')

      if args.titlesonly: continue

      for exam, measure in skill['how_examined'].items():
        print(' - ' + exam + ': ' + ', '.join(measure))

      print('')
      for line in skill['details'].splitlines():
        if len( line.strip() ) == 0: continue
        print('> ' + line)

      print('')

