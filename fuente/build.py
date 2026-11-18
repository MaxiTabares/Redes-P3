# Arma ../index.html (autocontenido) a partir de app.html + preguntas.js + simuladas.js + img/*.png
# Uso: python3 build.py
import base64, json, os
d = os.path.dirname(os.path.abspath(__file__))
app = open(os.path.join(d, 'app.html'), encoding='utf-8').read()
preg = open(os.path.join(d, 'preguntas.js'), encoding='utf-8').read()
simu = open(os.path.join(d, 'simuladas.js'), encoding='utf-8').read()
imgs = {}
for f in sorted(os.listdir(os.path.join(d, 'img'))):
    if f.endswith('.png'):
        imgs[f[:-4]] = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(d, 'img', f), 'rb').read()).decode()
out = app.replace('/*__PREGUNTAS__*/', preg).replace('/*__SIMULADAS__*/', simu).replace('/*__IMGS__*/', 'const IMGS = ' + json.dumps(imgs) + ';')
open(os.path.join(d, '..', 'index.html'), 'w', encoding='utf-8').write(out)
print('index.html', len(out) // 1024, 'KB')
