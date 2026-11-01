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

## [2026-11-01] correction | pilot-001 語意複查與修正

- 範圍：pilot-001 五個來源、22 頁逐頁對照 raw 三語原文；主要事實、日期、修補表、CTA 與證據分級均相符。
- 修正：news/45 繁中獨有的產品說明段（DefenseTrust 全球黑名單；AgileLink GTC DNS、DNSSEC、低軌衛星、X-View）補入語言差異 issue 與產品頁；news/56 DNS Security 定位補入 AgileLink；記錄「頻寬」原文用字、news/45 created_at、連結與英文標題瑕疵。
- claims：更新 claim-agilelink-multiwan；新增 claim-agilelink-dns-security（source_reported）、claim-news45-zh-only-product-paragraph（needs_review）。
- 結果：0 errors、14 warnings（[lint-004](reports/2026-11-01-lint-004.json)）；詳見 [語意複查報告](reports/2026-11-01-semantic-review-001.md)。pilot 仍為 pilot_ready_for_review，未核准任何現行宣稱。

## [2026-11-01] schema | 決策 Q8／Q9：繁中為主要來源，pilot-001 驗收

- 依據：使用者表示「基本上是中文語系為主要來源」及「開始處理71來源」。
- 變更：DECISIONS 新增 Q8／Q9；Schema 命名段、WORKFLOWS Ingest 步驟 1、3 與 AGENTS 目前階段同步更新。未改欄位、目錄或狀態定義，schema_version 維持 1.0.0。
- 套用：news/45 三語差異以繁中為準，issue-promotion-language 改為 historical_only；claim-news45-zh-only-product-paragraph 改 source_reported；繁中主動防禦段疑似重複貼上的觀察保留。產品宣稱仍未核准。
- pilot-001 ingest-runs 狀態改為 accepted；其餘 71 個來源開始分批 Ingest。

## [2026-11-01] ingest | ingest-002：其餘 71 個來源

- run：ingest-002；授權：使用者「開始處理71來源」（決策 Q9）；繁中為主要來源（決策 Q8）。
- 來源：官網 57 篇（52 全文、5 篇僅圖片或極短記 reference_only）、外部 14 筆（全部 reference_only）；登錄表 pending 0，全庫 56 ingested、20 reference_only。
- 頁面：新增 71 來源頁、27 主題頁；更新 16 既有頁；claims 12→39；共 120 頁。
- 發現：情資數字不一、英日翻譯錯誤、職稱與設立日不一致、ISO／NGFW 用語過強、健檢活動至 2026-12-31、AgileShaper 狀態未知。
- 詳見 [ingest-002 報告](reports/2026-11-01-ingest-002.md)、[lint-005](reports/2026-11-01-lint-005.json)。未核准任何現行宣稱；語意檢查為抽查。

## [2026-11-01] ingest | approval-001：使用者確認情資頻率與健檢活動

- 來源：human-2026-11-01-001，使用者原話「情資是每小時更新」「健檢活動還有在辦」，存為新 raw（raw/human/2026-11-01/human-2026-11-01-001/r1.json）並加入 raw 雜湊基準。
- 核准：claim-threat-intel-hourly（approved_current，複審 2027-05-01）；claim-health-check-campaign 改 approved_current（複審 2026-12-31）。舊的更新頻率矛盾 claim 改 superseded。
- 頁面：情資數字 issue 改為只追蹤筆數與成效數字；健檢活動頁 approved_current；DefenseTrust、雲端平台、時效 issue 同步更新。
- 範圍限制：未確認每小時涵蓋的產品／方案、情資筆數與攔截率；健檢資格與名額未確認。

## [2026-11-01] correction | approval-002：情資請求與更新頻率澄清

- 來源：human-2026-11-01-002，使用者原話「每3分鐘是dt的情資請求頻率，情資最晚是每小時更新」，存為新 raw 並加入雜湊基準。
- 核准：新增 claim-threat-intel-cadence（approved_current，複審 2027-05-01）；claim-threat-intel-hourly 改 superseded，原核准紀錄保留為歷史。
- 撰稿規則：可寫「DefenseTrust 每 3 分鐘請求情資、情資最晚每小時更新」，不可寫「情資每 3 分鐘更新」。
- 更新：情資數字 issue、DefenseTrust、雲端平台、human-2026-11-01-001 來源頁。

## [2026-11-01] correction | approval-003／004：情資量級與攔截率確認

- 來源：human-2026-11-01-003「最新情資保持在百萬」；human-2026-11-01-004「攔截超過 80%才是正確描述」。兩筆原話各存為新 raw 並加入雜湊基準。
- 核准：新增 claim-threat-intel-volume-current（approved_current）；claim-defensetrust-block-rate 改 approved_current；複審皆 2027-05-01。claim-threat-intel-volume 改 superseded，224 國覆蓋另立 claim-threat-intel-coverage（needs_review）。
- 撰稿規則：可寫「最新情資保持在百萬筆等級」「有效攔截超過 80% 已知惡意網站」；千萬、億級、約 600 萬不作現行依據；零誤判與 224 國仍待確認。
- 更新：情資數字 issue、DefenseTrust、雲端平台。

## [2026-11-01] correction | approval-005：224 國核准、零誤判禁用

- 來源：human-2026-11-01-005，使用者原話「涵蓋 224 個國家正確，零誤判／誤報率近乎零不可用可能被過度解釋」，存為新 raw 並加入雜湊基準。
- 核准：claim-threat-intel-coverage 改 approved_current（複審 2027-05-01）。
- 禁用：claim-defensetrust-zero-false-positive 改 historical_only，新內容不可使用「零誤判」「誤報率近乎零」。
- 情資數字 issue 全部項目已處理，頁面改 approved_current；DefenseTrust、雲端平台同步更新。

## [2026-11-01] correction | approval-005 頁面狀態更正

- 前一筆記錄「頁面改 approved_current」不正確：Lint 要求 approved_current 頁面的所有 claims 都已核准，而 issue-threat-intel-figures 仍掛有 superseded 與 historical_only 的歷史 claims。
- 實際處理：頁面狀態為 source_reported；各項核准由 claim-threat-intel-cadence、claim-threat-intel-volume-current、claim-defensetrust-block-rate、claim-threat-intel-coverage 個別承載。

## [2026-11-01] correction | approval-006：AgileShaper 開發狀態

- 來源：human-2026-11-01-006，使用者原話「AgileShaper目前開發中，預計明年下半年發布」，存為新 raw 並加入雜湊基準；「明年下半年」依說話日期解讀為 2027 年下半年。
- 核准：claim-agileshaper-status（approved_current，複審 2027-05-01）；原 Coming Soon claim 維持 historical_only 並指向新紀錄。
- 範圍：不可寫成已上市或確定日期；與 TrafficShaper 關係、最終功能、時程可否對外公開未確認。

## [2026-11-01] ingest | approval-007／008、ingest-003：汰舊換新、AgileShaper 定位與官網夥伴現況

- 使用者原話存為新 raw：human-2026-11-01-007「汰舊換新方案還在辦，代理商狀況請去官網及時確認」；human-2026-11-01-008「AgileShaper是 TrafficShaper得上位版」。
- 核准：claim-tradein-promotion 改 approved_current；新增 claim-agileshaper-relation；複審皆 2027-05-01。
- ingest-003：依指示擷取官網 /api/featured-partners 三語，存為 raw/official/2026-11-01/official-featured-partners/（含擷取紀錄），登錄來源並建立 entity-channel-partners。官網列出邁達特、敦新、創泓、INNOTEL、Sysnect、SecureOne；朔宇未列，未推論終止。
- claim-channel-partners 依官網快照更新（source_reported，as_of 2026-11-01）；邁達特、Innotel、朔宇、UGUARD、汰舊換新相關頁同步更新；新增 8 個別名。

## [2026-11-01] correction | approval-009：朔宇除名、Jason Yen 職稱、舊文章不修改（決策 Q10）

- 來源：human-2026-11-01-009，使用者原話「朔宇已從代理商中除名，Jason Yen是公司老闆不用特別描述，舊文章不修改」，存為新 raw 並加入雜湊基準。
- 核准：claim-shuoyu-removed、claim-jason-yen-role（approved_current，複審 2027-05-01）；claim-executive-titles 改 superseded；claim-translation-errors 改 historical_only；claim-channel-partners 更新朔宇狀態。
- 決策 Q10：官網既有文章不修改；問題只記錄在 Wiki，新稿以核准口徑為準。翻譯差異 issue 改 historical_only。
- 更新：朔宇、通路夥伴、朔宇合作、UGUARD、內容不一致、翻譯差異、情資數字頁。

## [2026-11-01] query | DefenseTrust 10 月時事推廣文三篇草稿

- 問題：依 10 月最新時事撰寫 DefenseTrust 推廣文章三個範例。
- 時事來源：iThome〈資安週報 1019～1022〉2026-10-23（微軟打擊網釣服務、Talos 揭露 UAT-11985 活動邀請網釣、Symantec 揭露 APT28 HookEdge 反向連線），2026-11-01 讀取；原始廠商報告未直接核對。PHP2Shell 疑與 UGUARD 自家產品受影響的 CVE 同一事件，未採用。
- 產出：drafts/2026-11-01-defensetrust-october-001（官網文）、002（社群貼文）、003（客戶 EDM），status draft，只使用 approved_current 口徑並列出待確認欄位。未對外發布。

## [2026-11-02] query | 新增時事多渠道撰稿提示詞範本

- 依使用者要求，把現場展示用的提示詞存為 templates/multichannel-campaign-prompt.md，渠道為官網文章、Facebook、LINE（IG 已改為官網文章）。
- 提示詞要求 AI 只使用 approved_current 的說法、不得編造時事與連結、附查核表，並把產出存入 drafts。本檔是範本，不是來源。
- 在產品文章寫法頁加上連結。
