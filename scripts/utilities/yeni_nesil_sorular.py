import json
import os

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

questions = [
    # ---- ÜNİTE 1 ----
    {
        "unite": U1,
        "konu": "Avrupa'daki Gelişmeler ve Osmanlı",
        "yil": 2024,
        "zorluk": "Zor",
        "soru": "Fransız İhtilali ile yayılan milliyetçilik akımı, çok uluslu bir yapıya sahip olan Osmanlı Devleti'ni derinden etkilemiştir. Sırplar, Yunanlar ve Bulgarlar gibi Balkan milletleri teker teker isyan ederek kendi bağımsız devletlerini kurmak istemişlerdir. Osmanlı aydınları ve devlet adamları ise bu parçalanmayı önlemek için Tanzimat ve Islahat fermanlarını yayımlamış, ayrıca meşrutiyeti ilan ederek halka yönetime katılma hakkı vermişlerdir.\n\nVerilen bu bilgilere göre Osmanlı Devleti'nin aldığı önlemlerin temel amacı aşağıdakilerden hangisidir?",
        "siklar": {
            "A": "Avrupa devletlerinin ekonomik desteğini almak",
            "B": "Sınırlarını genişleterek yeni topraklar fethetmek",
            "C": "Azınlıkların devlete bağlılığını artırarak dağılmayı önlemek",
            "D": "Milliyetçilik akımının Avrupa'daki etkisini kırmak"
        },
        "dogru_cevap": "C",
        "aciklama": "Parçada azınlık isyanlarına karşı Osmanlı'nın fermanlar ve meşrutiyet ile halka haklar vererek parçalanmayı (dağılmayı) engellemek istediği açıkça vurgulanmıştır. Yeni nesil sorularda okuduğunu anlama ve yorumlama ön plandadır."
    },
    {
        "unite": U1,
        "konu": "Mustafa Kemal'in Fikir Hayatı",
        "yil": 2023,
        "zorluk": "Orta",
        "soru": "Manastır Askerî İdadisinde öğrenim gördüğü yıllarda Mustafa Kemal'i en çok etkileyen olaylardan biri 1897 Türk-Yunan Savaşı'dır. Bu savaşta Türk ordusu cephede büyük bir zafer kazanmasına rağmen, masada yapılan antlaşma ile beklenen avantajı elde edememiştir. Mustafa Kemal, bu durum üzerine 'Savaş cephede kazanılır ama diplomasiyle sonuçlandırılır' gerçeğini yaşayarak öğrenmiştir.\n\nBu metinden yola çıkılarak Mustafa Kemal ile ilgili aşağıdaki yargılardan hangisine ulaşılabilir?",
        "siklar": {
            "A": "Sadece askerî deha ile devletin yönetilebileceğine inanmıştır.",
            "B": "Dış politikanın ve diplomatik başarıların askerî başarılar kadar önemli olduğunu kavramıştır.",
            "C": "Osmanlı Devleti'nin Avrupa tarzı okullar açmasını savunmuştur.",
            "D": "Gençlik yıllarında askerlikten çok siyasete ilgi duymuştur."
        },
        "dogru_cevap": "B",
        "aciklama": "Cephede kazanılan zaferin masa başında kaybedilmesi, diplomasi ve dış politikanın gücünü gösterir. Mustafa Kemal'in bu olaydan çıkardığı ders budur."
    },
    {
        "unite": U1,
        "konu": "Trablusgarp Savaşı",
        "yil": 2022,
        "zorluk": "Zor",
        "soru": "İtalya'nın Trablusgarp’a saldırması üzerine Osmanlı Devleti bölgeye donanma ve ordu gönderememiştir. Bunun üzerine Mustafa Kemal ve bir grup genç subay gönüllü olarak Trablusgarp’a gitmiş, yerel halkı İtalyanlara karşı örgütleyerek Derne ve Tobruk'ta önemli başarılar elde etmişlerdir.\n\nBu durum Mustafa Kemal'in;\nI. Vatansever\nII. Teşkilatçı (Örgütleyici)\nIII. İnkılapçı\nkişilik özelliklerinden hangilerini yansıtmaktadır?",
        "siklar": {
            "A": "Yalnız I",
            "B": "I ve II",
            "C": "II ve III",
            "D": "I, II ve III"
        },
        "dogru_cevap": "B",
        "aciklama": "Gönüllü olarak gitmesi 'Vatansever', yerel halkı bir araya getirip direnişe geçirmesi 'Teşkilatçı' (örgütleyici) olduğunu gösterir. İnkılapçılık ise yenilik yapmakla ilgilidir ve bu metinde vurgulanmamıştır."
    },
    {
        "unite": U1,
        "konu": "Eğitim Hayatı ve Fikir Gelişimi",
        "yil": 2021,
        "zorluk": "Orta",
        "soru": "Ömer Naci, Manastır Askerî İdadisinde Mustafa Kemal'e edebiyat ve hitabet sevgisi aşılamış; Yüzbaşı Nakiyüddin Bey ise Fransızca öğrenmesine ve Avrupa’daki gelişmeleri takip etmesine öncülük etmiştir. Aynı dönemde Mustafa Kemal, Ziya Gökalp ve Namık Kemal gibi aydınların eserleriyle tanışmıştır.\n\nBuna göre Manastır Askerî İdadisi yıllarının Mustafa Kemal'e katkısı aşağıdakilerden hangisidir?",
        "siklar": {
            "A": "Sırf askerî taktikler konusunda uzmanlaşmasını sağlamıştır.",
            "B": "Yabancı devlet adamlarının desteğini almasına zemin hazırlamıştır.",
            "C": "Çok yönlü ve yeniliklere açık bir fikir adamı olarak yetişmesinde etkili olmuştur.",
            "D": "İlk askerî görevine atanmasını doğrudan kolaylaştırmıştır."
        },
        "dogru_cevap": "C",
        "aciklama": "Edebiyat, hitabet, Fransızca, Avrupa'yı takip ve millîçi aydınları okuması onun sadece asker değil çok yönlü ve yeniliklere açık bir vizyon kazanmasını sağlamıştır."
    },
    {
        "unite": U1,
        "konu": "I. Dünya Savaşı ve Osmanlı Dönüşü",
        "yil": 2020,
        "zorluk": "Orta",
        "soru": "Mustafa Kemal, Sofya'da askerî ataşe olarak görev yaparken Bulgar Parlamentosu'nun toplantılarını yakından izlemiş, Avrupa devletlerinin temsilcileriyle diplomasi alanında fikir alışverişinde bulunmuştur.\n\nMustafa Kemal'in Sofya'daki bu deneyiminin ona sağladığı en önemli kazanım aşağıdakilerden hangisidir?",
        "siklar": {
            "A": "Parlamenter sistemin ve demokrasinin işleyişini yakından tanıması",
            "B": "Bulgar ordusunun askerî sırlarını Osmanlı'ya taşıması",
            "C": "Sofya ataşeliği sayesinde padişahın en yakın danışmanı olması",
            "D": "I. Dünya Savaşı'nın çıkış tarihini önceden tespit etmesi"
        },
        "dogru_cevap": "A",
        "aciklama": "Parlamento toplantılarını izleyerek ve yabancı elçilerle görüşerek parlamenter sistem (meclis sistemi) ve diplomasi hakkında eşsiz deneyimler kazanmıştır."
    },

    # ---- ÜNİTE 2 ----
    {
        "unite": U2,
        "konu": "Mondros Ateşkes Antlaşması",
        "yil": 2024,
        "zorluk": "Zor",
        "soru": "Mondros Mütarekesi’nin 7. maddesi: 'İtilaf Devletleri güvenliklerini tehdit edecek bir durum ortaya çıktığında, herhangi bir stratejik noktayı işgal etme hakkına sahip olacaktır.' şeklindedir.\n\nBu maddenin antlaşmaya konulmasındaki asıl amaç aşağıdakilerden hangisidir?",
        "siklar": {
            "A": "Osmanlı sınırlarını güvence altına alıp padişahı korumak",
            "B": "Anadolu'da yapacakları işgallere hukuki bir kılıf (zemin) hazırlamak",
            "C": "Osmanlı ordusunun ihtiyaçlarını İtilaf Devletleri'nin karşılamasını sağlamak",
            "D": "Sovyet Rusya'nın güneye (Sıcak denizlere) inmesini engellemek"
        },
        "dogru_cevap": "B",
        "aciklama": "İtilaf Devletleri bu çok muğlak ve geniş maddeyle, canları nereyi isterse orayı 'güvenliğimiz tehdit altında' bahanesiyle işgal etmeyi yasallaştırmışlardır."
    },
    {
        "unite": U2,
        "konu": "Amasya Genelgesi",
        "yil": 2023,
        "zorluk": "Zor",
        "soru": "Amasya Genelgesi'nde şu madde yer alır: 'Milletin bağımsızlığını, yine milletin azim ve kararı kurtaracaktır.'\n\nAşağıdakilerden hangisi bu karardan çıkarılabilecek bir sonuç değildir?",
        "siklar": {
            "A": "Milli Mücadele'nin yöntemi (nasıl yapılacağı) belirtilmiştir.",
            "B": "Üstü kapalı da olsa üstünlüğün ve egemenliğin millette olduğu vurgulanmıştır.",
            "C": "Osmanlı yönetiminin artık ülkeyi kurtaramayacağı ifade edilmiştir.",
            "D": "Manda ve himayenin kabul edilebileceği sinyali verilmiştir."
        },
        "dogru_cevap": "D",
        "aciklama": "'Milletin azmi ve kararı kurtaracaktır' ifadesi tam bağımsızlık ve ulusal egemenliğin temelidir. Manda ve himaye ile taban tabana zıttır."
    },
    {
        "unite": U2,
        "konu": "Erzurum Kongresi",
        "yil": 2022,
        "zorluk": "Orta",
        "soru": "Doğu Anadolu illerini Ermenilere verilmesini engellemek amacıyla toplanan Erzurum Kongresi’nde, “Milli sınırlar içinde vatan bir bütündür parçalanamaz” ve “Kuvay-ı Milliye'yi tek kuvvet olarak tanımak, milli iradeyi hakim kılmak esastır” kararları alınmıştır.\n\nBuna göre Erzurum Kongresi hakkında aşağıdaki yorumlardan hangisi yapılabilir?",
        "siklar": {
            "A": "Toplanma amacı bölgesel, aldığı kararlar ise tüm yurdu ilgilendirdiği için ulusaldır.",
            "B": "İstanbul Hükümeti'nin onayı ve desteğiyle toplanmıştır.",
            "C": "Alınan kararlarla padişahın yetkileri daha da artırılmıştır.",
            "D": "Sadece Doğu sınırlarındaki askeri durumu düzenlemekle yetinmiştir."
        },
        "dogru_cevap": "A",
        "aciklama": "Kongre Doğu illeri için toplanmış (bölgesel), ancak vatanın bütünlüğü ve milli irade gibi kararlarla bağımsızlık hareketini tüm ülkeye (ulusal) yaymıştır."
    },
    {
        "unite": U2,
        "konu": "Misak-ı Millî",
        "yil": 2021,
        "zorluk": "Zor",
        "soru": "Son Osmanlı Mebusan Meclisi tarafından kabul edilen Misak-ı Millî kararlarında; Arap çoğunluğun yaşadığı yerlerin, Kars-Ardahan-Batum'un ve Batı Trakya'nın gerekirse halk oylamasına (referandum) başvurularak kendi geleceklerini belirlemeleri istenmiştir.\n\nBu durum Misak-ı Millî'nin;\nI. Milli İrade (Halkın Kararı),\nII. Tam Bağımsızlık,\nIII. Sömürgecilik\nanlayışlarından hangilerine önem verdiğini gösterir?",
        "siklar": {
            "A": "Yalnız I",
            "B": "I ve II",
            "C": "II ve III",
            "D": "I, II ve III"
        },
        "dogru_cevap": "B",
        "aciklama": "Halk oylaması yapılması Milli İradeye (ve Wilson İlkeleri'ne) saygıyı, sömürgeciliğe karşı bağımsız duruşu temsil eder. Sömürgeciliğe ise karşıdır."
    },
    {
        "unite": U2,
        "konu": "Kuvâ-yı Millîye",
        "yil": 2020,
        "zorluk": "Orta",
        "soru": "İzmir'in işgali sonrasında halkın kendiliğinden silahlanarak oluşturduğu yöresel ve düzensiz direniş örgütlerine Kuvâ-yı Millîye adı verilir. Kuvâ-yı Millîye birlikleri düşman ilerleyişini yer yer yavaşlatmış ve halkta direniş ruhunu uyandırmıştır, fakat tam anlamıyla düşmanı yurttan atmaya yeterli olmamıştır.\n\nVerilen bilgiye göre aşağıdakilerden hangisi Kuvâ-yı Millîye'nin millî mücadeleye katkılarından biri değildir?",
        "siklar": {
            "A": "Halkın özgüvenini artırmış ve bağımsızlık ruhunu aşılamıştır.",
            "B": "Düzenli ordunun kurulması için zaman kazanılmasını sağlamıştır.",
            "C": "Düşmanı oyalayarak Anadolu içlerine hızla girmelerini geciktirmiştir.",
            "D": "Düşman ordularını kesin bir hezimete uğratarak Anadolu'dan atmıştır."
        },
        "dogru_cevap": "D",
        "aciklama": "Kuvâ-yı Millîye düşmanı yavaşlatmış ve zaman kazandırmıştır, ancak düşmanı kesin olarak yurttan atan Düzenli Ordu komutasındaki Büyük Taarruz'dur."
    },

    # ---- ÜNİTE 3 ----
    {
        "unite": U3,
        "konu": "Birinci İnönü Savaşı ve Teşkilat-ı Esasiye",
        "yil": 2024,
        "zorluk": "Zor",
        "soru": "Birinci İnönü Zaferi'nden kısa süre sonra, 20 Ocak 1921'de Teşkilat-ı Esasiye Kanunu (1921 Anayasası) kabul edilmiştir. Bu anayasanın birinci maddesi: 'Egemenlik kayıtsız şartsız milletindir. Yönetim şekli, milletin mukadderatını bizzat ve eylemli olarak yönetmesi ilkesine dayanır.' şeklindedir.\n\nBu anayasa maddesinin Türk Kurtuluş Savaşı ve devrim tarihi açısından en büyük önemi nedir?",
        "siklar": {
            "A": "Eski Osmanlı anayasasının tüm maddelerini kaldırması",
            "B": "Tek kişi egemenliğine dayalı padişahlık sisteminin hukuki zeminini yıkıp gücü halka vermesi",
            "C": "Azınlıklara kendi meclislerini kurma hakkı tanıması",
            "D": "Yalnızca yargı sisteminin işleyişini düzenlemesi"
        },
        "dogru_cevap": "B",
        "aciklama": "'Egemenlik kayıtsız şartsız milletindir' ilkesi tam anlamıyla Cumhuriyetin ayak sesleridir ve devleti kişi egemenliğinden millet egemenliğine taşıyan hukuki devrimdir."
    },
    {
        "unite": U3,
        "konu": "Sakarya Meydan Muharebesi ve Sonuçları",
        "yil": 2023,
        "zorluk": "Orta",
        "soru": "Sakarya Meydan Muharebesi öncesi meclis tarafından Mustafa Kemal’e üç aylığına başkomutanlık yetkisi ve meclisin yetkilerini tek başına kullanma hakkı verilmiştir. Mustafa Kemal bu yetkiyi alır almaz ilk iş olarak Tekalif-i Milliye Emirleri'ni (Milli Yükümlülükler) yayımlamıştır.\n\nBuna göre meclisin tüm yetkilerini Mustafa Kemal'e devretmesinin temel gerekçesi aşağıdakilerden hangisi olabilir?",
        "siklar": {
            "A": "Meclisteki sivil vekillerin askerlik hakkında fikir sahibi olmaması",
            "B": "Uluslararası antlaşmaları hızlıca imzalamak istemeleri",
            "C": "Savaş öncesi ortaya çıkan çok acil durumlarda hızlı ve etkili kararlar alınmasını sağlamak",
            "D": "Mustafa Kemal'in padişahın yerine geçmesinin hedeflenmesi"
        },
        "dogru_cevap": "C",
        "aciklama": "Düşmanın Ankara'ya dayandığı bir esnada, mecliste uzun uzun tartışılacak zaman kalmamıştı. Başkomutanlık yetkisi, hızlı karar alma ve uygulama zorunluluğundan doğmuştur."
    },
    {
        "unite": U3,
        "konu": "Maarif Kongresi",
        "yil": 2022,
        "zorluk": "Orta",
        "soru": "Eskişehir-Kütahya Savaşları tüm şiddetiyle devam ederken ve Yunan ordusu Ankara'ya yaklaşırken; Mustafa Kemal Ankara'da Maarif Kongresini (Eğitim Kongresi) toplamış ve kongreye cepheden gelip katılarak çok önemli bir konuşma yapmıştır.\n\nBu durum Mustafa Kemal'in en çok hangi konuya önem verdiğinin kanıtıdır?",
        "siklar": {
            "A": "Eğitime ve milli bir eğitim sistemine verilecek değere",
            "B": "Dış politikanın eğitimli diplomatlar tarafından yürütülmesine",
            "C": "Ordunun teknolojik okullarda eğitim görmesi gerektiğine",
            "D": "Eğitim masraflarının halktan kesilen vergilerle karşılanmasına"
        },
        "dogru_cevap": "A",
        "aciklama": "Cephede silahlı mücadele varken eğitim mücadelesinin de ihmal edilmemesi, Mustafa Kemal'in cehalete karşı savaşı düşmana karşı savaştan farksız gördüğünün kanıtıdır."
    },
    {
        "unite": U3,
        "konu": "Mudanya Ateşkes Antlaşması",
        "yil": 2021,
        "zorluk": "Zor",
        "soru": "Mudanya Ateşkes Antlaşması'nın bazı maddeleri şunlardır:\n- Doğu Trakya, Meriç nehrine kadar boşaltılarak TBMM hükümetine teslim edilecektir.\n- İstanbul ve Boğazların yönetimi TBMM hükümetine bırakılacaktır.\n\nBu maddelere bakılarak aşağıdaki çıkarımlardan hangisi kesin olarak yapılabilir?",
        "siklar": {
            "A": "Osmanlı Devleti hukuken tamamen sona ermiş ve yok sayılmıştır.",
            "B": "Yunanistan'ın Anadolu üzerindeki tüm planlarına İtilaf Devletleri son vermiştir.",
            "C": "Yeni Türk devleti kapitülasyonları kaldırarak ekonomik bağımsızlığını kazanmıştır.",
            "D": "Balkan ülkeleri Türkiye ile sınırlarını kapatmışlardır."
        },
        "dogru_cevap": "A",
        "aciklama": "İtilaf Devletleri'nin İstanbul ve Boğazların yönetimini padişahın bulunduğu Osmanlı Hükümetine değil TBMM'ye vermesi, Osmanlı'yı hukuken yok saydıklarının en net göstergesidir."
    },
    {
        "unite": U3,
        "konu": "Güney Cephesi ve Maraş Direnişi",
        "yil": 2020,
        "zorluk": "Orta",
        "soru": "Sütçü İmam, Maraş'ta Türk kadınına saldırmaya yeltenen Fransız askerine ve Ermeni lejyonerlere karşı ilk kurşunu sıkarak Maraş savunmasını başlatmıştır. Şehirdeki direniş, bölge halkı tarafından hiçbir düzenli ordu desteği olmadan yürütülmüş ve işgalciler püskürtülmüştür.\n\nBu bilgiye dayanarak, Güney Cephesi'ndeki mücadelenin doğası için aşağıdakilerden hangisi söylenebilir?",
        "siklar": {
            "A": "Rusya'nın doğrudan silah yardımına dayanmıştır.",
            "B": "Tamamen Kuvay-ı Milliye (milli direniş ve milis gücü) ruhuyla kazanılmıştır.",
            "C": "Osmanlı ordusunun bölgedeki son birliklerinin eseri olmuştur.",
            "D": "Ankara'daki TBMM meclisinin doğrudan yönettiği planlı askeri taarruzdur."
        },
        "dogru_cevap": "B",
        "aciklama": "Güney Cephesi'nin en büyük özelliği; ordunun olmadığı bölgede, halkın kendi inisiyatifi ve vatan sevgisiyle (Kuvay-ı Milliye ruhuyla) düşmanı atmasıdır."
    },

    # ---- ÜNİTE 4 ----
    {
        "unite": U4,
        "konu": "Siyasi Alanda İnkılaplar",
        "yil": 2024,
        "zorluk": "Orta",
        "soru": "I. Saltanatın kaldırılması (1 Kasım 1922)\nII. Cumhuriyetin İlanı (29 Ekim 1923)\nIII. Halifeliğin kaldırılması (3 Mart 1924)\n\nAtatürk döneminde siyasi alanda gerçekleşen bu üç büyük inkılabın ortak ve en önemli amacı aşağıdakilerden hangisidir?",
        "siklar": {
            "A": "Devletin sadece ekonomik yatırımlarını güçlendirmek",
            "B": "Sosyal hayatta kadın-erkek eşitliğini tam sağlamak",
            "C": "Laik devlet yapısını güçlendirmek ve Millî Egemenliği (Halk yönetimini) tam hakim kılmak",
            "D": "Dış siyasette Batılı devletlerle daha fazla ittifak oluşturmak"
        },
        "dogru_cevap": "C",
        "aciklama": "Saltanat, Hilafet gibi kurumlar bir kişinin veya ailenin güç odaklarıdır. Kaldırılmaları ve Cumhuriyetin ilanı, egemenliği kayıtsız şartsız millete verip yönetimi laikleştirmeyi hedefler."
    },
    {
        "unite": U4,
        "konu": "Eğitim - Tevhid-i Tedrisat",
        "yil": 2023,
        "zorluk": "Zor",
        "soru": "Tevhid-i Tedrisat Kanunu (3 Mart 1924) ile ülkedeki tüm eğitim kurumları ve yabancı okullar Millî Eğitim Bakanlığı’na bağlanmıştır. Din dersleri ve dini eğitim de devlet kontrolüne alınmış, farklı programlar uygulayan medreselerin yerine daha çağdaş eğitim kurumlarının temelleri atılmıştır.\n\nBuna göre Tevhid-i Tedrisat Kanunu'nun sağladığı faydalardan hangisi söylenemez?",
        "siklar": {
            "A": "Kültürel ikilik (çatışma) oluşturan çok başlı eğitim sistemini sona erdirmiştir.",
            "B": "Ülkedeki eğitim sisteminde birlik ve beraberlik sağlanmıştır.",
            "C": "Eğitimin akılcı, milli, çağdaş ve laik bir yapıya bürünmesi yolunu açmıştır.",
            "D": "Yabancı okulların ayrıcalıklı statüsü korunarak Avrupa desteği kazanılmıştır."
        },
        "dogru_cevap": "D",
        "aciklama": "Kanun yabancı okulları da devlet denetimine bağladığı için onların ayrıcalıklı, bağımsız statülerine son vermiş, böylece yasa önünde eşitlik (halkçılık) ve millilik sağlanmıştır."
    },
    {
        "unite": U4,
        "konu": "Hukuk - Medeni Kanun",
        "yil": 2022,
        "zorluk": "Orta",
        "soru": "1926 yılında kabul edilen Türk Medeni Kanunu ile kadınlara istedikleri mesleğe girme, mirasta erkeklerle eşit pay alma, mahkemelerde tanıklıkta erkekle eşit tutulma ve resmi nikâh zorunluluğu gibi haklar tanınmıştır.\n\nBuna göre Türk Medeni Kanunu’nun,\nI. Halkçılık\nII. Laiklik\nIII. Cumhuriyetçilik\nilkelerinden hangileri ile doğrudan ilgili olduğu söylenebilir?",
        "siklar": {
            "A": "Yalnız I",
            "B": "I ve II",
            "C": "II ve III",
            "D": "I, II ve III"
        },
        "dogru_cevap": "B",
        "aciklama": "Miras ve resmi nikâh eşitliği getirmesi halka (kadın-erkek eşitliği) yönelik olduğundan Halkçılık, hukukun dini kurallardan bağımsız, İsviçre tabanlı çağdaş hale gelmesi Laikliktir. Ancak Medeni Kanun 'Siyasi (seçme-seçilme)' hak içermediği için Cumhuriyetçilik ile doğrudan ilgili değildir."
    },
    {
        "unite": U4,
        "konu": "Atatürk İlkeleri - Devletçilik",
        "yil": 2021,
        "zorluk": "Zor",
        "soru": "'Devletçilik' ilkesi Türkiye’de, serbest piyasa ekonomisinin kendi başına yetemediği sert koşullarda zorunluluktan doğmuştur. Halkın sermayesinin yetersiz olması ve 1929 Dünya Ekonomik Bunalımı’nın etkisiyle yeni Türkiye devleti doğrudan yatırımlar yapmış, şeker fabrikaları, Sümerbank ve dokuma tesisleri devlet eliyle açılmıştır.\n\nBu metne göre 'Devletçilik' ilkesi hakkında aşağıdakilerden hangisine ulaşılabilir?",
        "siklar": {
            "A": "Temel amacı özel sektörün yurt içinde hiçbir iş yapmasına izin vermemektir.",
            "B": "Halkın ihtiyaçlarını en kısa sürede üretip dışa bağımlılığı (özellikle sanayide) kırma hedefine dayanır.",
            "C": "Tarımsal üretim ve çiftçinin kalkınması, sanayileşmeden daha çok desteklenmiştir.",
            "D": "Teknolojiyi dışardan satın alarak Osmanlı dönemi ekonomisini aynen devam ettirmeyi hedefler."
        },
        "dogru_cevap": "B",
        "aciklama": "Devletçilik ilkesinin temel vizyonu, özel sektörün sermaye bulamadığı alanlara bizzat devletin girerek üretimi tesis etmesi ve ekonomik bağımsızlığı perçinlemesidir."
    },
    {
        "unite": U4,
        "konu": "Ekonomi - Kabotaj Kanunu",
        "yil": 2020,
        "zorluk": "Orta",
        "soru": "1 Temmuz 1926’da çıkarılan Kabotaj Kanunu ile Türkiye limanları arasında yük ve yolcu taşıma hakkı, kılavuzluk hizmetleri gibi tüm denizcilik faaliyetleri yalnızca Türk vatandaşlarına ve Türk bayrağı taşıyan gemilere verilmiştir.\n\nBu kanun en başta Atatürk İlkeleri'nden hangisiyle doğrudan örtüşür?",
        "siklar": {
            "A": "Milliyetçilik",
            "B": "Cumhuriyetçilik",
            "C": "İnkılapçılık",
            "D": "Laiklik"
        },
        "dogru_cevap": "A",
        "aciklama": "Kapitülasyonların izlerini silen, Türk vatandaşlarına ayrıcalık verip kendi kaynaklarına (denizlerine) Türk insanını egemen kılan tüm uygulamalar Milliyetçilik doğasındadır."
    },

    # ---- ÜNİTE 5 ----
    {
        "unite": U5,
        "konu": "Çok Partili Hayata Geçiş Denemeleri",
        "yil": 2024,
        "zorluk": "Zor",
        "soru": "Cumhuriyetin ilk yıllarında Mustafa Kemal demokrasiyi tam anlamıyla işletmek için çok partili hayata geçmek istemiş, bu doğrultuda Terakkiperver Cumhuriyet Fırkası ve Serbest Cumhuriyet Fırkası kurulmuştur. Ancak her iki parti de rejime (Cumhuriyete ve yeniliklere) karşı olan kişilerin odak noktası haline geldiği ve isyanlar/olaylar (Şeyh Sait İsyanı, Menemen Olayı) çıkmasına zemin hazırladığı için kapatılmak zorunda kalmıştır.\n\nBu durum Türkiye Cumhuriyeti tarihi için aşağıdakilerden hangisinin göstergesidir?",
        "siklar": {
            "A": "Türk milletinin tek parti yönetim sistemini sonsuza kadar benimsediğinin",
            "B": "Devrimlerin henüz tam kökleşmediği bir dönemde çok partili yaşam denemelerinin başarısız olduğunun",
            "C": "Dış politikanın şekillenmesinde iç siyasetin hiçbir etkisinin kalmadığının",
            "D": "Mustafa Kemal'in tüm muhalefet partilerini planlı bir şekilde bilerek kapattığının"
        },
        "dogru_cevap": "B",
        "aciklama": "Partilerin kapatılma gerekçesi, inkılapların halk nezdinde tam yerleşmemesi ve demokrasi kültürünün henüz oturmaması sebebiyle Cumhuriyet karşıtlarının sığınabilecekleri bir siyasi platform bulmalarıdır."
    },
    {
        "unite": U5,
        "konu": "Şeyh Sait İsyanı",
        "yil": 2023,
        "zorluk": "Orta",
        "soru": "Şeyh Sait İsyanı (1925), Cumhuriyetin ilk yıllarında rejimi, laik sistemi ortadan kaldırmayı ve halifeliği geri getirmeyi amaçlayan geniş çaplı bir isyandı. Devlet bu isyanı bastırmak için Takrir-i Sükun Kanunu'nu çıkardı, İstiklal Mahkemelerini yeniden kurdu ve Terakkiperver Cumhuriyet Fırkası'nı kapattı.\n\nVerilen bilgilere göre Şeyh Sait İsyanı ile ilgili olarak;\nI. Sadece bölgesel eşitsizliklere tepki olarak çıkmıştır.\nII. Genç Cumhuriyetin varlığına yönelik ciddi bir tehdittir.\nIII. Demokratikleşme (çok partili hayat) sürecini olumsuz etkileyip sekteye uğratmıştır.\nyargılarından hangilerine ulaşılabilir?",
        "siklar": {
            "A": "Yalnız I",
            "B": "I ve II",
            "C": "II ve III",
            "D": "I, II ve III"
        },
        "dogru_cevap": "C",
        "aciklama": "İsyan sadece eşitsizlik için değil, halifeliği ve eski düzeni getirmek (rejimi devirmek) için çıkmıştır. Bu durum demokrasiye geçişi engellemiş ve partilerin kapanmasına yol açmıştır."
    },
    {
        "unite": U5,
        "konu": "Mustafa Kemal'e Suikast Girişimi",
        "yil": 2022,
        "zorluk": "Kolay",
        "soru": "1926 yılında gerçekleştirilmek istenen İzmir Suikastı planı, Giritli Şevki adlı kişinin durumu valiye bildirmesiyle son anda önlendi. Bu gelişme üzerine Mustafa Kemal Paşa Anadolu Ajansına şu meşhur tarihi demecini vermiştir: “Benim naçiz (değersiz) vücudum elbet bir gün toprak olacaktır; ancak Türkiye Cumhuriyeti ilelebet payidar kalacaktır.”\n\nMustafa Kemal'in bu sözüyle asıl vurgulamak istediği nedir?",
        "siklar": {
            "A": "Kendisine yönelik saldırıların daha da artmasını beklediği",
            "B": "Kurulan genç cumhuriyet sisteminin baki olduğu, kişilerin hayatlarından bağımsız olarak yaşamaya devam edeceği",
            "C": "Cumhuriyet rejimini bizzat sadece kendisinin yönetebileceği",
            "D": "Suikast planlayıcılarının hiçbir ceza almadan bırakılması gerektiği"
        },
        "dogru_cevap": "B",
        "aciklama": "Kendisinin ölümlü bir varlık olduğunu, ancak kurulan Cumhuriyetin kurumsallaştığını ve sonsuza dek korunacağını tarihi ve asil bir dille anlatmıştır."
    },
    {
        "unite": U5,
        "konu": "Kubilay (Menemen) Olayı",
        "yil": 2021,
        "zorluk": "Orta",
        "soru": "1930 yılında Menemen'de yaşanan olayda, kendini mehdî ilan eden Derviş Mehmet ve adamları halkı isyana teşvik etmiş; onlara engel olmaya çalışan ve asteğmen olarak askerliğini yapan öğretmen Kubilay bu yobaz isyancılar tarafından şehit edilmiştir. Toplanan askeri birlikler isyanı bastırmış, isyancılar yargılanarak cezalandırılmıştır.\n\nMenemen Olayına bakılarak aşağıda verilen çıkarımlardan hangisine varılabilir?",
        "siklar": {
            "A": "Ülkede dış baskıların giderek arttığına",
            "B": "Halkın tüm kesiminin laik sisteme tamamen alışmış ve uyum sağlamış olduğuna",
            "C": "Yeniliklere ve devrimlere (rejime) karşı gerici bir grubun varlığını sürdürdüğüne",
            "D": "Cumhuriyetin çok partili hayata başarılı bir adım attığına"
        },
        "dogru_cevap": "C",
        "aciklama": "Dini kullanarak isyan başlatmak ve öğretmeni katletmek, toplumda henüz laik inkılapları benimsememiş, irticai (gerici) karanlık odakların varlığını kanıtlar niteliktedir."
    },
    {
        "unite": U5,
        "konu": "Demokrasi ve Sorumluluk",
        "yil": 2020,
        "zorluk": "Zor",
        "soru": "Mustafa Kemal, Fethi Okyar'dan Serbest Cumhuriyet Fırkası'nı kurmasını isterken şu sözleri söylemiştir: “Bugünkü durumda Meclis’te bir fırka var. Biz de meclisi tek fikre mahkûm etmiş oluyoruz. Halbuki cumhuriyet esasına dayanan bir memlekette, memleket meselelerinin mecliste açıkça münakaşa edilmesi (tartışılması) lâzımdır.\"\n\nAtatürk'ün bu sözleriyle aşağıdakilerden hangisine vurgu yaptığı söylenemez?",
        "siklar": {
            "A": "Hükümetin farklı politikalar üzerinden eleştirilip denetlenmesi gerektiğine",
            "B": "Farklı görüş ve düşüncelerin meclis çatısı altında sesi olması gerektiğine",
            "C": "Tek parti yönetiminin dış politikada savaş kararı alma ihtimalinin yüksekliğine",
            "D": "Milli iradenin Meclis’te çok daha demokratik şartlarda tecelli etmesinin önemine"
        },
        "dogru_cevap": "C",
        "aciklama": "Mustafa Kemal'in sitemi mecliste serbestçe fikir tartışması yapılabilmesi içindir (denetlenme, fikir özgürlüğü vb.); dış politika ya da savaş kararı vermekle ilgisi yoktur."
    },

    # ---- ÜNİTE 6 ----
    {
        "unite": U6,
        "konu": "Atatürk Dönemi Türk Dış Politikası (Genel Vizyon)",
        "yil": 2024,
        "zorluk": "Orta",
        "soru": "Atatürk dönemi Türk dış politikasının dayandığı en önemli vizyon, 'Yurtta Sulh, Cihanda Sulh' sözüyle formüle edilmiştir. Aynı dönemde Türkiye, eski düşmanlarıyla diplomatik ve ticari bağlar kurmuş; Milletler Cemiyetine girmiş, Sadabat ve Balkan paktlarını onaylamıştır.\n\nYukarıdaki paragraftan yola çıkarak Atatürk dönemi dış politikası hakkında aşağıdakilerden hangisi söylenebilir?",
        "siklar": {
            "A": "Tarihi düşmanlıklara dayalı, rövanşist ve kapalı bir politika izlenmiştir.",
            "B": "Diğer devletlerin iç işlerine müdahale eden bir blok politikası benimsenmiştir.",
            "C": "Revizyonist (sürekli sınır değiştirmeyi arzulayan) yayılmacı bir nitelik taşımaktadır.",
            "D": "Bölgesel ve küresel güvenliği önceleyen barışçıl ve işbirliği odaklı bir çizgi yürütmüştür."
        },
        "dogru_cevap": "D",
        "aciklama": "Balkan Antantı, Sadabat Paktı ve Milletler Cemiyetine üyelik, saldırgan (revizyonist) politikalara karşı barışı ve güvenliği sağlamak amacını (Yurtta sulh, cihanda sulh) taşır."
    },
    {
        "unite": U6,
        "konu": "Nüfus Mübadelesi",
        "yil": 2023,
        "zorluk": "Orta",
        "soru": "Lozan Barış Antlaşması’na göre, Türkiye'deki Rumlarla Yunanistan'daki Türklerin değişimi (mübadele) kararlaştırılmıştı. Ancak İstanbul'daki Rumların ve Batı Trakya'daki Türklerin yerlerinde (etabli/yerleşik) kalması hükme bağlanmıştı. Yunanistan diplomatik oyunlarla İstanbul'da olabildiğince çok sayıda Rum tutmak isteyince iki ülke arasında 'Etabli (Yerleşik)' krizi yaşanmıştır. Konu önce Milletler Cemiyeti’ne taşınmış, sonuç çıkmayınca 1930'da Ankara antlaşması ile uzlaşma sağlanmıştır.\n\nBu krizin Türkiye tarafından barış ve hukuk yoluyla (savaşmadan) çözümlenmesi Türk dış politikasının hangi yönünü gösterir?",
        "siklar": {
            "A": "Dışarıdan gelen her talebi kolayca kabul eden teslimiyetçi bir diplomasiyi",
            "B": "Milli çıkarları Milletler Cemiyeti ilkeleri ve müzakerelerle (diplomasiyle) arayan bir tutumu",
            "C": "Lozan Anlaşması metnini baştan aşağı değiştirme arzusunu",
            "D": "Azınlıkların sorunlarıyla ilgilenmeyen, umursamaz bir yaklaşımı"
        },
        "dogru_cevap": "B",
        "aciklama": "Yunanistan'ın oyunlarına karşı derhal silahlı mücadeleye ya da tavize yönelmemiş; konuyu hukuki ve diplomatik bir çerçevede (müzakerelerle) uluslararası hukuka uygun şekilde çözmüştür."
    },
    {
        "unite": U6,
        "konu": "Montrö Boğazlar Sözleşmesi",
        "yil": 2022,
        "zorluk": "Zor",
        "soru": "Montrö Boğazlar Sözleşmesi (1936) ile; Lozan Anlaşması'nda belirlenen uluslararası boğazlar komisyonu tamamen kaldırılmış, boğazlar her iki yakasından da Türk askeri birimleri tarafından savunulacak statüye geçmiş ve silahsızlandırma iptal edilmiştir.\n\nBuna göre Montrö Sözleşmesi için aşağıdaki yargılardan hangisine ulaşılabilir?",
        "siklar": {
            "A": "Türkiye egemenlik haklarını kısıtlayan en büyük engellerden birini aşmış ve toprak bütünlüğünü güvenceye almıştır.",
            "B": "Türkiye, Montrö sonrası boğazları tüm dünya ticaret gemilerine süresiz olarak kapatmıştır.",
            "C": "Montrö Sözleşmesi sadece İngiltere ile Türkiye arasında yapılan ikili bir yardımlaşma antlaşmasıdır.",
            "D": "Sovyet Rusya'nın Karadeniz’deki güvenliği risk altına girmiştir."
        },
        "dogru_cevap": "A",
        "aciklama": "Komisyonun kaldırılması ve Türk askerinin boğazlara yerleşmesi, Lozan'da zedelenen (kısıtlanan) egemenliğimizin yeniden kazanıldığını net şekilde kanıtlar."
    },
    {
        "unite": U6,
        "konu": "Hatay Meselesi",
        "yil": 2021,
        "zorluk": "Zor",
        "soru": "Atatürk, hastalığının oldukça ilerlediği dönemde bile Hatay davasından vazgeçmemiş, 'Kırk asırlık Türk yurdu düşman elinde esir kalamaz' ve 'Hatay benim şahsi meselemdir' diyerek Mersin ve Adana seyahatlerine katılıp uzun askeri geçit törenlerini ayakta izlemiştir. Atatürk bu zorlu tavrıyla Fransa'ya karşı hem devletinin hem de ordusunun kararlı duruşunu sergilemiştir.\n\nMetne göre Atatürk'ün bu davranışını değerlendirirseniz, onda en çok hangi özelliğin belirgin olduğunu söyleyebilirsiniz?",
        "siklar": {
            "A": "Merhametli oluşu ve bağışlayıcılığı",
            "B": "Ümitsizliğe yer vermeyen kararlı (idealist) bir devlet adamı olması ve vatan sevgisi",
            "C": "Eğitime ve gençlerin bilgi birikimine değer vermesi",
            "D": "Ordunun teknolojik gücünü Avrupalı ülkelere kanıtlama hırsı"
        },
        "dogru_cevap": "B",
        "aciklama": "Metindeki 'hastalığına rağmen', 'benim şahsi meselemdir' ifadeleri onun hedefine kilitlenmiş tavizsiz idealizmini, vatanı için hayatını hiçe saymasını gösteren vatanseverliğidir."
    },
    {
        "unite": U6,
        "konu": "Balkan ve Sadabat Paktları",
        "yil": 2020,
        "zorluk": "Orta",
        "soru": "1930'lu yılların sonuna doğru İtalya'nın ve Almanya'nın yayılmacı, saldırgan ve aşırı ırkçı tutumları Ortadoğu, Akdeniz ve balkanlarda güvenliği tehdit etmeye başlamıştır. Bu duruma karşı Türkiye, batı sınırını güvence altına almak için Balkan Antantı (1934); doğu sınırı içinse (İtalya'nın ortadoğu iştahına karşı) Sadabat Paktı'nı (1937) imzalamıştır.\n\nVerilen bu dış politika hamleleri bir bütün olarak incelendiğinde aşağıdaki kavramlardan hangisiyle açıklanabilir?",
        "siklar": {
            "A": "Kolektif Güvenlik Arayışı ve Bölgesel İttifak",
            "B": "Yayılmacılık (Emperyalizm) ve Askeri Taarruz",
            "C": "Tam Tarafsızlık ve İçine Kapanık Siyaset (İzolasyon)",
            "D": "Manda ve Himaye Politikası"
        },
        "dogru_cevap": "A",
        "aciklama": "Saldırgan devletlerin tehdidine karşı çevresindeki devletlerle ittifak yapıp karşılıklı güvenliği sağlamak (güç birliği) 'Kolektif Güvenlik (Ortak Güvenlik)' kavramı ile izah edilir. Yeni nesil LGS bu tür kavram eşleşmelerini çok sever."
    }
]

file_path = "c:\\Users\\M.ATA\\Documents\\GitHub\\inkilap-cark-oyunu\\sorular.json"
try:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)
        print("Tebrikler! LGS 'Yeni Nesil' soruları başarıyla sorular.json dosyasına entegre edildi.")
except Exception as e:
    print(f"Hata oluştu: {e}")
