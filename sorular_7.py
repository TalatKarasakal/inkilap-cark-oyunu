import json, os

U1 = "Ünite 1 – Birey ve Toplum"
U2 = "Ünite 2 – Kültür ve Miras"
U3 = "Ünite 3 – İnsanlar, Yerler ve Çevreler"
U4 = "Ünite 4 – Bilim, Teknoloji ve Toplum"
U5 = "Ünite 5 – Üretim, Dağıtım ve Tüketim"
U6 = "Ünite 6 – Etkin Vatandaşlık"
U7 = "Ünite 7 – Küresel Bağlantılar"

questions = [
    # ---- ÜNİTE 1: BİREY VE TOPLUM (8 soru) ----
    {
        "unite": U1, "konu": "İletişim ve Olumlu İletişim Unsurları", "yil": 2024, "zorluk": "Orta",
        "soru": "Ahmet, arkadaşıyla tartışırken karşısındakinin sözünü kesmeden dinlemiş, 'Seni anlıyorum ama benim düşüncem farklı' diyerek fikrini ifade etmiştir.\n\nAhmet'in bu davranışı aşağıdaki iletişim unsurlarından hangisiyle en iyi açıklanabilir?",
        "siklar": {"A": "Empati kurma ve ben dili kullanma", "B": "Otorite kurarak iletişimi yönlendirme", "C": "Pasif iletişim tarzı benimseme", "D": "İletişimi tamamen karşı tarafa bırakma"},
        "dogru_cevap": "A",
        "aciklama": "Karşısındakini dinleyip anladığını belirtmesi empatiyi, 'benim düşüncem' demesi ben dilini gösterir. Bu olumlu iletişimin temelidir."
    },
    {
        "unite": U1, "konu": "İletişim ve Olumlu İletişim Unsurları", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir sınıfta öğretmen, öğrencilerin fikirlerini paylaşmaları için güvenli bir ortam oluşturmuş ve her öğrenciye eşit söz hakkı vermiştir. Ancak bazı öğrenciler arkadaşlarının fikirlerini küçümseyerek alay etmiştir.\n\nBu durumda sağlıklı iletişimi engelleyen temel faktör aşağıdakilerden hangisidir?",
        "siklar": {"A": "Öğretmenin yeterince otoriter olmaması", "B": "Karşılıklı saygı ve hoşgörü eksikliği", "C": "Sınıf mevcudunun fazla olması", "D": "Konuların öğrenci seviyesine uygun olmaması"},
        "dogru_cevap": "B",
        "aciklama": "Ortam uygun olsa bile karşılıklı saygı ve hoşgörü yoksa iletişim sağlıklı işlemez."
    },
    {
        "unite": U1, "konu": "Medyanın Hayatımızdaki Yeri", "yil": 2024, "zorluk": "Zor",
        "soru": "Sosyal medyada yayılan bir haberde, bir doğal afetin boyutları abartılarak verilmiş ve halk arasında panik oluşmuştur. Daha sonra resmi kurumlar haberin gerçeği yansıtmadığını açıklamıştır.\n\nBu olay medya okuryazarlığının hangi yönünün önemini ortaya koymaktadır?",
        "siklar": {"A": "Haberlerin hızlı yayılmasının her zaman faydalı olduğunu", "B": "Bilgi kaynaklarının güvenilirliğini sorgulamanın gerekliliğini", "C": "Sosyal medyanın geleneksel medyadan daha güvenilir olduğunu", "D": "Resmi kurumların haberleri sansürlemek istediğini"},
        "dogru_cevap": "B",
        "aciklama": "Medya okuryazarlığının en önemli yönü bilgi kaynağını sorgulamak ve doğrulamaktır."
    },
    {
        "unite": U1, "konu": "Medyanın Hayatımızdaki Yeri", "yil": 2022, "zorluk": "Orta",
        "soru": "Elif, internette gördüğü bir sağlık bilgisini hemen sosyal medyada paylaşmıştır. Ancak bu bilgi tıbbi olarak yanlış çıkmış ve birçok kişi yanlış yönlendirilmiştir.\n\nElif'in bu davranışından çıkarılacak en önemli ders aşağıdakilerden hangisidir?",
        "siklar": {"A": "Sağlık bilgileri asla internette paylaşılmamalıdır", "B": "Bilgiyi paylaşmadan önce güvenilir kaynaklardan doğrulamalıyız", "C": "Sosyal medya hesapları kapatılmalıdır", "D": "Sadece gazeteciler bilgi paylaşmalıdır"},
        "dogru_cevap": "B",
        "aciklama": "Bilgiyi paylaşmadan önce güvenilir ve uzman kaynaklardan doğrulamak sorumlu medya kullanımının temelidir."
    },
    {
        "unite": U1, "konu": "Kitle İletişim Özgürlüğü", "yil": 2023, "zorluk": "Zor",
        "soru": "Bir ülkede basın kuruluşları hükümet politikalarını eleştiren haberleri yayımlayabilmekte, gazeteciler özgürce haber yapabilmektedir. Ancak bu haberler kişisel hakları ihlal etmemekte ve toplum düzenini bozmamaktadır.\n\nBu durum aşağıdaki kavramlardan hangisini en iyi yansıtmaktadır?",
        "siklar": {"A": "Sansür uygulaması", "B": "Sorumlu basın özgürlüğü", "C": "Kontrolsüz medya düzeni", "D": "Tek sesli yayıncılık"},
        "dogru_cevap": "B",
        "aciklama": "Basının özgürce ama sorumluluk sınırları içinde haber yapması, sorumlu basın özgürlüğünün tanımıdır."
    },
    {
        "unite": U1, "konu": "Kitle İletişim Özgürlüğü", "yil": 2021, "zorluk": "Orta",
        "soru": "I. Farklı görüşlerin kamuoyuyla paylaşılması\nII. Yöneticilerin denetlenmesi\nIII. Bireylerin özel hayatının ifşa edilmesi\n\nYukarıdakilerden hangileri basın özgürlüğünün amaçları arasında sayılabilir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I, II ve III"},
        "dogru_cevap": "B",
        "aciklama": "Basın özgürlüğü farklı görüşlerin paylaşılmasını ve yöneticilerin denetlenmesini amaçlar. Özel hayatın ifşası hak ihlalidir."
    },
    {
        "unite": U1, "konu": "İletişim ve Olumlu İletişim Unsurları", "yil": 2022, "zorluk": "Orta",
        "soru": "Zeynep sınıf başkanlığı seçiminde rakibini tebrik etmiş ve 'Seni destekleyeceğim, birlikte güzel işler yapabiliriz' demiştir.\n\nZeynep'in bu tutumu;\nI. Hoşgörü\nII. Rekabetçilik\nIII. İşbirliği\nözelliklerinden hangilerini yansıtmaktadır?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "C",
        "aciklama": "Rakibini tebrik etmesi hoşgörüyü, birlikte çalışma teklifi işbirliğini gösterir. Rekabetçilik bu davranışta yoktur."
    },
    {
        "unite": U1, "konu": "Medyanın Hayatımızdaki Yeri", "yil": 2024, "zorluk": "Zor",
        "soru": "Bir araştırmaya göre gençlerin %70'i haberleri sosyal medyadan takip etmekte ve bu haberlerin doğruluğunu kontrol etmemektedir.\n\nBu durumun ortaya çıkarabileceği en büyük toplumsal sorun aşağıdakilerden hangisidir?",
        "siklar": {"A": "Gazete satışlarının düşmesi", "B": "Yanlış bilgi ve dezenformasyonun yaygınlaşması", "C": "Televizyon izleme oranlarının artması", "D": "İnternet kullanımının azalması"},
        "dogru_cevap": "B",
        "aciklama": "Doğrulanmamış haberlerin yaygın tüketimi dezenformasyon (yanlış bilgi) sorununu büyütür."
    },

    # ---- ÜNİTE 2: KÜLTÜR VE MİRAS (10 soru) ----
    {
        "unite": U2, "konu": "Beylikten Cihan Devletine", "yil": 2024, "zorluk": "Zor",
        "soru": "Osmanlı Devleti kuruluş döneminde, fethettiği bölgelerdeki Hristiyan halka din ve ibadet özgürlüğü tanımış, onların kendi mahkemelerinde yargılanmalarına izin vermiştir.\n\nOsmanlı'nın bu politikasının temel amacı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Avrupa devletlerinin desteğini kazanmak", "B": "Fethedilen bölgelerde kalıcı hâkimiyet sağlamak ve toplumsal huzuru korumak", "C": "Hristiyan halkı askerî güç olarak kullanmak", "D": "İslam dininin yayılmasını hızlandırmak"},
        "dogru_cevap": "B",
        "aciklama": "Hoşgörü politikası, farklı toplulukların devlete bağlılığını sağlayarak kalıcı hâkimiyetin temelini oluşturmuştur."
    },
    {
        "unite": U2, "konu": "Beylikten Cihan Devletine", "yil": 2023, "zorluk": "Orta",
        "soru": "Osmanlı Devleti'nin kuruluşunda;\nI. Bizans sınırında uç beyliği konumunda olması\nII. Diğer beyliklerin Moğol baskısından kaçan Türkmenleri kabul etmemesi\nIII. Osman Bey'in adaletli yönetimi sayesinde çevresine insanların toplanması\n\nfaktörlerinden hangileri etkili olmuştur?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "D",
        "aciklama": "Uç beyliği konumu gazâ ruhu kazandırmış, Türkmen göçü nüfusu artırmış, adaletli yönetim ise insanları çekmiştir."
    },
    {
        "unite": U2, "konu": "İnsanı Yaşat ki Devlet Yaşasın", "yil": 2024, "zorluk": "Zor",
        "soru": "Osmanlı Devleti'nde tımar sistemi uygulanmış; toprağı işleyen köylü, ürettiği ürünün bir kısmını tımar sahibine vermiş, tımar sahibi ise karşılığında asker yetiştirmiştir. Böylece devlet hem üretimi hem de ordunun ihtiyaçlarını karşılamıştır.\n\nBu sisteme bakılarak tımar uygulamasının;\nI. Tarımsal üretimin sürekliliğini sağlama\nII. Hazineden para harcamadan asker yetiştirme\nIII. Köylünün toprak sahibi olmasını engelleme\namaçlarından hangilerini taşıdığı söylenebilir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "II ve III", "D": "I, II ve III"},
        "dogru_cevap": "B",
        "aciklama": "Tımar sistemi hem üretim sürekliliğini hem de hazineye yük olmadan asker yetiştirilmesini sağlamıştır."
    },
    {
        "unite": U2, "konu": "İnsanı Yaşat ki Devlet Yaşasın", "yil": 2023, "zorluk": "Orta",
        "soru": "Osmanlı'da vakıflar; hastane, medrese, han, hamam, çeşme, köprü gibi pek çok yapı inşa ettirmiştir. Bu yapılar halkın ücretsiz olarak yararlanmasına sunulmuştur.\n\nVakıf kurumunun Osmanlı toplumuna en önemli katkısı aşağıdakilerden hangisidir?",
        "siklar": {"A": "Devletin vergi gelirlerini artırması", "B": "Toplumsal dayanışmayı ve sosyal refahı güçlendirmesi", "C": "Askeri gücün artırılması", "D": "Ticaret yollarının denetim altına alınması"},
        "dogru_cevap": "B",
        "aciklama": "Vakıflar toplumsal dayanışmanın ve sosyal devlet anlayışının Osmanlı'daki en güçlü yansımasıdır."
    },
    {
        "unite": U2, "konu": "Avrupa'da Uyanış", "yil": 2024, "zorluk": "Zor",
        "soru": "Avrupa'da Rönesans hareketinin başlamasında;\nI. Coğrafi Keşifler sonucu yeni kültürlerle tanışılması\nII. İstanbul'un fethinden sonra Bizanslı bilginlerin İtalya'ya göçü\nIII. Matbaanın yaygınlaşmasıyla bilgiye erişimin kolaylaşması\n\ngelişmelerinden hangileri etkili olmuştur?",
        "siklar": {"A": "Yalnız II", "B": "I ve II", "C": "II ve III", "D": "I, II ve III"},
        "dogru_cevap": "D",
        "aciklama": "Rönesans'ın doğuşunda yeni kültürlerle temas, bilgin göçü ve matbaanın yaygınlaşması hep birlikte etkili olmuştur."
    },
    {
        "unite": U2, "konu": "Avrupa'da Uyanış", "yil": 2022, "zorluk": "Orta",
        "soru": "Martin Luther, Katolik Kilisesi'nin endüljans (günah çıkarma kâğıdı) satışına karşı çıkarak 95 maddelik bir bildiri yayımlamıştır. Bu hareket Avrupa'da Reform hareketlerinin başlangıcı olmuştur.\n\nReform hareketinin en önemli sonucu aşağıdakilerden hangisidir?",
        "siklar": {"A": "Avrupa'da mezhep birliğinin sağlanması", "B": "Kilisenin siyasi gücünün zayıflaması ve laik düşüncenin güçlenmesi", "C": "Osmanlı Devleti'nin Avrupa'daki topraklarının genişlemesi", "D": "Feodalite sisteminin güçlenmesi"},
        "dogru_cevap": "B",
        "aciklama": "Reform hareketi kilisenin siyasi otoritesini zayıflatmış ve laik düşüncenin temellerini atmıştır."
    },
    {
        "unite": U2, "konu": "Değişen Dünya'da Değişen Osmanlı", "yil": 2023, "zorluk": "Zor",
        "soru": "XVII. yüzyıldan itibaren Osmanlı Devleti'nde tımar sisteminin bozulması, vergilerin artırılması ve Celâli İsyanlarının çıkması gibi olaylar yaşanmıştır. Aynı dönemde Avrupa'da bilimsel ve teknolojik gelişmeler hız kazanmıştır.\n\nBu iki gelişme birlikte değerlendirildiğinde aşağıdaki sonuçlardan hangisine ulaşılabilir?",
        "siklar": {"A": "Osmanlı Devleti Avrupa'dan daha güçlüdür", "B": "Osmanlı'nın Avrupa karşısında geri kalma sürecine girdiği", "C": "Avrupa devletlerinin Osmanlı'yı taklit ettiği", "D": "Celâli İsyanlarının Avrupa'yı da etkilediği"},
        "dogru_cevap": "B",
        "aciklama": "İç sorunlar ve Avrupa'nın yükselişi Osmanlı'nın gerileme/geri kalma sürecini başlatmıştır."
    },
    {
        "unite": U2, "konu": "Değişen Dünya'da Değişen Osmanlı", "yil": 2022, "zorluk": "Orta",
        "soru": "Lale Devri'nde (1718-1730) İstanbul'da ilk matbaa açılmış, çeşitli Avrupa başkentlerine elçiler gönderilmiş ve İstanbul'da pek çok bahçe ve çeşme yapılmıştır.\n\nBu bilgilere göre Lale Devri hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Sadece askeri alanda ıslahat yapılmıştır", "B": "Batı'nın kültürel ve teknolojik gelişmelerinden yararlanılmaya çalışılmıştır", "C": "Osmanlı toprakları genişlemiştir", "D": "Halk arasında eşitlik tam sağlanmıştır"},
        "dogru_cevap": "B",
        "aciklama": "Matbaa, elçi gönderimi gibi adımlar Batı'nın kültürel ve teknolojik birikiminden faydalanma çabasıdır."
    },
    {
        "unite": U2, "konu": "Osmanlı'dan Kalan Mirasımız", "yil": 2021, "zorluk": "Orta",
        "soru": "Osmanlı Devleti döneminde inşa edilen camiler, hanlar, hamamlar, medreseler ve köprüler günümüzde hâlâ ayaktadır ve turizm açısından büyük değer taşımaktadır.\n\nBu yapılar Osmanlı'nın hangi alanlardan günümüze miras bıraktığının kanıtıdır?",
        "siklar": {"A": "Askeri ve siyasi", "B": "Mimari ve kültürel", "C": "Ekonomik ve ticari", "D": "Bilimsel ve teknolojik"},
        "dogru_cevap": "B",
        "aciklama": "Osmanlı'nın cami, han, hamam gibi eserleri mimari ve kültürel mirası temsil eder."
    },
    {
        "unite": U2, "konu": "Beylikten Cihan Devletine", "yil": 2021, "zorluk": "Zor",
        "soru": "Fatih Sultan Mehmet, İstanbul'u fethettikten sonra farklı din ve milletlere mensup insanların İstanbul'a yerleşmesini teşvik etmiştir. Rum Patrikhanesi'nin varlığını sürdürmesine izin vermiş, Yahudi ve Ermeni cemaatlerine kendi dini liderlerini seçme hakkı tanımıştır.\n\nFatih'in bu uygulamalarının temel gerekçesi aşağıdakilerden hangisidir?",
        "siklar": {"A": "İstanbul'u bir dünya başkenti haline getirme isteği", "B": "Avrupa devletlerinin baskısına boyun eğmesi", "C": "Gayrimüslim halkı asimilasyona (zorla Müslümanlaştırma) tabi tutması", "D": "Halkın vergi ödememesi için yapılan düzenleme"},
        "dogru_cevap": "A",
        "aciklama": "Farklı din ve milletlerin bir arada yaşadığı kozmopolit bir başkent oluşturmak Fatih'in vizyonuydu."
    },

    # ---- ÜNİTE 3: İNSANLAR, YERLER VE ÇEVRELER (8 soru) ----
    {
        "unite": U3, "konu": "Yerleşme ve Seyahat Özgürlüğü", "yil": 2024, "zorluk": "Orta",
        "soru": "Anayasamıza göre her vatandaş, yurt içinde serbestçe dolaşabilir ve istediği yerde yerleşebilir. Ancak bu hak, salgın hastalık durumlarında veya suç soruşturması gibi durumlarda sınırlandırılabilir.\n\nBu bilgiye göre yerleşme ve seyahat özgürlüğü hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Bu hak hiçbir koşulda sınırlandırılamaz", "B": "Kamu düzeni ve güvenliği gereği belirli durumlarda sınırlandırılabilir", "C": "Sadece devlet memurları bu haktan yararlanabilir", "D": "Bu hak sadece yurt dışı seyahatleri kapsar"},
        "dogru_cevap": "B",
        "aciklama": "Temel haklar istisnai durumlarda (kamu düzeni, salgın vb.) yasayla sınırlandırılabilir."
    },
    {
        "unite": U3, "konu": "Türkiye'nin Nüfus Özellikleri", "yil": 2024, "zorluk": "Zor",
        "soru": "Türkiye'nin batı bölgeleri doğu bölgelerine göre çok daha yoğun nüfuslanmıştır. İstanbul, Ankara, İzmir gibi şehirler milyonlarca insana ev sahipliği yaparken, Hakkari, Tunceli gibi iller oldukça seyrek nüfusludur.\n\nBu durumun oluşmasında;\nI. Sanayileşme ve iş imkânları\nII. İklim ve yer şekilleri\nIII. Ulaşım imkânlarının gelişmişliği\nfaktörlerinden hangileri etkilidir?",
        "siklar": {"A": "Yalnız I", "B": "I ve II", "C": "I ve III", "D": "I, II ve III"},
        "dogru_cevap": "D",
        "aciklama": "Nüfus dağılışını sanayi/iş imkânları, doğal koşullar ve ulaşım birlikte etkiler."
    },
    {
        "unite": U3, "konu": "Türkiye'nin Nüfus Özellikleri", "yil": 2023, "zorluk": "Orta",
        "soru": "Türkiye'de son yıllarda doğum oranlarının düşmesi ve yaşam süresinin uzaması sonucunda yaşlı nüfus oranı artmaya başlamıştır.\n\nBu değişimin aşağıdakilerden hangisine yol açması beklenir?",
        "siklar": {"A": "Çalışabilir nüfus oranının ve üretimin azalması", "B": "Okul öncesi eğitim kurumlarına talebin artması", "C": "Doğum oranlarının yeniden hızla yükselmesi", "D": "Kırsal bölgelere göçün artması"},
        "dogru_cevap": "A",
        "aciklama": "Yaşlı nüfus oranının artması çalışabilir nüfusun ve üretimin azalmasına yol açabilir."
    },
    {
        "unite": U3, "konu": "Göç ve Sonuçları", "yil": 2024, "zorluk": "Zor",
        "soru": "Mehmet'in ailesi daha iyi iş imkânları ve çocuklarına kaliteli eğitim sağlamak için köyden büyükşehre taşınmıştır. Ancak şehirde yüksek kira, trafik yoğunluğu ve kalabalık gibi sorunlarla karşılaşmışlardır.\n\nBu durum göçün hangi yönünü ortaya koymaktadır?",
        "siklar": {"A": "Göçün sadece olumlu sonuçları vardır", "B": "Göçün hem itici hem çekici faktörleri ve olumsuz sonuçları bulunmaktadır", "C": "Köyden kente göç tamamen engellenmelidir", "D": "Göç sadece ekonomik nedenlerle gerçekleşir"},
        "dogru_cevap": "B",
        "aciklama": "İş ve eğitim çekici faktörler, yüksek kira ve kalabalık olumsuz sonuçlardır. Göç çok boyutlu bir olgudur."
    },
    {
        "unite": U3, "konu": "Göç ve Sonuçları", "yil": 2022, "zorluk": "Orta",
        "soru": "Türkiye'de 1950'lerden itibaren köyden kente büyük bir göç dalgası yaşanmıştır. Bu göçün sonucunda büyükşehirlerde gecekondulaşma, çarpık kentleşme ve altyapı yetersizlikleri ortaya çıkmıştır.\n\nBu bilgiye göre aşağıdakilerden hangisi köyden kente göçün sonuçlarından biri değildir?",
        "siklar": {"A": "Kentlerde konut sorunun ortaya çıkması", "B": "Şehirlerde nüfus yoğunluğunun artması", "C": "Kırsal alanda tarımsal üretimin artması", "D": "Kentlerde altyapı sorunlarının büyümesi"},
        "dogru_cevap": "C",
        "aciklama": "Köyden kente göç, kırsal alanda işgücü kaybına ve tarımsal üretimin düşmesine yol açar, artmasına değil."
    },
    {
        "unite": U3, "konu": "Geçmişten Günümüze Yerleşme", "yil": 2023, "zorluk": "Zor",
        "soru": "İlk insanlar su kenarlarına, verimli topraklara ve iklimi ılıman bölgelere yerleşmeyi tercih etmişlerdir. Günümüzde ise yerleşim yeri seçiminde sanayi tesislerinin, ulaşım ağlarının ve sosyal imkânların bulunması daha belirleyici hale gelmiştir.\n\nBu değişim aşağıdakilerden hangisinin sonucudur?",
        "siklar": {"A": "Doğal çevrenin insanlar için artık hiç önemli olmaması", "B": "Teknoloji ve sanayileşme ile beşeri faktörlerin önem kazanması", "C": "İnsanların tarımdan tamamen vazgeçmesi", "D": "İklim değişikliğinin yerleşimi belirleyen tek faktör olması"},
        "dogru_cevap": "B",
        "aciklama": "Teknoloji ve sanayileşme, yerleşim tercihlerinde beşeri faktörlerin öne çıkmasını sağlamıştır."
    },
    {
        "unite": U3, "konu": "Yerleşme ve Seyahat Özgürlüğü", "yil": 2021, "zorluk": "Orta",
        "soru": "Bir kişi, belediye tarafından afet riski nedeniyle yasaklanan bir bölgeye yerleşmek istemiş ancak izin verilmemiştir.\n\nBu kısıtlama aşağıdakilerden hangisiyle açıklanabilir?",
        "siklar": {"A": "Kişinin yerleşme hakkının ihlal edilmesi", "B": "Kamu güvenliği açısından hakların sınırlandırılabilmesi", "C": "Belediyenin yetkisini kötüye kullanması", "D": "Yerleşme özgürlüğünün sadece kağıt üzerinde olması"},
        "dogru_cevap": "B",
        "aciklama": "Afet riski gibi durumlarda can güvenliği için yerleşme hakkı kamu yararı gereği sınırlandırılabilir."
    },
    {
        "unite": U3, "konu": "Göç ve Sonuçları", "yil": 2021, "zorluk": "Zor",
        "soru": "Suriye'deki iç savaş nedeniyle milyonlarca insan, başta Türkiye olmak üzere komşu ülkelere sığınmak zorunda kalmıştır.\n\nBu göç hareketi aşağıdaki göç türlerinden hangisine örnek oluşturur?",
        "siklar": {"A": "İç göç – Gönüllü", "B": "Dış göç – Zorunlu", "C": "Mevsimlik göç", "D": "Beyin göçü"},
        "dogru_cevap": "B",
        "aciklama": "Savaş nedeniyle ülke dışına çıkmak zorunda kalmak zorunlu dış göçün en belirgin örneğidir."
    },

    # ---- ÜNİTE 4: BİLİM, TEKNOLOJİ VE TOPLUM (4 soru) ----
    {
        "unite": U4, "konu": "Kil Tabletlerden Akıllı Tabletlere", "yil": 2024, "zorluk": "Orta",
        "soru": "İnsanlık tarihi boyunca bilgiyi kaydetme yöntemleri sürekli değişmiştir. Sümerler kil tabletlere, Mısırlılar papirüse, Çinliler kâğıda yazmışlardır. Günümüzde ise bilgi dijital ortamda depolanmaktadır.\n\nBu gelişme süreci aşağıdakilerden hangisini en iyi kanıtlamaktadır?",
        "siklar": {"A": "Eski dönemlerin bilgi birikiminin tamamen kaybolduğunu", "B": "İnsanın bilgiyi koruma ve aktarma ihtiyacının her dönemde var olduğunu", "C": "Dijital teknolojinin diğer tüm yöntemleri gereksiz kıldığını", "D": "Sadece gelişmiş toplumların bilgi kaydettiğini"},
        "dogru_cevap": "B",
        "aciklama": "Araçlar değişse de bilgiyi koruma ve aktarma ihtiyacı insanlık tarihi boyunca süreklidir."
    },
    {
        "unite": U4, "konu": "Bilimin Öncüleri", "yil": 2023, "zorluk": "Orta",
        "soru": "Ali Kuşçu astronomi, İbn-i Sina tıp, Piri Reis haritacılık alanlarında dünyaca ünlü eserler vermiş Türk-İslam bilginleridir. Bu bilginlerin eserleri Avrupa üniversitelerinde de yüzyıllarca okunmuştur.\n\nBu durum aşağıdakilerden hangisini kanıtlamaktadır?",
        "siklar": {"A": "Bilim tek bir uygarlığın tekelindedir", "B": "Türk-İslam bilginleri evrensel bilime önemli katkılarda bulunmuştur", "C": "Avrupa'da bilimsel çalışma yapılmamıştır", "D": "Bu bilginlerin eserleri günümüzde geçerliliğini yitirmiştir"},
        "dogru_cevap": "B",
        "aciklama": "Eserlerinin Avrupa'da da okutulması, Türk-İslam bilginlerinin evrensel bilime katkısının kanıtıdır."
    },
    {
        "unite": U4, "konu": "Her Yenilik Geleceğimize Katkıdır", "yil": 2022, "zorluk": "Zor",
        "soru": "Buhar makinesinin icadı, fabrikaların kurulmasına, üretimin artmasına ve şehirlerin büyümesine yol açmıştır. Ancak aynı zamanda çevre kirliliği ve işçi hakları sorunları gibi olumsuzlukları da beraberinde getirmiştir.\n\nBu duruma göre teknolojik yenilikler hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Teknolojik yenilikler her zaman sadece olumlu sonuçlar doğurur", "B": "Yenilikler hem olumlu hem olumsuz toplumsal sonuçlar doğurabilir", "C": "Buhar makinesi toplum yaşamını hiç etkilememiştir", "D": "Teknolojik gelişmeler sadece bilim insanlarını ilgilendirir"},
        "dogru_cevap": "B",
        "aciklama": "Her teknolojik yeniliğin toplumsal, çevresel ve ekonomik boyutlarıyla hem olumlu hem olumsuz etkileri olabilir."
    },
    {
        "unite": U4, "konu": "Özgür Düşüncenin Bilime Katkısı", "yil": 2024, "zorluk": "Zor",
        "soru": "Galileo Galilei, Dünya'nın Güneş etrafında döndüğünü savunduğu için kilise tarafından yargılanmış ve ev hapsine mahkûm edilmiştir. Ancak yıllar sonra bilim dünyası onun haklı olduğunu kanıtlamıştır.\n\nBu olay bilim tarihi açısından aşağıdakilerden hangisini göstermektedir?",
        "siklar": {"A": "Bilimsel ilerlemeler için düşünce özgürlüğünün zorunlu olduğunu", "B": "Kilisenin bilim konusunda daima haklı olduğunu", "C": "Bilimin sadece güçlü devletlerde geliştiğini", "D": "Bilim insanlarının toplumdan soyutlanması gerektiğini"},
        "dogru_cevap": "A",
        "aciklama": "Galileo örneği, düşünce özgürlüğü olmadan bilimsel ilerlemenin engellenebileceğini gösterir."
    },

    # ---- ÜNİTE 5: ÜRETİM, DAĞITIM VE TÜKETİM (3 soru) ----
    {
        "unite": U5, "konu": "Dijital Dünya", "yil": 2024, "zorluk": "Orta",
        "soru": "E-ticaret sayesinde bir çiftçi, yetiştirdiği organik ürünleri aracısız olarak doğrudan tüketiciye ulaştırabilmektedir.\n\nBu durumun en önemli ekonomik faydası aşağıdakilerden hangisidir?",
        "siklar": {"A": "Üreticinin gelirinin artması ve tüketicinin daha uygun fiyata ürüne ulaşması", "B": "Aracıların zenginleşmesi", "C": "Tarımsal üretimin tamamen sona ermesi", "D": "İnternetin ekonomiye hiçbir etkisinin olmaması"},
        "dogru_cevap": "A",
        "aciklama": "E-ticaret aracıları devre dışı bırakarak hem üretici hem tüketici lehine fiyat avantajı sağlar."
    },
    {
        "unite": U5, "konu": "Vakıf Demek Medeniyet Demek", "yil": 2023, "zorluk": "Orta",
        "soru": "Osmanlı döneminde kurulan vakıflar; yolcuların barınması için kervansaraylar, öğrencilerin eğitimi için medreseler, hastaların tedavisi için darüşşifalar inşa ettirmiştir.\n\nBu bilgilere göre vakıf kültürü hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Vakıflar yalnızca dini hizmetler vermiştir", "B": "Vakıflar toplumsal ihtiyaçların karşılanmasında öncü bir rol üstlenmiştir", "C": "Vakıflar devletin kontrolünde ticari kurumlardır", "D": "Vakıflar sadece zenginlere hizmet vermiştir"},
        "dogru_cevap": "B",
        "aciklama": "Eğitim, sağlık ve barınma gibi alanlarda hizmet veren vakıflar toplumsal ihtiyaçları karşılayan öncü kurumlardır."
    },
    {
        "unite": U5, "konu": "Toprak Ana", "yil": 2022, "zorluk": "Orta",
        "soru": "Verimli tarım topraklarının hızlı kentleşme sonucu betonla kaplanması, uzun vadede gıda üretimini olumsuz etkilemektedir.\n\nBu sorunun çözümü için aşağıdakilerden hangisi en uygun yaklaşımdır?",
        "siklar": {"A": "Tarım arazilerinin imara açılmasının teşvik edilmesi", "B": "Kentleşmenin planlanarak tarım arazilerinin korunması", "C": "Tüm gıdaların ithal edilmesi", "D": "Tarımsal faaliyetlerin tamamen durdurulması"},
        "dogru_cevap": "B",
        "aciklama": "Planlı kentleşme ve tarım arazilerinin korunması, sürdürülebilir gıda üretiminin temelidir."
    },

    # ---- ÜNİTE 6: ETKİN VATANDAŞLIK (3 soru) ----
    {
        "unite": U6, "konu": "Demokrasinin Temel İlkeleri", "yil": 2024, "zorluk": "Zor",
        "soru": "Bir ülkede seçimler düzenli olarak yapılmakta, ancak muhalefet partileri kapatılmakta ve basın özgürlüğü kısıtlanmaktadır.\n\nBu ülkenin yönetim anlayışı hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Tam demokratik bir ülkedir", "B": "Seçim yapılması tek başına demokrasi için yeterli değildir", "C": "Basın özgürlüğü demokrasiyle ilgisizdir", "D": "Muhalefet partileri demokraside gereksizdir"},
        "dogru_cevap": "B",
        "aciklama": "Demokrasi sadece seçimden ibaret değildir; basın özgürlüğü, muhalefet ve hukukun üstünlüğü de gereklidir."
    },
    {
        "unite": U6, "konu": "Atatürk ve Demokrasi", "yil": 2023, "zorluk": "Orta",
        "soru": "Atatürk 'Egemenlik kayıtsız şartsız milletindir' ilkesini Cumhuriyetin temeli olarak belirlemiştir. Bu ilke doğrultusunda TBMM kurulmuş ve milletin yönetime katılması sağlanmıştır.\n\nBu ilke aşağıdaki yönetim anlayışlarından hangisiyle doğrudan ilişkilidir?",
        "siklar": {"A": "Monarşi", "B": "Teokrasi", "C": "Milli egemenlik ve demokrasi", "D": "Oligarşi"},
        "dogru_cevap": "C",
        "aciklama": "Egemenliğin millete ait olması, milli egemenlik ve demokratik yönetimin temelidir."
    },
    {
        "unite": U6, "konu": "Hakimiyet Milletindir", "yil": 2022, "zorluk": "Orta",
        "soru": "Seçme ve seçilme hakkı, düşünce özgürlüğü, basın özgürlüğü gibi haklar demokratik toplumların vazgeçilmez unsurlarıdır.\n\nBu hakların ortak özelliği aşağıdakilerden hangisidir?",
        "siklar": {"A": "Yalnızca belirli meslek gruplarına tanınmış olması", "B": "Vatandaşların yönetime katılımını ve denetimini sağlaması", "C": "Sadece seçim dönemlerinde geçerli olması", "D": "Devlet tarafından her zaman sınırlandırılabilmesi"},
        "dogru_cevap": "B",
        "aciklama": "Bu haklar vatandaşların yönetime katılmasını, yönetimi denetlemesini ve hesap sorabilmesini sağlar."
    },

    # ---- ÜNİTE 7: KÜRESEL BAĞLANTILAR (2 soru) ----
    {
        "unite": U7, "konu": "Yurtta Barış Dünya'da Barış", "yil": 2024, "zorluk": "Orta",
        "soru": "Atatürk'ün 'Yurtta sulh, cihanda sulh' ilkesi Türkiye'nin dış politikasının temelini oluşturmuştur. Bu ilke doğrultusunda Türkiye, BM ve NATO gibi uluslararası kuruluşlara üye olmuştur.\n\nBu bilgiye göre Türkiye'nin dış politikası hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {"A": "Saldırgan ve yayılmacı bir politika izlenmektedir", "B": "Uluslararası işbirliğine ve barışa dayalı bir politika benimsenmektedir", "C": "Türkiye hiçbir uluslararası kuruluşa üye değildir", "D": "Dış politikada yalnızca askeri güç kullanılmaktadır"},
        "dogru_cevap": "B",
        "aciklama": "Uluslararası kuruluşlara üyelik, işbirliği ve barışçıl dış politikanın göstergesidir."
    },
    {
        "unite": U7, "konu": "Küresel Sorunlara Çözüm", "yil": 2023, "zorluk": "Zor",
        "soru": "Küresel ısınma, açlık, salgın hastalıklar ve göç gibi sorunlar tek bir ülkenin çözebileceği boyutun ötesine geçmiştir.\n\nBu durum aşağıdakilerden hangisinin gerekliliğini ortaya koymaktadır?",
        "siklar": {"A": "Her ülkenin kendi sorunlarını tek başına çözmesi", "B": "Uluslararası işbirliği ve ortak çözüm arayışının zorunlu olduğu", "C": "Küresel sorunların çözümünün imkânsız olduğu", "D": "Sadece büyük devletlerin sorunlarla ilgilenmesi gerektiği"},
        "dogru_cevap": "B",
        "aciklama": "Küresel sorunlar sınır tanımaz; çözümleri de ancak uluslararası işbirliğiyle mümkündür."
    }
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sorular_7.json")
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=4)
    print(f"7. Sınıf: {len(questions)} soru başarıyla sorular_7.json dosyasına yazıldı.")
