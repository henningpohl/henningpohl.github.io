import re
import json
from collections import defaultdict

typemap = {
    'full': 'conf',
    'short': 'conf',
    'alt.chi': 'other',
    'journal': 'journal',
    'bookchapter': 'chapter',
    'poster': 'other',
    'demo': 'other',
    'workshop': 'other'
}

def load():
    bib = defaultdict(list)
    with open('publications.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    for paper in data:
        t = typemap.get(paper['type'], None)
        if t == None:
            pass
            #print('Skipping', paper['type'])
        else:
            bib[t].append(paper)
    return bib

data = load()

for t in data:
    papers = sorted(data[t], key=lambda x: x['year'], reverse=True)
    print('\\begin{hangparas}{1.5em}{1}')
    for p in papers:
        if t == 'conf':
            venue = re.match(r'.+? [-\(] ?(.+?)\)?$', p['venue']).group(1)
        else:
            venue = p['venue']
        print("%s. %s. ``%s''. \\textit{%s}." % (p['authors'], p['year'], p['title'], venue))
        print()
    print('\\end{hangparas}')


