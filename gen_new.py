#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mevcut sorular.json'a 65+ yeni soru ekler -> toplam 100+ soru."""
import json, os

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

# (unite, konu, yil, zorluk, soru, A, B, C, D, dogru_cevap, aciklama)
RAW = [
# ═══════════════════════════════════════════════════════
# ÜNİTE 1 – Bir Kahraman Doğuyor (15 yeni soru)
# ═══════════════════════════════════════════════════════
(U1,"Mustafa Kemal'in Ailesi",2016,"Kolay",
 "Mustafa Kemal'in babasının mesleği aşağıdakilerden hangisidir?",
 "Doktor","Çiftçi","Gümrük memuru","Asker","C",
 "Ali Rıza Efendi, Selanik'te gümrük memuru olarak çalışmıştır."),

(U1,"Mustafa Kemal'in Doğumu",2017,"Kolay",
 "Mustafa Kemal'in doğduğu şehir ve yıl hangisidir?",
 "İstanbul – 1880","Selanik – 1881","Ankara – 1881","Manastır – 1882","B",
 "Mustafa Kemal, 1881 yılında Osmanlı İmparatorluğu'nun Selanik şehrinde doğmuştur."),

(U1,"Mustafa Kemal'in Eğitimi",2019,"Orta",
 "Mustafa Kemal, Harp Akademisi'ni kaç yılında bitirmiştir?",
 "1899","1902","1905","1908","C",
 "Mustafa Kemal, 1905 yılında Harp Akademisi'ni kurmay yüzbaşı olarak bitirmiştir."),

(U1,"Trablusgarp Savaşı",2020,"Orta",
 "Mustafa Kemal, Trablusgarp Savaşı'nda hangi ülkeye karşı savaşmıştır?",
 "Yunanistan","Rusya","İtalya","Fransa","C",
 "Trablusgarp Savaşı (1911-1912), Osmanlı-İtalya arasında Libya üzerinde yaşanmıştır."),

(U1,"Balkan Savaşları",2018,"Orta",
 "Balkan Savaşları'nın (1912-1913) Osmanlı için en önemli sonucu aşağıdakilerden hangisidir?",
 "Doğu Anadolu'nun kaybedilmesi","Selanik dahil Rumeli topraklarının büyük bölümünün kaybedilmesi","Suriye'nin elden çıkması","İstanbul'un işgali","B",
 "Balkan Savaşları'nda Osmanlı, Balkan devletleri karşısında yenilerek Rumeli'nin büyük bölümünü ve Selanik'i kaybetti."),

(U1,"İttihat ve Terakki",2021,"Orta",
 "Mustafa Kemal'in İttihat ve Terakki Cemiyeti'yle ilişkisi için aşağıdakilerden hangisi doğrudur?",
 "Cemiyetin kurucusudur.","Cemiyetin politikalarını bütünüyle benimsemiştir.","Cemiyete katılmış ancak politikalarını eleştirmiştir.","Cemiyetle hiç ilişki kurmamıştır.","C",
 "Mustafa Kemal, örgütle ilişki kurmuş fakat özellikle Almanya'ya bağımlılık politikasını eleştirmiştir."),

(U1,"I. Dünya Savaşı – Çanakkale",2022,"Zor",
 "'Ben size taarruz etmiyorum, ölmeyi emrediyorum!' emri hangi muharebede ve kim tarafından verilmiştir?",
 "Sakarya – İsmet Paşa","Çanakkale – Mustafa Kemal","İnönü – Mustafa Kemal","Dumlupınar – Mustafa Kemal","B",
 "Bu tarihi emir, 57. Alay'a Çanakkale'de Conkbayırı'nı tutmaları için Mustafa Kemal tarafından verilmiştir."),

(U1,"I. Dünya Savaşı – Cepheler",2023,"Orta",
 "Mustafa Kemal, I. Dünya Savaşı'nda Çanakkale dışında hangi cephede görev yapmıştır?",
 "Kafkas Cephesi","Irak Cephesi","Suriye-Filistin Cephesi","Galiçya Cephesi","C",
 "Mustafa Kemal, savaşın son evresinde Yıldırım Orduları bünyesinde Suriye-Filistin Cephesi'nde görev yapmıştır."),

(U1,"Osmanlı'nın Savaşa Girişi",2017,"Orta",
 "Osmanlı'nın I. Dünya Savaşı'na girişinde hangi ittifak belirleyici olmuştur?",
 "İtilaf Devletleri (İngiltere-Fransa-Rusya)","İttifak Devletleri (Almanya-Avusturya-Macaristan)","Balkan İttifakı","Akdeniz İttifakı","B",
 "Osmanlı Devleti, Almanya ve Avusturya-Macaristan'dan oluşan İttifak Devletleri yanında savaşa girmiştir."),

(U1,"Mustafa Kemal'in Karakteri",2015,"Kolay",
 "Mustafa Kemal'in askerî okullardaki en belirgin özelliği aşağıdakilerden hangisidir?",
 "Kuralları harfiyen uygulaması","Matematik ve fen bilimlerine olan ilgisi","Sorgulayan ve eleştiren düşünce yapısı","Söz dinleyen yapısı","C",
 "Mustafa Kemal okul yıllarında sorgulamayı ve düşünmeyi seven kişiliğiyle öne çıkmıştır."),

(U1,"Mustafa Kemal'in İsmi",2024,"Kolay",
 "'Kemal' adını Mustafa'ya kim vermiştir?",
 "Annesi Zübeyde Hanım","Babası Ali Rıza Efendi","Matematik öğretmeni Yüzbaşı Mustafa","Okul müdürü","C",
 "Matematik öğretmeni Yüzbaşı Mustafa, zeki öğrencisini kendinden ayırt etmek için ona 'Kemal' adını vermiştir."),

(U1,"I. Dünya Savaşı Sonucu – Osmanlı",2023,"Orta",
 "I. Dünya Savaşı'nda yenilen Osmanlı Devleti hangi ateşkes antlaşmasını imzalamak zorunda kalmıştır?",
 "Gümrü Ateşkesi","Mudanya Ateşkesi","Mondros Ateşkesi","Lozan Ateşkesi","C",
 "Osmanlı, 30 Ekim 1918'de İtilaf Devletleri ile Mondros Mütarekesi'ni imzalayarak savaştan çekilmiştir."),

(U1,"Savaşın Getirdiği Yıkım",2016,"Orta",
 "I. Dünya Savaşı'nın Osmanlı toplumu üzerindeki en ağır etkisi aşağıdakilerden hangisidir?",
 "Ekonominin güçlenmesi","Büyük nüfus ve toprak kayıpları ile ekonomik çöküş","Sanayinin gelişmesi","Eğitimin yaygınlaşması","B",
 "Savaş, Osmanlı'ya büyük nüfus ve toprak kaybı ile birlikte ağır ekonomik yıkım yaşatmıştır."),

(U1,"Mustafa Kemal'in Suriye Görevi",2018,"Zor",
 "Mustafa Kemal, Suriye-Filistin Cephesi'ndeki görevini bırakıp Anadolu'ya geçmesinin temel nedenini nasıl açıklamıştır?",
 "Daha iyi bir görev için","Mondros Mütarekesi sonrası milleti örgütlemek amacıyla","İstanbul'da iş aramak için","Ailesiyle birlikte olmak için","B",
 "Mondros sonrası Anadolu'nun işgal tehlikesiyle karşı karşıya kaldığını gören Mustafa Kemal, millî mücadeleyi örgütlemek amacıyla Anadolu'ya geçmiştir."),

(U1,"Çanakkale'nin Önemi",2022,"Zor",
 "Çanakkale Savaşları'nın Osmanlı ve Türk tarihi açısından önemi değerlendirildiğinde aşağıdakilerden hangisi doğrudur?",
 "Osmanlı savaşı kolayca kazanmıştır.","İtilaf Devletleri'nin Boğazları geçmesi engellenmiş, bu Mustafa Kemal'i kahraman yapmıştır.",
 "Osmanlı'nın savaştan erken çekilmesini sağlamıştır.","Rusya'ya yardım yolu açılmıştır.","B",
 "Çanakkale Savaşları, İtilaf Devletleri'nin Osmanlı'yı çabuk çökertme planını engellemiş; Mustafa Kemal Anafartalar'daki başarılarıyla ün kazanmıştır."),

# ═══════════════════════════════════════════════════════
# ÜNİTE 2 – Millî Uyanış (10 yeni soru)
# ═══════════════════════════════════════════════════════
(U2,"Sevr Antlaşması",2021,"Zor",
 "Sevr Antlaşması (1920) ile Osmanlı topraklarına ne yapılmak istenmiştir?",
 "Osmanlı güçlendirilmek istenmiştir.","Anadolu başta olmak üzere Osmanlı toprakları paylaşılmak ve Türklere küçük bir alan bırakılmak istenmiştir.",
 "Osmanlı'nın toprakları korunmuştur.","Osmanlı'ya yeni topraklar verilmiştir.","B",
 "Sevr, Anadolu'yu çeşitli devletler arasında paylaştıran ve Türklere küçük bir iç bölgeyi bırakan ağır bir antlaşmadır."),

(U2,"Kuvay-ı Milliye",2019,"Orta",
 "Kuvay-ı Milliye birlikleri nasıl tanımlanabilir?",
 "Osmanlı ordusunun düzenli birlikleri","Düzenli ordu kurulmadan önce halkın oluşturduğu direniş güçleri",
 "İtilaf Devletleri'nin Anadolu'daki birlikleri","İstanbul Hükûmeti'ne bağlı kuvvetler","B",
 "Kuvay-ı Milliye, Mondros'tan sonra işgallere karşı halkın kendiliğinden oluşturduğu düzensiz direniş birlikleriydi."),

(U2,"Misak-ı Millî",2022,"Zor",
 "Son Osmanlı Meclis-i Mebusanı'nda kabul edilen Misak-ı Millî'de yer alan temel ilke aşağıdakilerden hangisidir?",
 "Osmanlı İmparatorluğu'nun yeniden kurulması","Türk milletinin bağımsız ve onurlu yaşayabileceği vatanın sınırlarının çizilmesi",
 "Manda yönetiminin kabul edilmesi","İstanbul'un başkent olarak korunması","B",
 "Misak-ı Millî, 28 Ocak 1920'de Türk milletinin vazgeçilmez olarak belirlediği vatan sınırlarını ve bağımsızlık hedeflerini ilan etmiştir."),

(U2,"Temsil Heyeti",2020,"Orta",
 "Sivas Kongresi sonunda kurulan Temsil Heyeti'nin görevi nedir?",
 "Osmanlı padişahını temsil etmek","Millî Mücadele'yi yürütecek yürütme organı olarak görev yapmak",
 "İtilaf Devletleri ile müzakere yürütmek","Düzenli orduyu kurmak","B",
 "Temsil Heyeti, Sivas Kongresi kararlarını uygulamak ve millî hareketi yönetmek amacıyla oluşturulmuştur."),

(U2,"İstanbul'un İşgali",2024,"Orta",
 "İtilaf Devletleri'nin 16 Mart 1920'de İstanbul'u resmen işgal etmesi hangi sonucu doğurmuştur?",
 "Millî Mücadele'nin zayıflamasına neden olmuştur.","Son Osmanlı Meclisi kapatılmış; bu, TBMM'nin Ankara'da açılmasını zorunlu kılmıştır.",
 "Osmanlı Hükümeti güçlenmiştir.","Mondros Mütarekesi iptal edilmiştir.","B",
 "İşgal üzerine Osmanlı Meclisi dağıtılmış, bu durum Ankara'da 23 Nisan 1920'de TBMM'nin açılmasına zemin hazırlamıştır."),

(U2,"Manda ve Himaye",2023,"Zor",
 "Sivas Kongresi'nde manda ve himaye fikri kesinlikle reddedilmiştir. Bu tutum aşağıdaki ilkelerden hangisiyle en çok örtüşür?",
 "Ekonomik bağımsızlık","Tam bağımsızlık (kayıtsız şartsız bağımsızlık) ilkesi","Bölgesel yönetim ilkesi","Anayasal monarşi ilkesi","B",
 "Manda ve himayenin reddi, tam bağımsızlık ilkesinin temel göstergesidir; başka bir devletin himayesi altına girmek kabul edilemez bulunmuştur."),

(U2,"Anadolu'daki İşgaller",2018,"Orta",
 "İzmir'in 15 Mayıs 1919'da Yunan kuvvetleri tarafından işgali hangi gelişmeye zemin hazırlamıştır?",
 "İstanbul'un terk edilmesine","Türk halkının millî bilincinin canlanmasına ve direnişin örgütlenmesine",
 "Osmanlı'nın savaşa yeniden girmesine","Lozan Antlaşması'nın imzalanmasına","B",
 "İzmir'in işgali, Anadolu halkında büyük bir milliyetçi uyanışa yol açmış ve Millî Mücadele'nin fiilen başlamasını tetiklemiştir."),

(U2,"Erzurum Kongresi Kararları",2024,"Orta",
 "Erzurum Kongresi'nin bölgesel değil ulusal nitelik taşıdığının en önemli kanıtı aşağıdakilerden hangisidir?",
 "Yalnızca Erzurum'u ilgilendiren kararlar alınmıştır.","'Millî sınırlar içinde vatan bir bütündür, parçalanamaz.' kararı alınmıştır.",
 "Saltanat kaldırılmıştır.","Yalnızca Doğu Anadolu'yu kapsayan bir savunma kararı alınmıştır.","B",
 "Erzurum Kongresi, bölgesel olmasına rağmen tüm yurdu kapsayan 'vatanın bölünmezliği' ilkesini benimseyerek ulusal nitelik kazanmıştır."),

(U2,"Amasya Görüşmeleri",2019,"Zor",
 "Amasya Görüşmeleri'nde (Ekim 1919) Osmanlı Hükümeti temsilcileriyle varılan uzlaşma hangi açıdan önemlidir?",
 "Saltanatın kaldırılması kararlaştırılmıştır.","İstanbul Hükümeti, ilk kez Millî Hareketi fiilen tanımış ve Misak-ı Millî'yi kabul etmiştir.",
 "TBMM'nin kurulmasına karar verilmiştir.","Mondros Mütarekesi iptal edilmiştir.","B",
 "Amasya Görüşmeleri ile İstanbul Hükümeti, Millî Hareketi fiilen tanıyıp Misak-ı Millî kararlarını pratikte kabul etmiştir."),

(U2,"Kuva-yı İnzibatiye",2022,"Zor",
 "İstanbul Hükümeti'nin TBMM'ye karşı kurduğu Kuva-yı İnzibatiye'nin (Hilafet Ordusu) amacı neydi?",
 "Yunan kuvvetlerine karşı savaşmak","Millî Mücadele kuvvetlerini bastırmak ve TBMM otoritesini sarsmak",
 "Düzenli orduya destek vermek","Mondros şartlarını uygulamak","B",
 "Kuva-yı İnzibatiye, İstanbul Hükümeti'nin desteğiyle Millî Mücadele hareketini engellemek amacıyla kurulmuştur; TBMM ona karşı 'Hıyanet-i Vataniye Kanunu'nu çıkarmıştır."),

# ═══════════════════════════════════════════════════════
# ÜNİTE 3 – Ya İstiklal Ya Ölüm (9 yeni soru)
# ═══════════════════════════════════════════════════════
(U3,"TBMM'nin Nitelikleri",2021,"Orta",
 "TBMM'nin 'olağanüstü yetkilere sahip meclis' olarak tanımlanmasının nedeni aşağıdakilerden hangisidir?",
 "Yalnızca yasama yetkisine sahip olması","Yasama, yürütme ve yargı yetkilerini tek çatıda birleştirmesi",
 "Yalnızca yargı yetkisine sahip olması","İstanbul Hükümeti'ne bağlı olması","B",
 "Olağanüstü koşullarda açılan TBMM, üç erki de bünyesinde toplamış ve meclis hükümeti sistemiyle yönetimi üstlenmiştir."),

(U3,"Doğu Cephesi – Ermeniler",2019,"Orta",
 "Doğu Cephesi'nde Ermeni kuvvetlerine karşı kazanılan zafer sonucunda imzalanan Gümrü Antlaşması'nın önemi nedir?",
 "Osmanlı'nın savaştan çekilmesini sağlamıştır.","TBMM'nin uluslararası alanda tanınan ilk antlaşmasıdır.",
 "Lozan Antlaşması'nın hazırlığıdır.","Boğazlar meselesini çözmüştür.","B",
 "3 Aralık 1920'de imzalanan Gümrü Antlaşması ile TBMM, uluslararası düzeyde ilk kez tanınmıştır."),

(U3,"İstiklal Mahkemeleri",2023,"Zor",
 "Millî Mücadele döneminde kurulan İstiklal Mahkemelerinin temel işlevi neydi?",
 "Müttefik devletlerle müzakere yürütmek","Cephe gerisinde asker kaçaklığını ve ihaneti yargılayarak millî birliği korumak",
 "İstanbul Hükümeti kararlarını uygulamak","Yabancı uyrukluları yargılamak","B",
 "İstiklal Mahkemeleri, savaş döneminde asker kaçaklarını ve devlet otoritesini tehdit eden kişileri yargılamış; böylece cephe gerisinde düzeni korumuştur."),

(U3,"Düzenli Ordu",2020,"Orta",
 "Kuvay-ı Milliye'den düzenli orduya geçişin nedeni aşağıdakilerden hangisidir?",
 "Kuvay-ı Milliye'nin Yunan kuvvetlerini kolayca yenmiş olması","Düzensiz birliklerin yetersiz kalması ve düzenli bir orduya ihtiyaç duyulması",
 "İstanbul Hükümeti'nin baskısı","İtilaf Devletleri'nin talebi","B",
 "Batı Cephesi'ndeki ilk yenilgilerden sonra Kuvay-ı Milliye'nin yetersizliği görülmüş ve 1921'de düzenli ordunun kurulmasına karar verilmiştir."),

(U3,"II. İnönü – Londra Konferansı",2021,"Zor",
 "II. İnönü Muharebesi'nin (Mart-Nisan 1921) siyasi sonucu aşağıdakilerden hangisidir?",
 "Doğu sınırının kesinleşmesi","Afgan-Türk dostluk antlaşmasının imzalanması","Londra Konferansı'nın Türk tarafının istekleri kabul edilmeden dağılması",
 "Yunanistan'ın barış teklifinde bulunması","C",
 "II. İnönü Zaferi'nin ardından toplanan Londra Konferansı herhangi bir sonuç vermeden dağılmış ve bu Türk tarafının gücünü göstermiştir."),

(U3,"Ankara Antlaşması – Fransa",2018,"Orta",
 "1921'de Türkiye ile Fransa arasında imzalanan Ankara Antlaşması neyi sağlamıştır?",
 "Yunanistan'la barışı","Güney Cephesi'nin kapanmasını ve Fransa'nın Millî Hareketi tanımasını",
 "TBMM'nin uluslararası alanda ilk kez tanınmasını","Boğazların Türk kontrolüne geçmesini","B",
 "Ankara Antlaşması ile Fransa Güney Cephesi'nden çekilmiş, Anadolu'daki Millî Hareketi fiilen tanımış ve TBMM diplomatik bir zafer kazanmıştır."),

(U3,"Sakarya Zaferi'nin Önemi",2024,"Zor",
 "Sakarya Meydan Muharebesi (Ağustos-Eylül 1921) hangi açıdan bir dönüm noktasıdır?",
 "Savaşın fiilen bittiği muharebedir.","Stratejik üstünlük Yunanistan'dan Türkiye'ye geçmiş; bu, Büyük Taarruz'un önünü açmıştır.",
 "Lozan müzakerelerini doğrudan başlatmıştır.","TBMM'nin kurulmasına zemin hazırlamıştır.","B",
 "Sakarya Zaferi ile savunma savaşı biten Türk ordusu stratejik üstünlük kazanmış ve Büyük Taarruz için gerekli ortam hazırlanmıştır."),

(U3,"Büyük Taarruz Tarihi",2017,"Kolay",
 "Büyük Taarruz ve Başkomutanlık Meydan Muharebesi'nin yapıldığı tarih aşağıdakilerden hangisidir?",
 "Ağustos 1921","Eylül 1921","Ağustos-Eylül 1922","Ekim 1923","C",
 "Büyük Taarruz 26 Ağustos 1922'de başlamış, 30 Ağustos'ta Başkomutanlık Meydan Muharebesi ile zaferle sonuçlanmıştır."),

(U3,"Lozan Öncesi Mudanya",2023,"Orta",
 "Mudanya Ateşkes Antlaşması'nın (11 Ekim 1922) Lozan Barış Antlaşması açısından önemi nedir?",
 "Lozan'ın yerini almıştır.","Ateşkesle silahlar susmuş; siyasi barışın çerçevesi Lozan'da çizilmiştir.",
 "Kapitülasyonları kaldırmıştır.","Yunanistan'la sınır belirlenmiştir.","B",
 "Mudanya, askeri düzeyde ateşkesi sağlayan antlaşmadır. Kalıcı barış ve sınırlar, 24 Temmuz 1923'te imzalanan Lozan Antlaşması ile belirlenmiştir."),

# ═══════════════════════════════════════════════════════
# ÜNİTE 4 – Atatürk ve Çağdaşlaşan Türkiye (8 yeni soru)
# ═══════════════════════════════════════════════════════
(U4,"Cumhuriyetin İlanı",2021,"Kolay",
 "Türkiye Cumhuriyeti hangi tarihte ilan edilmiştir?",
 "23 Nisan 1920","1 Kasım 1922","29 Ekim 1923","3 Mart 1924","C",
 "Türkiye Cumhuriyeti, 29 Ekim 1923'te Mustafa Kemal'in önerileriyle TBMM tarafından ilan edilmiştir."),

(U4,"Hukuk Alanı – Medeni Kanun",2020,"Orta",
 "1926 yılında kabul edilen Türk Medeni Kanunu hangi ülkenin medeni kanunundan uyarlanmıştır?",
 "Fransa","Almanya","İsviçre","İtalya","C",
 "Türk Medeni Kanunu, İsviçre Medeni Kanunu esas alınarak hazırlanmıştır."),

(U4,"Ekonomi Alanı – Kabotaj",2019,"Kolay",
 "1926'da çıkarılan Kabotaj Kanunu ile ne amaçlanmıştır?",
 "Yabancı sermayeyi ülkeye çekmek","Türk kara ve deniz sularında taşımacılık hakkının yalnızca Türk gemicilere verilmesi",
 "Osmanlı borçlarını ödemek","Tarım alanında reform yapmak","B",
 "Kabotaj Kanunu ile Türk kıyıları ve iç suları arasındaki taşımacılık münhasıran Türk bayraklı gemilere tanınmış; ekonomik egemenlik pekiştirilmiştir."),

(U4,"Kültür Alanı – Türk Tarih Kurumu",2022,"Orta",
 "1931'de kurulan Türk Tarih Kurumu'nun temel amacı aşağıdakilerden hangisidir?",
 "Osmanlı tarihini yeniden yazmak","Türk tarihini bilimsel yöntemlerle araştırmak ve Türk milletine milliyet bilinci kazandırmak",
 "Arap tarihini Türkçeye çevirmek","Yabancı tarihçileri ülkeye davet etmek","B",
 "Türk Tarih Kurumu, milli kimliğin güçlendirilmesi ve Türk tarihinin bilimsel düzeyde araştırılması amacıyla kurulmuştur."),

(U4,"Kültür Alanı – Türk Dil Kurumu",2023,"Kolay",
 "1932'de kurulan Türk Dil Kurumu'nun amacı nedir?",
 "Yabancı dillerin öğretimini yaygınlaştırmak","Türk dilini yabancı etkilerden arındırıp geliştirmek",
 "Arapça ve Farsçayı müfredata koymak","Osmanlıcayı korumak","B",
 "Türk Dil Kurumu, Türkçeyi yabancı sözcüklerden arındırarak özleştirmek ve geliştirmek amacıyla kurulmuştur."),

(U4,"Sosyal Alan – Soyadı Kanunu",2019,"Kolay",
 "1934 yılında kabul edilen Soyadı Kanunu ile aşağıdakilerden hangisi amaçlanmıştır?",
 "Osmanlı hanedanını onurlandırmak","Vatandaşlar arasında ayrım yaratmak","Nüfus kayıtlarını düzenlemek ve toplumsal modernleşmeye katkı sağlamak",
 "Yabancıların Türkçe soyad almasını engellemek","C",
 "Soyadı Kanunu ile her Türk vatandaşı bir soyadı almak zorunda kılınmış; nüfus kayıtları düzenlenmiş ve modernleşme sürecine katkı sağlanmıştır."),

(U4,"Eğitim – Köy Enstitüleri",2024,"Orta",
 "1940 yılında açılan Köy Enstitülerinin temel amacı aşağıdakilerden hangisidir?",
 "Şehirlerde eğitim kalitesini artırmak","Köy çocuklarını öğretmen yetiştirerek kırsal kesime eğitim götürmek",
 "Yabancı uzmanları eğitmek","Asker yetiştirmek","B",
 "Köy Enstitüleri, köy kökenli gençleri hem öğretmen hem de tarım ve zanaat alanında donanımlı bireyler olarak yetiştirmeyi hedeflemiştir."),

(U4,"Ekonomi – I. Beş Yıllık Kalkınma Planı",2021,"Orta",
 "1934'te başlayan I. Beş Yıllık Sanayi Planı hangi anlayışın ürünüdür?",
 "Liberal ekonomi","Devletçilik","Özel girişimcilik","Tarım ekonomisi","B",
 "Büyük Buhran'ın ardından devletin ekonomiye doğrudan müdahalesini öngören Devletçilik ilkesi çerçevesinde hazırlanan plan, ülkede ağır sanayinin temelini atmıştır."),

# ═══════════════════════════════════════════════════════
# ÜNİTE 5 – Demokratikleşme Çabaları (13 yeni soru)
# ═══════════════════════════════════════════════════════
(U5,"Serbest Cumhuriyet Fırkası",2020,"Orta",
 "Serbest Cumhuriyet Fırkası (1930) neden kısa sürede kapatılmıştır?",
 "Seçimleri kaybettiği için","Rejim karşıtı ve irticai hareketlere zemin hazırlandığından endişe duyulduğu için",
 "Ekonomi polituikaları yetersiz kaldığı için","Üye sayısı az olduğu için","B",
 "Serbest Cumhuriyet Fırkası, kısa sürede karşı cephelerin odak noktasına dönüşmesi üzerine kurucusu Fethi Okyar tarafından kapatılmıştır."),

(U5,"Kadın Hakları – Belediye",2023,"Kolay",
 "Türk kadınına belediye seçimlerinde oy kullanma ve seçilme hakkı hangi yılda verilmiştir?",
 "1923","1926","1930","1934","C",
 "Türk kadınına belediye seçimlerinde seçme ve seçilme hakkı 1930 yılında tanınmıştır."),

(U5,"Hukuk Reformu",2019,"Orta",
 "1926'da Türk Ceza Kanunu'nun yürürlüğe girmesiyle aşağıdakilerden hangisi gerçekleşmiştir?",
 "Şeriat hukuku güçlendirilmiştir.","Çağdaş Batı hukuku ilkeleri Türk ceza sistemine uyarlanmıştır.",
 "Osmanlı hukuku aynen korunmuştur.","Yalnızca ticaret hukuku düzenlenmiştir.","B",
 "İtalyan Ceza Kanunu'ndan uyarlanan Türk Ceza Kanunu, Türk hukuk sistemini modernize etmiştir."),

(U5,"Basın Özgürlüğü",2022,"Zor",
 "Tek parti dönemi (1923-1946) basın politikası değerlendirildiğinde aşağıdakilerden hangisi doğrudur?",
 "Basın tamamen özgürdü.","Basın, genel olarak tek parti yönetiminin denetimine tabi tutulmuştu.",
 "Yabancı gazeteler serbestçe yayımlanıyordu.","Muhalif basın destekleniyordu.","B",
 "Tek parti döneminde basın, hükümet çizgisinden çıkmamak şartıyla faaliyetini sürdürmekte; muhalif yayınlar denetim ve baskıyla karşılaşmaktaydı."),

(U5,"İzmir İktisat Kongresi",2024,"Orta",
 "1923'te toplanan İzmir İktisat Kongresi'nin temel mesajı aşağıdakilerden hangisidir?",
 "Osmanlı ekonomik sistemi korunacaktır.","Millî ekonomi politikasıyla bağımsız ve üretken bir ekonomi hedeflenmektedir.",
 "Yabancı sermayeye tam açılım sağlanacaktır.","Tarım kaldırılıp sanayi ekonomisine geçilecektir.","B",
 "İzmir İktisat Kongresi, millî ekonomi anlayışını esas alarak sanayi, ticaret ve tarım gibi alanlarda ortak hedefler belirlemiştir."),

(U5,"Çok Partili Geçiş – 1946",2021,"Orta",
 "Türkiye'de çok partili siyasi hayata geçişin kalıcı olarak gerçekleştiği yıl aşağıdakilerden hangisidir?",
 "1930","1938","1945","1946","D",
 "Demokrat Parti'nin kurulduğu 1945 ve ilk çok partili seçimlerin yapıldığı 1946, çok partili hayata kalıcı geçişin dönüm noktası olarak kabul edilir."),

(U5,"Demokrat Parti",2022,"Orta",
 "1946'da kurulan Demokrat Parti hangi partiden ayrılan isimler tarafından kurulmuştur?",
 "Terakkiperver Cumhuriyet Fırkası","Cumhuriyet Halk Partisi","Serbest Cumhuriyet Fırkası","Liberal Parti","B",
 "Celal Bayar, Adnan Menderes, Refik Şevket İnce ve Fuat Köprülü gibi CHP'li isimler ayrılarak Demokrat Parti'yi kurmuştur."),

(U5,"1950 Seçimleri",2023,"Kolay",
 "Türkiye'de ilk serbest ve demokratik genel seçim hangi sonuçla tamamlanmıştır?",
 "CHP iktidarı sürmüştür.","Demokrat Parti büyük çoğunlukla iktidara gelmiştir.",
 "Askerî yönetim kurulmuştur.","Seçimler iptal edilmiştir.","B",
 "14 Mayıs 1950 seçimlerinde Demokrat Parti ezici çoğunlukla kazanmış; Celal Bayar Cumhurbaşkanı, Adnan Menderes ise Başbakan olmuştur."),

(U5,"Basın ve İletişim",2017,"Orta",
 "Cumhuriyetin ilk yıllarında kurulan Anadolu Ajansı'nın işlevi neydi?",
 "Yabancı haber ajanslarıyla rekabet etmek","Millî haberleri toplamak ve yaymak; ulusal iletişimi sağlamak",
 "Osmanlı haberlerini arşivlemek","Radyo yayıncılığını yürütmek","B",
 "Anadolu Ajansı (AA), Millî Mücadele sırasında Ankara'da kurulmuş; millî haberleri toplayıp yayan, ulusal medyanın temel haber kaynağı olmuştur."),

(U5,"Atatürk Dönemi Siyasi Yapısı",2020,"Zor",
 "Cumhuriyetin ilk yıllarında tek parti yönetiminin benimsenmesinin temel nedeni aşağıdakilerden hangisidir?",
 "Demokrasinin reddedilmesi","İnkılap sürecini ve millî birliği sağlam biçimde yönetme zorunluluğu",
 "Halkın çok partili sistemi istememesi","Zaten çok partili bir sistem uygulanıyordu.","B",
 "Kuruluş sürecinde inkılapların hızlı biçimde hayata geçirilmesi ve millî birliğin korunması amacıyla tek parti sistemi benimsenmiştir."),

(U5,"Laikleşme Süreci",2021,"Orta",
 "Laikleşme sürecinde gerçekleştirilen aşağıdaki adımların kronolojik sırası hangisidir?",
 "Cumhuriyet İlanı → Halifeliğin Kaldırılması → Laikliğin Anayasaya Girmesi",
 "Halifeliğin Kaldırılması → Cumhuriyet İlanı → Laikliğin Anayasaya Girmesi",
 "Laikliğin Anayasaya Girmesi → Cumhuriyet İlanı → Halifeliğin Kaldırılması",
 "Cumhuriyet İlanı → Laikliğin Anayasaya Girmesi → Halifeliğin Kaldırılması","A",
 "Kronolojik sıra: Cumhuriyet İlanı (29 Ekim 1923) → Halifeliğin Kaldırılması (3 Mart 1924) → Laikliğin Anayasaya girmesi (1937)."),

(U5,"Takvim ve Ölçüler",2016,"Kolay",
 "1925'te Miladi takvime geçilmesinin temel amacı aşağıdakilerden hangisidir?",
 "İslam kültürünü terk etmek","Uluslararası ticaret ve iletişimi kolaylaştırmak","Eski takvimi tamamen silmek","Astronomi araştırmalarını geliştirmek","B",
 "Hicri ve Rumi takvimlerin yerine Miladi takvimin benimsenmesi, ülkenin uluslararası ticaret ve diplomasideki uyumunu artırmayı amaçlamıştır."),

(U5,"Şapka Kanunu",2018,"Orta",
 "1925'te kabul edilen Şapka Kanunu'na bazı bölgelerde direniş gösterilmesinin temel nedeni aşağıdakilerden hangisidir?",
 "Şapkaların pahalı olması","Şapkanın Batı kültürünü simgelemesine karşı geleneksel-dinî muhalefetin varlığı",
 "Kanunun uygulanmaması","İttihat-Terakki iktidarının devreye girmesi","B",
 "Bazı bölgelerde, Şapka Kanunu'nun geleneksel dini simgeleri (fes) kaldırması nedeniyle muhafazakâr-dini çevrelerden direniş gelmiştir."),

# ═══════════════════════════════════════════════════════
# ÜNİTE 6 – Atatürk Dönemi Türk Dış Politikası (12 yeni soru)
# ═══════════════════════════════════════════════════════
(U6,"İngilizlerle İlişkiler – Musul",2020,"Orta",
 "Türkiye ile İngiltere arasındaki Musul meselesi nasıl çözüme kavuşturulmuştur?",
 "Musul Türkiye'ye bırakılmıştır.","Milletler Cemiyeti kararıyla Musul İngiliz mandası altındaki Irak'a bırakılmıştır.",
 "Musul bağımsız bir devlet olmuştur.","Musul meselesi hiç çözüme kavuşturulamamıştır.","B",
 "1926'da Milletler Cemiyeti kararıyla Musul, İngiliz yönetimindeki Irak'a bırakılmış; Türkiye bu kararı kabul etmek zorunda kalmıştır."),

(U6,"Nüfus Mübadelesi",2022,"Orta",
 "Lozan Antlaşması çerçevesinde gerçekleştirilen Türk-Yunan nüfus mübadelesinin temel ölçütü neydi?",
 "Dil","Din","Etnik köken","Sosyal sınıf","B",
 "Mübadelede dini kimlik esas alınmış; Anadolu Rumları ile Yunanistan Müslümanları yer değiştirmiştir."),

(U6,"Milletler Cemiyeti",2019,"Orta",
 "Türkiye, Milletler Cemiyeti'ne hangi yılda kabul edilmiştir?",
 "1923","1929","1932","1936","C",
 "Türkiye, 1932 yılında Milletler Cemiyeti'ne üye olmuş; bu, Türkiye'nin uluslararası arenada tanınmasını ve güvenilir bir ortak olarak kabul edilmesini simgelemiştir."),

(U6,"Balkanlarda Barış Politikası",2021,"Orta",
 "Türkiye'nin Balkan Antantı'na katılmasının temel amacı nedir?",
 "Balkan devletleri üzerinde hâkimiyet kurmak","Balkanlar'da bölgesel barış ve güvenliği ortak güvence altına almak",
 "Sovyetler Birliği'ne karşı ittifak oluşturmak","İtalya'ya karşı cephe açmak","B",
 "1934'te Türkiye, Yunanistan, Romanya ve Yugoslavya'nın imzaladığı Balkan Antantı, Balkanlar'da statükonun korunmasını ve güvenliğin sağlanmasını amaçlamıştır."),

(U6,"Sadabat Paktı",2024,"Orta",
 "1937'de imzalanan Sadabat Paktı hangi devletleri kapsamaktadır?",
 "Türkiye, Irak, İran, Afganistan","Türkiye, Yunanistan, Romanya, Yugoslavya",
 "Türkiye, Suriye, Mısır, Libya","Türkiye, Almanya, İtalya, Japonya","A",
 "Sadabat Paktı, Türkiye, Irak, İran ve Afganistan arasında imzalanmış; Orta Doğu'da bölgesel güvenliği amaçlamıştır."),

(U6,"Türkiye'nin Dış Politika İlkeleri",2023,"Zor",
 "Atatürk döneminde Türk dış politikasının temel ilkesi olarak benimsenen 'Yurtta sulh, cihanda sulh' anlayışı hangi tutumu yansıtır?",
 "Saldırgan bir dış politika anlayışı","Barışçıl, statükocu ve revizyonist olmayan bir dış politika anlayışı",
 "Müttefik arayışına dayalı bir dış politika anlayışı","Yalnızcılık (izolasyonizm) politikası","B",
 "Bu ilke; Türkiye'nin toprak taleplerini savaşla değil, diplomatik yollarla çözmeyi ve barışı hem içeride hem dışarıda korumayı öngören politikayı simgelemektedir."),

(U6,"Lozan'dan Kalan Sorunlar",2019,"Orta",
 "Lozan Antlaşması sonrası çözüme kavuşturulması gereken BAşlıca sorun aşağıdakilerden hangisidir?",
 "Misak-ı Millî sınırları","Nüfus mübadelesi ve Boğazlar meselesi","Osmanlı borçları ve kapitülasyonlar","Hatay ve Boğazlar meselesi","D",
 "Lozan'dan sonra Türkiye'nin dış politikasının öncelikleri arasında Hatay meselesi ve Boğazlar üzerindeki egemenliğin tam sağlanması yer almıştır."),

(U6,"Türk-Sovyet İlişkileri",2022,"Orta",
 "Millî Mücadele döneminde Türkiye-Sovyetler Birliği ilişkisinin temelini ne oluşturmuştur?",
 "Ortak din bağı","Ortak düşmana karşı çıkar birliği; Sovyetlerin TBMM'ye silah ve mali destek sağlaması",
 "Ekonomik ortaklık","Askeri ittifak antlaşması","B",
 "Sovyetler Birliği, İtilaf Devletleri'ne karşı TBMM'yi desteklemiş; 1921'de Moskova Antlaşması imzalanmış ve Sovyetler Millî Mücadele'ye destek sağlamıştır."),

(U6,"Milletler Cemiyeti ve Hatay",2021,"Zor",
 "Türkiye'nin Hatay'ı anavatana katma sürecinde izlediği yol aşağıdakilerden hangisidir?",
 "Askeri işgal","Diplomatik müzakereler, Milletler Cemiyeti çerçevesi ve nihayet özgür Hatay halkının oyu",
 "Fransa'ya savaş açma","Sovyetlerin arabuluculuğu","B",
 "Türkiye, Hatay meselesini önce Fransa ile müzakereler ve Milletler Cemiyeti kanalıyla ele almış; 1939'da yapılan referandumla Hatay halkı Türkiye'ye katılmayı seçmiştir."),

(U6,"Boğazlar Meselesi – Lozan",2018,"Orta",
 "Lozan Antlaşması'nda Boğazlar için öngörülen düzenleme neydi?",
 "Boğazlar Türkiye'nin tam denetiminde bırakılmıştır.","Boğazlar uluslararası bir komisyonun denetimine bırakılmış; Türkiye asker konuşlandıramayacaktır.",
 "Boğazlar kapatılmıştır.","Boğazlar İngiltere'ye devredilmiştir.","B",
 "Lozan'da Boğazlar, askersizleştirilmiş ve uluslararası Boğazlar Komisyonu'nun yönetimine bırakılmıştır. Bu durum Montrö (1936) ile düzeltilmiştir."),

(U6,"İtalya'nın Tehdidi",2023,"Zor",
 "1930'larda büyüyen İtalyan yayılmacılığı karşısında Türkiye'nin temel dış politika refleksi ne olmuştur?",
 "İtalya ile ittifak arayışı","Bölgesel paktlar (Balkan ve Sadabat) oluşturarak kolektif güvenlik anlayışına sarılmak",
 "Almanya ile ittifak kurmak","Tarafsızlık politikasını terk etmek","B",
 "Türkiye, İtalya'nın Akdeniz'deki yayılmacı emellerine karşı hem Balkan Antantı hem de Sadabat Paktı çerçevesinde kolektif güvenlik anlayışını benimsemiştir."),

(U6,"Cumhuriyetin Dış Tanınırlığı",2016,"Orta",
 "Türkiye Cumhuriyeti'nin uluslararası alanda tam olarak tanınmasını sağlayan antlaşma hangisidir?",
 "Gümrü Antlaşması","Kars Antlaşması","Ankara Antlaşması","Lozan Barış Antlaşması","D",
 "24 Temmuz 1923'te imzalanan Lozan Barış Antlaşması, Türkiye Cumhuriyeti'nin uluslararası toplum tarafından resmen tanınmasını sağlamıştır."),
]

# ─── Yardımcı fonksiyon ───────────────────────────────
def make_q(idx, row):
    un, ko, yi, zo, so, a, b, c, d, dc, ac = row
    return {
        "id": idx,
        "unite": un,
        "konu": ko,
        "yil": yi,
        "zorluk": zo,
        "soru": so,
        "siklar": {"A": a, "B": b, "C": c, "D": d},
        "dogru_cevap": dc,
        "aciklama": ac,
    }

# ─── Mevcut soruları yükle ───────────────────────────
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sorular.json")
with open(path, "r", encoding="utf-8") as f:
    existing = json.load(f)

# Mevcut ünite isimlerini yeni adlandırmaya normalize et
UNITE_MAP = {
    "Ünite 1 – Bir Kahraman Doğuyor":                 U1,
    "Ünite 2 – Millî Uyanış":                         U2,
    "Ünite 3 – Ya İstiklal Ya Ölüm":                  U3,
    "Ünite 4 – Atatürkçülük":                          U4,
    "Ünite 5 – Demokratikleşme Çabaları":              U5,
    "Ünite 6 – Atatürk Dönemi Türk Dış Politikası":   U6,
    "Ünite 7 – Atatürk'ün Ölümü ve Sonrası":          U5,  # U5 ile birleştir
    U1: U1, U2: U2, U3: U3, U4: U4, U5: U5, U6: U6,
}
for q in existing:
    q["unite"] = UNITE_MAP.get(q["unite"], q["unite"])

# Yeni soruları oluştur
new_qs = [make_q(len(existing) + i + 1, row) for i, row in enumerate(RAW)]

# Birleştir ve kaydet
all_qs = existing + new_qs
# ID'leri sıfırdan ver
for i, q in enumerate(all_qs, 1):
    q["id"] = i

with open(path, "w", encoding="utf-8") as f:
    json.dump(all_qs, f, ensure_ascii=False, indent=2)

print(f"Toplam soru sayısı: {len(all_qs)}")
from collections import Counter
unite_counts = Counter(q["unite"] for q in all_qs)
for unite, cnt in sorted(unite_counts.items()):
    print(f"  {unite}: {cnt} soru")
