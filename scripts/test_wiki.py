#!/usr/bin/env python3
"""Regression checks in disposable copies; never mutate the repository."""
import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('wiki',Path(__file__).with_name('wiki.py'))
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)
ORIGINAL=w.ROOT
class WikiChecks(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ORIGINAL,self.root,ignore=shutil.ignore_patterns('__pycache__','.git'))
        w.ROOT=self.root
    def tearDown(self):w.ROOT=ORIGINAL;self.temp.cleanup()
    def errors(self):return '\n'.join(w.lint('2026-11-01')['errors'])
    def edit_json(self,path,fn):
        p=self.root/path;o=json.loads(p.read_text());fn(o);p.write_text(json.dumps(o,ensure_ascii=False))
    def test_clean(self):self.assertEqual(self.errors(),'')
    def test_raw_mutation(self):
        p=self.root/'raw/facebook/latest_post.json';p.write_text(p.read_text()+'\n')
        self.assertIn('raw baseline mismatch',self.errors())
    def test_broken_link(self):
        p=self.root/'wiki/entities/agilelink.md';p.write_text(p.read_text()+'\n[bad](missing.md)\n')
        self.assertIn('broken link',self.errors())
    def test_summary_not_full(self):
        p=self.root/'wiki/sources/external-cio-109792.md';p.write_text(p.read_text().replace('status: "reference_only"','status: "source_reported"'))
        self.assertIn('summary upgraded',self.errors())
    def test_unapproved_current_claim(self):
        self.edit_json('schema/claims.json',lambda o:o['claims'][0].update(status='approved_current'))
        self.assertIn('unapproved current claim',self.errors())
    def test_duplicate_id(self):
        p=self.root/'wiki/entities/agilelink.md';p.write_text(p.read_text().replace('id: "entity-agilelink"','id: "entity-uguard"'))
        self.assertIn('duplicate wiki page IDs',self.errors())
    def test_stale_index(self):
        (self.root/'index.md').write_text('# incomplete index\n')
        self.assertIn('index is stale',self.errors())
    def test_log_append_only(self):
        p=self.root/'log.md';old=Path(self.temp.name)/'baseline.md';old.write_text(p.read_text())
        p.write_text(p.read_text().replace('五個代表來源','changed'))
        self.assertIn('log is not append-only','\n'.join(w.lint('2026-11-01',old)['errors']))
if __name__=='__main__':unittest.main()
