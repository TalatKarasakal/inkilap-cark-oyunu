import json, os

U1 = "Ünite 1 – Birlikte Yaşamak"
U2 = "Ünite 2 – Evimiz Dünya"
U3 = "Ünite 3 – Ortak Mirasımız"
U4 = "Ünite 4 – Yaşayan Demokrasimiz"
U5 = "Ünite 5 – Hayatımızda Ekonomi"
U6 = "Ünite 6 – Teknoloji ve Sosyal Bilimler"

questions = [
    # ---- ÜNİTE 1: BİRLİKTE YAŞAMAK (10 soru) ----
    {
        "unite": U1, "konu": "Gruplar ve Roller", "yil": 2024, "zorluk": "Orta",
        "soru": "Ali, okulda sınıf başkanıdır ve arkadaşlarının sorunlarını öğretmenine iletir. Evde ise ailesine yardım eder ve ablasıyla birlikte ev işlerini paylaşır.\n\nBuna göre Ali'nin farklı gruplarda farklı roller üstlenmesi aşağıdakilerden hangisiyle açıklanabilir?",
        "siklar": {"A": "İnsanlar her ortamda aynı davranışı sergiler", "B": "Bireyler bulundukları gruba göre farklı roller üstlenebilir", "C": "Roller sadece okul ortamında geçerlidir", "D": "Aile içinde herkesin görevi aynıdır"},
        "dogru_cevap": "B",
        "aciklama": "Her birey bulunduğu gruba (aile, okul, arkadaş çevresi) göre farklı roller üstlenir."
    },
    {
        "unite": U1, "konu": "Gruplar ve Roller", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir futbol takımında kaleci topu tutar, forvet gol atmaya çalışır, kaptan takımı yönetir. Herkes kendi görevini en iyi şekilde yapar ve birlikte çalışırlar.\n\nBu bilgiye göre başarılı bir grup çalışması için en önemli unsur aşağıdakilerden hangisidir?",
        "siklar": {"A": "Herkesin aynı görevi yapması", "B": "Görev paylaşımı ve iş birliği", "C": "Sadece kaptanın karar vermesi", "D": "Grup üyelerinin birbirleriyle yarışması"},
        "dogru_cevap": "B",
        "aciklama": "Başarılı gruplar görev paylaşımı yapan ve işbirliği içinde çalışan gruplardır."
    },
    {
        "unite": U1, "konu": "Kültürel Özelliklere Saygı", "yil": 2024, "zorluk": "Zor",
        "soru": "Bir sınıfta farklı şehirlerden gelen öğrenciler bulunmaktadır. Her öğrenci kendi memleketinin yöresel yemeğini tanıtmış ve arkadaşlarına tattırmıştır. Öğrenciler birbirlerinin kültürel farklılıklarına saygı göstererek hoşgörülü davranmışlardır.\n\nBu etkinlik aşağıdakilerden hangisine katkı sağlamıştır?",
        "siklar": {"A": "Kültürel farklılıkların ortadan kalkmasına", "B": "Birlikte yaşama kültürünün ve toplumsal hoşgörünün güçlenmesine", "C": "Öğrencilerin kendi kültürlerinden vazgeçmesine", "D": "Tek bir kültürün üstünlüğünün kabul edilmesine"},
        "dogru_cevap": "B",
        "aciklama": "Farklı kültürleri tanımak ve saygı göstermek birlikte yaşama kültürünü güçlendirir."
    },
    {
        "unite": U1, "konu": "Kültürel Özelliklere Saygı", "yil": 2022, "zorluk": "Orta",
        "soru": "Türkiye'nin doğusunda yaygın olan 'halay', Karadeniz bölgesinde 'horon', Ege'de 'zeybek' oynanmaktadır. Bu oyunlar o bölgelerin kültürel kimliğinin bir parçasıdır.\n\nBu durum aşağıdakilerden hangisini göstermektedir?",
        "siklar": {"A": "Türkiye'de tek bir kültürel yapı vardır", "B": "Ülkemiz zengin ve çeşitli bir kültürel yapıya sahiptir", "C": "Halk oyunları sadece eğlence amaçlıdır", "D": "Bölgeler arası kültürel etkileşim yoktur"},
        "dogru_cevap": "B",
        "aciklama": "Farklı bölgelerde farklı halk oyunlarının yaşaması ülkemizin zengin kültürel çeşitliliğinin kanıtıdır."
    },
    {
        "unite": U1, "konu": "Yardımlaşma ve Dayanışma", "yil": 2024, "zorluk": "Orta",
        "soru": "Deprem sonrasında tüm Türkiye'den yardım tırları gönderilmiş, gönüllüler enkaz altında kalan insanları kurtarmak için çalışmıştır. Kan bağışı kampanyalarına binlerce kişi katılmıştır.\n\nBu durum aşağıdakilerden hangisinin en güçlü göstergesidir?",
        "siklar": {"A": "Devletin tüm sorumlulukları tek başına üstlendiğinin", "B": "Toplumsal dayanışma ve yardımlaşma duygusunun güçlü olduğunun", "C": "Sadece resmi kurumların afet yönetiminde etkili olduğunun", "D": "Yardımlaşmanın sadece afet dönemlerinde yapıldığının"},
        "dogru_cevap": "B",
        "aciklama": "Gönüllü yardımlar ve kan bağışı kampanyaları toplumsal dayanışmanın en güçlü göstergesidir."
    },
    {
        "unite": U1, "konu": "Yardımlaşma ve Dayanışma", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir mahallede yaşlı ve yalnız yaşayan komşuların alışverişlerini gençler yapmakta, bayramlarda herkes birbirini ziyaret etmektedir.\n\nBu uygulamalar;\nI. Toplumsal birliğin güçlenmesi\nII. Kuşaklar arası bağın korunması\nIII. Bireyciliğin artması\nsonuçlarından hangilerine yol açar?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I, II ve III"},
        "dogru_cevap": "B",
        "aciklama": "Komşuluk ilişkileri toplumsal birliği ve kuşaklar arası bağı güçlendirir. Bireycilikle ilgisi yoktur."
    },
    {
        "unite": U1, "konu": "Gruplar ve Roller", "yil": 2021, "zorluk": "Orta",
        "soru": "Ayşe, arkadaş grubunda en iyi resim çizen kişidir ve proje ödevlerinde poster tasarımını üstlenir. Ailede ise en küçük çocuk olduğu için sofra hazırlama görevini yapar.\n\nAyşe'nin bu durumu aşağıdakilerden hangisiyle açıklanabilir?",
        "siklar": {"A": "Bireyin yeteneği sadece bir alanda geçerlidir", "B": "Roller grubun ihtiyaçlarına ve bireyin özelliklerine göre belirlenir", "C": "Aile içi roller okul rolleriyle aynıdır", "D": "Roller hiçbir zaman değişmez"},
        "dogru_cevap": "B",
        "aciklama": "Roller hem grubun ihtiyaçlarına hem de bireyin yeteneklerine ve özelliklerine göre şekillenir."
    },
    {
        "unite": U1, "konu": "Kültürel Özelliklere Saygı", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir ülkede farklı dillerde yayın yapan televizyon kanalları bulunmakta, çeşitli etnik grupların festivalleri devlet tarafından desteklenmektedir.\n\nBu uygulamaların temel amacı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Toplumsal ayrışmayı teşvik etmek", "B": "Kültürel çoğulculuğu ve toplumsal barışı sağlamak", "C": "Tek bir dilin hakim olmasını engellemek", "D": "Yabancı ülkelerin kültürel etkisini artırmak"},
        "dogru_cevap": "B",
        "aciklama": "Farklı kültürlerin desteklenmesi kültürel çoğulculuğu güçlendirir ve toplumsal barışa katkı sağlar."
    },
    {
        "unite": U1, "konu": "Yardımlaşma ve Dayanışma", "yil": 2022, "zorluk": "Orta",
        "soru": "İmece usulü, Anadolu'da köylerin birlikte hasat toplama, ev yapma gibi işleri el birliğiyle yapması geleneğidir.\n\nİmece usulünün toplumsal faydası aşağıdakilerden hangisidir?",
        "siklar": {"A": "Bireysel rekabeti artırması", "B": "İşlerin daha hızlı ve dayanışma içinde tamamlanması", "C": "Herkesin kendi başına çalışmasını teşvik etmesi", "D": "Sadece tarım alanında uygulanması"},
        "dogru_cevap": "B",
        "aciklama": "İmece, toplumsal dayanışmanın en güzel örneğidir ve işlerin birlikte daha hızlı tamamlanmasını sağlar."
    },
    {
        "unite": U1, "konu": "Yardımlaşma ve Dayanışma", "yil": 2021, "zorluk": "Orta",
        "soru": "Kızılay, AFAD, AKUT gibi kuruluşlar afet dönemlerinde yardım faaliyetleri yürütmektedir.\n\nBu kuruluşların ortak amacı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Devletin gelir elde etmesi", "B": "İnsanlara yardım ulaştırarak toplumsal dayanışmayı sağlamak", "C": "Sadece uluslararası alanda çalışmak", "D": "Ticari faaliyetlerde bulunmak"},
        "dogru_cevap": "B",
        "aciklama": "Bu kuruluşlar ihtiyaç sahiplerine yardım ulaştırarak toplumsal dayanışmayı somutlaştıran sivil girişimlerdir."
    },

    # ---- ÜNİTE 2: EVİMİZ DÜNYA (6 soru) ----
    {
        "unite": U2, "konu": "Yaşadığımız İlin Göreceli Konumu", "yil": 2024, "zorluk": "Orta",
        "soru": "Öğretmen, öğrencilere 'Yaşadığımız il hangi illere komşudur ve bu illere göre nerede bulunmaktadır?' sorusunu sormuştur.\n\nBu soru aşağıdaki kavramlardan hangisiyle ilgilidir?",
        "siklar": {"A": "Mutlak konum", "B": "Göreceli (nispi) konum", "C": "Matematik konum", "D": "Deniz seviyesi"},
        "dogru_cevap": "B",
        "aciklama": "Bir yerin çevresindeki yer ve nesnelere göre tanımlanması göreceli (nispi) konumdur."
    },
    {
        "unite": U2, "konu": "Yaşadığımız İlin Göreceli Konumu", "yil": 2023, "zorluk": "Zor",
        "soru": "Mert arkadaşına evini tarif ederken 'Bankadan sonraki ikinci sokakta, parkın karşısındaki mavi binanın 3. katı' demiştir.\n\nMert'in bu tarifi aşağıdaki konum türlerinden hangisine örnektir?",
        "siklar": {"A": "Mutlak konum", "B": "Matematik konum", "C": "Göreceli konum", "D": "Coğrafi koordinat"},
        "dogru_cevap": "C",
        "aciklama": "Çevredeki referans noktalarına (banka, park) göre yer tarif etmek göreceli konum kullanımıdır."
    },
    {
        "unite": U2, "konu": "Doğal ve Beşeri Değişim", "yil": 2024, "zorluk": "Zor",
        "soru": "Bir ilin 50 yıl önceki ve günümüzdeki fotoğrafları karşılaştırıldığında; tarım alanlarının yerini alışveriş merkezlerinin aldığı, derelerin üzerinin kapatıldığı ve yeni yolların yapıldığı görülmüştür.\n\nBu değişimlerin temel sebebi aşağıdakilerden hangisidir?",
        "siklar": {"A": "Doğal afetlerin artması", "B": "Nüfus artışı ve kentleşmenin hızlanması", "C": "İklim değişikliğinin tek başına etkisi", "D": "Tarımsal üretimin artması"},
        "dogru_cevap": "B",
        "aciklama": "Tarım alanlarının yapılaşmaya dönüşmesi ve yeni yollar, nüfus artışı ve kentleşmenin doğrudan sonucudur."
    },
    {
        "unite": U2, "konu": "Doğal ve Beşeri Değişim", "yil": 2022, "zorluk": "Orta",
        "soru": "Bir köyde 20 yıl önce 500 kişi yaşarken şimdi 120 kişi yaşamaktadır. Okulun öğrenci sayısı da oldukça azalmıştır.\n\nBu durumun en olası nedeni aşağıdakilerden hangisidir?",
        "siklar": {"A": "Köyde doğum oranlarının çok yüksek olması", "B": "Köyden kente göçün yaşanması", "C": "Köye yeni aileler yerleşmesi", "D": "Köydeki tarım alanlarının genişlemesi"},
        "dogru_cevap": "B",
        "aciklama": "Nüfusun ve öğrenci sayısının azalması köyden kente göçün en belirgin göstergesidir."
    },
    {
        "unite": U2, "konu": "Doğal ve Beşeri Değişim", "yil": 2023, "zorluk": "Orta",
        "soru": "I. Fabrika yapılması\nII. Deprem sonucu yer şekillerinin değişmesi\nIII. Orman alanlarının tarla haline getirilmesi\n\nYukarıdakilerden hangileri beşeri (insan kaynaklı) değişimlere örnek oluşturur?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "C",
        "aciklama": "Fabrika yapımı ve ormanları tarlaya çevirme insan kaynaklı değişimlerdir. Deprem doğal bir değişimdir."
    },
    {
        "unite": U2, "konu": "Yaşadığımız İlin Göreceli Konumu", "yil": 2021, "zorluk": "Orta",
        "soru": "Ankara ili, İstanbul'un doğusunda, Konya'nın kuzeyinde ve Kırıkkale'nin batısında yer almaktadır.\n\nBu bilgide Ankara'nın konumu hangi yöntemle ifade edilmiştir?",
        "siklar": {"A": "Koordinat sistemi kullanılarak", "B": "Matematiksel konum olarak", "C": "Diğer illere göre göreceli konum olarak", "D": "Yükselti ve deniz seviyesine göre"},
        "dogru_cevap": "C",
        "aciklama": "Çevresindeki illere göre konumun belirlenmesi göreceli konum ifadesidir."
    },

    # ---- ÜNİTE 3: ORTAK MİRASIMIZ (8 soru) ----
    {
        "unite": U3, "konu": "Anadolu'da İlk Toplumlar", "yil": 2024, "zorluk": "Zor",
        "soru": "Çatalhöyük kazılarında evlerin bitişik düzende inşa edildiği, kapılarının çatıdan olduğu ve duvarlarına av sahneleri çizildiği belirlenmiştir. Ayrıca buğday ve arpa kalıntılarına da rastlanmıştır.\n\nBu bulgulara göre Çatalhöyük halkı hakkında;\nI. Tarımla uğraştıkları\nII. Yerleşik hayata geçtikleri\nIII. Sanata önem verdikleri\nyargılarından hangilerine ulaşılabilir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I, II ve III"},
        "dogru_cevap": "D",
        "aciklama": "Tahıl kalıntıları tarımı, bitişik evler yerleşik hayatı, duvar resimleri sanatsal faaliyetleri kanıtlar."
    },
    {
        "unite": U3, "konu": "Anadolu'da İlk Toplumlar", "yil": 2023, "zorluk": "Orta",
        "soru": "Göbeklitepe, bilinen en eski tapınak kalıntısıdır ve yaklaşık 12.000 yıl öncesine tarihlendirilmektedir. Bu yapı, henüz tarıma geçilmemiş dönemde avcı-toplayıcı topluluklar tarafından inşa edilmiştir.\n\nBu bilgi aşağıdaki yaygın düşüncelerden hangisini değiştirmektedir?",
        "siklar": {"A": "İlk insanların ateşi kullanamadığını", "B": "Büyük yapıların ancak yerleşik toplumlar tarafından yapılabileceğini", "C": "Anadolu'nun tarih öncesinde boş olduğunu", "D": "Avcı-toplayıcıların hiçbir alete sahip olmadığını"},
        "dogru_cevap": "B",
        "aciklama": "Göbeklitepe, yerleşik hayata geçmeden önce de büyük yapılar inşa edilebileceğini kanıtlamıştır."
    },
    {
        "unite": U3, "konu": "Mezopotamya ve Anadolu Medeniyetleri", "yil": 2024, "zorluk": "Zor",
        "soru": "Sümerler yazıyı, Lidyalılar parayı, Fenikeliler alfabeyi ilk kez kullanmışlardır. Bu icatlar daha sonra tüm dünyaya yayılmıştır.\n\nBu bilgilere göre eski uygarlıklar hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Her uygarlık diğerlerinden bağımsız gelişmiştir", "B": "Uygarlıklar birbirlerinin buluşlarından etkilenmiş ve ortak mirasa katkıda bulunmuştur", "C": "Sadece tek bir uygarlık tüm icatları yapmıştır", "D": "Bu icatlar günümüzde artık kullanılmamaktadır"},
        "dogru_cevap": "B",
        "aciklama": "Farklı uygarlıkların icatlarının yayılması, ortak insanlık mirasına katkıyı ve kültürel etkileşimi gösterir."
    },
    {
        "unite": U3, "konu": "Mezopotamya ve Anadolu Medeniyetleri", "yil": 2023, "zorluk": "Orta",
        "soru": "Hititler, tarihte bilinen ilk yazılı antlaşma olan Kadeş Antlaşması'nı Mısır ile imzalamışlardır.\n\nKadeş Antlaşması'nın tarih açısından en önemli özelliği aşağıdakilerden hangisidir?",
        "siklar": {"A": "En büyük savaşın sona ermesi", "B": "Diplomasi ve yazılı hukukun başlangıcına örnek oluşturması", "C": "Hititlerin Mısır'ı fethetmesi", "D": "Anadolu'nun ilk kez haritasının çıkarılması"},
        "dogru_cevap": "B",
        "aciklama": "İlk yazılı antlaşma olarak Kadeş, diplomasi ve uluslararası hukukun başlangıç noktasıdır."
    },
    {
        "unite": U3, "konu": "Ortak Miras Ögeleri", "yil": 2024, "zorluk": "Orta",
        "soru": "Efes Antik Kenti, Pamukkale travertenleri ve Göbeklitepe UNESCO Dünya Mirası Listesi'ndedir.\n\nBu yerlerin UNESCO listesinde yer almasının temel nedeni aşağıdakilerden hangisidir?",
        "siklar": {"A": "Sadece turizm geliri sağlamaları", "B": "Tüm insanlığa ait evrensel değer taşımaları ve korunmaları gerektiği", "C": "Sadece Türkiye'ye ait olmaları", "D": "Yeni inşa edilmiş yapılar olmaları"},
        "dogru_cevap": "B",
        "aciklama": "UNESCO listesi, evrensel değer taşıyan ve gelecek nesiller için korunması gereken miras ögelerini kapsar."
    },
    {
        "unite": U3, "konu": "Anadolu'da İlk Toplumlar", "yil": 2022, "zorluk": "Zor",
        "soru": "Arkeologlar bir yerleşim yerinde taş aletler, pişmiş topraktan kaplar, hayvan kemikleri ve buğday kalıntıları bulmuşlardır.\n\nBu bulgulara göre bu yerleşim yeri halkının;\nI. Avcılık ve toplayıcılık\nII. Tarım\nIII. El sanatları\nfaaliyetlerinden hangilerini yaptığı söylenebilir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "D",
        "aciklama": "Taş aletler ve kemikler avcılığı, buğday tarımı, pişmiş toprak kaplar el sanatlarını kanıtlar."
    },
    {
        "unite": U3, "konu": "Mezopotamya ve Anadolu Medeniyetleri", "yil": 2022, "zorluk": "Orta",
        "soru": "Sümerler, Fırat ve Dicle nehirleri arasındaki verimli topraklarda kurulmuş ve tarımda sulama kanalları geliştirmişlerdir. Böylece üretim artmış ve nüfus çoğalmıştır.\n\nBu bilgiye göre Mezopotamya medeniyetinin gelişmesinde en etkili faktör aşağıdakilerden hangisidir?",
        "siklar": {"A": "Deniz ticareti yapmaları", "B": "Coğrafi koşulların tarıma elverişli olması", "C": "Güçlü bir orduya sahip olmaları", "D": "Yazıyı çok erken kullanmaları"},
        "dogru_cevap": "B",
        "aciklama": "Verimli topraklar ve nehirler tarımı kolaylaştırmış, bu da medeniyetin gelişmesini sağlamıştır."
    },
    {
        "unite": U3, "konu": "Ortak Miras Ögeleri", "yil": 2021, "zorluk": "Orta",
        "soru": "Öğrenciler, yaşadıkları ildeki eski cami, köprü ve kervansaray gibi yapıları araştırıp fotoğraflamışlardır.\n\nBu etkinliğin amacı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Öğrencilerin fotoğrafçılık becerilerini geliştirmek", "B": "Yerel kültürel mirası tanımak ve koruma bilinci kazandırmak", "C": "Yeni yapılar inşa etmek için yer belirlemek", "D": "Tarihi yapıları yıkarak yerine modern binalar yapmak"},
        "dogru_cevap": "B",
        "aciklama": "Ortak miras ögelerini tanımak ve koruma bilinci kazandırmak sosyal bilgiler eğitiminin temel amaçlarındandır."
    },

    # ---- ÜNİTE 4: YAŞAYAN DEMOKRASİMİZ (4 soru) ----
    {
        "unite": U4, "konu": "Demokrasi ve Cumhuriyet", "yil": 2024, "zorluk": "Orta",
        "soru": "Demokrasilerde halk seçimler yoluyla kendini yönetecek temsilcileri belirler. Bu temsilciler halkın adına yasalar yapar ve ülkeyi yönetir.\n\nBuna göre demokrasinin en temel özelliği aşağıdakilerden hangisidir?",
        "siklar": {"A": "Yönetimin tek bir kişinin elinde olması", "B": "Yönetim yetkisinin halktan alınması (milli egemenlik)", "C": "Kanunların sadece yöneticiler tarafından belirlenmesi", "D": "Halkın yönetime katılmaması"},
        "dogru_cevap": "B",
        "aciklama": "Demokrasinin temeli, yönetim yetkisinin halktan (milli egemenlikten) kaynaklanmasıdır."
    },
    {
        "unite": U4, "konu": "Etkin Vatandaş Olmak", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir öğrenci, mahallesindeki parkın bakımsız olduğunu fark ederek belediyeye dilekçe yazmış ve parkın onarılmasını talep etmiştir. Belediye bu talebi değerlendirerek parkı yenilenmiştir.\n\nBu öğrencinin davranışı aşağıdakilerden hangisine örnek oluşturur?",
        "siklar": {"A": "Pasif vatandaşlık", "B": "Etkin vatandaşlık ve demokratik katılım", "C": "Yasadışı eylem", "D": "Bireysel çıkar arayışı"},
        "dogru_cevap": "B",
        "aciklama": "Sorunları fark edip yasal yollarla çözüm aramak etkin vatandaşlığın ve demokratik katılımın örneğidir."
    },
    {
        "unite": U4, "konu": "Temel Hak ve Sorumluluklar", "yil": 2022, "zorluk": "Orta",
        "soru": "Eğitim hakkı, sağlık hakkı ve yaşam hakkı her bireyin doğuştan sahip olduğu temel haklardandır.\n\nBu hakların ortak özelliği aşağıdakilerden hangisidir?",
        "siklar": {"A": "Sadece yetişkinlere tanınan haklardır", "B": "Devredilmez ve vazgeçilmez niteliktedir", "C": "Zenginlik durumuna göre değişir", "D": "Sadece belirli ülkelerde geçerlidir"},
        "dogru_cevap": "B",
        "aciklama": "Temel haklar doğuştan kazanılır, devredilmez ve vazgeçilmez niteliktedir."
    },
    {
        "unite": U4, "konu": "İhtiyaç Halinde Başvurulacak Kurumlar", "yil": 2021, "zorluk": "Orta",
        "soru": "Yangın durumunda 110 İtfaiye, acil sağlık durumunda 112 Ambulans, güvenlik sorunu için 155 Polis aranır.\n\nBu acil durum numaralarını bilmenin önemi aşağıdakilerden hangisidir?",
        "siklar": {"A": "Sadece yetişkinlerin bilmesi gereken bilgilerdir", "B": "Olağanüstü durumlarda hızlı ve doğru müdahale için hayati öneme sahiptir", "C": "Bu numaraları aramak ücretlidir", "D": "Bu kurumlar sadece hafta içi çalışır"},
        "dogru_cevap": "B",
        "aciklama": "Acil durum numaralarını bilmek, kriz anlarında hızlı müdahale sağlayarak hayat kurtarabilir."
    },

    # ---- ÜNİTE 5: HAYATIMIZDA EKONOMİ (3 soru) ----
    {
        "unite": U5, "konu": "Kaynakları Verimli Kullanma", "yil": 2024, "zorluk": "Orta",
        "soru": "Bir ailede su faturalarının çok yüksek olduğu fark edilmiş ve aile üyeleri tasarruf tedbirleri almıştır: Diş fırçalarken musluğu kapatmış, kısa süreli duş alıp, çamaşır makinesini tam dolduğunda çalıştırmıştır.\n\nBu uygulamaların en önemli katkısı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Sadece aile bütçesine katkı sağlaması", "B": "Hem doğal kaynakların korunması hem de ekonomik tasarruf sağlaması", "C": "Su kullanımının tamamen bırakılması", "D": "Sadece çevrecileri ilgilendirmesi"},
        "dogru_cevap": "B",
        "aciklama": "Bilinçli kaynak kullanımı hem doğayı korur hem de bireylerin ekonomik tasarruf yapmasını sağlar."
    },
    {
        "unite": U5, "konu": "İstek ve İhtiyaçlara Göre Bütçe", "yil": 2023, "zorluk": "Orta",
        "soru": "Ege, harçlığıyla hem yeni bir oyun almak hem de okul kırtasiyesini tamamlamak istemektedir. Ancak harçlığı ikisine de yetmemektedir.\n\nEge'nin en doğru kararı aşağıdakilerden hangisi olmalıdır?",
        "siklar": {"A": "Oyunu hemen alıp kırtasiyeyi ertelemek", "B": "Önce ihtiyaç olan kırtasiyeyi alıp oyunu daha sonraya bırakmak", "C": "İkisinden de vazgeçmek", "D": "Borç alarak ikisini de almak"},
        "dogru_cevap": "B",
        "aciklama": "Bütçe planlamasında ihtiyaçlar isteklerden önce gelmelidir. Kırtasiye ihtiyaç, oyun istektir."
    },
    {
        "unite": U5, "konu": "Yaşadığımız İldeki Ekonomik Faaliyetler", "yil": 2022, "zorluk": "Orta",
        "soru": "Rize'de çay üretimi, Gaziantep'te baklava yapımı, Bursa'da otomotiv sanayisi ön plana çıkmaktadır.\n\nBu durum aşağıdakilerden hangisini göstermektedir?",
        "siklar": {"A": "Türkiye'de sadece tarım yapılmaktadır", "B": "Her ilin coğrafi ve beşeri özelliklerine göre farklı ekonomik faaliyetleri öne çıkmaktadır", "C": "Sadece büyük şehirlerde ekonomik faaliyet vardır", "D": "Tüm illerde aynı ürünler üretilmektedir"},
        "dogru_cevap": "B",
        "aciklama": "Her ilin doğal koşulları ve beşeri özellikleri farklı ekonomik faaliyetlerin gelişmesini sağlar."
    },

    # ---- ÜNİTE 6: TEKNOLOJİ VE SOSYAL BİLİMLER (3 soru) ----
    {
        "unite": U6, "konu": "Teknolojik Gelişmelerin Sosyal Hayata Etkisi", "yil": 2024, "zorluk": "Orta",
        "soru": "Akıllı telefonların yaygınlaşmasıyla insanlar dünyanın her yerinden anlık iletişim kurabilmekte, video görüşmesi yapabilmekte ve bilgiye hızla ulaşabilmektedir.\n\nAncak bu teknolojinin;\nI. Yüz yüze iletişimin azalması\nII. Bilgiye hızlı erişim\nIII. Siber zorbalık riskinin artması\ngibi etkileri de bulunmaktadır. Bunlardan hangileri olumsuz etkilerdir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "C",
        "aciklama": "Yüz yüze iletişimin azalması ve siber zorbalık olumsuz etkilerdir. Bilgiye hızlı erişim olumlu bir etkidir."
    },
    {
        "unite": U6, "konu": "Teknolojik Aletlerin Bilinçli Kullanımı", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir öğrenci, tablet bilgisayarını günde 6 saat oyun oynayarak kullanmakta ve bu nedenle ders çalışamamakta, gözlerinde yorgunluk yaşamaktadır.\n\nBu durumun çözümü için en uygun yaklaşım aşağıdakilerden hangisidir?",
        "siklar": {"A": "Tableti tamamen yasaklamak", "B": "Kullanım süresini sınırlayarak teknolojiyi bilinçli ve dengeli kullanmak", "C": "Öğrencinin tüm derslerini tabletten takip etmesini sağlamak", "D": "Oyun oynama süresini daha da artırmak"},
        "dogru_cevap": "B",
        "aciklama": "Teknoloji yasaklanmamalı, bilinçli ve dengeli kullanımı öğretilmelidir."
    },
    {
        "unite": U6, "konu": "Teknolojik Gelişmelerin Sosyal Hayata Etkisi", "yil": 2022, "zorluk": "Orta",
        "soru": "Uzaktan eğitim sayesinde öğrenciler evlerinden derslere katılabilmiş, öğretmenler dijital materyaller kullanarak ders anlatmıştır.\n\nUzaktan eğitimin en önemli avantajı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Öğrencilerin sosyalleşmesini tamamen sağlaması", "B": "Eğitime mekândan bağımsız erişim olanağı sunması", "C": "Yüz yüze eğitimin yerini tamamen alması", "D": "Sadece üniversite seviyesinde uygulanabilmesi"},
        "dogru_cevap": "B",
        "aciklama": "Uzaktan eğitimin en büyük avantajı, mekân sınırlaması olmadan eğitime erişim sağlamasıdır."
    }
]

file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "sorular_5.json")
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
    print(f"5. Sınıf: {len(questions)} soru başarıyla sorular_5.json dosyasına yazıldı.")
