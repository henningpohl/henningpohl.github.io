import yaml

with open('bibtex.yaml', 'r', encoding='utf8') as f:
    data = yaml.safe_load(f)

bib = '\n\n'.join(data.values())

with open('henning.bib', 'w', encoding='utf8') as f:
    f.write(bib)


