#!/usr/bin/env python3
"""從 stories.json 生成故事與題目語音（edge-tts 曉臻，語速 -10% 適合 8 歲）。

用法：python3 gen_audio.py [--only s01,s02]  # 不帶參數 = 全部重生
"""
import asyncio
import json
import sys
from pathlib import Path

import edge_tts

VOICE = "zh-TW-HsiaoChenNeural"
RATE = "-10%"
ROOT = Path(__file__).parent
AUDIO = ROOT / "audio"

OUTRO = "故事說完了，換你回答問題囉！"


async def synth(text: str, out: Path):
    tts = edge_tts.Communicate(text, VOICE, rate=RATE)
    await tts.save(str(out))
    print(f"  ✅ {out.name} ({out.stat().st_size // 1024} KB)")


async def main():
    only = None
    if len(sys.argv) > 2 and sys.argv[1] == "--only":
        only = set(sys.argv[2].split(","))

    data = json.loads((ROOT / "stories.json").read_text())
    AUDIO.mkdir(exist_ok=True)

    for s in data["stories"]:
        if only and s["id"] not in only:
            continue
        text = f"現在要說的故事是，{s['title']}。{s['text']}{OUTRO}"
        await synth(text, AUDIO / f"{s['id']}.mp3")

    for q in data["questions"]:
        if only and q["id"] not in only:
            continue
        await synth(q["text"], AUDIO / f"{q['id']}.mp3")


if __name__ == "__main__":
    asyncio.run(main())
