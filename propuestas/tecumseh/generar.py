import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
datos = json.loads((d/'datos.json').read_text(encoding='utf-8'))
html = (d/'plantilla.html').read_text(encoding='utf-8')
for k, v in datos.items():
    html = html.replace('{'+k+'}', v)
(d/'propuesta-tecumseh.html').write_text(html, encoding='utf-8')
