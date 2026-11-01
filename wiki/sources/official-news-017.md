---
schema_version: "1.0.0"
id: "official-news-017"
type: "source"
title: "DefenseTrust 對應 ISO/IEC 27001:2022 新增 11 項控制"
summary: "2025 年新聞稿把 DefenseTrust 功能對應到 ISO 27001:2022 新增控制；屬合規類來源說法，未經驗證。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-017"]
related: ["concept-iso-27001", "entity-defensetrust", "concept-threat-intelligence", "entity-cloud-platforms"]
---

# DefenseTrust 對應 ISO/IEC 27001:2022 新增 11 項控制

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/17)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/43`，`id=17`，分類「台北訊息」。

- API `date`：2025-03-08
- `created_at`：2026-05-25T14:45:44Z；`updated_at`：2026-09-15T09:58:32Z
- 內文日期：「台北訊，2025年3月7日」

## 內容摘要

- 開頭段：以截至 2025 年 2 月的國內資安事件（欣興電子檔案外洩、馬偕紀念醫院無法存取病歷，各附外部新聞連結）切入；稱 DefenseTrust「涵蓋ISO/IEC 27001:2022新增之11項控制標準」並逐項列出：實體安全監控、使用雲端服務之資訊安全、營運持續之 ICT 準備、威脅情資、組態管理、資訊刪除、資料遮蔽、預防資料洩漏、活動監測、網頁過濾、安全編碼。
- 情資來源段：自建情資雲（Defense Cloud）的獵捕系統（Hunting System），整合開源威脅情資與第三方情資，提供 IP／網域情報名單，以落實零日防護。
- 組態管理與活動監測段：內建群組／用戶功能、存取者身分比對、網路活動監控與紀錄、通報。
- 預防資料外洩段：內建安全策略、流量管理（頻寬控管與流量管制）。
- 網頁過濾段：IP/URL 黑白名單、本機與第三方憑證管理、Radius 認證伺服器。
- 公司簡介：產品線列 AgileLink、Traffic Shaper、SD-WAN、DefenseTrust。

## 時效與限制

- 合規類說法：「涵蓋」11 項控制、「完美協助」「全面性安全監控」都是 2025-03 的來源說法，未說明如何對應各控制，也沒有稽核或驗證依據；不可寫成「符合 ISO 27001」或通過認證。標題用語是「符合企業……之期待」，比正文的「涵蓋」保守。
- 列出的 11 項中，正文只對威脅情資、組態管理、活動監測、預防資料洩漏、網頁過濾給出功能說明；其餘 6 項（如資訊刪除、資料遮蔽、安全編碼）無對應功能敘述，屬缺口。
- 引用的資安事件為 2025 年初的外部報導，只供時間背景。
- 與 [official-news-016](official-news-016.md) 共用 DM 圖，與 [official-news-018](official-news-018.md)、[official-news-020](official-news-020.md) 同屬 2025 年 DefenseTrust 新聞稿系列，共用公司簡介段落。

## 原文瑕疵

- 「新加坡商UGUAR NETWORKS聯絡資訊」缺字母 D；LinkedIn 連結為管理後台路徑 `/admin/feed/posts/`。
- 英文版把出處寫成 "Info Security Magazine revealed"，繁中無此歸屬；英文 "Address Book/Chart Management"、"Firewall Policy" 等功能名與繁中「群組/用戶」「安全策略」不同，記為翻譯差異。
- 圖片未下載／OCR。

## 整合去向

[ISO 27001](../concepts/iso-27001.md)、[DefenseTrust](../entities/defensetrust.md)、[威脅情資](../concepts/threat-intelligence.md)、[雲端平台](../entities/cloud-platforms.md)。
