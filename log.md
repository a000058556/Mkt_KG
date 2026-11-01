# Wiki 操作日誌

本檔僅追加；既有紀錄的修正另加 correction entry。日期使用 Asia/Tokyo；來源事件日期保持原值。

## [2026-11-01] schema | 建立 UGUARD 行銷 Wiki v1.0.0

- 依據：使用者提供 LLM Wiki pattern，並確認 Q1–Q7 全部建議，明確授權開始建置。
- 建立 AGENTS、Schema、命名、來源狀態、核准紀錄、操作流程及範本；保留既有 raw。
- 維護：例行操作完成檢查後直接提交 main；重大設計先 /grill-me；不含對外發布。
- 範圍：首次 5 個來源試行，完成後等待使用者驗收再擴大。

## [2026-11-01] ingest | pilot-001：五個代表來源

- 來源：official-news-045、official-news-056、official-news-060、FB 威脅情資更新貼文、external-cio-109792。
- 三篇官網讀取繁中全文並核對英日主要事實；同源語言版本不算獨立證據。FB 只取得可見全文，日期未知；CIO 只使用既存摘要線索。
- 建立 22 頁，分別為 5 來源、6 實體、2 概念、1 事件、3 寫作、4 問題與 1 綜合頁；registry 共 76 個邏輯來源，71 待處理。
- 發現：原訂促銷到期、三語促銷段落差異、FB CTA 目的地不符、修補狀態只到 2026-10-30。
- 詳情：[試行報告](reports/2026-11-01-ingest-pilot-001.md)。結果：pilot_ready_for_review，尚未全量 Ingest，沒有核准現行產品宣稱。

## [2026-11-01] lint | pilot-001 結構與語意檢查

- 初次檢查發現 TrafficShaper 頁缺少正文 inbound link，已由修補來源表格補上產品關聯。
- 最終結構檢查：22 頁、0 errors、13 warnings。警告保留 4 項待確認頁、CIO 不完整證據及歷史／過期宣稱，不代表檢查未執行。
- 八項隔離測試通過：乾淨資料、raw 修改、斷鏈、摘要冒充全文、未核准現行宣稱、重複 ID、舊索引及改寫日誌均有對應檢查。
- 操作驗證：搜尋「AgileLink 備援」優先命中產品頁；prepare-ingest 對已處理 news/56 回報三語 digest 相同，no-op。
- Agent 語意檢查與限制詳見 [試行報告](reports/2026-11-01-ingest-pilot-001.md)；[結構檢查結果](reports/2026-11-01-lint-001.json)。尚未核准任何現行產品宣稱。

## [2026-11-01] correction | Lint 報告連結建立順序

保存 lint-001 時，日誌與 Ingest 報告已引用尚未建立的報告檔，該次因此記錄 2 個連結錯誤。報告生成後重新檢查，結果為 0 errors、13 warnings。保留 lint-001 作過程紀錄，最終結果以 [lint-002](reports/2026-11-01-lint-002.json) 為準；前項「0 errors」指修正後結果，不能用 lint-001 作通過證據。

## [2026-11-01] correction | Windows 環境：工具編碼與換行

- 問題：Windows（cp932 預設編碼）下 wiki.py 讀寫中文失敗；core.autocrlf=true 且無 .gitattributes，checkout 時 raw JSON 被轉成 CRLF，lint 誤報 205 個 raw hash errors。已提交的 raw blob 與 raw_sha256 基準一致，raw 內容未被修改。
- 修正：scripts/*.py 檔案讀寫明確指定 UTF-8 與 LF，CLI 輸出改 UTF-8；新增 .gitattributes（文字檔 eol=lf，raw/** -text 保持原始位元組），並重新 checkout 工作目錄。
- 驗證：不需 PYTHONUTF8 即可執行 status／search／prepare-ingest／lint；結構檢查 0 errors、13 warnings（[lint-003](reports/2026-11-01-lint-003.json)）；8 項隔離測試通過。未變更 Wiki 內容、來源狀態或宣稱。
