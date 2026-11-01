---
schema_version: "1.0.0"
id: "official-news-020"
type: "source"
title: "DefenseTrust：補強 NGFW 與 EDR 的情資方案"
summary: "以 Akira 攻擊無 EDR 攝影機為例，說明 DefenseTrust Inline 情資阻斷、情資規模與 X-View 報表。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-020"]
related: ["concept-ngfw-complement", "entity-defensetrust", "entity-cloud-platforms", "concept-threat-intelligence"]
---

# DefenseTrust：補強 NGFW 與 EDR 的情資方案

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/20)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/40`，`id=20`，分類「台北訊息」。

- API `date`：2025-04-08
- `created_at`：2026-05-25T14:45:44Z；`updated_at`：2026-09-15T09:58:32Z
- 內文日期：無

## 內容摘要

- 開頭：引英國資安公司 S-RM 揭露勒索軟體 Akira 透過缺乏 EDR 的 Linux 網路攝影機侵入企業內網，指出萬物連網下連網裝置與單一 EDR 的相容性問題。
- 方案：自建情資雲（Defense Cloud）主動蒐集威脅情資黑名單，即時匯入 DefenseTrust 主機進行惡意連網偵測阻斷；Inline 部署，Non-SQL Database 加快比對，「可同時比對100＋萬筆名單」。
- 與 NGFW 比較：NGFW 需手動更新黑名單，DefenseTrust 自動即時判別；Defense Cloud 整合、比對全球約 600 萬筆 OSINT 及第三方情資（如 X-Force），提供 13 種威脅情資分類（約 100 萬筆），稱可攔截「＞80% 已知惡意網站」。
- X-View 報表：依日／週／月／年查詢用戶／群組活動與阻斷紀錄，可匯出 PDF/CSV/HTML。
- 公司簡介同 news/17、news/18。

## 時效與限制

- 600 萬、100 萬、13 類、＞80% 皆為 2025-04 的來源說法，無統計時間點與方法；數字會隨時間變動，不可作現行規格。
- 英文版的數字歸屬不同：13 類約 100 萬筆來自 UGUARD Defense Cloud，約 600 萬筆來自開源／第三方；繁中則是比對 600 萬筆後「提供」13 類約 100 萬筆。依決策 Q8 以繁中為準，記為翻譯差異，撰稿前需人員確認。
- 標題「超越」NGFW 與 EDR 是比較性宣傳；正文論述是補足 EDR 覆蓋不到的裝置與 NGFW 手動更新的不足，撰稿宜用「補強」而非「取代／超越」（Agent 建議）。
- 「徹底防堵」為絕對化用語。

## 原文瑕疵

- 圖片 `DefenseCloud-flowchart.png` 未下載／OCR，不推測流程圖內容。

## 整合去向

[補強 NGFW／EDR](../concepts/ngfw-complement.md)、[DefenseTrust](../entities/defensetrust.md)、[雲端平台](../entities/cloud-platforms.md)、[威脅情資](../concepts/threat-intelligence.md)。
