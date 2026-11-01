#!/usr/bin/env python3
"""Small stdlib tools for the agent-maintained Wiki; no model calls or raw writes."""
import argparse, datetime as dt, hashlib, json, re, sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote
from zoneinfo import ZoneInfo
ROOT=Path(__file__).resolve().parents[1]
TYPES={'source','entity','concept','event','writing','synthesis','issue'}
STATES={'source_reported','historical_only','inferred','reference_only','needs_review','approved_current','expired','superseded'}
REQUIRED={'schema_version','id','type','title','summary','language','status','created','updated','sources','related'}
def today():return dt.datetime.now(ZoneInfo('Asia/Tokyo')).date().isoformat()
def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def sha(b):return hashlib.sha256(b).hexdigest()
def pointer(value,ptr):
    for token in ptr.split('/')[1:] if ptr else []:
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value

def metadata(p):
    s=p.read_text(encoding='utf-8')
    if not s.startswith('---\n') or '\n---\n' not in s[4:]:raise ValueError('missing frontmatter')
    head,body=s[4:].split('\n---\n',1);m={}
    for line in head.splitlines():
        k,v=line.split(':',1)
        if k in m:raise ValueError('duplicate key '+k)
        m[k]=json.loads(v.strip())
    return m,body

def pages():return [(p,*metadata(p)) for p in sorted((ROOT/'wiki').rglob('*.md'))]
def registry():return load('schema/source-registry.json')['sources']
def make_index():
    ps=pages();ss=registry();counts=Counter(x['ingest_status'] for x in ss)
    out=['# UGUARD 行銷知識庫','',
    '先從產品、議題或寫作頁閱讀；需要查證時沿來源頁追溯 raw。頁面是來源化知識，不代表現行宣稱已核准。','',
    f"來源登錄 {len(ss)} 筆：全文已 Ingest {counts['ingested']}、線索已登記 {counts['reference_only']}、待處理 {counts['pending']}。",'',
    '目前進度：[pilot 執行紀錄](schema/ingest-runs.json)；[首次整合發現](wiki/syntheses/pilot-findings.md)。','',
    '[Agent 規範](AGENTS.md) · [Schema](schema/SCHEMA.md) · [流程](docs/WORKFLOWS.md) · [操作日誌](log.md) · [首次報告](reports/2026-11-01-ingest-pilot-001.md)','']
    labels={'source':'來源摘要','entity':'公司、夥伴與產品','concept':'概念與受眾問題','event':'合作與活動','writing':'寫作知識','synthesis':'綜合分析','issue':'待確認與缺口'}
    for typ in ['entity','concept','event','writing','synthesis','source','issue']:
        out += ['## '+labels[typ],'']
        for p,m,_ in ps:
            if m['type']==typ:out.append(f"- [{m['title']}]({p.relative_to(ROOT).as_posix()}) — {m['summary']}（{m['status']}）")
        out.append('')
    return '\n'.join(out).rstrip()+'\n'
def status():
    ss=registry();print(json.dumps({'sources':len(ss),'states':dict(Counter(x['ingest_status'] for x in ss)),'wiki_pages':len(pages()),'runs':load('schema/ingest-runs.json')['runs']},ensure_ascii=False,indent=2))
def prepare(ids):
    rs={x['id']:x for x in registry()}
    for id in ids:
        r=rs[id];unchanged=True
        print(id, r['title'],r['ingest_status'],r['completeness'])
        for lang,v in r['variants'].items():
            val=pointer(load(v['path']),v['pointer']);d=sha(json.dumps(val,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
            same=r.get('ingested_record_sha256',{}).get(lang)==d;unchanged &= same
            print(' ',lang,v['path'],v['pointer'] or '/', 'already_read' if same else 'needs_read')
        print('action:', 'no-op (same ingested record hashes)' if unchanged else 'Agent must read, synthesize and follow Ingest workflow')
def search(q):
    aliases=load('schema/aliases.json');terms=[t.casefold() for t in q.split()];wanted={v for k,v in aliases.items() if k.casefold() in q.casefold()}
    hits=[]
    for p,m,b in pages():
        text=(m['title']+' '+m['summary']+' '+b).casefold()
        score=sum(text.count(t) for t in terms)+ (20 if m['id'] in wanted else 0)
        if score:hits.append((score,p,m))
    print('Read index.md first; keyword/alias matches, not generated answers:')
    for score,p,m in sorted(hits,key=lambda x:(-x[0],str(x[1])))[:12]:print(f"{score:3} {p.relative_to(ROOT)} [{m['status']}] {m['title']} — {m['summary']}")

def lint(asof,baseline_log=None):
    errors=[];warnings=[];ps=[]
    def err(s):errors.append(s)
    def warn(s):warnings.append(s)
    date=dt.date.fromisoformat(asof)
    for p in sorted((ROOT/'wiki').rglob('*.md')):
        try:
            m,b=metadata(p);ps.append((p,m,b))
            if not REQUIRED<=m.keys():err(str(p.relative_to(ROOT))+': missing fields '+str(REQUIRED-m.keys()));continue
            if m['type'] not in TYPES or m['status'] not in STATES:err(m['id']+': invalid type/status')
            if m['language']!='zh-TW' or m['schema_version']!='1.0.0':err(m['id']+': incompatible language/schema')
            if not isinstance(m['sources'],list) or not m['sources'] or not isinstance(m['related'],list) or not m['related']:err(m['id']+': sources/related must be nonempty arrays')
            for k in ['id','title','summary']:
                if not isinstance(m[k],str) or not m[k].strip():err(str(p)+': invalid '+k)
            if dt.date.fromisoformat(m['created'])>dt.date.fromisoformat(m['updated']):err(m['id']+': updated before created')
            if dt.date.fromisoformat(m['updated'])>date:err(m['id']+': future updated date')
            if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',p.stem):err(str(p)+': invalid filename')
            if len(b.strip())<80 or not b.lstrip().startswith('# '):err(m['id']+': empty/invalid body')
        except Exception as e:err(str(p.relative_to(ROOT))+': '+str(e))
    ids=[m.get('id') for _,m,_ in ps];byid={m.get('id'):(p,m,b) for p,m,b in ps}
    if len(ids)!=len(set(ids)):err('duplicate wiki page IDs')
    rs=registry();bySource={r['id']:r for r in rs}
    if len(rs)!=len(bySource):err('duplicate source IDs')
    for r in rs:
        if r['ingest_status'] not in {'pending','ingested','reference_only'}:err(r['id']+': invalid ingest state')
        for lang,v in r['variants'].items():
            try:
                p=(ROOT/v['path']).resolve()
                if not p.is_relative_to((ROOT/'raw').resolve()):raise ValueError('source outside raw')
                raw=p.read_bytes();record=pointer(json.loads(raw),v['pointer'])
                rd=sha(json.dumps(record,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
                if sha(raw)!=v['file_sha256'] or rd!=v['record_sha256']:err(r['id']+': raw hash changed '+lang)
                if r['ingest_status']!='pending' and r.get('ingested_record_sha256',{}).get(lang)!=rd:err(r['id']+': ingest stale '+lang)
            except Exception as e:err(r['id']+': raw reference '+str(e))
        if r['ingest_status']!='pending':
            p=ROOT/(r.get('source_page') or '__missing__')
            try:
                m,_=metadata(p)
                if m['type']!='source' or r['id'] not in m['sources']:err(r['id']+': wrong source page')
                if r['ingest_status']=='reference_only' and m['status']!='reference_only':err(r['id']+': summary upgraded to full evidence')
            except Exception as e:err(r['id']+': missing source page '+str(e))
    baseline=load('catalog/raw_sha256.json')
    for p,d in baseline.items():
        if not (ROOT/p).is_file() or sha((ROOT/p).read_bytes())!=d:err('raw baseline mismatch: '+p)
    for p in (ROOT/'raw').rglob('*'):
        if p.is_file() and p.relative_to(ROOT).as_posix() not in baseline:err('raw file missing baseline: '+p.relative_to(ROOT).as_posix())
    for p,m,b in ps:
        for id in m.get('sources',[]):
            if id not in bySource:err(m['id']+': missing source '+id)
            elif bySource[id]['ingest_status']=='pending':err(m['id']+': cites unprocessed source '+id)
        for id in m.get('related',[]):
            if id not in byid:err(m['id']+': missing related page '+id)
            elif id==m['id']:err(m['id']+': self relation')
        if m.get('status')=='needs_review':warn('open issue/review: '+m['id'])
        if m.get('type')=='source' and m.get('status')=='reference_only':warn('incomplete evidence: '+m['id'])
    # Validate literal relative Markdown links (raw, old reading files and templates excluded).
    managed=[ROOT/'AGENTS.md',ROOT/'README.md',ROOT/'index.md',ROOT/'log.md']
    managed+=list((ROOT/'wiki').rglob('*.md'))+list((ROOT/'schema').glob('*.md'))+list((ROOT/'docs').glob('*.md'))+list((ROOT/'reports').glob('*.md'))+list((ROOT/'drafts').glob('*.md'))
    inbound=Counter()
    def anchors(text):
        counts=Counter();out=set()
        for h in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
            slug=re.sub(r'[^\w\-\s]','',h.lower()).replace(' ','-');n=counts[slug];counts[slug]+=1;out.add(slug+(f'-{n}' if n else ''))
        return out
    for p in managed:
        if not p.exists():err('missing managed file '+str(p.relative_to(ROOT)));continue
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',p.read_text()):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            path,_,anchor=unquote(target).partition('#');dest=(p.parent/path).resolve() if path else p.resolve()
            if not dest.is_relative_to(ROOT.resolve()):err(str(p.relative_to(ROOT))+': escaping link '+target);continue
            if not dest.exists():err(str(p.relative_to(ROOT))+': broken link '+target);continue
            if anchor and dest.suffix=='.md' and anchor not in anchors(dest.read_text()):err(str(p.relative_to(ROOT))+': broken anchor '+target)
            if p.is_relative_to(ROOT/'wiki') and dest!=p.resolve():inbound[str(dest)]+=1
    for p,m,_ in ps:
        if not inbound[str(p.resolve())]:err('orphan page (index excluded): '+m['id'])
    try:
        if (ROOT/'index.md').read_text()!=make_index():err('index is stale; run index command')
    except Exception as e:err('index invalid: '+str(e))
    claims=load('schema/claims.json')['claims'];approved=load('schema/approvals.json')['approvals'];cm={c['id']:c for c in claims}
    if len(cm)!=len(claims):err('duplicate claim IDs')
    amap={}
    for a in approved:
        try:
            for key in ['claim_id','approved_by','approved_at','review_due','scope','evidence_path']:
                if not a.get(key):raise ValueError('missing approval field '+key)
            if a['claim_id'] not in cm:raise ValueError('unknown claim')
            if a['approved_by'].casefold() in {'agent','ai','llm','codex','chatgpt'}:raise ValueError('self approval')
            evidence=(ROOT/a['evidence_path']).resolve()
            if not evidence.is_relative_to((ROOT/'raw').resolve()) or not evidence.is_file():raise ValueError('missing raw approval evidence')
            if dt.date.fromisoformat(a['approved_at'])>date:raise ValueError('future approval')
            if dt.date.fromisoformat(a['review_due'])<dt.date.fromisoformat(a['approved_at']):raise ValueError('invalid review period')
            amap[a['claim_id']]=a
        except Exception as e:err('approval invalid: '+str(e))
    for c in claims:
        try:
            if c['status'] not in STATES:raise ValueError('unknown status')
            if c['page_id'] not in byid:raise ValueError('unknown page')
            if not c['sources'] or any(s not in bySource or bySource[s]['ingest_status']=='pending' for s in c['sources']):raise ValueError('invalid evidence')
            if not c['locator']:raise ValueError('missing locator')
            dt.date.fromisoformat(c['as_of'])
            expired=c.get('valid_until') and dt.date.fromisoformat(c['valid_until'])<date
            if expired and c['status'] not in {'expired','historical_only','superseded'}:
                (err if c['status']=='approved_current' else warn)('claim passed valid_until: '+c['id'])
            if c['status']=='approved_current':
                a=amap.get(c['id'])
                if not a:err('unapproved current claim: '+c['id'])
                elif dt.date.fromisoformat(a['review_due'])<date:err('approval review expired: '+c['id'])
            if c['status'] in {'expired','historical_only','needs_review'}:warn('restricted claim: '+c['id']+' ['+c['status']+']')
        except Exception as e:err('claim invalid: '+c.get('id','?')+' '+str(e))
    for _,m,_ in ps:
        if m.get('status')=='approved_current':
            pc=[c for c in claims if c['page_id']==m['id']]
            if not pc or any(c['status']!='approved_current' or c['id'] not in amap for c in pc):err('page lacks scoped approvals: '+m['id'])
    log=(ROOT/'log.md').read_text() if (ROOT/'log.md').exists() else ''
    headings=re.findall(r'^## .*$',log,re.M)
    if not headings:err('empty operation log')
    for h in headings:
        match=re.fullmatch(r'## \[(\d{4}-\d{2}-\d{2})\] (schema|ingest|query|lint|correction) \| .+',h)
        if not match:err('invalid log heading: '+h)
        elif dt.date.fromisoformat(match.group(1))>date:err('future log entry: '+h)
    if baseline_log and not log.startswith(Path(baseline_log).read_text()):err('log is not append-only versus baseline')
    warnings.append('Semantic evidence, contradictions and publication approval require Agent/human review; structural success is not factual verification.')
    return {'schema_version':'1.0.0','as_of':asof,'wiki_pages':len(ps),'registered_sources':len(rs),'ingest_states':dict(Counter(x['ingest_status'] for x in rs)),'errors':errors,'warnings':warnings,'result':'fail' if errors else 'pass_with_warnings' if warnings else 'pass'}

def main():
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('status');sub.add_parser('index')
    p=sub.add_parser('search');p.add_argument('query')
    p=sub.add_parser('prepare-ingest');p.add_argument('ids',nargs='+')
    p=sub.add_parser('lint');p.add_argument('--as-of',default=today());p.add_argument('--baseline-log');p.add_argument('--report')
    p=sub.add_parser('log');p.add_argument('operation',choices=['schema','ingest','query','lint','correction']);p.add_argument('title');p.add_argument('--details',required=True);p.add_argument('--date',default=today())
    a=ap.parse_args()
    if a.command=='status':status()
    elif a.command=='index':(ROOT/'index.md').write_text(make_index(),encoding='utf-8');print('index.md updated')
    elif a.command=='search':search(a.query)
    elif a.command=='prepare-ingest':prepare(a.ids)
    elif a.command=='log':
        dt.date.fromisoformat(a.date)
        if '\n' in a.title:raise ValueError('title must be one line')
        with (ROOT/'log.md').open('a',encoding='utf-8') as f:f.write(f'\n## [{a.date}] {a.operation} | {a.title}\n\n{a.details}\n')
    elif a.command=='lint':
        result=lint(a.as_of,a.baseline_log);s=json.dumps(result,ensure_ascii=False,indent=2)+'\n';print(s)
        if a.report:
            p=(ROOT/a.report).resolve()
            if not p.is_relative_to((ROOT/'reports').resolve()):raise ValueError('report must be under reports/')
            p.parent.mkdir(parents=True,exist_ok=True)
            with p.open('x',encoding='utf-8') as f:f.write(s)
        return int(bool(result['errors']))
    return 0
if __name__=='__main__':sys.exit(main())
