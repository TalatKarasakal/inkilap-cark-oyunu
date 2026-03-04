"""6. sınıf batch JSON dosyalarını birleştirip sorular_6.json oluşturur."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
all_q = []

for part in ["sorular_6_a.json", "sorular_6_b.json", "sorular_6_c.json", "sorular_6_d.json"]:
    path = os.path.join(BASE, part)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_q.extend(data)
        print(f"  {part}: {len(data)} soru")

U1 = "Ünite 1 – Birlikte Yaşamak"
U2 = "Ünite 2 – Evimiz Dünya"
U3 = "Ünite 3 – Ortak Mirasımız"
U4 = "Ünite 4 – Yaşayan Demokrasimiz"
U5 = "Ünite 5 – Hayatımızdaki Ekonomi"
U6 = "Ünite 6 – Teknoloji ve Sosyal Bilimler"

ek = [
    {"unite": U1, "konu": "Toplumsal Birliktelik", "yil": 2024, "zorluk": "Orta",
     "soru": "Bir şehirde yaşayan farklı etnik gruplardaki insanlar ortak bir festival düzenlemiştir.\n\nBu festival hangisine katkı sağlar?",
     "siklar": {"A": "Ayrımcılığın artmasına", "B": "Toplumsal kaynaşma ve kültürel zenginliğe", "C": "Tek tip kültür oluşmasına", "D": "Gruplar arası çatışmaya"},
     "dogru_cevap": "B", "aciklama": "Ortak festival toplumsal kaynaşma ve kültürel zenginliğe katkı sağlar."},
    {"unite": U1, "konu": "Toplumsal Sorunlar ve Çözümler", "yil": 2023, "zorluk": "Orta",
     "soru": "Bir okulda gürültü sorunu çözümü için;\n- Öğrenci meclisi toplantı yapmış\n- Gürültü ölçer cihazı koridorlara yerleştirilmiş\n- 'Sessiz koridor' kampanyası başlatılmış\n\nBu çözüm yaklaşımının özelliği hangisidir?",
     "siklar": {"A": "Cezaya dayalı çözüm", "B": "Katılımcı ve bilinçlendirmeye dayalı çözüm", "C": "Otoriter müdahale", "D": "Sorunu görmezden gelme"},
     "dogru_cevap": "B", "aciklama": "Öğrenci katılımı ve farkındalık kampanyası bilinçlendirmeye dayalı demokratik çözümdür."},
    {"unite": U2, "konu": "Katman ve Oluşumları Koruma", "yil": 2024, "zorluk": "Zor",
     "soru": "Biyoçeşitlilik, bir bölgedeki farklı canlı türlerinin zenginliğidir.\n\nBiyoçeşitliliğin korunması neden önemlidir?",
     "siklar": {"A": "Sadece estetik bir değere sahip olduğu için", "B": "Ekosistemlerin dengeli işleyişi ve insanlığın geleceği için hayati olduğu için", "C": "Yalnızca bilimsel araştırma için", "D": "Sadece turizm geliri sağladığı için"},
     "dogru_cevap": "B", "aciklama": "Biyoçeşitlilik ekosistemlerin dengeli işleyişi ve insanlığın geleceği için hayati önemdedir."},
    {"unite": U2, "konu": "Doğal ve Beşeri Özellikler", "yil": 2023, "zorluk": "Orta",
     "soru": "Karadeniz bölgesinde;\nI. Bol yağış\nII. Dik yamaçlar\nIII. Yeşil bitki örtüsü\n\nBu özelliklerin tümü hangi kavramla ilişkilidir?",
     "siklar": {"A": "Beşeri özellikler", "B": "Doğal özellikler", "C": "Sanayi faaliyetleri", "D": "Kentleşme süreci"},
     "dogru_cevap": "B", "aciklama": "Yağış, yamaçlar ve bitki örtüsü bölgenin doğal özellikleridir."},
    {"unite": U3, "konu": "Türkistan'da Kurulan Türk Devletleri", "yil": 2024, "zorluk": "Orta",
     "soru": "Büyük Hun Devleti dönemi;\nI. Çin Seddi'nin yapılma nedenidir\nII. İlk Türk siyasi birliğini oluşturmuştur\nIII. Onlu askeri sistemi geliştirmiştir\n\nBu bilgilere göre Hunlar hakkında hangisi söylenebilir?",
     "siklar": {"A": "Zayıf bir devlet oldukları", "B": "Türk tarihinin ilk önemli devletini kurarak büyük bir güç oluşturdukları", "C": "Yerleşik hayat sürdürdükleri", "D": "Çin ile ticaret yapmadıkları"},
     "dogru_cevap": "B", "aciklama": "Hunlar ilk Türk siyasi birliğini kurarak güçlü bir devlet oluşturmuştur."},
    {"unite": U3, "konu": "Askeri Mücadelelerin Anadolu'ya Etkileri", "yil": 2023, "zorluk": "Zor",
     "soru": "Anadolu'da kurulan beylikler;\nI. Aydınoğulları → Denizcilik\nII. Karamanoğulları → Türkçeyi resmi dil ilan etme\nIII. Osmanoğulları → İmparatorluk kurma\n\nBeyliklerden Osmanlı'ya geçiş sürecinde hangisi en kalıcı etkiyi yapmıştır?",
     "siklar": {"A": "Yalnız I", "B": "Yalnız II", "C": "Yalnız III", "D": "I, II ve III"},
     "dogru_cevap": "D", "aciklama": "Her beylik farklı alanlarda kalıcı etki yapmıştır; hepsi önemlidir."},
    {"unite": U3, "konu": "İslam Medeniyetinin Ortak Mirası", "yil": 2024, "zorluk": "Orta",
     "soru": "İslam medeniyetinde hastanelere 'darüşşifa', eczanelere 'aktar dükkânı', akıl hastanelerine 'bimaristan' denilmiştir.\n\nBu kavramlar İslam medeniyetinin hangi alandaki gelişimini gösterir?",
     "siklar": {"A": "Askeri", "B": "Sağlık", "C": "Hukuk", "D": "Ticaret"},
     "dogru_cevap": "B", "aciklama": "Darüşşifa, aktar ve bimaristan İslam medeniyetinin sağlık alanındaki gelişimini gösterir."},
    {"unite": U4, "konu": "Yönetim ve Karar Alma Süreci", "yil": 2023, "zorluk": "Orta",
     "soru": "Okulda düzenlenen sınıf başkanlığı seçimi sonuçlarını kabul etmek demokratik kültürün bir parçasıdır.\n\nSeçim sonuçlarının kabul edilmesinin önemi hangisidir?",
     "siklar": {"A": "Kazananın güçlenmesi", "B": "Demokratik sürecin işlerliğinin ve toplumsal barışın korunması", "C": "Kaybedenlerin cezalandırılması", "D": "Seçimin tekrarlanması"},
     "dogru_cevap": "B", "aciklama": "Seçim sonuçlarını kabul etmek demokratik sürecin işlerliğini ve toplumsal barışı korur."},
    {"unite": U5, "konu": "Ekonomik Faaliyetler ve Meslekler", "yil": 2024, "zorluk": "Orta",
     "soru": "Bir ülkenin ithalatı;\nI. Petrol\nII. Doğalgaz\nIII. Teknolojik ürünler\n\nBu ürünlerde dışa bağımlılığı azaltmanın yolu hangisidir?",
     "siklar": {"A": "İthalatı tamamen durdurmak", "B": "Yerli üretim ve yenilenebilir enerji yatırımlarını artırmak", "C": "Sadece tarıma yönelmek", "D": "Dış borç almak"},
     "dogru_cevap": "B", "aciklama": "Yerli üretim ve yenilenebilir enerji dışa bağımlılığı azaltmanın en etkili yoludur."},
    {"unite": U5, "konu": "Yatırım ve Pazarlama Süreci", "yil": 2024, "zorluk": "Zor",
     "soru": "Bir şirketin;\nI. Ar-Ge (Araştırma Geliştirme) departmanı var\nII. Yeni ürünler tasarlıyor\nIII. Patent başvurusunda bulunuyor\n\nBu şirketin öne çıkan özelliği hangisidir?",
     "siklar": {"A": "Geleneksel üretim yapması", "B": "Yenilikçi ve inovasyon odaklı çalışması", "C": "Sadece ithalat yapması", "D": "Küçük ölçekli olması"},
     "dogru_cevap": "B", "aciklama": "Ar-Ge, yeni tasarımlar ve patent yenilikçi ve inovasyon odaklı çalışmanın göstergeleridir."},
    {"unite": U6, "konu": "Ulaşım ve İletişim Teknolojileri", "yil": 2024, "zorluk": "Orta",
     "soru": "Bulut bilişim (cloud computing) sayesinde veriler uzak sunucularda saklanmakta ve her yerden erişilebilmektedir.\n\nBulut bilişimin en önemli avantajı hangisidir?",
     "siklar": {"A": "Verilerin fiziksel olarak taşınması", "B": "Verilerin her cihazdan ve her yerden erişilebilir olması", "C": "İnternet bağlantısı gerektirmemesi", "D": "Sadece büyük şirketlerin kullanabilmesi"},
     "dogru_cevap": "B", "aciklama": "Bulut bilişim verilere her cihaz ve konumdan erişim sağlayan çağdaş teknolojidir."},
    {"unite": U6, "konu": "Telif ve Patent Süreci", "yil": 2023, "zorluk": "Orta",
     "soru": "Bir tasarımcı özgün logo tasarlamış ve bunu ticari marka olarak tescil ettirmiştir.\n\nBu tescil ne sağlar?",
     "siklar": {"A": "Logonun herkes tarafından kullanılmasını", "B": "Logonun yasal koruma altına alınarak taklit edilmesini önlemeyi", "C": "Tasarımın kamu malı olmasını", "D": "Tasarımcının telif hakkından vazgeçmesini"},
     "dogru_cevap": "B", "aciklama": "Ticari marka tescili logoyu yasal koruma altına alarak taklit edilmesini önler."},
    {"unite": U1, "konu": "Gruplar ve Roller", "yil": 2024, "zorluk": "Orta",
     "soru": "Bir sivil toplum kuruluşu (STK) deprem bölgesinde;\n- Çadır kurmuş\n- Psikolojik destek vermiş\n- Çocuklara eğitim sağlamış\n\nSTK'ların toplumsal rolü hangisidir?",
     "siklar": {"A": "Devletin yerini almak", "B": "Toplumsal sorunlara gönüllü olarak çözüm üretmek", "C": "Kâr elde etmek", "D": "Siyasi parti kurmak"},
     "dogru_cevap": "B", "aciklama": "STK'lar toplumsal sorunlara gönüllü ve sivil çözüm üreten kuruluşlardır."},
    {"unite": U2, "konu": "Katman ve Oluşumları Koruma", "yil": 2023, "zorluk": "Orta",
     "soru": "Sıfır atık projesi kapsamında;\nI. Ambalaj azaltılmış\nII. Geri dönüşüm yaygınlaştırılmış\nIII. Kompost üretimi teşvik edilmiş\n\nBu projenin amacı hangisidir?",
     "siklar": {"A": "Üretimi durdurmak", "B": "Atık miktarını minimuma indirerek çevre kirliliğini önlemek", "C": "Tüketimi artırmak", "D": "Sadece ekonomik tasarruf sağlamak"},
     "dogru_cevap": "B", "aciklama": "Sıfır atık projesi çevre kirliliğini önlemeyi ve kaynakları verimli kullanmayı hedefler."},
    {"unite": U3, "konu": "İslamiyet ile Türklerde Değişim", "yil": 2024, "zorluk": "Orta",
     "soru": "Anadolu Selçukluları döneminde;\n- Mevlana insanlığa hoşgörüyü öğretmiş\n- Yunus Emre Türkçe şiirler yazmış\n- Hacı Bektaş Veli insan sevgisini yaymış\n\nBu kişilerin Anadolu'ya ortak katkısı hangisidir?",
     "siklar": {"A": "Askeri başarılar kazanma", "B": "Kültürel ve manevi değerlerin yayılarak toplumsal barışa katkı sağlama", "C": "Ticaret yollarını kontrol etme", "D": "Şehirler kurma"},
     "dogru_cevap": "B", "aciklama": "Mevlana, Yunus Emre ve Hacı Bektaş Veli kültürel-manevi değerlerin yayılmasına katkı sağlamıştır."},
    {"unite": U4, "konu": "Temel Hak ve Sorumluluklar", "yil": 2024, "zorluk": "Orta",
     "soru": "Türkiye'de 18 yaşını dolduran her vatandaş seçme hakkına sahiptir.\n\nSeçme hakkının bu şekilde tanımlanmasının nedeni hangisidir?",
     "siklar": {"A": "18 yaş altının yeterince bilgili olmaması", "B": "Hukuki olarak reşit olma yaşı ile vatandaşlık sorumluluğunun örtüşmesi", "C": "Sadece geleneksel bir uygulama olması", "D": "Uluslararası baskı nedeniyle"},
     "dogru_cevap": "B", "aciklama": "18 yaş hukuki reşit olma yaşıdır ve vatandaşlık hak ve sorumluluklarının aktif kullanılmaya başlandığı yaştır."},
    {"unite": U5, "konu": "Ekonomik Faaliyetler ve Meslekler", "yil": 2024, "zorluk": "Orta",
     "soru": "Serbest ticaret bölgeleri;\nI. Gümrük vergisi uygulanmaz\nII. İhracatı teşvik eder\nIII. Yabancı yatırımı çeker\n\nBu bölgelerin ülke ekonomisine katkısı hangisidir?",
     "siklar": {"A": "Ekonomiyi daraltması", "B": "Dış ticaret ve yatırımı artırarak ekonomik büyümeyi desteklemesi", "C": "İthalatı engellemesi", "D": "Yerli üretimi azaltması"},
     "dogru_cevap": "B", "aciklama": "Serbest ticaret bölgeleri dış ticaret ve yatırımı artırarak ekonomik büyümeyi destekler."},
    {"unite": U6, "konu": "Ulaşım ve İletişim Teknolojileri", "yil": 2024, "zorluk": "Zor",
     "soru": "IoT (Nesnelerin İnterneti) ile;\nI. Buzdolabı eksik ürünü otomatik sipariş ediyor\nII. Akıllı termostat enerji tasarrufu sağlıyor\nIII. Trafik lambaları yoğunluğa göre ayarlanıyor\n\nBu örneklerin ortak özelliği hangisidir?",
     "siklar": {"A": "İnsanların tamamen gereksiz hale gelmesi", "B": "Günlük yaşamı akıllı ve verimli hale getiren teknolojik entegrasyon", "C": "Sadece endüstride kullanılması", "D": "Çevreye zararlı olması"},
     "dogru_cevap": "B", "aciklama": "IoT günlük yaşamı akıllı ve verimli hale getiren teknolojik entegrasyondur."},
]
all_q.extend(ek)

out = os.path.join(BASE, "sorular_6.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(all_q, f, ensure_ascii=False, indent=2)
print(f"\n6. Sınıf TOPLAM: {len(all_q)} soru -> sorular_6.json")

units = {}
for q in all_q:
    u = q["unite"]
    units[u] = units.get(u, 0) + 1
for u, c in units.items():
    print(f"  {u}: {c} soru")
