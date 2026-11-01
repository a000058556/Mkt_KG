---
schema_version: "1.0.0"
id: "official-news-001"
type: "source"
title: "AgileLink 作為 FortiWAN 替代方案的短文"
summary: "以 FortiWAN 為標題切入，介紹 AgileLink NGWM 的多線路整合與故障移轉說法；無規格或測試條件。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-001"]
related: ["entity-agilelink", "concept-legacy-replacement", "concept-wan-resilience", "writing-product-article"]
---

# AgileLink 作為 FortiWAN 替代方案的短文

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/1)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/59`，`id=1`，分類「台北訊息」，作者 UGUARD NETWORKS。

- API `date`：2024-02-21
- `created_at`／`updated_at`：皆為 2026-05-25T14:45:44Z（資料匯入時間，不代表原始上線日）
- 內文日期：無

英日版同 ID 為翻譯版本，不算獨立佐證。

## 內容摘要

標題「不必擔心沒有FortiWAN，交給我們一次搞定!!」；正文本身未再提及 FortiWAN，只介紹「AgileLink New Generation WAN Management (NGWM) 新世代廣域網路管理」。依據正文單一段落：

- 提供虛擬與實體線路整合，協助管理者整併多種線路，並在不同實體辦公室間建立虛擬連線頻寬，以增進關鍵流量的速率、穩定性與品質。
- 線路故障時自動選擇品質較好的線路；具線路狀態偵測，異常時將該服務流量導向正常線路。
- 透過域名解析與線路狀態偵測整合，維持企業服務持續營運。

## 時效與限制

- 「即便使用者正在使用網路電話，也不會有任何中斷或延遲的感覺」是 2024 年的來源說法，沒有切換時間、測試環境或條件；不可寫成零中斷保證。
- 標題暗示可替代 FortiWAN，但正文未說明相容性、移轉方式或 FortiWAN 狀態；替代定位只能作為歷史行銷角度引用。
- 圖片 `news-fortiwan.jpg` 未下載／OCR，不推測圖內內容。
- 英日版內容與繁中一致（重點核對）。

## 整合去向

[AgileLink](../entities/agilelink.md)、[舊設備替代與汰舊換新](../concepts/legacy-replacement.md)、[WAN 韌性](../concepts/wan-resilience.md)、[產品文章寫法](../writing/product-article.md)。
