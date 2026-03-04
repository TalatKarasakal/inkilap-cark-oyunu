import json, os

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

questions = [
    # U1 ek
    {"unite": U1, "konu": "Atatürk'ün Çocukluk ve Öğrenim Hayatı", "yil": 2024, "zorluk": "Orta",
     "soru": "Mustafa Kemal öğrenim hayatında;\nI. Mahalle mektebinde başlamış\nII. Annesinin isteğiyle Şemsi Efendi İlkokulu'na geçmiş\nIII. Askeri eğatim tercih etmiş\n\nAnnesi Zübeyde Hanım'ın rolü hangisidir?",
     "siklar": {"A": "Askeri okulu istemesi", "B": "Modern eğitim veren okulu tercih etmesi", "C": "Eğitimle ilgilenmemesi", "D": "Medreseyi istemesi"},
     "dogru_cevap": "B", "aciklama": "Zübeyde Hanım modern eğitim veren Şemsi Efendi İlkokulu'nu tercih etmiştir."},
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2024, "zorluk": "Zor",
     "soru": "I. Dünya Savaşı'nın temel nedenleri;\nI. Sömürge rekabeti\nII. Silahlanma yarışı\nIII. Milliyetçilik akımları\nIV. Bloklaşma (İttifak-İtilaf)\n\nBu nedenler hangisini gösterir?",
     "siklar": {"A": "Savaşın ani başladığını", "B": "Savaşın çok boyutlu ve yapısal nedenlerden kaynaklandığını", "C": "Tek bir nedenin yeterli olduğunu", "D": "Barışın korunduğunu"},
     "dogru_cevap": "B", "aciklama": "I. Dünya Savaşı sömürge, silahlanma, milliyetçilik ve bloklaşma gibi çok boyutlu nedenlerden kaynaklanmıştır."},
    {"unite": U1, "konu": "Mustafa Kemal'in Askerlik Hayatı", "yil": 2024, "zorluk": "Orta",
     "soru": "Mustafa Kemal Çanakkale'de Conkbayırı'nda cebindeki saat şarapnel parçasını durdurarak hayatını kurtarmıştır.\n\nBu olay neyi simgeler?",
     "siklar": {"A": "Savaşın kolay olduğunu", "B": "Kaderle liderliğin buluştuğunu ve Mustafa Kemal'in ölümden dönerek milletine hizmet etmeye devam ettiğini", "C": "Saatlerin kalitesini", "D": "Şansın yeterli olduğunu"},
     "dogru_cevap": "B", "aciklama": "Bu olay Mustafa Kemal'in ölümden dönerek milletine hizmet etmeye devam etmesini simgeler."},
    {"unite": U1, "konu": "Osmanlı'nın Son Döneminde Yaşanan Gelişmeler", "yil": 2023, "zorluk": "Zor",
     "soru": "Osmanlıcılık fikir akımı;\n- 'Din, dil, ırk ayrımı yapılmaksızın tüm Osmanlı vatandaşlarını bir arada tutmak'\nilkesine dayanır.\n\nBu akımın başarısız olmasının nedeni hangisidir?",
     "siklar": {"A": "Padişahın desteklememesi", "B": "Milliyetçilik akımlarının güçlenmesiyle azınlıkların bağımsızlık istemesi", "C": "Halkın benimsememesi", "D": "Savaş çıkması"},
     "dogru_cevap": "B", "aciklama": "Milliyetçilik güçlendikçe azınlıklar bağımsızlık istemiş ve Osmanlıcılık işlevini yitirmiştir."},

    # U2 ek
    {"unite": U2, "konu": "Mustafa Kemal Samsun'da", "yil": 2024, "zorluk": "Zor",
     "soru": "Mustafa Kemal 9. Ordu Müfettişi olarak Samsun'a gönderilme gerekçesi;\n- Pontus Rum çetelerinin faaliyetlerini engellemek\n\nAncak gerçek amacı hangisidir?",
     "siklar": {"A": "Çeteleri kontrol etmek", "B": "Millî Mücadele'yi organize etmek ve milletin bağımsızlık iradesini harekete geçirmek", "C": "Padişah adına hareket etmek", "D": "İstanbul'a dönmek"},
     "dogru_cevap": "B", "aciklama": "Mustafa Kemal'in asıl amacı Millî Mücadele'yi organize etmek ve bağımsızlık iradesini harekete geçirmekti."},
    {"unite": U2, "konu": "TBMM'nin Açılması", "yil": 2024, "zorluk": "Orta",
     "soru": "TBMM'ye karşı çıkarılan iç isyanlar;\n- Anzavur, Çerkez Ethem, Bolu, Düzce isyanları\n\nBu isyanların ortak amacı hangisidir?",
     "siklar": {"A": "Millî Mücadele'yi desteklemek", "B": "TBMM'nin otoritesini zayıflatmak ve millî birliği bozmak", "C": "Ekonomiyi güçlendirmek", "D": "Barış sağlamak"},
     "dogru_cevap": "B", "aciklama": "İç isyanlar TBMM otoritesini zayıflatmak ve millî birliği bozmak amacıyla çıkarılmıştır."},
    {"unite": U2, "konu": "Kongreler ve Amasya Genelgesi", "yil": 2023, "zorluk": "Orta",
     "soru": "Havza Genelgesi'nde (28 Mayıs 1919) işgallere karşı protesto mitingleri düzenlenmesi istenmiştir.\n\nBu genelgenin amacı hangisidir?",
     "siklar": {"A": "İşgalleri kabul etmek", "B": "Halkta millî bilinç uyandırmak ve tepkiyi örgütlemek", "C": "Padişahı desteklemek", "D": "İtilaf devletleriyle anlaşmak"},
     "dogru_cevap": "B", "aciklama": "Havza Genelgesi halkta millî bilinç uyandırmayı ve tepkiyi örgütlemeyi amaçlamıştır."},

    # U3 ek
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2024, "zorluk": "Zor",
     "soru": "Kütahya-Eskişehir Savaşları'nda (1921) Türk ordusu geri çekilme kararı almıştır.\n\nMustafa Kemal'in Sakarya'nın doğusuna çekilme kararının askeri amacı hangisidir?",
     "siklar": {"A": "Savaştan kaçmak", "B": "Düşmanın ikmal hatlarını uzatarak zayıflatmak ve savunma hattını güçlendirmek", "C": "Teslim olmak", "D": "Barış yapmak"},
     "dogru_cevap": "B", "aciklama": "Stratejik çekilme düşman ikmal hatlarını uzatarak zayıflatmayı ve savunmayı güçlendirmeyi amaçlamıştır."},
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2023, "zorluk": "Orta",
     "soru": "Mustafa Kemal TBMM'den Başkomutanlık yetkisini üç aylığına almıştır (5 Ağustos 1921).\n\nBu yetkinin verilme nedeni hangisidir?",
     "siklar": {"A": "Diktatörlük kurmak", "B": "Sakarya Savaşı öncesi hızlı ve etkili kararlar alarak orduyu hazırlamak", "C": "TBMM'yi kapatmak", "D": "Barış görüşmeleri yapmak"},
     "dogru_cevap": "B", "aciklama": "Başkomutanlık yetkisi savaş öncesi hızlı karar almak ve orduyu hazırlamak için verilmiştir."},
    {"unite": U3, "konu": "Mudanya Ateşkesi ve Lozan", "yil": 2024, "zorluk": "Zor",
     "soru": "Lozan görüşmelerinde Türk heyetini İsmet İnönü başkanlığında temsil etmiştir.\n\nİsmet Paşa'nın Lozan'daki en kararlı tutumu hangi konudadır?",
     "siklar": {"A": "Toprak tavizi verme", "B": "Kapitülasyonların kesinlikle kabul edilmemesi", "C": "Azınlık haklarını reddetme", "D": "Boğazlardan vazgeçme"},
     "dogru_cevap": "B", "aciklama": "İsmet Paşa kapitülasyonların kaldırılması konusunda kesinlikle taviz vermemiştir."},

    # U4 ek
    {"unite": U4, "konu": "Cumhuriyetin İlanı", "yil": 2024, "zorluk": "Zor",
     "soru": "1 Kasım 1922'de saltanat kaldırılmış, 29 Ekim 1923'te cumhuriyet ilan edilmiş, 3 Mart 1924'te halifelik kaldırılmıştır.\n\nBu üç olayın kronolojik sıralamasının mantığı hangisidir?",
     "siklar": {"A": "Rastgele yapılmıştır", "B": "Her adım bir sonraki için zemin hazırlamış; aşamalı ve planlı bir geçiş süreci uygulanmıştır", "C": "Aynı gün yapılmalıydı", "D": "Hepsi gereksizdi"},
     "dogru_cevap": "B", "aciklama": "Saltanat→Cumhuriyet→Halifelik kaldırma aşamalı ve planlı bir geçiş sürecidir."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2024, "zorluk": "Orta",
     "soru": "Takvim ve ölçü birimi değişiklikleri;\n- Hicri→Miladi takvim\n- Arşın→Metre sistemi\n- Okka→Kilogram\n\nBu değişikliklerin amacı hangisidir?",
     "siklar": {"A": "Gelenekleri yıkmak", "B": "Uluslararası standartlara uyum sağlamak ve ticari ilişkileri kolaylaştırmak", "C": "Batı'yı taklit etmek", "D": "Ekonomiyi güçlendirmek"},
     "dogru_cevap": "B", "aciklama": "Uluslararası standartlara geçiş ticari ilişkileri ve çağdaş dünyayla uyumu kolaylaştırmıştır."},
    {"unite": U4, "konu": "Atatürk İlkeleri", "yil": 2024, "zorluk": "Zor",
     "soru": "Milliyetçilik ilkesi;\n- Irk, din, mezhep ayrımı yapmaz\n- 'Ne mutlu Türküm diyene!' anlayışını benimser\n- Vatandaşlık bağına dayanır\n\nAtatürk milliyetçiliğinin ayırt edici özelliği hangisidir?",
     "siklar": {"A": "Irk temelli olması", "B": "Kapsayıcı, birleştirici ve vatandaşlık bağına dayalı olması", "C": "Dini temelli olması", "D": "Dışlayıcı olması"},
     "dogru_cevap": "B", "aciklama": "Atatürk milliyetçiliği ırk ayrımı yapmayan, kapsayıcı ve vatandaşlık bağına dayalıdır."},

    # U5 ek
    {"unite": U5, "konu": "Çok Partili Hayata Geçiş Denemeleri", "yil": 2024, "zorluk": "Zor",
     "soru": "Serbest Cumhuriyet Fırkası (1930);\n- Atatürk'ün isteğiyle kurulmuş\n- Fethi Okyar liderliğinde\n- İnkılâp karşıtlarının sığınağı olunca kapatılmış\n\nAtatürk'ün bu partiyi kurdurup kapatmasının amacı hangisidir?",
     "siklar": {"A": "Diktatörlük istemesi", "B": "Demokrasiyi denemek ancak inkılâpları koruma zorunluluğu nedeniyle geri adım atmak", "C": "Muhalefeti zayıflatmak", "D": "Halkı test etmek"},
     "dogru_cevap": "B", "aciklama": "Atatürk demokrasiyi denemiş ancak inkılâplara yönelik tehditle karşılaşınca geri adım atmıştır."},
    {"unite": U5, "konu": "1946 ve Sonrası Demokratikleşme", "yil": 2024, "zorluk": "Orta",
     "soru": "Türkiye'nin NATO'ya katılması (1952);\nI. Soğuk Savaş'ta Batı bloğunda yer alması\nII. Askeri güvenlik güvencesi kazanması\nIII. Demokratikleşme sürecini hızlandırması\n\nNATO üyeliğinin Türkiye'ye katkısı hangileridir?",
     "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "Yalnız III", "D": "I, II ve III"},
     "dogru_cevap": "D", "aciklama": "NATO üyeliği Batı bloğu konumu, güvenlik güvencesi ve demokratikleşme hızını artırmıştır."},
    {"unite": U5, "konu": "Askeri Müdahaleler ve Demokrasi", "yil": 2022, "zorluk": "Zor",
     "soru": "12 Eylül 1980 askeri darbesı;\nI. Siyasi istikrarsızlık ve terör ortamı\nII. Siyasi partiler kapatılmış\nIII. Sendikal haklar sınırlandırılmış\nIV. 1982 Anayasası hazırlanmış\n\n1980 darbenin Türk demokrasisi üzerindeki kalıcı etkisi hangisidir?",
     "siklar": {"A": "Demokrasinin güçlenmesi", "B": "Sivil siyasetin uzun süre vesayet altında kalması", "C": "Ekonominin büyümesi", "D": "Barışın sağlanması"},
     "dogru_cevap": "B", "aciklama": "1980 darbesi sivil siyasetin uzun süre askeri vesayet altında kalmasına yol açmıştır."},

    # U6 ek
    {"unite": U6, "konu": "Atatürk Dönemi Dış Politika İlkeleri", "yil": 2024, "zorluk": "Zor",
     "soru": "Atatürk döneminde Türkiye;\nI. Milletler Cemiyeti'ne katılmış\nII. Balkan Antantı ve Sadabat Paktı kurmuş\nIII. Montrö ile Boğazlarda egemenlik sağlamış\nIV. Hatay'ı diplomatik yolla kazanmış\n\nBu başarılar hangisini kanıtlar?",
     "siklar": {"A": "Türkiye'nin savaşçı olduğunu", "B": "Barışçıl, aktif ve onurlu dış politikanın somut sonuçlar verdiğini", "C": "İçe kapandığını", "D": "Batı'ya bağımlı olduğunu"},
     "dogru_cevap": "B", "aciklama": "Tüm bu başarılar barışçıl, aktif ve onurlu dış politikanın somut sonuçlarıdır."},
    {"unite": U6, "konu": "Türkiye'nin Milletler Cemiyetine Girişi", "yil": 2023, "zorluk": "Orta",
     "soru": "Türkiye Milletler Cemiyeti'ne 1932'de İspanya'nın teklifi ve Yunanistan'ın desteğiyle katılmıştır.\n\nYunanistan'ın Türkiye'yi desteklemesi hangisini gösterir?",
     "siklar": {"A": "Savaş isteğini", "B": "İki ülke arasındaki ilişkilerin normalleşmesini ve barış politikasının başarısını", "C": "Yunanistan'ın zayıflığını", "D": "Türkiye'nin baskı yapmasını"},
     "dogru_cevap": "B", "aciklama": "Yunanistan'ın desteği ilişkilerin düzelmesini ve Türk barış politikasının başarısını gösterir."},
    {"unite": U6, "konu": "Montrö Boğazlar Sözleşmesi", "yil": 2024, "zorluk": "Zor",
     "soru": "II. Dünya Savaşı öncesi Montrö'nün imzalanması;\n\nMontrö'nün zamanlamasının stratejik önemi hangisidir?",
     "siklar": {"A": "Savaşa katılmak", "B": "Olası bir savaşta Boğazlar üzerinde tam kontrol sağlayarak güvenliği güçlendirmek", "C": "Barışı reddetmek", "D": "Sömürge edinmek"},
     "dogru_cevap": "B", "aciklama": "Montrö II. Dünya Savaşı öncesi Boğazlar kontrolü ile güvenliği güçlendirmiştir."},
]

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sorular_8_c.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"8. Sınıf Batch C (LGS): {len(questions)} soru yazıldı")
