# 資料欄位與後續使用

## 官網原始記錄

`raw/official/api/news-{language}.json` 保存 API 回應。每篇記錄包含 id、title、summary、content（HTML）、author、date、created_at、updated_at、image、category 等原有欄位。未改寫原文，未自行翻譯。原始內容即使有錯字、失效連結、過期活動或過時規格也保留。

`catalog/official_records.json` 提供可定位的 raw_path 與 JSON Pointer（raw_record_pointer），以及 source_url、published_at、updated_at、requested language、reading_path、正文 hash。record_id 形式為 `official-news-060-zh-TW`，跨語言使用 source_id 關聯。

## 完整性狀態

| status | 意義 | 可否當作全文 |
|---|---|---|
| api_full_html | 官網 API 原有正文 | 可；圖片內文字除外 |
| full_visible_post_text | Facebook 展開後可見正文轉錄 | 可用於該篇文字，不代表歷史清單完整 |
| official_curated_reference_only | 官網列出的外部來源資料 | 否 |
| metadata_and_generated_summary_only | 外部來源資訊與生成短摘要 | 否 |

圖片只收錄 URL，catalog/assets.json 的 download_status=url_only。若需離線展示原圖，必須另補圖檔；不可把未 OCR 的圖片宣稱為已擷取文字。

## 建議下一階段

1. 原始資料保持不可變，另建 normalized/chunks 層；不要在 raw 直接改寫。
2. 建立來源 ID、文章 ID、語言、發布與更新時間、來源網址和段落位置的映射。
3. 中文現場展示可先用繁中 60 篇；英文／日文同一 ID 歸為同源版本。
4. 依正文雜湊處理相同內容；跨平台相似文章僅建立關聯，不丟掉來源證據。
5. 摘要與全文分開檢索；補齊全文前不得以摘要作精確引述。
6. 生成文章時附上引用清單、使用的歷史資料時間，以及需要人員確認的最新產品與活動資訊。

沒有提供向量資料庫、模型金鑰或已上線應用；此倉庫是下一階段建置的資料基礎。
