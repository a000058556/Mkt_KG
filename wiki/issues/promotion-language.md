---
schema_version: "1.0.0"
id: "issue-promotion-language"
type: "issue"
title: "待確認：news/45 中英日內容差異"
summary: "中文版多出產品說明段及主動防禦段的 AgileLink 條件，英日版皆無。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045"]
related: ["event-metaage-partnership", "writing-partnership-announcement", "entity-agilelink", "entity-defensetrust"]
---

# 待確認：news/45 中英日內容差異


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

兩處均確認存在文案差異；尚不能判定中文多貼／新增、英日漏譯或內容原本就不同。請業務／行銷確認原始方案與產品說明，Agent 不自行選擇正確版本。兩項活動均已過原訂 2026-10-31 截止日，不能因修正文案就恢復為有效優惠。相關頁：[合作事件](../events/metaage-partnership.md)。
