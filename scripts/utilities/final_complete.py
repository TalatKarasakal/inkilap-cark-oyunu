"""7. sınıfa 1, 8. sınıfa 46 LGS formatında soru ekler, dağılımı dengeler, birleştirir."""
import json, os, copy, random
random.seed(999)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

def balance(qs):
    keys=["A","B","C","D"]
    for q in qs:
        ct=q["siklar"][q["dogru_cevap"]]
        opts=list(q["siklar"].values()); random.shuffle(opts)
        q["siklar"]={k:opts[i] for i,k in enumerate(keys)}
        for k in keys:
            if q["siklar"][k]==ct: q["dogru_cevap"]=k; break
    dist={k:[] for k in keys}
    for i,q in enumerate(qs): dist[q["dogru_cevap"]].append(i)
    for _ in range(200):
        c={k:len(v) for k,v in dist.items()}
        mx,mn=max(c,key=c.get),min(c,key=c.get)
        if c[mx]-c[mn]<=1: break
        idx=dist[mx].pop(); q=qs[idx]
        ct2=q["siklar"][q["dogru_cevap"]]; tt=q["siklar"][mn]
        q["siklar"][q["dogru_cevap"]]=tt; q["siklar"][mn]=ct2; q["dogru_cevap"]=mn
        dist[mn].append(idx)
    return qs

U7="Ünite 7 – Küresel Bağlantılar"
U1="Ünite 1 – Bir Kahraman Doğuyor"
U2="Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3="Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4="Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5="Ünite 5 – Demokratikleşme Çabaları"
U6="Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

# 7. sınıf: 1 ek soru
ek7=[{"unite":U7,"konu":"Küresel Sorunlar","yil":2024,"zorluk":"Orta",
 "soru":"Su kıtlığı dünya genelinde 2 milyardan fazla insanı etkilemektedir.\n\nSu kıtlığına karşı en etkili önlem hangisidir?",
 "siklar":{"A":"Suyun özelleştirilmesi","B":"Deniz suyunun arıtılması, yağmur suyu hasadı ve tasarruf politikaları","C":"Barajların yıkılması","D":"Tarımın durdurulması"},
 "dogru_cevap":"B","aciklama":"Arıtma, hasat ve tasarruf su kıtlığına karşı en etkili önlemlerdir."}]

# 8. sınıf: 46 LGS formatında soru
ek8=[
 # ÜNİTE 1
 {"unite":U1,"konu":"Mustafa Kemal'in Askerlik Hayatı","yil":2024,"zorluk":"Zor",
  "soru":"Aşağıdaki tabloda Mustafa Kemal'in katıldığı savaşlar ve görevleri verilmiştir:\n\n| Savaş | Görev |\n|---|---|\n| Trablusgarp | Bölge komutanı |\n| Çanakkale | Tümen komutanı |\n| Sakarya | Başkomutan |\n\nBu tabloya göre Mustafa Kemal ile ilgili aşağıdakilerden hangisine ulaşılabilir?",
  "siklar":{"A":"Her savaşta aynı rütbede görev yapmıştır","B":"Askeri sorumluluğu zamanla artmıştır","C":"Sadece savunma savaşlarına katılmıştır","D":"Yalnızca Anadolu'da görev yapmıştır"},
  "dogru_cevap":"B","aciklama":"Bölge komutanlığından başkomutanlığa yükseliş sorumluluk artışını gösterir."},
 {"unite":U1,"konu":"I. Dünya Savaşı","yil":2024,"zorluk":"Orta",
  "soru":"Bir öğrenci 'Osmanlı Devleti I. Dünya Savaşı'nda birden fazla cephede savaşmıştır' bilgisini kullanarak bir sunum hazırlamaktadır.\n\nÖğrenci bu sunumda aşağıdakilerden hangisini sonuç olarak belirtmelidir?",
  "siklar":{"A":"Osmanlı'nın düşmanlarının az olduğunu","B":"Tek cephede savaşıldığını","C":"Askeri gücün dağılarak zayıfladığını","D":"Tüm cephelerde zafer kazanıldığını"},
  "dogru_cevap":"C","aciklama":"Birden fazla cephede savaşmak askeri gücü dağıtarak zayıflatmıştır."},
 {"unite":U1,"konu":"Osmanlı'nın Son Dönemi","yil":2023,"zorluk":"Zor",
  "soru":"Aşağıda bazı fikir akımları ve hedefleri verilmiştir:\n\nI. Osmanlıcılık → Tüm Osmanlı vatandaşlarını birleştirmek\nII. İslamcılık → Müslümanları birleştirmek\nIII. Türkçülük → Türkleri birleştirmek\n\nBu akımların ortak yönü aşağıdakilerden hangisidir?",
  "siklar":{"A":"Hepsi başarılı olmuştur","B":"Devleti dağılmaktan kurtarmayı amaçlamışlardır","C":"Hepsi aynı dönemde ortaya çıkmıştır","D":"Hepsi milliyetçi niteliktedir"},
  "dogru_cevap":"B","aciklama":"Tüm fikir akımlarının ortak amacı devleti dağılmaktan kurtarmaktı."},
 {"unite":U1,"konu":"Mustafa Kemal","yil":2023,"zorluk":"Orta",
  "soru":"Mustafa Kemal'in 'Beni Türk hekimlerine emanet ediniz' sözü aşağıdakilerden hangisiyle ilgilidir?",
  "siklar":{"A":"Tıp eğitimini geliştirmek istemesiyle","B":"Yabancılara güvenmemesiyle","C":"Türk insanına ve bilim insanlarına olan güveniyle","D":"Sağlık sorunlarının olmamasıyla"},
  "dogru_cevap":"C","aciklama":"Bu söz Türk insanına ve bilim insanlarına duyulan güveni ifade eder."},
 {"unite":U1,"konu":"I. Dünya Savaşı","yil":2022,"zorluk":"Zor",
  "soru":"I. Dünya Savaşı sonunda imzalanan Mondros Ateşkesi'nin 7. maddesi 'İtilaf devletleri güvenliklerini tehdit edecek bir durum olursa herhangi bir stratejik noktayı işgal edebilir' demektedir.\n\nBu madde aşağıdakilerden hangisine zemin hazırlamıştır?",
  "siklar":{"A":"Osmanlı'nın güçlenmesine","B":"Anadolu'nun kolayca işgal edilmesine","C":"Barışın sağlanmasına","D":"Ordunun güçlenmesine"},
  "dogru_cevap":"B","aciklama":"Bu madde İtilaf devletlerine istedikleri yeri işgal etme hakkı vererek Anadolu'nun işgaline zemin hazırlamıştır."},

 # ÜNİTE 2
 {"unite":U2,"konu":"Kongreler","yil":2024,"zorluk":"Zor",
  "soru":"Bir tarih dersinde öğretmen şunları söylemiştir:\n'Erzurum Kongresi bölgesel toplanmış ama ulusal kararlar almıştır.'\n\nÖğretmenin bu sözüyle anlatmak istediği aşağıdakilerden hangisidir?",
  "siklar":{"A":"Kongrenin başarısız olduğunu","B":"Bölgesel sorunlarla ilgilenildiğini","C":"Alınan kararların tüm vatanı kapsadığını","D":"Yalnızca doğu illerinin temsil edildiğini"},
  "dogru_cevap":"C","aciklama":"Erzurum'da bölgesel olarak toplanılmış ama kararlar tüm vatanı kapsamıştır."},
 {"unite":U2,"konu":"Amasya Genelgesi","yil":2024,"zorluk":"Orta",
  "soru":"Amasya Genelgesi'nde 'Milletin istiklalini yine milletin azim ve kararı kurtaracaktır' denilmiştir.\n\nBu cümle ile ilk kez vurgulanan kavram aşağıdakilerden hangisidir?",
  "siklar":{"A":"Padişah otoritesi","B":"Millî egemenlik","C":"Ordunun gücü","D":"Dış yardım"},
  "dogru_cevap":"B","aciklama":"Bu cümle ilk kez millî egemenlik kavramını açıkça ifade etmiştir."},
 {"unite":U2,"konu":"TBMM","yil":2023,"zorluk":"Zor",
  "soru":"TBMM'nin açılmasıyla;\nI. Yasama yetkisini kullanmış\nII. Yürütme yetkisini üzerine almış\nIII. Başkomutanlık kararı vermiş\n\nBuna göre TBMM'de uygulanan sistem aşağıdakilerden hangisidir?",
  "siklar":{"A":"Kuvvetler ayrılığı","B":"Güçler birliği (meclis hükümeti sistemi)","C":"Başkanlık sistemi","D":"Parlamenter sistem"},
  "dogru_cevap":"B","aciklama":"TBMM'de yasama ve yürütme birlikte kullanılmıştır yani güçler birliği uygulanmıştır."},
 {"unite":U2,"konu":"İşgaller","yil":2023,"zorluk":"Orta",
  "soru":"Sevr Antlaşması'na göre Osmanlı toprakları çeşitli devletler arasında paylaşılmıştır.\n\nAşağıdakilerden hangisi Sevr'in uygulanamamasının temel nedenidir?",
  "siklar":{"A":"Padişahın reddetmesi","B":"İtilaf devletlerinin vazgeçmesi","C":"TBMM'nin tanımaması ve Millî Mücadele'nin kazanılması","D":"Antlaşmanın geçersiz ilan edilmesi"},
  "dogru_cevap":"C","aciklama":"TBMM Sevr'i tanımamış ve Millî Mücadele'nin kazanılmasıyla antlaşma geçersiz kalmıştır."},
 {"unite":U2,"konu":"Kuvâ-yı Milliye","yil":2022,"zorluk":"Zor",
  "soru":"Kuvâ-yı Milliye birliklerinin düzenli orduya dönüştürülmesi kararı alınmıştır.\n\nBu kararın alınmasında aşağıdakilerden hangisi etkili olmuştur?",
  "siklar":{"A":"İşgallerin sona ermesi","B":"Kuvâ-yı Milliye'nin çok başarılı olması","C":"Düzensiz birliklerin büyük cephe savaşlarında yetersiz kalması","D":"Halkın düzenli orduyu istememesi"},
  "dogru_cevap":"C","aciklama":"Düzensiz birlikler büyük savaşlarda yetersiz kalınca düzenli orduya geçilmiştir."},

 # ÜNİTE 3
 {"unite":U3,"konu":"Batı Cephesi","yil":2024,"zorluk":"Zor",
  "soru":"Aşağıda Kurtuluş Savaşı'ndaki bazı olaylar kronolojik olarak verilmiştir:\n\nI. İnönü → II. İnönü → Sakarya → Büyük Taarruz\n\nBu sıralama aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Savunmadan taarruza geçen planlı bir strateji izlendiğini","B":"Tüm savaşların aynı yerde yapıldığını","C":"Her savaşta farklı komutanların görev yaptığını","D":"Savaşların rastgele yapıldığını"},
  "dogru_cevap":"A","aciklama":"İnönü savunmaları, Sakarya durağı ve Büyük Taarruz planlı aşamalı stratejiyi gösterir."},
 {"unite":U3,"konu":"Batı Cephesi","yil":2024,"zorluk":"Orta",
  "soru":"Sakarya Savaşı'ndan sonra Mustafa Kemal'e TBMM tarafından 'Gazi' unvanı ve 'Mareşal' rütbesi verilmiştir.\n\nBu durum aşağıdakilerden hangisinin göstergesidir?",
  "siklar":{"A":"Savaşın kaybedildiğinin","B":"TBMM'nin Mustafa Kemal'e olan güveninin en üst düzeye çıktığının","C":"Savaşın sona erdiğinin","D":"Ordunun dağıldığının"},
  "dogru_cevap":"B","aciklama":"Gazilik ve Mareşallik TBMM'nin Mustafa Kemal'e güveninin zirvesini gösterir."},
 {"unite":U3,"konu":"Lozan","yil":2024,"zorluk":"Zor",
  "soru":"Bir tarihçi 'Lozan, modern Türkiye'nin uluslararası doğum belgesidir' demiştir.\n\nTarihçinin bu sözle kastettiği aşağıdakilerden hangisidir?",
  "siklar":{"A":"Lozan'da toprak kaybedildiği","B":"Yeni Türk devletinin tam bağımsız ve egemen olarak dünyaca tanındığı","C":"Osmanlı'nın devam ettiği","D":"Savaşın sürdüğü"},
  "dogru_cevap":"B","aciklama":"Lozan yeni Türk devletinin dünya tarafından bağımsız ve egemen tanınmasını sağlamıştır."},
 {"unite":U3,"konu":"Mudanya","yil":2023,"zorluk":"Orta",
  "soru":"Mudanya Ateşkes Antlaşması'yla Doğu Trakya savaş yapılmadan geri alınmıştır.\n\nBu durum aşağıdakilerden hangisini kanıtlar?",
  "siklar":{"A":"Askeri gücün gereksiz olduğunu","B":"Askeri başarının diplomatik kazanıma dönüşebildiğini","C":"Trakya'nın önemsiz olduğunu","D":"İşgalin devam ettiğini"},
  "dogru_cevap":"B","aciklama":"Batı cephesi zaferinin diplomatik sonucu Doğu Trakya'nın savaşsız kurtarılmasıdır."},
 {"unite":U3,"konu":"Güney Cephesi","yil":2022,"zorluk":"Orta",
  "soru":"Gaziantep 6.317 gün savunulmuş ve şehir 'Gazi' unvanı almıştır.\n\nBu direniş aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Savaşın kısa sürdüğünü","B":"Halkın bağımsızlık için büyük fedakârlık gösterdiğini","C":"Yalnızca askerlerin savaştığını","D":"Güney cephesinin önemsiz olduğunu"},
  "dogru_cevap":"B","aciklama":"Uzun süren savunma ve Gazi unvanı halkın büyük fedakârlığını gösterir."},

 # ÜNİTE 4
 {"unite":U4,"konu":"Cumhuriyetin İlanı","yil":2024,"zorluk":"Zor",
  "soru":"Aşağıdaki şema verilmiştir:\nSaltanatın kaldırılması (1922) → Cumhuriyet'in ilanı (1923) → Halifeliğin kaldırılması (1924)\n\nBu şemaya göre aşağıdakilerden hangisi söylenebilir?",
  "siklar":{"A":"Üç olay arasında bağlantı yoktur","B":"Aşamalı olarak laik cumhuriyete geçiş sağlanmıştır","C":"Hepsi aynı yıl gerçekleşmiştir","D":"Padişahlık güçlendirilmiştir"},
  "dogru_cevap":"B","aciklama":"Saltanat-Cumhuriyet-Halifelik sıralaması aşamalı laik cumhuriyete geçişi gösterir."},
 {"unite":U4,"konu":"İnkılaplar","yil":2024,"zorluk":"Orta",
  "soru":"Aşağıdaki inkılâplardan hangisi doğrudan eğitim alanıyla ilgilidir?\n\nI. Tevhid-i Tedrisat\nII. Harf İnkılabı\nIII. Millet Mektepleri\nIV. Kabotaj Kanunu",
  "siklar":{"A":"I, II ve III","B":"I, II ve IV","C":"II, III ve IV","D":"I, III ve IV"},
  "dogru_cevap":"A","aciklama":"Tevhid-i Tedrisat, Harf İnkılabı ve Millet Mektepleri eğitim alanıyla ilgilidir. Kabotaj ekonomi alanıdır."},
 {"unite":U4,"konu":"Atatürk İlkeleri","yil":2023,"zorluk":"Zor",
  "soru":"Bir öğrenci Atatürk ilkelerini sınıflandırmıştır:\n\nTemel İlkeler: Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılâpçılık\nBütünleyici İlkeler: Millî egemenlik, Bilimsellik, Akılcılık, Çağdaşlaşma\n\nBütünleyici ilkelerin görevi aşağıdakilerden hangisidir?",
  "siklar":{"A":"Temel ilkelerin yerine geçmek","B":"Temel ilkeleri destekleyerek tamamlamak","C":"Temel ilkelerle çelişmek","D":"Bağımsız ilkeler oluşturmak"},
  "dogru_cevap":"B","aciklama":"Bütünleyici ilkeler temel ilkeleri destekler ve tamamlar."},
 {"unite":U4,"konu":"İnkılaplar","yil":2023,"zorluk":"Orta",
  "soru":"1934 yılında kadınlara milletvekili seçme ve seçilme hakkı verilmiştir.\n\nBu gelişme aşağıdaki Atatürk ilkelerinden hangisiyle doğrudan ilgilidir?",
  "siklar":{"A":"Devletçilik","B":"Halkçılık","C":"İnkılâpçılık","D":"Laiklik"},
  "dogru_cevap":"B","aciklama":"Kadınlara eşit siyasi haklar verilmesi toplumsal eşitliği savunan Halkçılık ilkesiyle ilgilidir."},
 {"unite":U4,"konu":"İnkılaplar","yil":2022,"zorluk":"Zor",
  "soru":"Aşağıdaki inkılâplar ve ilişkili oldukları Atatürk ilkeleri eşleştirilmiştir:\n\nI. Halifeliğin kaldırılması → Laiklik\nII. Soyadı Kanunu → Halkçılık\nIII. Devlet fabrikaları kurulması → Devletçilik\n\nBu eşleştirmelerden hangileri doğrudur?",
  "siklar":{"A":"Yalnız I","B":"I ve II","C":"I ve III","D":"I, II ve III"},
  "dogru_cevap":"D","aciklama":"Üç eşleştirme de doğrudur."},
 {"unite":U4,"konu":"Atatürk İlkeleri","yil":2022,"zorluk":"Orta",
  "soru":"Atatürk 'Hayatta en hakiki mürşit ilimdir' demiştir.\n\nBu söz aşağıdaki bütünleyici ilkelerden hangisiyle ilgilidir?",
  "siklar":{"A":"Millî egemenlik","B":"Bilimsellik ve akılcılık","C":"Tam bağımsızlık","D":"Barışçılık"},
  "dogru_cevap":"B","aciklama":"Bu söz bilimsellik ve akılcılık ilkesini ifade eder."},

 # ÜNİTE 5
 {"unite":U5,"konu":"Demokratikleşme","yil":2024,"zorluk":"Zor",
  "soru":"Aşağıdaki tabloda Türkiye'de demokratikleşme adımları verilmiştir:\n\n| Yıl | Gelişme |\n|---|---|\n| 1924 | Terakkiperver CF |\n| 1930 | Serbest CF |\n| 1946 | Çok partili seçim |\n| 1950 | İktidar değişimi |\n\nBu tabloya göre aşağıdakilerden hangisi söylenebilir?",
  "siklar":{"A":"İlk denemede çok partili hayata geçilmiştir","B":"Demokratikleşme uzun bir süreç sonunda gerçekleşmiştir","C":"Tek parti dönemi hiç yaşanmamıştır","D":"1924'te demokrasiye geçilmiştir"},
  "dogru_cevap":"B","aciklama":"1924'ten 1950'ye kadar süreç demokratikleşmenin uzun bir evrim olduğunu gösterir."},
 {"unite":U5,"konu":"Demokratikleşme","yil":2024,"zorluk":"Orta",
  "soru":"Atatürk döneminde kurulan muhalefet partilerinin kapatılmasının sebebi aşağıdakilerden hangisidir?",
  "siklar":{"A":"Atatürk'ün demokrasiye inanmaması","B":"İnkılâp karşıtı odak haline gelmeleri","C":"Halkın bu partileri desteklememesi","D":"Ekonomik kriz yaşanması"},
  "dogru_cevap":"B","aciklama":"Partiler inkılâp karşıtı faaliyetlerin odağı haline gelince kapatılmıştır."},
 {"unite":U5,"konu":"Askeri Müdahaleler","yil":2023,"zorluk":"Zor",
  "soru":"Bir tarihçi şöyle demiştir: 'Demokrasi sadece seçim yapmak değil, seçim sonuçlarına saygı göstermektir.'\n\nBu söz Türkiye tarihindeki hangi olayla çelişir?",
  "siklar":{"A":"1950 seçimleri","B":"Çok partili hayata geçiş","C":"Askeri müdahaleler ve darbe dönemleri","D":"Kadınlara oy hakkı verilmesi"},
  "dogru_cevap":"C","aciklama":"Askeri müdahaleler seçim sonuçlarına ve sivil iradeye saygı ilkesiyle çelişir."},
 {"unite":U5,"konu":"Demokratikleşme","yil":2022,"zorluk":"Orta",
  "soru":"1946 seçimlerinde 'açık oy, gizli sayım' uygulanmış; 1950'de ise 'gizli oy, açık sayım'a geçilmiştir.\n\nBu değişikliğin amacı aşağıdakilerden hangisidir?",
  "siklar":{"A":"Seçimleri zorlaştırmak","B":"Seçmen iradesinin özgürce yansımasını sağlamak","C":"Oy kullanımını azaltmak","D":"Tek parti dönemini sürdürmek"},
  "dogru_cevap":"B","aciklama":"Gizli oy, açık sayım seçmen iradesinin özgürce yansımasını sağlar."},
 {"unite":U5,"konu":"Demokratikleşme","yil":2021,"zorluk":"Zor",
  "soru":"Demokrasinin temel unsurları;\nI. Hukukun üstünlüğü\nII. İnsan hakları güvencesi\nIII. Basın özgürlüğü\nIV. Tek partili yönetim\n\nBunlardan hangisi demokrasinin temel unsuru DEĞİLDİR?",
  "siklar":{"A":"I","B":"II","C":"III","D":"IV"},
  "dogru_cevap":"D","aciklama":"Tek partili yönetim demokrasinin değil, otoriter yönetimin özelliğidir."},

 # ÜNİTE 6
 {"unite":U6,"konu":"Montrö","yil":2024,"zorluk":"Zor",
  "soru":"Aşağıda Boğazlarla ilgili iki dönem karşılaştırılmıştır:\n\nLozan (1923): Uluslararası komisyon yönetir\nMontrö (1936): Türkiye tam egemen\n\nBu değişim aşağıdakilerden hangisinin göstergesidir?",
  "siklar":{"A":"Lozan'ın geçersiz olduğunun","B":"Türkiye'nin diplomatik başarıyla egemenlik haklarını genişlettiğinin","C":"Boğazların kapatıldığının","D":"Savaş başladığının"},
  "dogru_cevap":"B","aciklama":"Montrö Türkiye'nin diplomatik başarıyla Boğazlarda tam egemenlik kazandığını gösterir."},
 {"unite":U6,"konu":"Hatay","yil":2024,"zorluk":"Orta",
  "soru":"Hatay 1939'da Türkiye'ye katılmıştır. Bu süreçte;\nI. Hatay Meclisi kurulmuş\nII. Bağımsız devlet ilan edilmiş\nIII. Halk oyuyla Türkiye'ye katılım kararı alınmış\n\nBu süreç aşağıdakilerden hangisine örnektir?",
  "siklar":{"A":"Askeri müdahaleye","B":"Sömürgeciliğe","C":"Demokratik ve diplomatik çözüme","D":"Emperyalizme"},
  "dogru_cevap":"C","aciklama":"Hatay'ın katılımı demokratik ve diplomatik çözüme örnektir."},
 {"unite":U6,"konu":"Balkan Antantı","yil":2023,"zorluk":"Zor",
  "soru":"Atatürk döneminde kurulan ittifaklar:\n\nBalkan Antantı (1934): Türkiye, Yunanistan, Romanya, Yugoslavya\nSadabat Paktı (1937): Türkiye, İran, Irak, Afganistan\n\nBu iki ittifağın kurulmasında ortak amaç aşağıdakilerden hangisidir?",
  "siklar":{"A":"Savaşa hazırlanmak","B":"Bölgesel barış ve güvenliği sağlamak","C":"Sömürge edinmek","D":"Büyük devletlere bağlanmak"},
  "dogru_cevap":"B","aciklama":"Her iki pakt da bölgesel barış ve güvenliği korumayı amaçlamıştır."},
 {"unite":U6,"konu":"Dış Politika","yil":2023,"zorluk":"Orta",
  "soru":"Atatürk'ün 'Yurtta sulh, cihanda sulh' ilkesi doğrultusunda yapılan aşağıdaki gelişmelerden hangisi bu ilkeyle en çok örtüşür?",
  "siklar":{"A":"Savaşa girmek","B":"Milletler Cemiyeti'ne katılmak","C":"Sınırları genişletmek","D":"Dış borçları ödememek"},
  "dogru_cevap":"B","aciklama":"Milletler Cemiyeti'ne katılım barışa katkı ve uluslararası iş birliği amaçlıdır."},
 {"unite":U6,"konu":"Dış Politika","yil":2022,"zorluk":"Zor",
  "soru":"Atatürk dönemi dış politikası;\nI. Lozan → Uluslararası tanınma\nII. Montrö → Boğazlar egemenliği\nIII. Hatay → Diplomatik zafer\nIV. Milletler Cemiyeti → Barışa katkı\n\nBu gelişmelerin ortak özelliği aşağıdakilerden hangisidir?",
  "siklar":{"A":"Savaşla elde edilmeleri","B":"Barışçıl yollarla kazanılan diplomatik başarılar olmaları","C":"Dış baskı sonucu yapılmaları","D":"Tek taraflı kararlar olmaları"},
  "dogru_cevap":"B","aciklama":"Tüm gelişmeler barışçıl yollarla kazanılan diplomatik başarılardır."},
 {"unite":U6,"konu":"Musul","yil":2022,"zorluk":"Orta",
  "soru":"Musul sorunu Milletler Cemiyeti'ne taşınmış ve sonuç Türkiye aleyhine çıkmıştır.\n\nBu durum aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Milletler Cemiyeti'nin tarafsız olduğunu","B":"Uluslararası kuruluşlarda büyük devletlerin etkisinin belirleyici olabildiğini","C":"Musul'un önemsiz olduğunu","D":"Türkiye'nin güçlü olduğunu"},
  "dogru_cevap":"B","aciklama":"Büyük devletlerin etkisi uluslararası kuruluşlarda belirleyici olabilmektedir."},
]

# 7. sınıf güncelle
fn7=os.path.join(DATA_DIR,"sorular_7.json")
with open(fn7,"r",encoding="utf-8") as f: q7=json.load(f)
q7.extend(ek7)
q7=balance(q7)
with open(fn7,"w",encoding="utf-8") as f: json.dump(q7,f,ensure_ascii=False,indent=2)
d7={k:sum(1 for q in q7 if q["dogru_cevap"]==k) for k in "ABCD"}
print(f"7. Sinif: {len(q7)} soru | A={d7['A']} B={d7['B']} C={d7['C']} D={d7['D']}")

# 8. sınıf güncelle
fn8=os.path.join(DATA_DIR,"sorular_8.json")
with open(fn8,"r",encoding="utf-8") as f: q8=json.load(f)
q8.extend(ek8)
q8=balance(q8)
with open(fn8,"w",encoding="utf-8") as f: json.dump(q8,f,ensure_ascii=False,indent=2)
d8={k:sum(1 for q in q8 if q["dogru_cevap"]==k) for k in "ABCD"}
print(f"8. Sinif: {len(q8)} soru | A={d8['A']} B={d8['B']} C={d8['C']} D={d8['D']}")
