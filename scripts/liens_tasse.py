# Liens vers la page citée de Tassé (1878) sur archive.org dans canadiens-ouest(-en).html (idempotent)
import re
ID = {1: 'lescanadiensdelo01tassuoft', 2: 'lescanadiensdelo02tass'}
def url(t, pg):
    m = re.match(r'\s*(\d+)', pg)
    return f"https://archive.org/details/{ID[t]}" + (f"/page/{m.group(1)}/mode/1up" if m else '')
for fn in ['canadiens-ouest.html', 'canadiens-ouest-en.html']:
    h = open(fn, encoding='utf-8').read()
    if 'lescanadiensdelo01tassuoft' in h: continue
    pos = {k: h.find(f'id="{k}"') for k in ['liens1', 'liens2', 'vies1', 'vies2', 'intro', 'donnees']}
    bornes = sorted((v, k) for k, v in pos.items() if v >= 0)
    tome = {'liens1': 1, 'liens2': 2, 'vies1': 1, 'vies2': 2, 'intro': 1, 'donnees': 0}
    out, last = [], 0
    for i, (p, k) in enumerate(bornes):
        out.append((h[last:p], 0)); last = p
        fin = bornes[i + 1][0] if i + 1 < len(bornes) else len(h)
        out.append((h[p:fin], tome[k])); last = fin
    out.append((h[last:], 0))
    res = []
    for seg, t in out:
        if t:
            seg = re.sub(r'<span style="color:#6b604f">\(p\. ([^)<]*)\)</span>',
                         lambda m: f'<span style="color:#6b604f">(<a href="{url(t, m.group(1))}" target="_blank" rel="noopener">p. {m.group(1)}</a>)</span>', seg)
            seg = re.sub(r'(<p class="source">Tassé, t\. (I{1,2}), )(p\. ([^<.]*(?:\.\d+)?))', lambda m: f'{m.group(1)}<a href="{url(2 if m.group(2) == "II" else 1, m.group(4))}" target="_blank" rel="noopener">{m.group(3)}</a>', seg)
        res.append(seg)
    h = ''.join(res)
    h = h.replace("<small>Tassé, t. '+(p.tome==2?'II':'I')+', p. '+p.pages+'</small>", '<small><a target="_blank" rel="noopener" href="https://archive.org/details/\'+(p.tome==2?\'lescanadiensdelo02tass\':\'lescanadiensdelo01tassuoft\')+\'/page/\'+parseInt(p.pages)+\'/mode/1up">Tassé, t. \'+(p.tome==2?\'II\':\'I\')+\', p. \'+p.pages+\'</a></small>')
    open(fn, 'w', encoding='utf-8').write(h)
    print(fn, h.count('lescanadiensdelo01tassuoft'), h.count('lescanadiensdelo02tass'))
