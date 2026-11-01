# Schema 1.0.0

本檔是目錄、命名、欄位與證據狀態的唯一規範；AGENTS.md 為入口，操作順序見 [WORKFLOWS](../docs/WORKFLOWS.md)。修改重大行為先與使用者確認並記錄版本遷移。使用者本次決策見 [DECISIONS](../docs/DECISIONS.md)。

## 三層與目錄

| 路徑 | 責任 |
|---|---|
| `raw/official/`、`raw/facebook/`、`raw/external/` | 不可變來源快照；新增可以，既有內容不可覆寫 |
| `reading/`、`catalog/` | 前階段擷取衍生資料；不是已完成 Ingest 的 Wiki |
| `wiki/sources/` | 已讀來源的摘要、原文定位、可信程度與限制 |
| `wiki/entities/` | 公司、夥伴、產品等跨來源整合 |
| `wiki/concepts/` | 技術概念與受眾問題 |
| `wiki/events/` | 合作、活動、日期與期限 |
| `wiki/writing/` | 品牌語氣、文案結構及寫作知識；觀察與正式規範分開 |
| `wiki/syntheses/` | 跨來源分析、值得留存的 Query 成果 |
| `wiki/issues/` | 矛盾、時效、缺口與待確認事項 |
| `schema/` | 本規範、來源登錄、別名、宣稱與核准紀錄 |
| `templates/` | Wiki 與稿件範本；不視為來源 |
| `drafts/` | 待審文章，保持與知識證據隔離 |
| `reports/` | Ingest 與 Lint 報告，每次另建，不覆蓋歷史報告 |
| `docs/` | 決策、操作流程、使用方式與原始設計參考 |
| 根 `index.md`／`log.md` | 全 Wiki 內容索引／僅追加的操作紀錄 |

使用一般相對 Markdown 連結，兼容 GitHub 與 Obsidian。index、log 保持根目錄，避免多份權威入口。圖片若日後補入，保存 `raw/assets/<source-id>/<sha256>.<ext>`，另外記錄 URL、取得日與對應來源；未檢視圖片不得推測內容。

## 命名

- 新路徑採 ASCII 小寫 `kebab-case`，副檔名 `.md`；H1 與 title 使用繁中，產品專名保留原拼法。
- 來源頁優先用穩定供應者 ID：`official-news-045.md`、`external-cio-109792.md`。FB 本次檔名簡短可讀，frontmatter id 保留完整平台 ID；日後新增 FB 頁以 `facebook-<post-id>.md`。
- 主題頁使用概念名稱，不用發文日期：`agilelink.md`、`wan-resilience.md`。ID 為 `entity-agilelink`、`concept-wan-resilience` 等類型前綴，建立後保持穩定。
- 報告與草稿採 `YYYY-MM-DD-<topic>-<sequence>.md`；以執行日建立，未知發布日期填 null，不以取得日替代。
- 新來源快照用 `raw/<kind>/YYYY-MM-DD/<source-id>/<revision>.<ext>`；既有路徑全部保留。相同 URL 的內容更新是新修訂，不覆蓋舊快照。
- 同一文章三語共享來源 ID，variants 分別記錄；譯文不是獨立佐證。別名依 `aliases.json` 查找；只統一檢索名稱，引用原文保留原拼法。
- 移動／拆分 Wiki 頁須同步全數 inbound links、registry、aliases、index；來源歷史與 log 仍可追溯。

## Wiki frontmatter

每個 `wiki/**/*.md` 使用 `---` 包住 YAML frontmatter。為免依賴第三方套件，本版只接受一行一欄位、值為 JSON literal 的 YAML 子集（字串、陣列、null 等），例如 `sources: ["official-news-045"]`。

| 欄位 | 規則 |
|---|---|
| schema_version | `1.0.0` |
| id | 全 Wiki 唯一且穩定 |
| type | source / entity / concept / event / writing / synthesis / issue |
| title / summary | 繁中標題／一行用途摘要 |
| language | `zh-TW` |
| status | 下表所列證據狀態；不等於人員核准 |
| created / updated | ISO 日期；created 不變，實質變更更新 updated |
| sources | source-registry 中的來源 ID 陣列；至少一個 |
| related | 已存在的 Wiki page ID 陣列；每頁至少一個 |

正文以主題需要分節；來源頁必須有原文路徑＋JSON Pointer／穩定 ID、時間、摘要與限制。綜合頁的具體事實旁附來源頁連結及段落名稱，來源頁再連 raw。圖片、生成摘要與缺文狀態須保留。新增無內容的佔位頁不算完成 Ingest。

## 證據狀態

| 狀態 | 說明 |
|---|---|
| source_reported | 來源曾如此描述；未證實現況 |
| historical_only | 只供歷史引用，保留截至時間 |
| inferred | Agent 整理／推論／寫作觀察；正文說明依據 |
| reference_only | 僅 metadata、摘要或不完整線索，不能冒充全文 |
| needs_review | 矛盾、缺口或需人員確認 |
| approved_current | 有人員核准及明確適用範圍／期限，需 approvals.json 支持 |
| expired | 已超過明確有效期 |
| superseded | 有新依據取代，保留歷史及新頁連結 |

一頁可涵蓋多種宣稱；頁面狀態是整體提示，不讓核准自動擴及每一句。時間敏感、數字、性能與正式品牌規則在 `claims.json` 逐項記錄；正文中的操作規則以使用者決策為依據，與產品事實分開。

## 來源登錄與重複 Ingest

`source-registry.json` 為來源處理進度的唯一依據。每筆含 id、kind、title、url、published_at、completeness、provenance、variants、ingest_status、source_page。variants 保存檔案 path、JSON Pointer、file_sha256 與 canonical record_sha256；後者以 UTF-8、sort_keys=true、ensure_ascii=false、separators=(',',':') 的 JSON 計算。

- ingest_status：pending / ingested / reference_only。前者仍待讀取，後兩者均須有來源頁。
- 完成後記錄 ingested_at、ingest_run、ingested_record_sha256。相同 digest 重跑屬 no-op，不新增重複頁；回報即可。新修訂須保留舊 variants 於 `revisions` 後再更新當前 variants，並重讀受影響頁。
- 初次 pilot 為 5 個邏輯來源（4 個全文、1 個摘要線索），不是 5 個 API 檔，也不是所有 76 筆來源已處理。
- 新 raw 入庫後將檔案 SHA 加入 raw_sha256 基準；既有基準值不可藉重算來掩蓋修改。

## 宣稱與人員核准

`claims.json` 欄位：id、statement、status、sources、locator、page_id、as_of、valid_until。as_of 是來源／評估時間，valid_until 只在有明確期限時填入，未知為 null。超過期限的核准需重新審視。

`approvals.json` 只記錄明確的人員確認，欄位含 claim_id、approved_by、approved_at、review_due、scope、evidence_path。evidence_path 指向保存使用者確認或核准原稿的新 raw 記錄。`approved_by` 不得填 Agent 自己。核准只套用所列宣稱、範圍與期限。首次為空；同意建置知識庫不代表核准歷史產品宣稱。

## 草稿與日誌

草稿前文必須顯示 `status: draft`（frontmatter）、受眾、通路、目標、來源及待確認項目；範本見 templates。草稿不是 source-registry 可使用的證據，經確認的新事實需保存獨立的人員來源。

log 僅追加：`## [YYYY-MM-DD] <schema|ingest|query|lint|correction> | <摘要>`，另記 run ID、影響檔案／來源、結果與未解事項。簡單 Query 只記必要的問題摘要，不保存秘密或個人敏感內容。提交前對照舊版本，舊 log 必須是新 log 的完整前綴。
