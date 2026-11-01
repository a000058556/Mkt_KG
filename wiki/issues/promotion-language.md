---
schema_version: "1.0.0"
id: "issue-promotion-language"
type: "issue"
title: "紀錄：news/45 中英日內容差異"
summary: "中文版多出產品說明段及主動防禦段 AgileLink 條件；依決策 Q8 以繁中為準。"
language: "zh-TW"
status: "historical_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045"]
related: ["event-metaage-partnership", "writing-partnership-announcement", "entity-agilelink", "entity-defensetrust"]
---

# 紀錄：news/45 中英日內容差異


## 精確位置

[繁中 API](../../raw/official/api/news-zh-TW.json)、[英文 API](../../raw/official/api/news-en.json)、[日文 API](../../raw/official/api/news-jp.json) 各 `/data/15/content`，同為 news/45。

## 差異一：主動防禦優惠條件

中文「主動防禦強化專案」下先出現 AgileLink 2 年保固、加贈 1 年及 60 天 DefenseCloud，再接 DefenseTrust 1 年加贈 1 年。英文 Proactive Defense Upgrade 及日文 プロアクティブ防御強化 的對應段只寫 DefenseTrust。

## 差異二：中文獨有的產品說明段

中文「UGUARD NETWORKS企業資安升級專案啟動」標題下、活動方案之前有一段產品說明，英日版均無對應內容（2026-11-01 語意複查發現，pilot-001 三語核對時遺漏）：

- DefenseTrust：「整合全球即時黑名單與情資來源，提供零時差防禦能力」。
- AgileLink：「支援 GTC DNS 與 DNSSEC 保護機制，並可整合多線路與低軌衛星技術，確保企業連線穩定不中斷」，以及透過「X-View 集中報表與 AI 情資分析報告」掌握風險。

這些是單一語言版本的來源說法，已收錄於 [AgileLink](../entities/agilelink.md) 與 [DefenseTrust](../entities/defensetrust.md)，標為 source_reported；「零時差」「不中斷」仍依 [時效及宣稱事項](time-sensitive-claims.md) 處理。

## 判斷與處置

2026-11-01 使用者確認官網以繁中為主要來源（[決策 Q8](../../docs/DECISIONS.md)）。因此兩處差異均以繁中版為準，英日版視為翻譯缺漏，不再阻擋使用；本頁保留為歷史差異紀錄。

仍保留的觀察：繁中「主動防禦強化專案」的 AgileLink 文字與「WAN 架構強化專案」逐字相同，可能是重複貼上；兩項活動均已過原訂 2026-10-31 截止日，此疑點不影響現行撰稿，也不能因修正文案就恢復為有效優惠。以繁中為準不等於核准其中的產品宣稱。相關頁：[合作事件](../events/metaage-partnership.md)。
