from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text(encoding='utf-8')
css = (root / 'styles.css').read_text(encoding='utf-8')
js = (root / 'script.js').read_text(encoding='utf-8')
ids = set(re.findall(r'id="([^"]+)"', html))
hrefs = re.findall(r'href="([^"]+)"', html)
linked = [h for h in hrefs if h.endswith('.css')]
scripts = re.findall(r'src="([^"]+)"', html)
missing = [f for f in linked + scripts if not (root / f).exists()]
bad = [h for h in hrefs if h.startswith('#') and h != '#' and h[1:] not in ids]
required_text = [
    'Guild Task Tracker',
    'Twilio',
    'OpenClaw Intake Agent',
    'Sage-Nexus',
    'Email / LinkedIn / resume PDF to add',
]
missing_text = [text for text in required_text if text not in html]

print('html bytes', len(html))
print('css bytes', len(css))
print('js bytes', len(js))
print('missing linked assets', missing)
print('bad internal anchors', bad)
print('missing expected text', missing_text)
print('has placeholder email', 'your.email@example.com' in html)
print('sections', sorted(ids & {'top', 'work', 'case-studies', 'skills', 'contact', 'main', 'nav-links'}))

if missing or bad or missing_text:
    raise SystemExit(1)
