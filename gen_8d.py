import json, os

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

questions = [
    # U1
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2024, "zorluk": "Orta",
     "soru": "Kafkas Cephesi'nde Sarıkamış Harekâtı'nda;\n- Kış şartlarında taarruz yapılmış\n- 90.000'e yakın asker donarak veya hastalıktan şehit olmuştur\n\nBu harekâtın başarısız olmasının temel nedeni hangisidir?",
     "siklar": {"A": "Askerlerin az olması", "B": "Ağır kış koşullarında yetersiz hazırlık ve lojistik planlama eksikliği", "C": "Düşmanın çok güçlü olması", "D": "İhanet yaşanması"},
     "dogru_cevap": "B", "aciklama": "Sarıkamış'ta ağır kış koşulları ve lojistik yetersizlik felakete yol açmıştır."},
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2023, "zorluk": "Zor",
     "soru": "I. Dünya Savaşı sonunda;\nI. Osmanlı, Avusturya-Macaristan, Rus imparatorlukları yıkılmış\nII. Milletler Cemiyeti kurulmuş\nIII. Sınırlar yeniden çizilmiş\nIV. Manda ve himaye sistemi oluşmuş\n\nSavaşın dünya düzenine etkisi hangisidir?",
     "siklar": {"A": "Hiçbir şey değişmemiş", "B": "Eski düzen yıkılarak yeni uluslararası sistem kurulmuş", "C": "İmparatorluklar güçlenmiş", "D": "Sömürgecilik bitmiş"},
     "dogru_cevap": "B", "aciklama": "I. Dünya Savaşı imparatorlukları yıkarak yeni uluslararası düzen oluşturmuştur."},
    {"unite": U1, "konu": "Mustafa Kemal'in Askerlik Hayatı", "yil": 2022, "zorluk": "Orta",
     "soru": "Mustafa Kemal I. Dünya Savaşı sonrası İstanbul'a dönmüş ve;\n'Geldikleri gibi giderler' demiştir.\n\nBu söz hangisini ifade eder?",
     "siklar": {"A": "Savaşın biteceğini", "B": "İşgalcilerin bir gün çekilmek zorunda kalacağına olan inancı", "C": "İstanbul'un güzel olduğunu", "D": "Savaşa devam etmek istemediğini"},
     "dogru_cevap": "B", "aciklama": "'Geldikleri gibi giderler' işgalcilerin çekilmeye mahkûm olacağına inancı ifade eder."},

    # U2
    {"unite": U2, "konu": "İşgaller ve Tepkiler", "yil": 2024, "zorluk": "Orta",
     "soru": "İstanbul'un resmen işgali (16 Mart 1920);\nI. Mebusan Meclisi basılarak kapatılmış\nII. Milletvekilleri tutuklanmış\nIII. İtilaf devletleri kontrolü ele almış\n\nBu olayın en önemli sonucu hangisidir?",
     "siklar": {"A": "İstanbul'un kurtulması", "B": "TBMM'nin Ankara'da açılmasının zorunlu hale gelmesi", "C": "Padişahın güçlenmesi", "D": "Barışın sağlanması"},
     "dogru_cevap": "B", "aciklama": "İstanbul'un işgali ve meclisin kapatılması TBMM'nin Ankara'da açılmasını zorunlu kılmıştır."},
    {"unite": U2, "konu": "Mustafa Kemal Samsun'da", "yil": 2023, "zorluk": "Zor",
     "soru": "Mustafa Kemal askerlik görevinden istifa etmiştir (8 Temmuz 1919).\n\nBu istifanın anlamı hangisidir?",
     "siklar": {"A": "Savaşı bırakması", "B": "Millî Mücadele'yi sivil lider olarak yürütme kararlılığını göstermesi", "C": "Osmanlı'ya bağlılığını", "D": "Siyasetten çekilmesi"},
     "dogru_cevap": "B", "aciklama": "İstifa Mustafa Kemal'in millî mücadeleyi sivil lider olarak sürdürme kararlılığıdır."},
    {"unite": U2, "konu": "Kongreler ve Amasya Genelgesi", "yil": 2024, "zorluk": "Zor",
     "soru": "Amasya Genelgesi'nin ihtilal bildirisi niteliğinde olmasının nedeni;\n- İlk kez millî iradeyi padişah yetkisinin üstünde görmesidir\n\nBu yaklaşım hangisinin habercisidir?",
     "siklar": {"A": "Padişahlığın güçlenmesinin", "B": "Millî egemenliğe dayalı yeni bir devletin kurulacağının", "C": "İşgallerin kabulünün", "D": "Osmanlı'nın devam edeceğinin"},
     "dogru_cevap": "B", "aciklama": "Millî irade vurgusu yeni bir millet egemenliğine dayalı devletin habercisidir."},

    # U3
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2024, "zorluk": "Orta",
     "soru": "Dumlupınar Meydan Muharebesi (30 Ağustos 1922) Türk tarihinde 'Başkomutan Meydan Muharebesi' olarak anılır.\n\n30 Ağustos'un önem hangisidir?",
     "siklar": {"A": "Savaşın başlaması", "B": "Kurtuluş Savaşı'nın kesin zaferle sonuçlanması ve Zafer Bayramı olarak kutlanması", "C": "Barış görüşmelerinin başlaması", "D": "İstanbul'un kurtarılması"},
     "dogru_cevap": "B", "aciklama": "30 Ağustos kesin zafer günü olup Zafer Bayramı olarak kutlanır."},
    {"unite": U3, "konu": "Güney ve Doğu Cepheleri", "yil": 2022, "zorluk": "Orta",
     "soru": "Kars Antlaşması (1921) Türkiye ile Sovyet Cumhuriyetleri arasında imzalanmıştır.\n\nBu antlaşmanın önemi hangisidir?",
     "siklar": {"A": "Batı sınırının belirlenmesi", "B": "Doğu sınırının kesinleşmesi ve güvenlik sağlanması", "C": "Boğazların kontrolü", "D": "Kapitülasyonların kaldırılması"},
     "dogru_cevap": "B", "aciklama": "Kars Antlaşması doğu sınırını kesinleştirerek güvenlik sağlamıştır."},
    {"unite": U3, "konu": "Mudanya Ateşkesi ve Lozan", "yil": 2022, "zorluk": "Zor",
     "soru": "Lozan Antlaşması'nda Sevr ile karşılaştırıldığında;\nI. Sevr: Osmanlı paylaşılıyor ↔ Lozan: Tam bağımsızlık\nII. Sevr: Kapitülasyonlar devam ↔ Lozan: Kaldırılmış\nIII. Sevr: Ordu sınırlı ↔ Lozan: Tam askeri egemenlik\n\nBu karşılaştırma hangisini gösterir?",
     "siklar": {"A": "İkisinin aynı olduğunu", "B": "Millî Mücadele'nin Sevr'i yıkarak onurlu bir barış (Lozan) kazandığını", "C": "Sevr'in uygulandığını", "D": "Lozan'ın eksik olduğunu"},
     "dogru_cevap": "B", "aciklama": "Millî Mücadele Sevr'in dayattığı esareti yıkarak Lozan'la onurlu barış kazanmıştır."},

    # U4
    {"unite": U4, "konu": "İnkılaplar", "yil": 2024, "zorluk": "Orta",
     "soru": "Tevhid-i Tedrisat Kanunu (1924);\n- Tüm okullar MEB'e bağlanmış\n- Medreseler kapatılmış\n- Eğitimde birlik sağlanmış\n\nBu kanunun amacı hangisidir?",
     "siklar": {"A": "Dini eğitimi güçlendirmek", "B": "Laik, çağdaş ve birleşik bir eğitim sistemi oluşturmak", "C": "Okulları kapatmak", "D": "Sadece askeri eğitim vermek"},
     "dogru_cevap": "B", "aciklama": "Tevhid-i Tedrisat laik, çağdaş ve birleşik eğitim sistemini oluşturmuştur."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2023, "zorluk": "Zor",
     "soru": "1926 Kabotaj Kanunu;\n- Türk kıyılarında ve limanlarında deniz taşımacılığı hakkı yalnız Türk gemilerine verilmiş\n\nBu kanunun anlamı hangisidir?",
     "siklar": {"A": "Denizcilikten vazgeçme", "B": "Ulusal denizcilik egemenliğinin sağlanması ve ekonomik bağımsızlığın güçlenmesi", "C": "Yabancı gemilere kolaylık sağlama", "D": "İthalatın artması"},
     "dogru_cevap": "B", "aciklama": "Kabotaj ulusal denizcilik egemenliğini ve ekonomik bağımsızlığı güçlendirmiştir."},
    {"unite": U4, "konu": "Atatürk İlkeleri", "yil": 2022, "zorluk": "Orta",
     "soru": "İnkılâpçılık ilkesi;\n- Durağan kalmak yerine sürekli gelişmek\n- Çağın gereklerine uyum sağlamak\n\nBu ilkenin günümüzdeki karşılığı hangisidir?",
     "siklar": {"A": "Gelenekçilik", "B": "Sürekli yenilenme ve modernleşme", "C": "Değişime karşı durma", "D": "Geçmişe dönme"},
     "dogru_cevap": "B", "aciklama": "İnkılâpçılık sürekli yenilenme ve modernleşme anlayışını ifade eder."},

    # U5
    {"unite": U5, "konu": "Çok Partili Hayata Geçiş Denemeleri", "yil": 2023, "zorluk": "Orta",
     "soru": "Atatürk;\n'Benim naciz vücudum elbet bir gün toprak olacaktır. Fakat Türkiye Cumhuriyeti ilelebet payidar kalacaktır.'\n\nBu söz hangisini ifade eder?",
     "siklar": {"A": "Kişi kültünü", "B": "Cumhuriyet'in kişilerden bağımsız, kalıcı bir rejim olduğunu", "C": "Atatürk'ün sağlık sorunlarını", "D": "Diktatörlüğü"},
     "dogru_cevap": "B", "aciklama": "Bu söz Cumhuriyet'in kişilerden bağımsız, kalıcı bir devlet rejimi olduğunu vurgular."},
    {"unite": U5, "konu": "Askeri Müdahaleler ve Demokrasi", "yil": 2024, "zorluk": "Zor",
     "soru": "Demokrasi kültürünün güçlenmesi için;\nI. Sivil toplumun güçlü olması\nII. Hukukun üstünlüğünün sağlanması\nIII. Basın özgürlüğünün korunması\nIV. Askeri vesayetin önlenmesi\n\nBunlardan hangileri gereklidir?",
     "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I, II ve III", "D": "I, II, III ve IV"},
     "dogru_cevap": "D", "aciklama": "Demokrasi sivil toplum, hukuk, basın özgürlüğü ve vesayetin önlenmesini birlikte gerektirir."},
    {"unite": U5, "konu": "1946 ve Sonrası Demokratikleşme", "yil": 2023, "zorluk": "Orta",
     "soru": "1946'da yapılan ilk çok partili seçimde 'açık oy, gizli sayım' yöntemi kullanılmıştır.\n\nBu yöntemin sorunu hangisidir?",
     "siklar": {"A": "Hızlı olması", "B": "Seçmen iradesinin baskı altına alınabilmesi ve şeffaflık eksikliği", "C": "Çok kolay olması", "D": "Herkesin oy kullanabilmesi"},
     "dogru_cevap": "B", "aciklama": "Açık oy seçmen iradesinin baskı altına alınmasına yol açabilirdi."},

    # U6
    {"unite": U6, "konu": "Atatürk Dönemi Dış Politika İlkeleri", "yil": 2023, "zorluk": "Zor",
     "soru": "Atatürk;\n'Savaş zorunlu ve hayati olmalıdır. Milletin hayatı tehlikeye girmedikte savaş bir cinayettir.'\n\nBu söz hangi dış politika ilkesini yansıtır?",
     "siklar": {"A": "Savaşçılık", "B": "Barışçılık ve savunma odaklı güvenlik politikası", "C": "Yayılmacılık", "D": "Tarafsızlık"},
     "dogru_cevap": "B", "aciklama": "Bu söz barışçılık ve zorunlu olmadıkça savaşa başvurmama ilkesini ifade eder."},
    {"unite": U6, "konu": "Balkan ve Sadabat Paktları", "yil": 2024, "zorluk": "Orta",
     "soru": "Balkan Antantı (1934) üyeleri;\n- Türkiye, Yunanistan, Romanya, Yugoslavya\n\nBu antantın önemi hangisidir?",
     "siklar": {"A": "Balkanları paylaşmak", "B": "Balkanlarda barışı ve karşılıklı sınır güvenliğini korumak", "C": "Avrupa'ya savaş açmak", "D": "Balkanlarden çekilmek"},
     "dogru_cevap": "B", "aciklama": "Balkan Antantı Balkanlarda barış ve karşılıklı sınır güvenliğini korumayı amaçlamıştır."},
    {"unite": U6, "konu": "Musul Sorunu", "yil": 2023, "zorluk": "Zor",
     "soru": "Musul sorununun Türkiye aleyhine sonuçlanmasındaki faktörler;\nI. İngiltere'nin uluslararası alanda güçlü olması\nII. Milletler Cemiyeti'nin İngiltere lehine karar vermesi\nIII. Şeyh Sait İsyanı'nın iç güvenliği tehdit etmesi\n\nBu faktörler hangisini gösterir?",
     "siklar": {"A": "Türkiye'nin hatalı olduğunu", "B": "Dış politikada iç sorunların ve uluslararası güç dengelerinin etkili olduğunu", "C": "Musul'un önemsiz olduğunu", "D": "İngiltere'nin haklı olduğunu"},
     "dogru_cevap": "B", "aciklama": "Musul sorunu iç sorunların ve uluslararası güç dengelerinin dış politikayı etkilediğini gösterir."},
]

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sorular_8_d.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"8. Sınıf Batch D (LGS): {len(questions)} soru yazıldı")
