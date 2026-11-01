#!/usr/bin/env python3
"""Build reading copies and provenance catalog from preserved public API responses."""
import csv, hashlib, json, re
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.assets=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ('p','div','br','tr','h1','h2','h3','li'): self.parts.append('\n')
        if tag in ('td','th'): self.parts.append(' | ')
        if tag=='img' and a.get('src'): self.assets.append(a['src']); self.parts.append('\n[圖片：'+a.get('alt','')+'] '+a['src']+'\n')
    def handle_data(self, data): self.parts.append(data)
    def text(self): return re.sub(r'\n[ \t]*\n+', '\n\n', ''.join(self.parts)).strip()
def write_json(path, value):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def load(name): return json.loads((ROOT/'raw/official/api'/name).read_text())
zh={x['id']:x for x in load('news-zh-TW.json')['data']}
rows=[];stats={};assets=[]
for lang,prefix in [('zh-TW',''),('en','/en'),('jp','/jp')]:
    items=load('news-'+lang+'.json')['data']; assert len({x['id'] for x in items})==len(items)
    stats[lang]={'records':len(items),'same_body_as_zh':0,'low_text_records':[]}
    for x in items:
        parser=Text();parser.feed(x['content']);body=parser.text()
        plain=re.sub('<[^>]+>','',x['content']).strip()
        same=lang!='zh-TW' and x['content']==zh[x['id']]['content']
        stats[lang]['same_body_as_zh']+=int(same)
        if len(plain)<80: stats[lang]['low_text_records'].append(x['id'])
        ident=f"official-news-{x['id']:03d}-{lang}"
        path=f"reading/official/{lang}/{x['id']:03d}.md"
        url=f"https://www.uguardnetworks.com{prefix}/news/{x['id']}"
        row=dict(record_id=ident,source_type='official',source_id=x['id'],language_requested=lang,title=x['title'],published_at=x['date'],updated_at=x.get('updated_at'),source_url=url,api_url='https://api2.uguardnetworks.com/api/news?lang='+lang,raw_path='raw/official/api/news-'+lang+'.json',raw_record_pointer='/data/'+str(items.index(x)),reading_path=path,content_status='api_full_html',same_body_as_zh=same,plain_text_chars=len(plain),body_sha256=hashlib.sha256(x['content'].encode()).hexdigest(),image_urls=parser.assets)
        rows.append(row)
        p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(f"# {x['title']}\n\n- 原始網址：{url}\n- 發布日期：{x['date']}\n- 更新日期：{x.get('updated_at','')}\n- 語言 API：{lang}\n- 作者：{x.get('author','')}\n- 分類：{x.get('category_name','')}\n- 原始資料：`{row['raw_path']}` → `{row['raw_record_pointer']}`\n- 正文與中文版相同：{same}\n\n## 原文轉文字（原始 HTML 以 raw API 為準）\n\n{body}\n",encoding='utf-8')
        for asset in [x.get('image')]+parser.assets:
            if asset: assets.append({'record_id':ident,'url':asset,'download_status':'url_only'})
write_json(ROOT/'catalog/official_records.json',rows)
write_json(ROOT/'catalog/assets.json',assets)
external=load('news-links.json')['data']; requested=json.loads((ROOT/'raw/external/requested_sources.json').read_text())
refs={x['url']:{'source_url':x['url'],'title':x['title'],'publisher':x['source'],'listed_date':x['newsDate'],'status':'official_curated_reference_only','raw_path':'raw/official/api/news-links.json','date_note':'Date as listed by UGUARD; not independently verified publication date.'} for x in external}
for x in requested: refs[x['source_url']]={'source_url':x['source_url'],'title':x['title'],'publisher':x['publisher'],'published_at':x['published_at'],'status':x['status'],'raw_path':'raw/external/requested_sources.json'}
write_json(ROOT/'catalog/external_records.json',list(refs.values()))
with (ROOT/'catalog/official_index.csv').open('w',newline='',encoding='utf-8-sig') as f:
    fields=['record_id','source_type','language_requested','title','published_at','updated_at','source_url','raw_path','raw_record_pointer','reading_path','content_status','same_body_as_zh','plain_text_chars','body_sha256']
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
sitemap=(ROOT/'raw/official/sitemap.xml').read_text()
sitemap_ids=set(map(int,re.findall(r'<loc>https://www\.uguardnetworks\.com/(?:en/|jp/)?news/(\d+)',sitemap)))
write_json(ROOT/'catalog/validation.json',{'unique_news':len(zh),'language_records':len(rows),'per_language':stats,'sitemap_news_ids':sorted(sitemap_ids),'sitemap_ids_missing_from_api':sorted(sitemap_ids-set(zh)),'official_curated_external_references':len(external),'unique_external_references_including_requested':len(refs),'insights_count':len(load('articles.json')['data']),'assertions_passed':['unique article IDs within each language','all raw news entries have content','all three language ID sets match']})
assert all(x['content'] for l in ['zh-TW','en','jp'] for x in load('news-'+l+'.json')['data'])
assert all({x['id'] for x in load('news-'+l+'.json')['data']}==set(zh) for l in ['en','jp'])
checks={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'raw').rglob('*')) if p.is_file()}
write_json(ROOT/'catalog/raw_sha256.json',checks)
print(json.dumps({'records':len(rows),'unique_news':len(zh),'external_references':len(refs),'language_stats':stats},ensure_ascii=False))
