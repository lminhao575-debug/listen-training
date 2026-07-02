# 聽故事大挑戰（listen-training）

給奕霆的聽力記憶訓練工具：無圖聽故事 + 5W 提問（記憶提取 / 因果推論 / 情緒推論 / 高階應用）。

- **線上網址**：https://lminhao575-debug.github.io/listen-training/
- **架構**：純靜態（index.html + stories.json + audio/），GitHub Pages 部署，push 到 main 即上線
- **語音**：edge-tts `zh-TW-HsiaoChenNeural`，語速 -10%（8 歲適用）
- **注音**：手標於 stories.json（titleZ/textZ/nameZ，`字|注音` 空格分隔），台灣教育部標準（輕聲 ˙ 前置）

## 書架輪替規則

每個主題一次顯示 5 篇未完成的故事（依 id 排序取前 5），答完四題（localStorage 記錄）即下架、庫存遞補；已完成的收在「已聽完的故事」區可重聽。每主題庫存 8 篇，快耗完要補寫新故事。

## 新增/修改故事

1. 編輯 `stories.json`。story 需含：id/topic/title/titleZ/text/refs×4/**questions×4**。
   - text 約 200-300 字，主角要有明確的行動、動機、情緒，四題才答得出來
   - questions 四題必須是「聽力記憶」題——從故事內容才能提取答案（VK 2026-07-02 兩次校正後定案），依序 dim = 記憶提取（主旨）/細節記憶（數字・東西・地點）/因果推論/情緒推論
   - 「換作是你」開放題不進答題流程，放 story 的 extend 欄位（家長對照區的延伸聊天）
   - ⚠️ 改題目內容或順序後，音檔檔名不變但內容變了 → index.html 的題目音檔 src 版本參數（?v=N）要 +1，否則手機快取會唸出舊題
   - titleZ/textZ 注音格式：`字|注音` 空格分隔，台灣教育部標準（輕聲 ˙ 前置、誰=ㄕㄟˊ、和=ㄏㄢˋ、一/不標本調）
2. `python3 gen_audio.py`（自動補缺少的音檔：故事 {id}.mp3 + 題目 {id}q1~q4.mp3）
3. 注音驗證：pypinyin 交叉檢查會誤報大陸慣例差異，人工確認 flagged 項即可
4. commit + push → GitHub Pages 自動部署

## 本地測試

`python3 -m http.server 8901` → http://localhost:8901/
（注意：http.server 不支援 Range request，音檔拖曳進度會卡，正式環境 GitHub Pages 沒這問題）
