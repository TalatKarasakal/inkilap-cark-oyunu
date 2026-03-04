"""
Tum sinif soru bankalarini tek bir sorular.json dosyasinda birlestirir.
Yapi:  { "5": [...], "6": [...], "7": [...], "8": [...] }
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

combined = {}
files = {
    "5": "sorular_5.json",
    "6": "sorular_6.json",
    "7": "sorular_7.json",
    "8": "sorular_8.json",
}

for grade, fname in files.items():
    path = os.path.join(BASE, fname)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            combined[grade] = json.load(f)
        print(f"  [OK] {grade}. Sinif: {len(combined[grade])} soru yuklendi ({fname})")
    else:
        print(f"  [EKSIK] {fname} bulunamadi, atlaniyor.")

out = os.path.join(BASE, "sorular.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=4)

total = sum(len(v) for v in combined.values())
print(f"\nToplam {total} soru -> sorular.json birlestirildi.")
