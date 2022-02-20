#!/env/python

import re, json, argparse

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
      skill = m.group(1) + ': ' + m.group(2)
      if debug: print(topic, skill)
      data['structure'][topic][skill] = {'details':'','how_examined':{},'notes':''}
      continue

    if skill == '': continue

    # How examined
    m = re.search(r'^ ?- ([AI]CE):([MCP, ]+)$', line)
    if m:
      data['structure'][topic][skill]['how_examined'][m.group(1)] = [x.strip() for x in m.group(2).split(',')]
      continue

    # Details
    m = re.search(r'^> *(.*)', line)
    if m:
      data['structure'][topic][skill]['details'] += '\n' + m.group(1)
      continue

    # Anything else is revision notes added in
    if topic != '' and skill != '':
      data['structure'][topic][skill]['notes'] += line + '\n'

topicletters = [x[0] for x in data['structure'].keys()]

parser = argparse.ArgumentParser(description="A CLI front end for the CREST CCT Syllabus")
parser.add_argument("-a", "--app", help="Show CCT App skills relevant to MC and/or P")
parser.add_argument("-i", "--inf", help="Show CCT Inf skills relevant to MC and/or P")
parser.add_argument('-S', '--topic', choices=topicletters, help='Restrict results to this section only')
parser.add_argument('-f', '--format', default='md', choices=['md','json'], help='Output results in this format')
parser.add_argument('-s', "--search", help="Search for text")

args = parser.parse_args()

if not args.app and not args.inf:
  args.app = 'MC,P'
  args.inf = 'MC,P'

if args.app:
  app_measure = [x.strip() for x in args.app.split(',')]
else:
  app_measure = []

if args.inf:
  inf_measure = [x.strip() for x in args.inf.split(',')]
else:
  inf_measure = []

results = {}

for topicname, topic in data['structure'].items():
  for skillname, skill in topic.items():
    if len([v for v in app_measure if v in skill['how_examined']['ACE']]) == 0 and len([v for v in inf_measure if v in skill['how_examined']['ICE']]) == 0:
      continue
    if args.search:
      if args.search.lower() not in skillname.lower() and args.search.lower() not in skill['details'].lower(): 
        continue
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

      for exam, measure in skill['how_examined'].items():
        print(' - ' + exam + ': ' + ', '.join(measure))

      print('')
      for line in skill['details'].splitlines():
        if len( line.strip() ) == 0: continue
        print('> ' + line)

      print('')

