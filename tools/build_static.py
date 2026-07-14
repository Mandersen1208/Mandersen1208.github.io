from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

SITE_FILES = [
    'index.html',
    'styles.css',
    'script.js',
]

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)

for filename in SITE_FILES:
    source = ROOT / filename
    if not source.exists():
        raise FileNotFoundError(f'Missing required site file: {filename}')
    shutil.copy2(source, DIST / filename)

assets = ROOT / 'assets'
if assets.exists() and any(assets.iterdir()):
    shutil.copytree(assets, DIST / 'assets')
else:
    (DIST / 'assets').mkdir()

# Prevent GitHub Pages/Jekyll processing from ignoring underscore files later.
(DIST / '.nojekyll').write_text('', encoding='utf-8')

print(f'Built static site artifact at {DIST}')
for path in sorted(DIST.rglob('*')):
    if path.is_file():
        print(path.relative_to(DIST))
