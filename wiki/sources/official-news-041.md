---
schema_version: "1.0.0"
id: "official-news-041"
type: "source"
title: "DefenseTrust 威脅資料庫介紹與老客戶健檢活動"
summary: "DefenseTrust 產品說法（80%、業界最快、每天更新等）及至 2026-12-31 的健檢活動，均屬來源說法。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-041"]
related: ["entity-defensetrust", "entity-cloud-platforms", "concept-threat-intelligence", "issue-time-sensitive-claims"]
---

# DefenseTrust 威脅資料庫介紹與老客戶健檢活動

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/41)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/19`，`id=41`。API `date` 2026-02-26；`created_at` 2026-05-25T14:45:44Z（晚於 date）；`updated_at` 2026-09-15T09:58:32Z。內文無新聞稿日期；活動期限寫「即日起至 2026 年 12 月 31 日」。 英日同 ID 為翻譯版本，不算獨立證據；圖片未下載、未 OCR，不推測圖內內容。

## 內容摘要

- 開頭段：以「傳統靜態規則難以因應」切入，宣稱 DefenseTrust 提供「最全面的 IP 和 Domain 威脅資料庫」、「有效攔截超過 80% 的已知惡意網站」、Inline 模式高速比對、「情資資料庫每天更新」、「業界最快、誤報率近乎零」、內建硬體與軟體旁路。
- 「現今企業的痛點」：特徵更新時間差、人工輸入黑名單至防火牆效率低、EOL 設備（如 IXIA）缺乏維護、ISO 27001:2022 合規要求等。
- 「DefenseTrust 核心特色」條列：全球 IP／Domain 威脅資料庫、IP 洗白名單機制（1 小時）、19 種惡意檢測引擎、Geo-IP 國別阻擋／DNS 攔截、SSL 連線判斷、XFF 代理 IP 解析、軟硬體 Bypass、X-View 報表內建 AI 情資分析報告。
- 「DefenseCloud 企業級雲端威脅情資搜尋服務」：一句話描述為 SaaS 平台、威脅情資與蜜罐獵捕系統。
- 結尾：適用政府、金融、跨國企業、大型製造業；「台灣區老客戶免費企業健檢服務」活動至 2026-12-31；公司簡介稱「於2026年成立台灣分公司」。

## 時效與限制

- 80%、「最全面」「業界最快」「誤報率近乎零」「確保服務不中斷」均為來源宣傳用語，無測試條件，不可寫成保證。英文版改為 one of the industry's most comprehensive／one of the fastest，語氣較保守（翻譯差異）。
- 本篇「每天更新」與 COMPUTEX 系列及 [news/55](official-news-055.md) 的「3 分鐘」更新說法不同，需產品端確認現行頻率。
- 健檢活動截止 2026-12-31，以 2026-11-01 判斷尚未過期，但仍須業務確認是否持續辦理及資格。
- ISO 27001:2022 僅作為客戶痛點提及，並非產品取得認證的說法。

## 原文瑕疵

- 「減少敢備故障」應為「設備」之誤，raw 保留。
- 本篇連結使用 `tw.uguardnetworks.com` 網域（defense-trust、free-enterprise-health-for-taiwan-event），與後期文章使用的 `www.uguardnetworks.com/products/...` 不同，連結現況未檢查。
- 「IP 洗白名單機制（1小時）單位」語意不清，保留原文。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[雲端平台](../entities/cloud-platforms.md)、[威脅情資](../concepts/threat-intelligence.md)、[時效事項](../issues/time-sensitive-claims.md)。同段產品說明亦見於 [news/54](official-news-054.md)。
