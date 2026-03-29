"""7. sınıf batch JSON dosyalarını birleştirip sorular_7.json oluşturur."""
import json, os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARTS_DIR = os.path.join(PROJECT_ROOT, "data", "parts")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
all_q = []

for part in ["sorular_7_a.json", "sorular_7_b.json", "sorular_7_c.json", "sorular_7_d.json"]:
    path = os.path.join(PARTS_DIR, part)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_q.extend(data)
        print(f"  {part}: {len(data)} soru")

U1 = "Ünite 1 – Birey ve Toplum"
U2 = "Ünite 2 – Kültür ve Miras"
U3 = "Ünite 3 – İnsanlar, Yerler ve Çevreler"
U4 = "Ünite 4 – Bilim, Teknoloji ve Toplum"
U5 = "Ünite 5 – Üretim, Dağıtım ve Tüketim"
U6 = "Ünite 6 – Etkin Vatandaşlık"
U7 = "Ünite 7 – Küresel Bağlantılar"

ek = [
    {"unite": U1, "konu": "İletişim ve Olumlu İletişim Unsurları", "yil": 2024, "zorluk": "Orta",
     "soru": "Dijital iletişimde emojiler ve GIF'ler;\n- Duyguları ifade etmeye yardımcı olur\n- Yanlış anlaşılmayı önleyebilir\n\nAnlam bakımından emojilerin rolü hangisidir?",
     "siklar": {"A": "Gereksiz süsleme", "B": "Yazılı iletişimde eksik kalan duygu ve ton ifadesini tamamlama", "C": "Profesyonel ortamda kullanılmaması gereken unsur", "D": "Sadece gençlerin kullandığı araçlar"},
     "dogru_cevap": "B", "aciklama": "Emojiler yazılı ortamda duygu ve ton ifadesini tamamlayarak iletişimi güçlendirir."},
    {"unite": U1, "konu": "Medyanın Hayatımızdaki Yeri", "yil": 2024, "zorluk": "Zor",
     "soru": "Propaganda ve reklamcılık arasındaki fark;\nI. Propaganda siyasi/ideolojik amaç taşır\nII. Reklamcılık ticari amaç taşır\nIII. İkisi de ikna tekniklerini kullanır\n\nDoğru olanlar hangileridir?",
     "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
     "dogru_cevap": "D", "aciklama": "Propaganda siyasi, reklam ticari amaçlıdır; ikisi de ikna tekniklerini kullanır."},
    {"unite": U2, "konu": "Beylikten Cihan Devletine", "yil": 2023, "zorluk": "Orta",
     "soru": "Osmanlı'da Divan-ı Hümayun;\n- Devlet işlerinin görüşüldüğü en yüksek organdır\n- Sadrazam, vezirler ve kazaskerler katılır\n\nDivan-ı Hümayun'un işlevi hangisidir?",
     "siklar": {"A": "Sadece askeri kararlar almak", "B": "Devlet yönetimi, adalet ve dış politika konularında karar almak", "C": "Sadece vergi toplamak", "D": "Dini kurallar belirlemek"},
     "dogru_cevap": "B", "aciklama": "Divan devlet yönetimi, adalet ve dış politika konularında karar alan en yüksek organdır."},
    {"unite": U2, "konu": "İnsanı Yaşat ki Devlet Yaşasın", "yil": 2024, "zorluk": "Zor",
     "soru": "Osmanlı'da adalet anlayışı;\n- 'İnsanı yaşat ki devlet yaşasın' (Şeyh Edebali)\n- Kadı'lar bağımsız yargılama yapardı\n- Şikâyet hakkı tüm vatandaşlara açıktı\n\nBu ilkeler hangisini gösterir?",
     "siklar": {"A": "Osmanlı'da insan hakları ve adalet anlayışının güçlü olduğunu", "B": "Sadece zenginlerin adalete erişebildiğini", "C": "Padişahın her şeye karar verdiğini", "D": "Adaletin sadece Müslümanlar için olduğunu"},
     "dogru_cevap": "A", "aciklama": "Kadı bağımsızlığı ve şikâyet hakkı güçlü adalet anlayışının göstergeleridir."},
    {"unite": U3, "konu": "Nüfus ve Yerleşme", "yil": 2024, "zorluk": "Zor",
     "soru": "Akıllı şehir (smart city) konsepti;\nI. IoT sensörleriyle traffic akışını yönetir\nII. Enerji tüketimini optimize eder\nIII. Vatandaşlara dijital hizmetler sunar\n\nAkıllı şehirlerin amacı hangisidir?",
     "siklar": {"A": "Nüfusu azaltmak", "B": "Teknolojiyi kullanarak yaşam kalitesini artırmak ve kaynakları verimli kullanmak", "C": "İnsanları kontrol etmek", "D": "Kırsal alanları ortadan kaldırmak"},
     "dogru_cevap": "B", "aciklama": "Akıllı şehirler teknolojiyle yaşam kalitesini artırır ve kaynakları verimli kullanır."},
    {"unite": U3, "konu": "İklim ve İnsan", "yil": 2024, "zorluk": "Orta",
     "soru": "Yeşil bina standartları;\n- Enerji verimliliği yüksek\n- Çevre dostu malzemeler kullanılır\n- Yağmur suyu geri dönüştürülür\n\nYeşil binaların en önemli katkısı hangisidir?",
     "siklar": {"A": "Daha pahalı olması", "B": "Çevre etkisini azaltarak sürdürülebilir yaşam alanları oluşturması", "C": "Sadece zenginler için olması", "D": "Daha az oda sunması"},
     "dogru_cevap": "B", "aciklama": "Yeşil binalar çevre etkisini azaltarak sürdürülebilir yaşam alanları oluşturur."},
    {"unite": U4, "konu": "Avrupa'daki Bilimsel ve Teknolojik Değişimler", "yil": 2024, "zorluk": "Orta",
     "soru": "Endüstri 4.0 (Dördüncü Sanayi Devrimi);\n- Yapay zekâ\n- Robotik\n- Nesnelerin interneti\n- Büyük veri\n\nEndüstri 4.0'ın en önemli özelliği hangisidir?",
     "siklar": {"A": "Fabrikaların kapanması", "B": "Üretimin akıllı, otomatik ve birbirine bağlı hale gelmesi", "C": "İşçilerin tamamen gereksiz olması", "D": "Sadece büyük şirketlerin kullanabilmesi"},
     "dogru_cevap": "B", "aciklama": "Endüstri 4.0 üretimi akıllı, otomatik ve birbirine bağlı hale getiren teknolojik dönüşümdür."},
    {"unite": U5, "konu": "Toprak ve İklimin Üretime Etkisi", "yil": 2024, "zorluk": "Orta",
     "soru": "Coğrafi işaret (Cİ) belgesi;\n- Antep baklavası, Aydın inciri, Isparta gülü gibi ürünlere verilir\n- Ürünün orijinalliğini ve kalitesini korur\n\nCİ belgesi hangisine hizmet eder?",
     "siklar": {"A": "Ürün fiyatını düşürmek", "B": "Yerel üretimi korumak ve bölgesel markalamayı güçlendirmek", "C": "İthalatı teşvik etmek", "D": "Reklamı yasaklamak"},
     "dogru_cevap": "B", "aciklama": "Cİ belgesi yerel üretimi korur ve bölgesel markalamayı güçlendirir."},
    {"unite": U6, "konu": "Toplumsal Katılım", "yil": 2024, "zorluk": "Orta",
     "soru": "Dilekçe hakkı anayasal bir haktır. Her vatandaş devlet kurumlarına dilekçe ile başvurabilir.\n\nDilekçe hakkının önemi hangisidir?",
     "siklar": {"A": "Bürokrasiyi artırması", "B": "Vatandaşların sorun ve taleplerini yasal yollarla yöneticilere iletmesini sağlaması", "C": "Sadece avukatların kullanabilmesi", "D": "Devlet kurumlarını kapatması"},
     "dogru_cevap": "B", "aciklama": "Dilekçe hakkı sorun ve taleplerin yasal yollarla yöneticilere iletilmesini sağlar."},
    {"unite": U7, "konu": "Küresel Sorunlar ve Çözümleri", "yil": 2024, "zorluk": "Zor",
     "soru": "Dijital uçurum (digital divide);\n- Zengin ve yoksul ülkeler arasındaki teknoloji erişim farkı\n- Kırsal ve kentsel arasındaki internet erişim farkı\n\nDijital uçurumun sonucu hangisidir?",
     "siklar": {"A": "Eşitliğin artması", "B": "Eğitim ve ekonomik fırsat eşitsizliğinin derinleşmesi", "C": "Teknolojinin gereksiz hale gelmesi", "D": "İnternetin pahalılaşması"},
     "dogru_cevap": "B", "aciklama": "Dijital uçurum eğitim ve ekonomik fırsat eşitsizliğini derinleştirir."},
    {"unite": U1, "konu": "Kitle İletişim Özgürlüğü", "yil": 2024, "zorluk": "Orta",
     "soru": "Vatandaş gazeteciliği;\n- Sıradan vatandaşlar olayları kayda alıp paylaşır\n- Sosyal medya aracılığıyla yayılır\n\nVatandaş gazeteciliğinin olumlu yönü hangisidir?",
     "siklar": {"A": "Her zaman doğru haber vermesi", "B": "Ana akım medyanın ulaşamadığı olayların görünür olmasını sağlaması", "C": "Profesyonel gazeteciliğin yerini tamamen alması", "D": "Devlet sansürünü güçlendirmesi"},
     "dogru_cevap": "B", "aciklama": "Vatandaş gazeteciliği ana akım medyanın ulaşamadığı olayları görünür kılar."},
    {"unite": U2, "konu": "Avrupa'da Uyanış", "yil": 2022, "zorluk": "Orta",
     "soru": "Rönesans döneminin önemli sanatçıları;\n- Leonardo da Vinci: Mona Lisa\n- Michelangelo: Sistine Şapeli\n- Rafael: Atina Okulu\n\nBu sanatçıların ortak özelliği hangisidir?",
     "siklar": {"A": "Sadece dini eserler yapmaları", "B": "İnsan merkezli (hümanist) yaklaşımla evrensel eserler yaratmaları", "C": "Sadece heykel yapmaları", "D": "Bilimle hiç ilgilenmemeleri"},
     "dogru_cevap": "B", "aciklama": "Rönesans sanatçıları insan merkezli yaklaşımla evrensel eserler yaratmıştır."},
    {"unite": U3, "konu": "Nüfus ve Yerleşme", "yil": 2022, "zorluk": "Zor",
     "soru": "Dünyada kentsel nüfus 2050'ye kadar %68'e ulaşması beklenmektedir.\n\nBu durumun sonuçları;\nI. Konut ihtiyacının artması\nII. Altyapı sorunlarının çoğalması\nIII. Çevresel baskının artması\nhangilerini kapsar?",
     "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
     "dogru_cevap": "D", "aciklama": "Hızlı kentleşme konut, altyapı ve çevre sorunlarını birlikte artırır."},
    {"unite": U4, "konu": "Osmanlı'da Bilim ve Teknoloji", "yil": 2023, "zorluk": "Orta",
     "soru": "Osmanlı'da II. Meşrutiyet (1908);\n- Kanun-i Esasi yeniden yürürlüğe girmiş\n- Meclis yeniden açılmış\n- Siyasi partiler kurulmuş\n\nBu gelişmelerin önemi hangisidir?",
     "siklar": {"A": "Padişahlığın güçlenmesi", "B": "Çok partili siyasi hayatın başlaması ve parlamenter sistemin güçlenmesi", "C": "Askeri gücün artması", "D": "Toprak kazanılması"},
     "dogru_cevap": "B", "aciklama": "II. Meşrutiyet çok partili siyasi hayatı başlatmış ve parlamenter sistemi güçlendirmiştir."},
    {"unite": U5, "konu": "Toprak ve İklimin Üretime Etkisi", "yil": 2022, "zorluk": "Orta",
     "soru": "Gıda güvenliği;\n- Yeterli, güvenli ve besleyici gıdaya sürekli erişim\n\nGıda güvenliğini tehdit eden faktörler hangileridir?",
     "siklar": {"A": "Sadece kuraklık", "B": "İklim değişikliği, nüfus artışı, toprak bozulması ve savaşlar", "C": "Sadece savaşlar", "D": "Sadece nüfus artışı"},
     "dogru_cevap": "B", "aciklama": "Gıda güvenliği iklim, nüfus, toprak ve savaş gibi çok faktörlü tehditlere maruz kalır."},
    {"unite": U6, "konu": "Haklar, Özgürlükler ve Sorumluluklar", "yil": 2024, "zorluk": "Zor",
     "soru": "Osmanlı'dan Cumhuriyet'e hak ve özgürlük gelişimi;\nSened-i İttifak(1808) → Tanzimat(1839) → Islahat(1856) → Kanun-i Esasi(1876) → TBMM(1920) → Cumhuriyet(1923)\n\nBu sürecin gösterdiği temel eğilim hangisidir?",
     "siklar": {"A": "Hakların daraltılması", "B": "Bireysel hak ve özgürlüklerin giderek genişleyip kurumsallaşması", "C": "Padişahlığın güçlenmesi", "D": "Dinin güçlenmesi"},
     "dogru_cevap": "B", "aciklama": "Sened-i İttifak'tan Cumhuriyet'e haklar giderek genişlemiş ve kurumsallaşmıştır."},
    {"unite": U7, "konu": "Uluslararası Örgütler ve Kuruluşlar", "yil": 2024, "zorluk": "Orta",
     "soru": "IMF (Uluslararası Para Fonu);\n- Ekonomik kriz yaşayan ülkelere mali destek sağlar\n- Küresel finansal istikrarı korumayı amaçlar\n\nIMF'nin rolü hangisidir?",
     "siklar": {"A": "Ülkeleri yönetmek", "B": "Küresel ekonomik istikrarın korunmasına katkıda bulunmak", "C": "Askeri yardım yapmak", "D": "Eğitim vermek"},
     "dogru_cevap": "B", "aciklama": "IMF küresel ekonomik istikrarın korunmasına mali destek ve danışmanlıkla katkıda bulunur."},
    {"unite": U2, "konu": "Osmanlı'dan Kalan Mirasımız", "yil": 2023, "zorluk": "Orta",
     "soru": "Osmanlı mimari mirası;\n- İstanbul: Topkapı Sarayı, Sultanahmet Camii\n- Edirne: Selimiye Camii\n- Bosna: Mostar Köprüsü\n\nBu eserlerin farklı coğrafyalarda bulunması hangisini gösterir?",
     "siklar": {"A": "Osmanlı'nın küçük bir devlet olduğunu", "B": "Osmanlı kültürel mirasının geniş coğrafyaya yayıldığını", "C": "Sadece cami inşa ettiklerini", "D": "Mimariyle ilgilenmediklerini"},
     "dogru_cevap": "B", "aciklama": "Farklı ülkelerdeki eserler Osmanlı kültürel mirasının geniş coğrafyaya yayıldığını gösterir."},
    {"unite": U4, "konu": "Avrupa'daki Bilimsel ve Teknolojik Değişimler", "yil": 2021, "zorluk": "Zor",
     "soru": "Amerikan ve Fransız devrimleri;\nI. Halk egemenliği\nII. İnsan hakları\nIII. Cumhuriyet yönetimi\nilkelerini yaymıştır.\n\nBu devrimlerin dünyaya etkisi hangisidir?",
     "siklar": {"A": "Monarşilerin güçlenmesi", "B": "Demokratik yönetim ve insan hakları düşüncesinin küresel ölçekte yayılması", "C": "Sömürgeciliğin artması", "D": "Feodalitenin geri dönmesi"},
     "dogru_cevap": "B", "aciklama": "Amerikan ve Fransız devrimleri demokratik yönetim ve insan haklarının küresel yayılımını sağlamıştır."},
    {"unite": U5, "konu": "Vakıfların Toplumsal Rolü", "yil": 2024, "zorluk": "Zor",
     "soru": "Günümüzde sosyal girişimcilik;\nI. Toplumsal soruna çözüm üretir\nII. Sürdürülebilir bir iş modeli kurar\nIII. Sadece kâr amacı güder\n\nSosyal girişimciliğin özellikleri hangileridir?",
     "siklar": {"A": "Yalnız III", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
     "dogru_cevap": "B", "aciklama": "Sosyal girişimcilik toplumsal çözüm üretir ve sürdürülebilir iş modeli kurar; sadece kâr odaklı değildir."},
    {"unite": U6, "konu": "Toplumsal Katılım", "yil": 2023, "zorluk": "Orta",
     "soru": "Bütçe şeffaflığı;\n- Devlet bütçesinin halka açık olması\n- Vatandaşların kamu harcamalarını görebilmesi\n\nBütçe şeffaflığının demokrasiye katkısı hangisidir?",
     "siklar": {"A": "Harcamaları gizlemek", "B": "Yönetimin denetlenmesini ve hesap verebilirliğini sağlamak", "C": "Bütçeyi azaltmak", "D": "Vergileri artırmak"},
     "dogru_cevap": "B", "aciklama": "Bütçe şeffaflığı yönetimin denetlenmesini ve hesap verebilirliğini sağlar."},
    {"unite": U7, "konu": "Küresel Sorunlar ve Çözümleri", "yil": 2022, "zorluk": "Orta",
     "soru": "Biyoteknoloji;\nI. GDO (genetiği değiştirilmiş organizma)\nII. Gen terapisi\nIII. Biyoyakıt üretimi\n\nBiyoteknolojinin tartışmalı yönü hangisidir?",
     "siklar": {"A": "Tamamen zararsız olması", "B": "Potansiyel yararları yanında etik, çevre ve sağlık endişeleri taşıması", "C": "Hiç kullanılmaması", "D": "Sadece ilaç alanında uygulanması"},
     "dogru_cevap": "B", "aciklama": "Biyoteknoloji yararlı olmasına rağmen etik, çevre ve sağlık endişeleri de taşır."},
]
all_q.extend(ek)

out = os.path.join(DATA_DIR, "sorular_7.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(all_q, f, ensure_ascii=False, indent=2)
print(f"\n7. Sınıf TOPLAM: {len(all_q)} soru -> sorular_7.json")

units = {}
for q in all_q:
    u = q["unite"]
    units[u] = units.get(u, 0) + 1
for u, c in sorted(units.items()):
    print(f"  {u}: {c} soru")
