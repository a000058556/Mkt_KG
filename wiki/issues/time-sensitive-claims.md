---
schema_version: "1.0.0"
id: "issue-time-sensitive-claims"
type: "issue"
title: "待確認：活動、修補進度與絕對化宣稱"
summary: "區分過期、歷史狀態及缺乏測試條件的宣傳措辭。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "official-news-056", "official-news-060", "official-news-005", "official-news-015", "official-news-023", "official-news-025", "official-news-027", "official-news-032", "official-news-033", "official-news-034", "official-news-035", "official-news-039", "official-news-041", "official-news-043", "official-news-044", "official-news-059"]
related: ["entity-agilelink", "entity-defensetrust", "event-metaage-partnership", "event-health-check-campaign", "event-cve-2026-php", "issue-threat-intel-figures"]
---

# 待確認：活動、修補進度與絕對化宣稱


## 問題清單（評估日 2026-11-01）

| 事項 | 依據 | 處理 |
|---|---|---|
| 兩項優惠原訂至 2026-10-31 | [合作來源](../sources/official-news-045.md) 活動段 | expired；延長需新證據 |
| 汰舊換新原訂至 2027-12-25 | 同上 | 尚未到期但仍待業務確認現況 |
| 產品修補進度截至 2026-10-30 | [修補來源](../sources/official-news-060.md) 表格 | historical_only；由產品／資安確認新狀態 |
| 台灣區老客戶免費企業健檢至 2026-12-31 | [news/32](../sources/official-news-032.md)、[news/34](../sources/official-news-034.md)、[news/35](../sources/official-news-035.md)、[news/39](../sources/official-news-039.md)、[news/41](../sources/official-news-041.md) | 使用者 2026-11-01 確認仍在辦理（approved_current，複審 2026-12-31），見 [健檢活動](../events/health-check-campaign.md) |
| COMPUTEX 2025 禮券、抽獎；2024 資安大會贈品 | [news/23](../sources/official-news-023.md)、[news/27](../sources/official-news-027.md) 等 | expired |
| PHP 漏洞說明與修補（截至 2026-10-30） | [news/59](../sources/official-news-059.md)、[news/60](../sources/official-news-060.md) | historical_only，見 [CVE 事件](../events/cve-2026-php.md) |
| 「不中斷」「零時差」 [備援文章](../sources/official-news-056.md)、合作文章 | 缺測試條件，不能轉成 SLA 或全威脅保證 |

## 後續處理

建議業務確認活動、產品／資安確認版本與適用條件。以上是建議角色，不代表已指定或通知任何人。只在獲得可追溯的人員確認後記入核准紀錄。現行核准記錄目前為空。

## ingest-002 補充

「零時差」「不中斷」「全面守護」「零誤判」等用語在 2024–2026 多篇出現，包括節慶文（[news/5](../sources/official-news-005.md)、[news/15](../sources/official-news-015.md)）、產品文（[news/33](../sources/official-news-033.md)、[news/41](../sources/official-news-041.md)）與合作稿；數字口徑另見 [情資數字](threat-intel-figures.md)。處理原則不變：保留為來源用語，撰稿改用有條件的說法。
