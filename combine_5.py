"""Tüm 5. sınıf batch JSON dosyalarını birleştirip sorular_5.json oluşturur."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
all_q = []

for part in ["sorular_5_a.json", "sorular_5_b.json", "sorular_5_c.json", "sorular_5_d.json"]:
    path = os.path.join(BASE, part)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_q.extend(data)
        print(f"  {part}: {len(data)} soru")

# Ek sorular (200+ ye ulaşmak için)
U1 = "Ünite 1 – Birlikte Yaşamak"
U2 = "Ünite 2 – Evimiz Dünya"
U3 = "Ünite 3 – Ortak Mirasımız"
U4 = "Ünite 4 – Yaşayan Demokrasimiz"
U5 = "Ünite 5 – Hayatımızda Ekonomi"
U6 = "Ünite 6 – Teknoloji ve Sosyal Bilimler"

ek = [
    {"unite": U1, "konu": "Gruplar ve Roller", "yil": 2024, "zorluk": "Orta",
     "soru": "Bir sınıfta öğrenciler bilim fuarı için takımlar kurmuştur. Her takımda biri deney yapıyor, biri rapor yazıyor, biri sunum hazırlıyor.\n\nBu uygulama aşağıdakilerden hangisinin yararını gösterir?",
     "siklar": {"A": "Bireysel çalışmanın", "B": "İş bölümü ve ekip çalışmasının", "C": "Rekabetin", "D": "Ezberin"},
     "dogru_cevap": "B", "aciklama": "Farklı görevlerin paylaşılması iş bölümü ve ekip çalışmasının faydasını gösterir."},
    {"unite": U2, "konu": "Doğal ve Beşeri Değişim", "yil": 2024, "zorluk": "Orta",
     "soru": "Bir nehrin taşkın alanına yapılan binalar her yıl sel tehlikesiyle karşı karşıyadır.\n\nBu sorunu önlemenin en etkili yolu hangisidir?",
     "siklar": {"A": "Nehri tamamen kurutmak", "B": "Taşkın alanlarına yapılaşmaya izin vermemek", "C": "Binaları daha yükseğe yapmak", "D": "Nehri beton kanala almak"},
     "dogru_cevap": "B", "aciklama": "Taşkın alanlarına yapılaşma izni vermemek sel riskini önlemenin en etkili yoludur."},
    {"unite": U3, "konu": "Anadolu'da İlk Toplumlar", "yil": 2023, "zorluk": "Zor",
     "soru": "Troy (Truva) antik kentinde yapılan kazılarda 9 farklı yerleşim katmanı bulunmuştur.\n\nBu durum aşağıdakilerden hangisini gösterir?",
     "siklar": {"A": "Kent bir kez iskân edilmiş sonra terk edilmiştir", "B": "Aynı bölge binlerce yıl boyunca farklı toplumlar tarafından iskân edilmiştir", "C": "Kent sadece savaş amaçlı kullanılmıştır", "D": "Tek bir uygarlık burada yaşamıştır"},
     "dogru_cevap": "B", "aciklama": "9 farklı yerleşim katmanı aynı bölgenin uzun süre boyunca farklı topluluklar tarafından kullanıldığını gösterir."},
    {"unite": U4, "konu": "Etkin Vatandaş Olmak", "yil": 2024, "zorluk": "Zor",
     "soru": "Bir öğrenci okul bahçesinde gördüğü kirliliği;\nI. Fotoğraflamış\nII. Okul müdürüne rapor sunmuş\nIII. 'Temiz Okul' afişleri hazırlayarak farkındalık oluşturmuş\n\nBu öğrencinin davranışları;\nA. Sorumluluk bilinci\nB. Demokratik katılım\nC. Çevre duyarlılığı\nkavramlarından hangileriyle ilişkilidir?",
     "siklar": {"A": "Yalnız A", "B": "A ve B", "C": "B ve C", "D": "A, B ve C"},
     "dogru_cevap": "D", "aciklama": "Sorunla ilgilenme sorumluluk, yetkililere bildirme demokratik katılım, çevre afiş çalışması duyarlılık göstergesidir."},
    {"unite": U5, "konu": "Kaynakları Verimli Kullanma", "yil": 2023, "zorluk": "Zor",
     "soru": "Bir şehirde;\n- Çatılara güneş paneli kurulmuş\n- Otobüslere elektrikli motorlar takılmış\n- Bisiklet park alanları artırılmış\n\nBu uygulamalar;\nI. Hava kirliliğini azaltır\nII. Fosil yakıt tüketimini düşürür\nIII. Ulaşım süresini uzatır\nsonuçlarından hangilerine yol açar?",
     "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
     "dogru_cevap": "B", "aciklama": "Güneş paneli, elektrikli otobüs ve bisiklet hem kirliliği hem fosil yakıt tüketimini azaltır."},
    {"unite": U6, "konu": "Teknolojik Aletlerin Bilinçli Kullanımı", "yil": 2024, "zorluk": "Zor",
     "soru": "Bir öğrenci;\n- Şifresini arkadaşıyla paylaşmış\n- Bilmediği bir uygulamayı indirmiş\n- Ekran süresini 8 saate çıkarmış\n\nBu öğrencinin davranışlarından hangileri dijital güvenlik açısından risklidir?",
     "siklar": {"A": "Yalnız ilki", "B": "İlk ikisi", "C": "Son ikisi", "D": "Hepsi"},
     "dogru_cevap": "D", "aciklama": "Şifre paylaşma güvenlik, bilinmeyen uygulama virüs, aşırı ekran süresi sağlık açısından risklidir."},
    {"unite": U1, "konu": "Yardımlaşma ve Dayanışma", "yil": 2023, "zorluk": "Orta",
     "soru": "Gönüllü itfaiyeciler, orman yangınlarını söndürmek için hiçbir ücret almadan çalışmaktadır.\n\nBu davranış hangi kavramla en iyi açıklanır?",
     "siklar": {"A": "Profesyonel meslek", "B": "Toplumsal gönüllülük ve fedakârlık", "C": "Zorunlu görev", "D": "Ticari faaliyet"},
     "dogru_cevap": "B", "aciklama": "Ücretsiz çalışarak topluma katkı sağlamak gönüllülük ve fedakârlıktır."},
    {"unite": U2, "konu": "Yaşadığımız İlin Göreceli Konumu", "yil": 2022, "zorluk": "Orta",
     "soru": "Bir ilin;\n- Hangi ülkeye komşu olduğu\n- Hangi deniz kıyısında yer aldığı\n- Hangi dağların yakınında bulunduğu\nbilgileri hangi konum türüyle ifade edilir?",
     "siklar": {"A": "Mutlak konum", "B": "Göreceli konum", "C": "Astronomik konum", "D": "Matematiksel konum"},
     "dogru_cevap": "B", "aciklama": "Çevresindeki yer ve nesnelere göre bir yerin konumunu belirlemek göreceli konumdur."},
    {"unite": U3, "konu": "Ortak Miras Ögeleri", "yil": 2023, "zorluk": "Orta",
     "soru": "Sumela Manastırı, Ani Harabeleri ve Divriği Ulu Camii UNESCO Dünya Mirası Listesi'ndedir.\n\nBu eserlerin korunmasının evrensel önemi hangisidir?",
     "siklar": {"A": "Sadece Türkiye ekonomisine katkı sağlaması", "B": "İnsanlık tarihinin ve kültürel çeşitliliğin tanıklığını yapması", "C": "Modern mimari için örnek olması", "D": "Askeri açıdan önemli olması"},
     "dogru_cevap": "B", "aciklama": "Bu eserler insanlık tarihinin ve kültürel çeşitliliğin somut kanıtlarıdır."},
    {"unite": U4, "konu": "Demokrasi ve Cumhuriyet", "yil": 2023, "zorluk": "Zor",
     "soru": "Atatürk;\n- 'Hâkimiyet milletindir'\n- 'Cumhuriyeti biz kurduk, onu yükseltecek olan sizlersiniz'\nsözlerini söylemiştir.\n\nBu sözlerin ortak mesajı hangisidir?",
     "siklar": {"A": "Yönetimin tek kişiye ait olması", "B": "Milli egemenlik ve demokrasinin korunması gereği", "C": "Eğitimin gereksizliği", "D": "Ordunun her şeyin üstünde olması"},
     "dogru_cevap": "B", "aciklama": "Her iki söz de milli egemenlik ve demokratik cumhuriyetin önemini vurgular."},
]
all_q.extend(ek)

out = os.path.join(BASE, "sorular_5.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(all_q, f, ensure_ascii=False, indent=2)
print(f"\n5. Sınıf TOPLAM: {len(all_q)} soru -> sorular_5.json")

# Ünite dağılımı
units = {}
for q in all_q:
    u = q["unite"]
    units[u] = units.get(u, 0) + 1
for u, c in units.items():
    print(f"  {u}: {c} soru")
