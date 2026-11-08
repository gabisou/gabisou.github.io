"""Prepare static production files; never publish or change DNS."""
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
from html import escape as html_escape
import argparse
import json
import shutil

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--origin', required=True, help='Confirmed HTTPS origin, without a path')
parser.add_argument('--output', default='build')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
u = urlsplit(args.origin)
if u.scheme != 'https' or not u.hostname or u.username or u.password or u.query or u.fragment or u.path not in ('', '/'):
    parser.error('Use an HTTPS origin without credentials, query or path.')
origin = f'https://{u.netloc}'
out = (root / args.output).resolve()
if out == root or root / 'dist' == out or out in root.parents:
    parser.error('Output must be a separate build directory.')
out.mkdir(parents=True, exist_ok=True)
for src in (root / 'dist').rglob('*'):
    if src.is_file() and not src.name.startswith('__'):
        dest = out / src.relative_to(root / 'dist')
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
html = (out / 'index.html').read_text()
html = html.replace('<meta name="robots" content="noindex, nofollow">', '<meta name="robots" content="index, follow">')
data = {'@context':'https://schema.org','@type':'Organization','name':'GABiSOU','url':origin+'/', 'email':'gabisoudev@gmail.com','logo':origin+'/assets/logo.png'}
metadata = f'<link rel="canonical" href="{html_escape(origin, quote=True)}/">\n  <meta property="og:url" content="{html_escape(origin, quote=True)}/">\n  <script type="application/ld+json">{json.dumps(data,ensure_ascii=False).replace("<", chr(92)+"u003c")}</script>\n'
html = html.replace('</head>', metadata + '</head>')
(out / 'index.html').write_text(html)
(out / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {origin}/sitemap.xml\n')
(out / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{escape(origin)}/</loc></url></urlset>\n')
print(f'Prepared {out}; no deployment performed.')
