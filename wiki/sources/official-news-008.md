---
schema_version: "1.0.0"
id: "official-news-008"
type: "source"
title: "Traffic Shaper 部署模式：In-line 與 SPAN"
summary: "以文字說明 tOS 的 In-line 與 SPAN 兩種部署模式及各自功能。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-008"]
related: ["entity-trafficshaper", "concept-traffic-management"]
---

# Traffic Shaper 部署模式：In-line 與 SPAN

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/8)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/52`，`id=8`，分類「台北訊息」。

- API `date`：2024-08-07
- `created_at`／`updated_at`：皆為 2026-05-25T14:45:44Z
- 內文日期：無

## 內容摘要

正文是配合圖片 `tOS-deployment-simple.jpg` 的圖說：

- In-line Mode：使用者經過 L2/L3、行經防火牆到雲端，tOS 在其間管理流量；功能列為 B/W-M、QoS、AAA、Behavior Mgt、Security、Reporting。
- SPAN Mode：將經過 L2/L3 兩個 port 的流量複製一份到 tOS，tOS 只負責報表查看與產出；功能列為 Connection Logging、Reporting。

## 時效與限制

- 標題稱 Traffic Shaper，正文只稱 tOS；兩者對應關係僅由標題推得，屬推論，需確認命名。
- 正文是圖說，圖片未下載／OCR，不補寫拓撲細節。
- 功能清單為 2024-08 來源說法，未標版本。

## 原文瑕疵

- 標題「部屬」應為「部署」（保留原文）。
- 英文 "duplicated to tOS is SPAN Mode" 語法錯誤。

## 整合去向

[Traffic Shaper](../entities/trafficshaper.md)、[頻寬與流量管理](../concepts/traffic-management.md)。
