# CCT Syllabus 

The CREST Certified Tester Syllabus transposed into markdown and then a script to query that markdown.

## But Why

You have to resit your CCT exam every 3 years. This is my third renewal and I'm struggling to make the exact same topics interesting.

The first CREST exam I sat (CRT) had notes scribbled all over a printout of the syllabus.

The next one I sat I had it all as a big separate Google doc.

The next one I sat I did it in markdown and it wasn't too bad, plus I could do some grep-fu around which topics needed more work.

This time I'm going full CLI-python script on it. There are maybe three other people in the world who would appreciate this too.

## Editing Convention

The markdown version of the syllabus in this repo is a version of the PDF doc, converted to flat text with `pdf2text` and then tidied up in Typora. It has the following features:

 - Document properties are in a *Frontmatter* block at the top of the doc
 - Most of the pre-appendix sections are just verbatim copies of the actual doc and not that useful
 - The topic listings in the appendix are separated out as topics under H2s
 - Skill names are under H3s 
 - Under each skill the "how examined" column is shown as the first unordered list in that section
 - Everything in block quotes is the "details" column
 - Everything else is your own notes

## Querying the Syllabus

This includes a tool, `syllabus.py` that interprets the structure of the markdown file and allows it to be queried.

### Examples 

Show all skills that will be tackled in the CCT App practical exam:

```
python syllabus.py --app P
```

Search for all skills including the word "script" in any exam:

```
python syllabus.py --search script
```

Output all the CCT Inf multiple choice skills as JSON:

```
python syllabus.py --inf MC --format json
```
