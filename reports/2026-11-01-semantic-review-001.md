# pilot-001 語意複查報告

日期：2026-11-01；範圍：pilot-001 的 5 個來源及其 22 頁 Wiki。基準 commit：5c9fed8803cea1aa7fe5c56d025f54c3983bdb6e。結果：**4 項遺漏已修正，其餘內容與來源相符；pilot 狀態仍為 pilot_ready_for_review**。

## 方法

逐頁對照 raw：官網 news/45、56、60 的 zh-TW／en／jp `content` 及 metadata、[FB 轉錄](../raw/facebook/latest_post.json)、[CIO 記錄](../raw/external/requested_sources.json) `/1`。檢查每項敘述是否有指定段落支持、日期語意、三語差異、證據狀態與 claims 是否一致。未查核外部 CVE 資料或現行產品規格。

## 確認相符

| 項目 | 結果 |
|---|---|
| news/45 日期、優惠截止日（2026-10-31／2027-12-25）、舊機型號 | 與 raw 一致 |
| news/45 中文主動防禦段多出 AgileLink 優惠 | 屬實，英日版只有 DefenseTrust |
| news/56 PBR、應用情境、功能條列 | 與 raw 一致；英日版連線種類與 PBR 一致 |
| news/60 修補版本、三項產品狀態、5.9 版 2026-09-30 停止維護、截至 10/30 | 三語一致，Wiki 轉述正確 |
| FB CTA 指向 `/products/trafficshaper`、只有相對日期 | 屬實 |
| CIO `content_text=null`，reference_only | 正確 |
| 「不中斷」「零時差」未升格為保證；approvals 為空 | 正確 |

## 發現與修正

| # | 發現 | 程度 | 處置 |
|---|---|---|---|
| 1 | news/45 繁中「企業資安升級專案啟動」段有 DefenseTrust／AgileLink 產品說明（全球即時黑名單、GTC DNS、DNSSEC、低軌衛星、X-View），英日版沒有；pilot 三語核對遺漏。news/56 的 DNS Security 定位也未整合進產品頁 | 中 | 擴充 [語言差異 issue](../wiki/issues/promotion-language.md)；[AgileLink](../wiki/entities/agilelink.md)、[DefenseTrust](../wiki/entities/defensetrust.md) 補來源說法；新增 claim-agilelink-dns-security（source_reported）及 claim-news45-zh-only-product-paragraph（needs_review） |
| 2 | news/56 繁中原文三處寫「頻寬」（英日為 broadband），Wiki 未註明即寫成「寬頻」 | 低 | [來源頁](../wiki/sources/official-news-056.md) 記錄原文用字；產品頁及 claim 註明 |
| 3 | news/45 `created_at` 2026-05-25 晚於 `date` 2026-04-21，「發布日」語意未說明 | 低 | 來源頁與 [合作事件](../wiki/events/metaage-partnership.md) 時間軸補列 |
| 4 | news/45 邁達特連結文字 `.com` 與實際 `.com.tw` 不符；英文版小標題截斷 | 低 | [來源頁](../wiki/sources/official-news-045.md) 新增原文瑕疵段；raw 不修改 |

## 檢查結果

結構 Lint：22 頁、0 errors、14 warnings（新增 1 項 needs_review claim）；見 [lint-004](2026-11-01-lint-004.json)。8 項隔離測試通過。

## 尚待使用者決策

- 驗收 pilot：摘要深度、頁面分類及寫作觀察是否符合行銷需求；確認後才將 pilot 標為 accepted 並處理其餘 71 個來源。
- 業務／行銷確認：news/45 中英日差異的正確版本、FB CTA 目的地、汰舊換新方案現況、修補進度最新狀態。
