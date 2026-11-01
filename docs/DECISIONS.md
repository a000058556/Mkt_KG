# 已確認決策

2026-11-01，使用者兩輪回答「全建議」，最後明確授權「全建議，開始建置」。本檔記錄本專案決策，不從其他專案推定規則。

| 項目 | 決策 |
|---|---|
| Q1 | 資料＋寫作知識庫；品牌語氣與範本的歸納須標為觀察 |
| Q2 | 繁中 Wiki，關聯英日同源版本 |
| Q3 | 區分來源證據與現行核准；時效敏感／矛盾先待確認 |
| Q4 | 首次先試行 5 篇；使用者確認成果後再擴大其餘來源 |
| Q5 | 有價值分析自動保存 Wiki；文章草稿另存 drafts；簡單問答記操作 |
| Q6 | 例行 Ingest／保存 Query／修復 Lint 完成檢查後可直接提交 main；重大 Schema 調整先確認 |
| Q7 | 不完整來源分級納入；摘要與圖片線索不可冒充全文 |

已授權的是知識庫建置、維護及本次 pilot，不包含對外發布、通知他人、排程自動抓取或核准產品宣稱。首次只有使用者明確確認成果後才將 pilot 狀態改為 accepted 並啟動剩餘來源。

技術落地採標準 Markdown 相對連結、ASCII 檔名、繁中標題、Python 標準庫及 GitHub；保留既有 raw/catalog/reading，新增 wiki/schema 等目錄。這些是已確認設計下的例行實作選擇。

原始架構依據：[使用者提供的 LLM Wiki pattern](reference/llm-wiki-pattern.md)。其 three-layer / Ingest / Query / Lint 概念已具體化到 [Schema](../schema/SCHEMA.md) 與 [流程](WORKFLOWS.md)。
