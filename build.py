#!/usr/bin/env python3
"""build.py — content.json generate karta hai (single source of truth).
Edit workflow: build_part1.py / build_part2.py / build_part3.py badlo → python3 build.py → content.json ready → frontend + terminal auto-update."""
import json, sys

from build_part1 import META, VFS, MAN, LEVELS_A
from build_part2 import LEVELS_B
from build_part3 import HUB

data = {
    "meta": META,
    "vfs": VFS,
    "man": MAN,
    "levels": LEVELS_A + LEVELS_B,
    "hub": HUB,
}

out = json.dumps(data, ensure_ascii=False, indent=1)
# validate round-trip
json.loads(out)
with open("content.json", "w", encoding="utf-8") as f:
    f.write(out + "\n")

# stats
total = withans = tasks = 0
for L in data["levels"]:
    for g in L.get("g", []):
        for it in g["i"]:
            total += 1
            if len(it) > 1 and it[1]:
                withans += 1
    tasks += len(L.get("tasks", []))
for L in data["hub"]["levels"]:
    tasks += len(L.get("tasks", []))
print(f"OK content.json | levels={len(data['levels'])} hub_levels={len(data['hub']['levels'])} "
      f"resources={len(data['hub']['resources'])} tools={len(data['hub']['tools'])} "
      f"vfs_files={len(data['vfs']['files'])} man={len(data['man'])} "
      f"topics={total} answers={withans} lab_tasks={tasks}")
