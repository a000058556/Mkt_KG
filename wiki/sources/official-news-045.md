---
schema_version: "1.0.0"
id: "official-news-045"
type: "source"
title: "UGUARD 與邁達特合作公告"
summary: "合作訊息、企業定位及促銷條款並存，須分離事件時間與有效期間。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045"]
related: ["entity-uguard", "entity-metaage", "event-metaage-partnership", "issue-promotion-language"]
---

# UGUARD 與邁達特合作公告


## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/45)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/15`，`id=45`。發布日 2026-04-21，更新日 2026-09-15；內文新聞稿日期為 2026-03-26。三者分別保留，不推斷合約實際簽署日期。API 的 `created_at` 為 2026-05-25T14:45:44Z，晚於 `date` 欄位；「發布日」只是 `date` 欄位值，不能證明網頁實際上線日。

## 內容摘要

內文宣布 UGUARD 與 MetaAge 邁達特的代理合作，結合網路安全技術及在地通路服務，並以威脅情資、雲端平台、AI 網路分析與 WAN／邊界防護描述服務整合。引述管理層時涉及 DefenseCloud、AgileCloud；這些是當時公告的定位，不能據此驗證所有現行功能或人員職稱。依據：原文開頭、四大核心領域及管理層引言。

## 時效與差異

- WAN 架構強化與主動防禦強化的原訂截止日為 2026-10-31；以本次 2026-11-01 評估已過期，沒有已延長的證據。
- 汰舊換新載明至 2027-12-25。尚未到原訂截止日，不等於條件仍有效，須業務確認。
- 中文的主動防禦強化段落多出一段 AgileLink 優惠；英日對應段只描述 DefenseTrust。原文保留，詳見 [語言差異](../issues/promotion-language.md)。
- 中文「企業資安升級專案啟動」段有 DefenseTrust（全球即時黑名單、零時差）與 AgileLink（GTC DNS、DNSSEC、低軌衛星、X-View 集中報表與 AI 情資分析報告）的產品說明，英日版均無；同見 [語言差異](../issues/promotion-language.md)。
- 「零時差」及「不中斷」保留為歷史宣傳措辭，不提升為核准的量化承諾。

## 原文瑕疵（保留於 raw）

- 繁中版邁達特網址的連結文字為 `www.metaage.com`，實際連結為 `https://www.metaage.com.tw`。
- 英文版小標題截斷為「Proactive Defense Upgrade Projec」「2026 Enterprise Network Enhancement Progra」「Trade-In & Upgrade Progra」。撰稿引用時不沿用這些錯誤。

## 整合去向

[合作事件](../events/metaage-partnership.md)、[UGUARD](../entities/uguard.md)、[邁達特](../entities/metaage.md)、[合作新聞稿寫法](../writing/partnership-announcement.md)。
