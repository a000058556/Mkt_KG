---
schema_version: "1.0.0"
id: "official-news-034"
type: "source"
title: "DefenseTrust：次世代防火牆的好幫手"
summary: "以減輕 NGFW 負載為角度介紹 DefenseTrust 與 Defense Cloud，含每 3 分鐘更新 120 萬筆情資的來源說法。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-034"]
related: ["entity-defensetrust", "concept-ngfw-complement", "concept-threat-intelligence", "concept-iso-27001"]
---

# DefenseTrust：次世代防火牆的好幫手

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/34)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/26`，`id=34`。

- API `date`：2025-11-30
- `created_at`：2026-05-25T14:45:44Z；`updated_at`：2026-09-15T09:58:32Z
- 內文日期：健檢活動「即日起至 2026 年 12 月 31 日」

## 內容摘要

依各小標：

- **新世代威脅管理－全面減輕 NGFW 工作負載**：傳統防火牆難單獨因應惡意 IP、釣魚與殭屍網路；DefenseTrust 透過全球威脅情資整合與第三方情資串接，即時比對與更新全球黑名單，「在攻擊抵達前就完成阻擋」；可「大幅降低」NGFW 工作負擔，讓防火牆專注於更複雜的威脅分析。
- **哪些企業最需要威脅情資平台？**：政府、醫療與大型企業內網；提到 ISO 27001:2022 改版與資安法規趨嚴，需要「即時」「可信」「自動化」的威脅情報平台；避免人工黑名單更新落後造成設備滿載或誤判。
- **Defense Cloud 亞洲獵捕系統**：結合欺敵技術與蜜罐，將攻擊者導向可控環境、回傳獵捕系統分析；「每 3 分鐘即時更新超過 120 萬筆全球情資」，與 DefenseTrust 交叉比對，降低誤判率、以少許人力達成防護。
- **健檢活動**：重複「台灣區老客戶免費企業健檢服務」至 2026-12-31 的段落。

## 時效與限制

- 「每 3 分鐘」「120 萬筆」是 2025-11 的來源數字，無測量日期或方法；與 [official-news-024](official-news-024.md)（2025-05：「約百萬筆」「每分/日」）不同，需標示時間並經產品確認才可引用。
- 「大幅降低」「攻擊抵達前就完成阻擋」「降低誤判率」無量化依據，是來源說法。
- 提及 ISO 27001:2022 只是背景，原文未宣稱取得認證或符合特定條款。
- 健檢活動截止 2026-12-31，以 2026-11-01 評估尚未到期，但需業務確認仍有效。
- 圖片 `dOS-network-threat-analysis.jpg`、`dOS-update-3min.jpg` 未檢視。

## 原文瑕疵

- 標題用「次世代防火牆」，小標用「NGFW」，產品名用「新世代威脅管理」，新／次世代混用；原文保留。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[補強 NGFW](../concepts/ngfw-complement.md)、[威脅情資](../concepts/threat-intelligence.md)、[ISO 27001](../concepts/iso-27001.md)。健檢段同見 [032](official-news-032.md)。
