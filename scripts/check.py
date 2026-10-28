"""Validate the contact route, local references and draft/release indexing."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import argparse
import gzip

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('directory',nargs='?',default='dist')
p.add_argument('--public',action='store_true')
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
folder=(root/a.directory).resolve()
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.links=[]; self.assets=[]; self.meta={}; self.h1=0; self.images=[]; self.lang=None; self.scripts=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d:self.ids.append(d['id'])
        if tag=='html':self.lang=d.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='a':self.links.append(d.get('href',''))
        if tag=='img':self.images.append(d);self.assets.append(d.get('src',''))
        if tag=='link' and d.get('rel') in ('stylesheet','icon'):self.assets.append(d.get('href',''))
        if tag=='meta':self.meta[d.get('name') or d.get('property')]=d.get('content')
        if tag=='script':self.scripts.append(d)
html=(folder/'index.html').read_text()
page=Page();page.feed(html)
assert page.lang=='pt-BR' and page.h1==1
assert len(page.ids)==len(set(page.ids)), 'Duplicate IDs'
for link in page.links:
    assert link and link!='#', 'Empty link'
    if link.startswith('#'):assert link[1:] in page.ids,link
    if link.startswith('mailto:'):assert urlsplit(link).path=='gabisoudev@gmail.com',link
for asset in page.assets:assert (folder/asset).is_file(),asset
for img in page.images:assert img.get('alt') and img.get('width') and img.get('height')
for script in page.scripts:
    if 'src' not in script:continue
    src=script['src'] or ''
    url=urlsplit(src)
    assert src and not url.scheme and not url.netloc and not src.startswith('/'), 'Script must be local: '+src
    target=(folder/unquote(url.path)).resolve()
    assert target.is_relative_to(folder) and target.is_file(), 'Script missing or outside dist: '+src
    assert 'defer' in script, 'Local script requires defer: '+src
assert 'description' in page.meta
assert 'wa.me' not in html, 'WhatsApp still requires a confirmed number'
if a.public:
    assert page.meta['robots']=='index, follow'
    assert 'rel="canonical"' in html and (folder/'sitemap.xml').is_file()
    assert 'Disallow: /' not in (folder/'robots.txt').read_text()
else:
    assert page.meta['robots']=='noindex, nofollow'
    assert 'Disallow: /' in (folder/'robots.txt').read_text()
files=[x for x in folder.rglob('*') if x.is_file() and not x.name.startswith('__')]
print(f'PASS: {len(page.links)} links, {len(page.ids)} unique IDs, {len(page.images)} images, contact recipient, assets, metadata, indexing.')
print(f'{len(files)} static files; {sum(x.stat().st_size for x in files):,} bytes uncompressed; {sum(len(gzip.compress(x.read_bytes())) for x in files):,} bytes gzip estimate (not a measured network transfer).')
