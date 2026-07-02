# 聽故事大挑戰（listen-training）

給奕霆的聽力記憶訓練工具：無圖聽故事 + 5W 提問（記憶提取 / 因果推論 / 情緒推論 / 高階應用）。

- **線上網址**：https://lminhao575-debug.github.io/listen-training/
- **架構**：純靜態（index.html + stories.json + audio/），GitHub Pages 部署，push 到 main 即上線
- **語音**：edge-tts `zh-TW-HsiaoChenNeural`，語速 -10%（8 歲適用）
- **注音**：手標於 stories.json（titleZ/textZ/nameZ，`字|注音` 空格分隔），台灣教育部標準（輕聲 ˙ 前置）

## 新增/修改故事

1. 編輯 `stories.json`（story 需含 id/topic/title/titleZ/text/refs×4，text 約 200-300 字，注意主角要有明確的行動、動機、情緒，四題才答得出來）
2. `python3 gen_audio.py --only s11`（重生指定音檔；不帶參數 = 全部重生）
3. commit + push → GitHub Pages 自動部署

## 本地測試

`python3 -m http.server 8901` → http://localhost:8901/
（注意：http.server 不支援 Range request，音檔拖曳進度會卡，正式環境 GitHub Pages 沒這問題）
