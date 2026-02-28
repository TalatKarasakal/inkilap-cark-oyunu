#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soru havuzu genişletici - Batch 2 (soru 101-200)"""
import json
Q=[]
def q(u,k,y,z,s,a,b,c,d,x,ac=""):
    Q.append({"id":len(Q)+1,"unite":u,"konu":k,"yil":y,"zorluk":z,"soru":s,"siklar":{"A":a,"B":b,"C":c,"D":d},"dogru_cevap":x,"aciklama":ac})
U1="Ünite 1 – Bir Kahraman Doğuyor"
U2="Ünite 2 – Millî Uyanış"
U3="Ünite 3 – Ya İstiklal Ya Ölüm"
U4="Ünite 4 – Çağdaş Türkiye Yolunda Adımlar"
U5="Ünite 5 – Atatürkçülük"
U6="Ünite 6 – Demokratikleşme Çabaları"
U7="Ünite 7 – Atatürk Dönemi Türk Dış Politikası"
# U1 ek
q(U1,"Mustafa Kemal'in Doğduğu Yer",2018,"Kolay","Mustafa Kemal hangi şehirde doğmuştur?","İstanbul","Ankara","Selanik","Manastır","C","Mustafa Kemal 1881'de Selanik'te doğmuştur.")
q(U1,"31 Mart Olayı",2020,"Zor","31 Mart Olayı'nın bastırılmasında görev alan ordu hangisidir?","Yıldırım Ordusu","Hareket Ordusu","9. Ordu","Kuva-yı Milliye","B","31 Mart İsyanı, Hareket Ordusu tarafından bastırılmıştır. Mustafa Kemal bu ordunun kurmay başkanıdır.")
q(U1,"Balkan Savaşları",2021,"Orta","Balkan Savaşları sonucunda Osmanlı Devleti'nin kaybettiği en önemli toprak hangisidir?","Kıbrıs","Selanik dahil Rumeli'nin büyük bölümü","Suriye","Mısır","B")
q(U1,"Mustafa Kemal'in Etkilendiği Düşünürler",2023,"Zor","Mustafa Kemal'in fikrî gelişiminde etkili olan Fransız düşünür kimdir?","Marks","Rousseau","Hegel","Darwin","B","Rousseau'nun toplum sözleşmesi ve millî egemenlik düşünceleri Mustafa Kemal'i etkilemiştir.")
q(U1,"Harp Akademisi",2019,"Kolay","Mustafa Kemal Harp Akademisi'ni hangi rütbeyle bitirmiştir?","Yüzbaşı","Kurmay Yüzbaşı","Binbaşı","Albay","B")
# U2 ek
q(U2,"Mondros Maddeleri",2022,"Zor","Mondros'un hangi maddesi Osmanlı ordusunun silahsızlandırılmasını öngörmüştür?","1. madde","5. madde","7. madde","24. madde","B","Mondros'un 5. maddesi ordu terhisini ve silahların teslimatını öngörmüştür.")
q(U2,"İtilaf-İttifak Blokları",2017,"Kolay","I. Dünya Savaşı'nda İtilaf Devletleri arasında hangisi yer almaz?","İngiltere","Fransa","Almanya","Rusya","C")
q(U2,"Cemiyetler Arası Birlik",2019,"Orta","Sivas Kongresi'nde tüm yararlı cemiyetlerin birleştirildiği üst kuruluşun adı nedir?","Kuva-yı Milliye","Anadolu ve Rumeli Müdafaa-i Hukuk Cemiyeti","Temsil Heyeti","Heyet-i Temsiliye","B")
q(U2,"Temsil Heyeti",2023,"Orta","Temsil Heyeti'nin yürütme yetkisini kullanmaya başlaması hangi olayla gerçekleşmiştir?","Erzurum Kongresi","Sivas Kongresi","Amasya Görüşmeleri","TBMM'nin açılması","C","Amasya Görüşmeleri'nde İstanbul Hükûmeti Temsil Heyeti'ni resmen muhatap almıştır.")
q(U2,"I. Dünya Savaşı Sonuçları",2016,"Kolay","I. Dünya Savaşı'nı kazanan taraf hangisidir?","İttifak Devletleri","İtilaf Devletleri","Osmanlı Devleti","Avusturya-Macaristan","B")
q(U2,"Kanal Cephesi",2020,"Orta","Kanal Cephesi hangi amaçla açılmıştır?","Savunma","İngiltere'nin Mısır ile bağlantısını kesmek","Rusya'yı durdurmak","Fransa'yı yenmek","B")
q(U2,"Çanakkale Savaşı Sonuçları",2024,"Zor","Çanakkale Savaşı'nın kazanılmasının en önemli uluslararası sonucu nedir?","Osmanlı sınırları genişledi","Rusya'ya yardım ulaşamadı ve Rusya'da ihtilal süreci hızlandı","İngiltere savaştan çekildi","ABD savaşa girdi","B")
q(U2,"Mustafa Kemal'in Görevden Alınması",2021,"Orta","Mustafa Kemal, Samsun'a çıktıktan sonra İstanbul Hükûmeti tarafından görevden alınmıştır. Buna karşılık ne yapmıştır?","İstanbul'a dönmüştür","Askerlik mesleğinden istifa ederek mücadeleye sivil olarak devam etmiştir","Başka bir göreve atanmıştır","Yurt dışına çıkmıştır","B")
q(U2,"Batı Anadolu İşgalleri",2015,"Kolay","İzmir hangi devlet tarafından işgal edilmiştir?","İngiltere","Fransa","İtalya","Yunanistan","D")
# U3 ek
q(U3,"Hıyanet-i Vataniye Kanunu",2018,"Orta","TBMM'nin çıkardığı Hıyanet-i Vataniye Kanunu'nun amacı nedir?","Vergi toplamak","TBMM'ye karşı yapılan ayaklanmaları bastırmak","Dış politika yürütmek","Eğitimi düzenlemek","B")
q(U3,"İstiklal Mahkemeleri",2022,"Zor","İstiklal Mahkemeleri'nin kurulma amacı nedir?","Ekonomik suçları yargılamak","İç ayaklanmaları bastırmak ve asker kaçaklarını cezalandırmak","Dış politika düzenlemek","Eğitim sorunlarını çözmek","B")
q(U3,"Kars Antlaşması",2020,"Orta","Kars Antlaşması hangi devletlerle imzalanmıştır?","İngiltere ve Fransa","Gürcistan, Ermenistan ve Azerbaycan","İtalya ve Yunanistan","Rusya ve İran","B","1921 Kars Antlaşması ile Güney Kafkasya devletleri TBMM'yi ve sınırları tanımıştır.")
q(U3,"Batı Cephesi Komutanı",2017,"Kolay","Batı Cephesi Komutanlığı'na atanan kişi kimdir?","Mustafa Kemal","İsmet Paşa","Kâzım Karabekir","Ali Fuat Paşa","B")
q(U3,"Doğu Cephesi Komutanı",2019,"Kolay","Doğu Cephesi Komutanı kimdir?","İsmet Paşa","Kâzım Karabekir","Refet Bele","Ali Fuat Cebesoy","B")
q(U3,"Sakarya'dan Büyük Taarruz'a",2021,"Orta","Sakarya Zaferi'nden Büyük Taarruz'a kadar geçen sürede ordunun yaptığı temel hazırlık nedir?","Barış görüşmeleri","Ordunun güçlendirilmesi ve lojistik hazırlık","Yeni anayasa yapımı","Saltanatın kaldırılması","B")
q(U3,"30 Ağustos",2024,"Kolay","30 Ağustos Zafer Bayramı hangi muharebeden sonra kutlanmaktadır?","I. İnönü","Sakarya","Başkomutanlık Meydan Muharebesi","Çanakkale","C")
q(U3,"9 Eylül",2023,"Kolay","Türk ordusunun İzmir'e girdiği tarih hangisidir?","26 Ağustos 1922","30 Ağustos 1922","9 Eylül 1922","11 Ekim 1922","C")
q(U3,"TBMM Hükûmetleri",2016,"Orta","TBMM'nin ilk hükûmet başkanı kimdir?","İsmet Paşa","Fevzi Çakmak","Mustafa Kemal","Rauf Orbay","C","TBMM'nin başkanı aynı zamanda hükûmetin de başkanıydı; Mustafa Kemal bu görevi üstlenmiştir.")
q(U3,"Yunan Mezalimi",2020,"Zor","Yunanlıların Anadolu'daki sivil halka yönelik zulümleri uluslararası alanda hangi gelişmeye yol açmıştır?","Görmezden gelinmiştir","Bazı İtilaf devletlerinin Yunanistan'a desteğini sorgulamasına","Yunanistan'ın savaştan çekilmesine","Türkiye'nin Milletler Cemiyeti'ne alınmasına","B")
q(U3,"Lozan'da Sınırlar",2022,"Orta","Lozan'da çözülemeyen sınır sorunu hangisidir?","Suriye sınırı","Irak (Musul) sınırı","Yunanistan sınırı","Bulgaristan sınırı","B","Musul meselesi Lozan'da çözülememiş ve İngiltere ile ikili görüşmelere bırakılmıştır.")
q(U3,"Misak-ı Millî ve Lozan",2015,"Zor","Lozan Antlaşması'nda Misak-ı Millî'den vazgeçilen konu hangisidir?","Kapitülasyonlar","Batı Trakya","Boğazlar","Azınlık hakları","B","Batı Trakya, Misak-ı Millî sınırları içindeydi ancak Lozan'da Yunanistan'a bırakılmıştır.")
# U4 ek
q(U4,"Saltanat ve Halifelik Farkı",2019,"Orta","Saltanat kaldırıldığında halifelik neden devam ettirilmiştir?","Halk istememiştir","Tepkileri aşamalı olarak azaltmak ve geçiş sürecini kolaylaştırmak","İngiltere baskısı","Anayasa gereği","B")
q(U4,"Ankara'nın Başkent İlanı",2021,"Kolay","Ankara hangi tarihte başkent ilan edilmiştir?","29 Ekim 1923","13 Ekim 1923","1 Kasım 1922","3 Mart 1924","B")
q(U4,"Şeriye ve Evkaf Vekâleti",2023,"Orta","Şeriye ve Evkaf Vekâleti'nin kaldırılması hangi ilkeyle ilişkilidir?","Cumhuriyetçilik","Laiklik","Devletçilik","Halkçılık","B")
q(U4,"Anayasa Değişiklikleri",2024,"Zor","1924 Anayasası'na 1937'de eklenen ve devletin niteliğini belirleyen ifade hangisidir?","Federatif devlet","Türkiye Devleti cumhuriyetçi, milliyetçi, halkçı, devletçi, laik ve inkılapçıdır","Meşruti monarşi","Tek parti sistemi","B")
q(U4,"Maarif Teşkilatı Kanunu",2017,"Orta","1926 Maarif Teşkilatı Kanunu ile ne düzenlenmiştir?","Askerlik sistemi","Eğitim kurumlarının yapısı ve programları","Ekonomi politikaları","Dış ilişkiler","B")
q(U4,"Hukuk Devrimi",2022,"Orta","Osmanlı hukuk sisteminin yerine Avrupa'dan alınan kanunların benimsenmesinin temel amacı nedir?","Avrupa ile ittifak kurmak","Çağdaş ve laik bir hukuk düzeni oluşturmak","Dinî kurumları güçlendirmek","Askerî reformlar yapmak","B")
q(U4,"Sanayi Teşvik Kanunu",2020,"Orta","1927'de çıkarılan Teşvik-i Sanayi Kanunu'nun amacı nedir?","Tarımı desteklemek","Özel sektörün sanayi yatırımlarını teşvik etmek","İthalatı artırmak","Yabancı sermayeyi engellemek","B")
q(U4,"I. Beş Yıllık Kalkınma Planı",2018,"Zor","1933'te başlayan I. Beş Yıllık Sanayi Planı hangi ilkenin uygulamasıdır?","Halkçılık","Devletçilik","İnkılapçılık","Milliyetçilik","B")
q(U4,"Kadın Hakları ve Medeni Kanun",2016,"Kolay","Medeni Kanun ile kadınlara tanınan haklar arasında hangisi vardır?","Askerlik yapma","Boşanma hakkı","Cumhurbaşkanı olma","Parti kurma","B")
q(U4,"Üniversite Reformu",2015,"Orta","1933 Üniversite Reformu ile ne amaçlanmıştır?","Üniversiteleri kapatmak","Yükseköğretimi çağdaş ve bilimsel temellere oturtmak","Medreseleri yeniden açmak","Yabancı öğrenci almak","B")
# U5 ek
q(U5,"Atatürk İlkeleri Genel",2021,"Zor","Atatürk ilkelerinden hangisi hem iç hem dış politikayı doğrudan etkiler?","Halkçılık","Milliyetçilik","Devletçilik","Laiklik","B","Milliyetçilik ilkesi hem iç bütünlüğü (birleştiricilik) hem dış politikayı (bağımsızlık, milli çıkar) etkiler.")
q(U5,"Laiklik Uygulamaları",2023,"Orta","Aşağıdakilerden hangisi laiklik ilkesiyle doğrudan ilişkili değildir?","Halifeliğin kaldırılması","Tekke ve zaviyelerin kapatılması","Soyadı Kanunu","Şeriye Vekâleti'nin kaldırılması","C")
q(U5,"Devletçilik Uygulaması",2018,"Orta","Sümerbank ve Etibank'ın kurulması hangi ilkenin uygulamasıdır?","Cumhuriyetçilik","Devletçilik","Halkçılık","İnkılapçılık","B")
q(U5,"İnkılapçılık ve Çağdaşlaşma",2015,"Kolay","İnkılapçılık ilkesinin topluma kazandırmak istediği temel değer nedir?","Geleneklere bağlılık","Sürekli gelişme ve çağdaşlaşma","Değişmezlik","Muhafazakârlık","B")
q(U5,"Halkçılık ve Eşitlik",2022,"Kolay","Halkçılık ilkesini en iyi yansıtan uygulama hangisidir?","Kabotaj Kanunu","Kadınlara seçme-seçilme hakkı verilmesi","Harf İnkılabı","Şapka Kanunu","B")
q(U5,"Bütünleyici İlkeler",2024,"Zor","Aşağıdakilerden hangisi Atatürk'ün bütünleyici ilkelerinden biridir?","Devletçilik","Bilimsellik ve akılcılık","Cumhuriyetçilik","Milliyetçilik","B","Bilimsellik, akılcılık, çağdaşlaşma, ulusal egemenlik gibi ilkeler bütünleyici ilkelerdir.")
q(U5,"Cumhuriyetçilik ve Seçim",2016,"Kolay","Cumhuriyetçilik ilkesine göre yöneticiler nasıl belirlenir?","Atama ile","Halk tarafından seçimle","Miras yoluyla","Din adamlarınca","B")
q(U5,"Milliyetçilik ve Dil",2017,"Orta","Türk Dil Kurumu'nun kurulması hangi ilkeyle en çok ilişkilidir?","Devletçilik","Milliyetçilik","Laiklik","Halkçılık","B")
# U6 ek
q(U6,"Takrir-i Sükûn Kanunu",2020,"Zor","1925'te çıkarılan Takrir-i Sükûn Kanunu'nun çıkarılma nedeni nedir?","Ekonomik kriz","Şeyh Sait İsyanı ve rejim karşıtı faaliyetler","Dış tehditler","Seçim yasası","B")
q(U6,"Kadın Hakları Kronolojisi 2",2021,"Kolay","Kadınlara il genel meclisi seçimlerine katılma hakkı hangi yıl tanınmıştır?","1930","1933","1934","1935","B","1930 belediye, 1933 muhtarlık ve il genel meclisi, 1934 milletvekili seçilme hakkı verilmiştir.")
q(U6,"Anayasal Gelişmeler",2022,"Orta","1921 ve 1924 anayasalarının ortak özelliği nedir?","İkisi de laiklik ilkesini içerir","İkisi de egemenliğin millete ait olduğunu belirtir","İkisi de çok partili sistemi öngörür","İkisi de padişahlığı kabul eder","B")
q(U6,"Parti Kapatmaları",2024,"Orta","Serbest Cumhuriyet Fırkası neden kapanmıştır?","Hükûmet kapatmıştır","Rejim karşıtlarının partiye sızması nedeniyle kendi kendini feshetmiştir","Seçim kaybetmiştir","Halka hitap edememiştir","B")
q(U6,"1921 Anayasası Özelliği",2017,"Orta","1921 Anayasası'nın diğer anayasalardan farkı nedir?","En uzun anayasadır","Olağanüstü dönemde hazırlanmış kısa ve öz bir anayasadır","Padişahlığı korumuştur","Laiklik içerir","B")
q(U6,"Terakkiperver Cumhuriyet Fırkası",2016,"Kolay","Terakkiperver Cumhuriyet Fırkası'nın kurucuları arasında kim yoktur?","Kâzım Karabekir","Ali Fuat Cebesoy","İsmet İnönü","Rauf Orbay","C")
q(U6,"Hukuk Birliği",2015,"Zor","Hukuk birliğinin sağlanmasının demokratikleşme açısından önemi nedir?","Askerî güç artmıştır","Tüm vatandaşların aynı yasalara tabi olması sağlanmıştır","Ekonomi canlanmıştır","Dış ilişkiler güçlenmiştir","B")
# U7 ek
q(U7,"Montrö'nün Önemi",2019,"Orta","Montrö Sözleşmesi Lozan'a göre hangi konuda ilerleme sağlamıştır?","Kapitülasyonlar","Boğazlar üzerinde tam Türk egemenliği sağlanması","Sınırlar","Azınlık hakları","B")
q(U7,"Hatay'ın Katılması",2016,"Kolay","Hatay Türkiye'ye hangi yıl katılmıştır?","1936","1937","1938","1939","D")
q(U7,"Atatürk'ün Vefat Tarihi",2017,"Kolay","Atatürk ne zaman vefat etmiştir?","10 Kasım 1937","10 Kasım 1938","29 Ekim 1938","23 Nisan 1938","B")
q(U7,"Atatürk'ün Dış Politika İlkesi",2023,"Orta","Atatürk'ün dış politikadaki temel ilkesi nedir?","Yayılmacılık","Yurtta sulh, cihanda sulh","Bloklaşma","Sömürgecilik","B")
q(U7,"II. Dünya Savaşı Öncesi",2024,"Zor","Atatürk döneminde kurulan Balkan Antantı ve Sadabat Paktı hangi tehlikeye karşı oluşturulmuştur?","Ekonomik kriz","Yayılmacı ve saldırgan devletlerin tehdidi","İç isyanlar","Doğal afetler","B")
q(U7,"Milletler Cemiyeti'ne Katılım",2021,"Orta","Türkiye'nin Milletler Cemiyeti'ne kabul edilmesi neyi gösterir?","Savaşa katılacağını","Uluslararası arenada itibar kazandığını","Osmanlı'nın devam ettiğini","Sınırların değişeceğini","B")
q(U7,"Musul Meselesi",2022,"Orta","Musul meselesi nasıl sonuçlanmıştır?","Türkiye aldı","1926 Ankara Antlaşması ile İngiltere'ye (Irak'a) bırakıldı","Lozan'da çözüldü","Halk oylaması yapıldı","B")
q(U7,"Dış Borçlar",2020,"Kolay","Osmanlı'dan kalan dış borçlar hangi antlaşmayla düzenlenmiştir?","Mudanya","Lozan","Ankara","Mondros","B")

with open("/Users/talatkarasakal/Documents/Çark/batch2.json","w",encoding="utf-8") as f:
    json.dump(Q, f, ensure_ascii=False, indent=2)
print(f"Batch 2: {len(Q)} soru yazıldı.")
