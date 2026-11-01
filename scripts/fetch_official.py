#!/usr/bin/env python3
"""Fetch a new, separate snapshot. Uses only public endpoints used by the website.
Usage: python3 scripts/fetch_official.py /path/to/new-snapshot
Does not overwrite the committed snapshot or access Facebook/authenticated APIs.
"""
import datetime,hashlib,json,subprocess,sys,time
from pathlib import Path
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
base='https://api2.uguardnetworks.com'
urls={f'news-{lang}.json':base+'/api/news?lang='+lang for lang in ['zh-TW','en','jp']}
urls.update({'news-links.json':base+'/api/news-links?lang=zh-TW','articles.json':base+'/api/articles?lang=zh-TW'})
log=[]
for name,url in urls.items():
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    r=subprocess.run(['curl','--fail','--location','--silent','--show-error','--max-time','45',url],capture_output=True,check=True)
    j=json.loads(r.stdout)
    if not isinstance(j.get('data'),list): raise ValueError('Unexpected response schema: '+url)
    (out/name).write_bytes(r.stdout)
    log.append(dict(url=url,retrieved_at=at,file=name,records=len(j['data']),sha256=hashlib.sha256(r.stdout).hexdigest()))
    time.sleep(1)
(out/'fetch_log.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Saved',len(log),'API snapshots to',out)
