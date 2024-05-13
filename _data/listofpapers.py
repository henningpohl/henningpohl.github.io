from jinja2 import Template
import yaml

template = Template(r'''
\begin{filecontents}{bibliography.bib}

{% for key in bib %}
{{bib[key]}}
{% endfor %}

\end{filecontents}
\documentclass[a4paper, 10pt]{report}

\usepackage[margin=2cm]{geometry}
\usepackage{Arvo}
\renewcommand\bibname{Henning Pohl --- Publication List}

\begin{document}

\nocite{*}

\bibliographystyle{acm}
\bibliography{bibliography.bib}

\end{document}
''')

with open('bibtex.yaml', 'r', encoding='utf8') as f:
    data = yaml.safe_load(f)

doc = template.render(bib=data)

with open('ListOfPapers.tex', 'w', encoding='utf8') as f:
    f.write(doc)
print(doc)

