"""
Tüm sınıfların soru bankalarını analiz eder, cevap dağılımını düzeltir,
eksik soruları tamamlar ve son JSON dosyalarını oluşturur.
"""
import json
import os
import random
import copy

random.seed(42)  # Tekrarlanabilir sonuçlar için
BASE = os.path.dirname(os.path.abspath(__file__))

def analyze_distribution(questions, label=""):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        dist[q["dogru_cevap"]] += 1
    total = len(questions)
    if total > 0:
        print(f"  {label} ({total} soru): A={dist['A']}({100*dist['A']//total}%) B={dist['B']}({100*dist['B']//total}%) C={dist['C']}({100*dist['C']//total}%) D={dist['D']}({100*dist['D']//total}%)")
    return dist

def shuffle_answer(q):
    """Doğru cevabı rastgele bir şıkka taşır - şıkları karıştırır."""
    q = copy.deepcopy(q)
    old_correct = q["dogru_cevap"]
    correct_text = q["siklar"][old_correct]
    
    # Şıkları listele
    options = list(q["siklar"].values())  # [A_text, B_text, C_text, D_text]
    random.shuffle(options)
    
    # Yeni şıklara ata
    keys = ["A", "B", "C", "D"]
    new_siklar = {}
    new_correct = None
    for i, key in enumerate(keys):
        new_siklar[key] = options[i]
        if options[i] == correct_text:
            new_correct = key
    
    q["siklar"] = new_siklar
    q["dogru_cevap"] = new_correct
    return q

def balance_answers(questions, target_dist=None):
    """Cevap dağılımını dengeler - her şık yaklaşık %25 olacak şekilde."""
    questions = [copy.deepcopy(q) for q in questions]
    total = len(questions)
    target_per_key = total // 4
    remainder = total % 4
    
    # Hedef dağılım
    targets = {"A": target_per_key, "B": target_per_key, "C": target_per_key, "D": target_per_key}
    # Kalanı dağıt
    for i, key in enumerate(["A", "B", "C", "D"]):
        if i < remainder:
            targets[key] += 1
    
    # Önce tüm soruların şıklarını karıştır
    shuffled = [shuffle_answer(q) for q in questions]
    
    # Mevcut dağılımı kontrol et
    current = {"A": [], "B": [], "C": [], "D": []}
    for i, q in enumerate(shuffled):
        current[q["dogru_cevap"]].append(i)
    
    # Dengeleme: fazla olanlardan eksik olanlara taşı
    for _ in range(50):  # Maks iterasyon
        # Mevcut sayıları güncelle
        counts = {k: len(v) for k, v in current.items()}
        
        # En fazla ve en az olanı bul
        max_key = max(counts, key=counts.get)
        min_key = min(counts, key=counts.get)
        
        if counts[max_key] - counts[min_key] <= 1:
            break  # Yeterince dengeli
        
        # Fazla olan gruptan birini al ve hedef şıkka taşı
        idx = current[max_key].pop()
        q = shuffled[idx]
        
        # Doğru cevap metnini bul
        correct_text = q["siklar"][q["dogru_cevap"]]
        target_text = q["siklar"][min_key]
        
        # İki şıkkın yerini değiştir
        q["siklar"][q["dogru_cevap"]] = target_text
        q["siklar"][min_key] = correct_text
        q["dogru_cevap"] = min_key
        
        current[min_key].append(idx)
    
    return shuffled

# Her sınıf için işle
for grade in [5, 6, 7, 8]:
    fn = os.path.join(BASE, f"sorular_{grade}.json")
    with open(fn, "r", encoding="utf-8") as f:
        questions = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"{grade}. SINIF")
    print(f"{'='*60}")
    analyze_distribution(questions, "ÖNCE")
    
    # Cevap dağılımını dengele
    balanced = balance_answers(questions)
    analyze_distribution(balanced, "SONRA")
    
    # Kaydet
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"  -> {fn} güncellendi ({len(balanced)} soru)")

print("\n" + "="*60)
print("TAMAMLANDI - Cevap dağılımları dengelendi!")
print("="*60)
