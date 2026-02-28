#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İki batch'i birleştirip sorular.json oluşturur. Kullanım: python3 birlestir.py"""
import json, os, subprocess, sys

base = os.path.dirname(os.path.abspath(__file__))

# Batch'leri çalıştır
for s in ["gen_batch1.py", "gen_batch2.py"]:
    p = os.path.join(base, s)
    subprocess.run([sys.executable, p], check=True)

# JSON'ları oku ve birleştir
all_q = []
for f in ["batch1.json", "batch2.json"]:
    with open(os.path.join(base, f), "r", encoding="utf-8") as fh:
        all_q.extend(json.load(fh))

# Tekrarlanan soruları kontrol et (soru metnine göre)
seen = set()
unique = []
for q in all_q:
    key = q["soru"].strip()[:80]
    if key not in seen:
        seen.add(key)
        unique.append(q)

# ID'leri yeniden numaralandır
for i, q in enumerate(unique):
    q["id"] = i + 1

# sorular.json'a yaz
out = os.path.join(base, "sorular.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(unique, f, ensure_ascii=False, indent=2)

# Temizlik
for f in ["batch1.json", "batch2.json"]:
    p = os.path.join(base, f)
    if os.path.exists(p):
        os.remove(p)

# İstatistik
from collections import Counter
unite_c = Counter(q["unite"] for q in unique)
zorluk_c = Counter(q["zorluk"] for q in unique)
print(f"\n✅ Toplam {len(unique)} soru yazıldı → sorular.json")
print(f"\nÜnite dağılımı:")
for u, c in sorted(unite_c.items()):
    print(f"  {u}: {c}")
print(f"\nZorluk dağılımı:")
for z, c in sorted(zorluk_c.items()):
    print(f"  {z}: {c}")
print(f"\nGen script'leri silmek isterseniz:")
print(f"  rm gen_batch1.py gen_batch2.py birlestir.py")
