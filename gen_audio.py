#!/usr/bin/env python3
"""從 stories.json 生成故事與題目語音（edge-tts 曉臻，語速 -10% 適合 8 歲）。

每篇故事產出：{id}.mp3（故事）+ {id}q1~q4.mp3（四題）。

用法：
  python3 gen_audio.py            # 只補缺少的音檔
  python3 gen_audio.py --force    # 全部重生
  python3 gen_audio.py --only s01,s02
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


async def synth(text: str, out: Path, force: bool):
    if out.exists() and not force:
        return False
    tts = edge_tts.Communicate(text, VOICE, rate=RATE)
    await tts.save(str(out))
    print(f"  ✅ {out.name} ({out.stat().st_size // 1024} KB)")
    return True


async def main():
    force = "--force" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))

    data = json.loads((ROOT / "stories.json").read_text())
    AUDIO.mkdir(exist_ok=True)

    made = 0
    for s in data["stories"]:
        if only and s["id"] not in only:
            continue
        text = f"現在要說的故事是，{s['title']}。{s['text']}{OUTRO}"
        made += await synth(text, AUDIO / f"{s['id']}.mp3", force)
        for i, q in enumerate(s["questions"], 1):
            made += await synth(q["text"], AUDIO / f"{s['id']}q{i}.mp3", force)
    print(f"完成，共生成 {made} 個音檔")


if __name__ == "__main__":
    asyncio.run(main())
