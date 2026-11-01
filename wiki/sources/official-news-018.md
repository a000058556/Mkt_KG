---
schema_version: "1.0.0"
id: "official-news-018"
type: "source"
title: "DefenseTrust 情資雲與 Inline 部署新聞稿"
summary: "介紹 Defense Cloud 蜜罐／欺敵、OSINT 與第三方情資整合、DPDK 與旁路機制；含 >80% 與零誤判說法。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-018"]
related: ["entity-defensetrust", "concept-threat-intelligence", "entity-cloud-platforms", "concept-ngfw-complement"]
---

# DefenseTrust 情資雲與 Inline 部署新聞稿

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/18)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/42`，`id=18`，分類「台北訊息」。

- API `date`：2025-03-18
- `created_at`：2026-05-25T14:45:44Z；`updated_at`：2026-09-15T09:58:32Z
- 內文日期：繁中「台北訊，2025年3月10日」；英文 "New Taipei City, Taiwan (March 11, 2025)"，地點與日期皆不同，以繁中為準並記為差異。

## 內容摘要

- 開頭：以欣興遭勒索軟體攻擊、馬偕受 CrazyHunter 勒索軟體入侵為背景；稱有別於次世代防火牆的手動更新與 IP 資料庫侷限，DefenseTrust 自動、快速整合全球威脅情資，協助實現零時差攻擊防禦。
- 「新世代情資雲（Defense Cloud）」小節：自建情資雲與獵捕系統以蜜罐（Honeypot）設誘餌、以欺敵技術（Deception Technology）誘導攻擊者，用以識別未明攻擊；再整合 OSINT 及第三方情資（如 X-Force），稱可攔截「＞80%已知惡意網站」，並「零誤判地阻擋惡意IP及SSL加密連線」。
- 「快速、輕易、直觀地部署資安防護」小節：Inline Mode 建置，採 DPDK 提升封包雙向轉發、Non-SQL Database 加快比對、降低延遲；內建硬體旁路與軟體旁路，減少設備故障或電源不足造成的停機。
- 公司簡介同 news/17、news/20。

## 時效與限制

- 「＞80%」「零誤判」「徹底避免」「大幅降低延遲」為 2025-03 的來源說法，沒有測試基準或期間；不可寫成保證。英文版改寫為 "stop any single malicious IP"，未保留「零誤判」，屬翻譯差異。
- 與 NGFW 的比較是來源自述定位，不構成對特定 NGFW 產品的事實評比。
- 「＞80%」與 [official-news-020](official-news-020.md) 一致，兩篇同屬官網新聞稿系列，不互為獨立佐證。

## 原文瑕疵

- 「操作部建」應為「部署」；「新加坡商UGUAR NETWORKS」缺字母 D；LinkedIn 連結為管理後台路徑。
- 封面圖檔名為 `tOS-news-banner.png`（tOS 系列命名）而內容是 DefenseTrust；只記錄檔名，未檢視圖片。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[威脅情資](../concepts/threat-intelligence.md)、[雲端平台](../entities/cloud-platforms.md)、[補強 NGFW／EDR](../concepts/ngfw-complement.md)。
