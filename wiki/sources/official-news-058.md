---
schema_version: "1.0.0"
id: "official-news-058"
type: "source"
title: "可疑 IP／Domain 的即時阻擋：DefenseTrust 情資比對"
summary: "說明 DefenseTrust 情資更新、分類比對、策略阻擋與日誌；即既有 FB 貼文所連結的官網全文。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-058"]
related: ["entity-defensetrust", "concept-threat-intelligence", "writing-social-posts"]
---

# 可疑 IP／Domain 的即時阻擋：DefenseTrust 情資比對

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/58)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/2`，`id=58`。API `date` 2026-10-27；`created_at` 2026-10-27T09:05:31Z；`updated_at` 2026-10-28T07:37:32Z。 英日同 ID 為翻譯版本，不算獨立證據；圖片未下載、未 OCR，不推測圖內內容。

## 內容摘要

- 開頭：威脅來源持續變化，關鍵是「公司防禦的威脅情資，是否持續更新？」；DefenseTrust 以持續更新的 IP／Domain 情資分類比對，命中時依企業安全策略阻擋。
- 「從威脅情資比對，到策略阻擋」四點：IP 比對、Domain 比對、策略阻擋、持續更新威脅情資。
- 「黑名單不是愈多愈好，重要的是情資能否持續更新」：流程「威脅情資更新 ⮕ 分類與比對 ⮕ 命中 ⮕ 依策略阻擋」。
- 「不只阻擋，也能從日誌掌握」：命中紀錄、相關 IP／Domain、部分連線狀況、策略處理結果。

本篇措辭相對保守：未出現 80%、3 分鐘、224 國等數字，強調「依企業所設定的安全策略」與「已識別的惡意 IP / Domain」。

## 與 Facebook 貼文的關係

[Facebook：威脅情資持續更新](facebook-threat-intelligence-update.md) 的「更多電子內容」連到本篇（news/58）。貼文的機制說明（分類比對、命中後依策略阻擋、從日誌查看）與本篇對應段落一致，是同一內容的社群摘要版，不算獨立佐證。該 FB 頁曾註記 news/58 未 Ingest，本頁補上。FB 的「了解更多 DefenseTrust」CTA 指向 TrafficShaper 的問題仍屬貼文本身；本篇兩個 CTA 均正確連到 `/products/defensetrust`。

## 時效與限制

內容為 2026-10 來源說法；「部分連線狀況」明示日誌並非完整連線紀錄，撰稿時不要擴寫。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[威脅情資](../concepts/threat-intelligence.md)、[社群短文](../writing/social-posts.md)。
