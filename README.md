# UGUARD 行銷 LLM Wiki

以歷年行銷文章為來源，由 Agent 持續整理產品、合作、概念與寫作知識，協助行銷產出有依據的新文章。

**從 [index.md](index.md) 開始閱讀。** Agent 先讀 [AGENTS.md](AGENTS.md)，依 [Schema](schema/SCHEMA.md) 執行 [Ingest／Query／Lint](docs/WORKFLOWS.md)。

## 目前成果

- 來源登錄 76 個邏輯來源全部處理：pilot-001 5 個、ingest-002 71 個；56 個全文整合，20 個只有線索（外部摘要或只有圖片的貼文），記為 reference_only。
- 官網三語算同一來源的不同版本，以繁中為主要來源（[決策 Q8](docs/DECISIONS.md)）。
- 120 個 Wiki 頁面：產品、夥伴、概念、活動、寫作、待確認事項與 [訊息時間軸](wiki/syntheses/messaging-timeline.md)。
- 全部現行宣稱核准紀錄為空；歷史來源、Agent 歸納、待確認與過期優惠清楚分開。

[ingest-002 報告](reports/2026-11-01-ingest-002.md) · [首次 Ingest 報告](reports/2026-11-01-ingest-pilot-001.md) · [整合發現](wiki/syntheses/pilot-findings.md) · [待確認事項](wiki/issues/source-gaps.md) · [操作日誌](log.md)

## 現場可展示的操作

```bash
python3 scripts/wiki.py status
python3 scripts/wiki.py search 'AgileLink 備援'
python3 scripts/wiki.py prepare-ingest official-news-056
python3 scripts/wiki.py lint
```

這些工具使用 Python 3 標準庫。search 是關鍵字／別名查找；Ingest 與 Query 的閱讀及綜合仍由遵循 AGENTS.md 的 LLM 執行，不需要向量資料庫，也沒有背景自動爬文排程。

可對 Agent 說：「根據 Wiki，哪些合作優惠不能直接放進新文章？請附依據。」或「依產品文章範本，先確認受眾與目的，再草擬一篇 AgileLink 文章。」草稿保存於 drafts，對外發布需另有明確指示。

## Raw Data 收錄範圍

官網 60 篇、中英日共 180 筆語言記錄，日期涵蓋 2024-02-21 至 2026-10-27；FB 只有一篇文字；外部 15 個不重複來源網址以 metadata／摘要為主。圖檔、影片與圖片 OCR 未取得，歷年資料不完整。詳細限制見 [原始收錄報告](docs/COLLECTION_REPORT.md)。

既有 raw 不修改；reading 與 catalog 是前階段的擷取衍生檔，並非完成 Ingest 的 Wiki。更新官網仍可使用 `scripts/fetch_official.py` 另存新快照；`build_catalog.py` 是舊擷取工具，會重建 raw hash 基準，應先確認既有 raw 完整性，不能用重算掩蓋原文改動。新維護優先遵守本 Wiki 流程。

本次只更新知識庫，沒有對外發布文章；第三方來源權利仍屬各權利人。
