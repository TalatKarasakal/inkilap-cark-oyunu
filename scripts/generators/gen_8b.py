import json, os

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

questions = [
    # Ünite 1 ek
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2024, "zorluk": "Zor",
     "soru": "I. Dünya Savaşı'nda;\nI. İttifak: Almanya, Avusturya-Macaristan, Osmanlı, Bulgaristan\nII. İtilaf: İngiltere, Fransa, Rusya, İtalya\n\nOsmanlı'nın İttifak'ta yer almasının nedeni hangisidir?",
     "siklar": {"A": "Rakipleriyle aynı safta olmak", "B": "İngiltere ve Fransa'nın Osmanlı'yı reddetmesi ve Almanya ile yakın ilişkiler", "C": "Rusya'yla ittifak kurmak", "D": "Tarafsız kalmak istememesi"},
     "dogru_cevap": "B", "aciklama": "İtilaf devletlerinin reddi ve Alman yakınlığı Osmanlı'yı İttifak safına çekmiştir."},
    {"unite": U1, "konu": "Osmanlı'nın Son Döneminde Yaşanan Gelişmeler", "yil": 2024, "zorluk": "Orta",
     "soru": "Trablusgarp Savaşı (1911-1912) Osmanlı'nın son Afrika topraklarının kaybedilmesiyle sonuçlanmıştır.\n\nBu savaş hangisiyle doğrudan ilişkilidir?",
     "siklar": {"A": "Osmanlı'nın güçlenmesiyle", "B": "İtalya'nın sömürgecilik politikasıyla", "C": "Balkan Savaşları'yla", "D": "I. Dünya Savaşı'yla"},
     "dogru_cevap": "B", "aciklama": "İtalya sömürge elde etmek amacıyla Osmanlı'nın Afrika topraklarına saldırmıştır."},
    {"unite": U1, "konu": "Mustafa Kemal'in Askerlik Hayatı", "yil": 2023, "zorluk": "Zor",
     "soru": "Mustafa Kemal;\nI. Selanik'te Vatan ve Hürriyet Cemiyeti'ni kurmuş\nII. İttihat ve Terakki ile ilişki kurmuş\nIII. 'Ordu siyasete karışmamalıdır' görüşünü savunmuş\n\nBu bilgiler Mustafa Kemal hakkında hangisini gösterir?",
     "siklar": {"A": "Sadece asker olduğunu", "B": "Siyasi bilinçli ama ordunun siyasetten uzak kalmasını savunan bir lider olduğunu", "C": "Siyasetle ilgilenmediğini", "D": "Osmanlı'yı desteklediğini"},
     "dogru_cevap": "B", "aciklama": "Mustafa Kemal siyasi bilinçli ama ordunun siyasetten uzak kalmasını savunmuştur."},
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2022, "zorluk": "Orta",
     "soru": "Wilson İlkeleri'nin Osmanlı'yı ilgilendiren maddesi;\n- 'Osmanlı'daki Türk kısmına güvenli egemenlik, diğer milletlere özerk gelişme imkânı'\n\nBu madde hangisinin habercisidir?",
     "siklar": {"A": "Osmanlı'nın güçlenmesinin", "B": "Osmanlı topraklarının paylaşılacağının", "C": "Türkiye'nin kurulacağının", "D": "Savaşın biteceğinin"},
     "dogru_cevap": "B", "aciklama": "Wilson İlkeleri'ndeki bu madde Osmanlı topraklarının paylaşılacağının işaretidir."},

    # Ünite 2 ek
    {"unite": U2, "konu": "Kongreler ve Amasya Genelgesi", "yil": 2024, "zorluk": "Orta",
     "soru": "Mustafa Kemal'in Amasya Genelgesi'nde;\n- Her yerin en güvenilir ve vatansever insanlarının seçilerek Sivas'a gönderilmesini istemiştir\n\nBu talep hangisine temel oluşturmuştur?",
     "siklar": {"A": "Padişahın güçlenmesine", "B": "Millî iradeye dayalı yeni bir yönetim anlayışına", "C": "İşgallerin kabul edilmesine", "D": "Osmanlı ordusunun güçlenmesine"},
     "dogru_cevap": "B", "aciklama": "Halk temsilcilerinin toplanması millî iradeye dayalı yönetim anlayışının temelini oluşturmuştur."},
    {"unite": U2, "konu": "TBMM'nin Açılması", "yil": 2024, "zorluk": "Zor",
     "soru": "TBMM açıldığında;\nI. Yasama, yürütme ve yargı yetkilerini üzerine almış\nII. Güçler birliği ilkesi uygulanmış\nIII. Meclis hükümeti sistemi kurulmuş\n\nTBMM'nin bu geniş yetkilere ihtiyaç duymasının nedeni hangisidir?",
     "siklar": {"A": "Demokrasiyi güçlendirmek", "B": "Savaş koşullarında hızlı ve etkili karar almak", "C": "Padişahı desteklemek", "D": "Avrupa'yı taklit etmek"},
     "dogru_cevap": "B", "aciklama": "Savaş koşulları hızlı karar almayı gerektirdiğinden TBMM tüm yetkileri üzerine almıştır."},
    {"unite": U2, "konu": "İşgaller ve Tepkiler", "yil": 2023, "zorluk": "Orta",
     "soru": "Millî Mücadele döneminde kurulan cemiyetler;\nI. Müdafaa-i Hukuk cemiyetleri (bölgesel savunma)\nII. Reddi İlhak Cemiyeti (İzmir)\nIII. Kilikyalılar Cemiyeti (Adana)\n\nBu cemiyetlerin ortak amacı hangisidir?",
     "siklar": {"A": "Osmanlı'yı yıkmak", "B": "Yerel halkın işgallere karşı örgütlenerek direnmesi", "C": "Padişaha destek vermek", "D": "İtilaf devletleriyle anlaşmak"},
     "dogru_cevap": "B", "aciklama": "Cemiyetler yerel halkın işgallere karşı örgütlenmesini sağlamıştır."},
    {"unite": U2, "konu": "Kuvâ-yı Milliye", "yil": 2023, "zorluk": "Zor",
     "soru": "Kuvâ-yı Milliye'nin özellikleri;\nI. Düzensiz milis güçleri\nII. Bölgesel kahramanlar: Yörük Ali Efe, Demirci Mehmet Efe\nIII. İşgalcilere karşı ilk direniş\nIV. TBMM'ye bağlı düzenli ordu\n\nYanlış olan hangisidir?",
     "siklar": {"A": "I", "B": "II", "C": "III", "D": "IV"},
     "dogru_cevap": "D", "aciklama": "Kuvâ-yı Milliye düzenli ordu değil, düzensiz milis güçleriydi."},
    {"unite": U2, "konu": "Kongreler ve Amasya Genelgesi", "yil": 2022, "zorluk": "Orta",
     "soru": "Misak-ı Millî kararları (28 Ocak 1920);\nI. Millî sınırlar içindeki vatan bölünmez bir bütündür\nII. Azınlık hakları korunacaktır\nIII. Kapitülasyonlar kabul edilemez\n\nMisak-ı Millî'nin önemi hangisidir?",
     "siklar": {"A": "Osmanlı'nın devam etmesi", "B": "Yeni Türk devletinin sınır ve egemenlik haklarını belirleyen ulusal ant", "C": "İşgallerin kabulü", "D": "Barış görüşmesi"},
     "dogru_cevap": "B", "aciklama": "Misak-ı Millî yeni Türk devletinin sınır ve egemenlik haklarını belirleyen ulusal anttır."},

    # Ünite 3 ek
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2024, "zorluk": "Orta",
     "soru": "II. İnönü Zaferi (1921) sonucu;\n- İsmet Paşa'nın prestiji artmış\n- TBMM'ye olan güven güçlenmiş\n\nBu zafer hangisini kanıtlamıştır?",
     "siklar": {"A": "Savaşın gereksiz olduğunu", "B": "Düzenli Türk ordusunun işgalcileri yenebilecek güçte olduğunu", "C": "Barışın sağlandığını", "D": "Yunanlıların güçlü olduğunu"},
     "dogru_cevap": "B", "aciklama": "II. İnönü düzenli ordunun işgalcileri yenebilecek güçte olduğunu kanıtlamıştır."},
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2023, "zorluk": "Zor",
     "soru": "Mustafa Kemal Sakarya Savaşı'ndan sonra;\nI. TBMM tarafından Gazilik unvanı verilmiş\nII. Mareşallik rütbesi verilmiş\nIII. Başkomutanlık yetkileri uzatılmış\n\nBu kararlar hangisini gösterir?",
     "siklar": {"A": "Savaşın kaybedildiğini", "B": "Mustafa Kemal'e olan güvenin zirveye ulaştığını", "C": "TBMM'nin zayıfladığını", "D": "Barışın sağlandığını"},
     "dogru_cevap": "B", "aciklama": "Gazilik, Mareşallik ve yetki uzatma Mustafa Kemal'e güvenin zirveye çıktığını gösterir."},
    {"unite": U3, "konu": "Mudanya Ateşkesi ve Lozan", "yil": 2023, "zorluk": "Orta",
     "soru": "Lozan Antlaşması'nda çözülemeyen konular;\nI. Musul sorunu\nII. Boğazlar rejimi\nIII. Batı Trakya\n\nBu sorunlar sonradan nasıl çözülmüştür?",
     "siklar": {"A": "Savaşla", "B": "Diplomatik görüşmeler ve uluslararası antlaşmalarla", "C": "BM müdahalesiyle", "D": "Çözülmemiştir"},
     "dogru_cevap": "B", "aciklama": "Lozan'da çözülemeyen sorunlar sonradan diplomatik yollarla çözülmüştür."},
    {"unite": U3, "konu": "Güney ve Doğu Cepheleri", "yil": 2023, "zorluk": "Orta",
     "soru": "Ankara Antlaşması (1921) ile Fransa;\nI. Güney cephesinden çekilmiş\nII. TBMM'yi tanımış\nIII. Hatay hariç güney sınırı belirlenmiş\n\nBu antlaşmanın önemi hangisidir?",
     "siklar": {"A": "Savaşın uzaması", "B": "İtilaf bloğunda ilk çatlağın oluşması ve TBMM'nin uluslararası tanınması", "C": "Fransa'nın güçlenmesi", "D": "İşgalin devam etmesi"},
     "dogru_cevap": "B", "aciklama": "Ankara Antlaşması İtilaf bloğunda çatlak oluşturmuş ve TBMM'yi uluslararası alanda tanıtmıştır."},

    # Ünite 4 ek
    {"unite": U4, "konu": "Cumhuriyetin İlanı", "yil": 2024, "zorluk": "Orta",
     "soru": "Cumhuriyet'in ilanıyla;\n- Osmanlı hanedanına son verilmiş\n- Devlet başkanı seçimle belirlenmiş\n- Millî egemenlik ilkesi somutlaşmış\n\nBu değişimler neyi temsil eder?",
     "siklar": {"A": "Monarşiden cumhuriyete geçişi", "B": "İmparatorluğun güçlenmesini", "C": "Padişahlığın devam etmesini", "D": "Dini yönetimin güçlenmesini"},
     "dogru_cevap": "A", "aciklama": "Cumhuriyet'in ilanı monarşiden halk egemenliğine geçişi temsil eder."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2024, "zorluk": "Zor",
     "soru": "Atatürk inkılâplarının alanları;\nI. Siyasi: Cumhuriyet, laiklik\nII. Hukuki: Medeni Kanun, hukuk birliği\nIII. Eğitim: Tevhid-i Tedrisat, Harf İnkılabı\nIV. Ekonomik: Devletçilik, planlı kalkınma\nV. Toplumsal: Kılık kıyafet, takvim, ölçü\n\nBu inkılâpların ortak amacı hangisidir?",
     "siklar": {"A": "Osmanlı'yı yıkmak", "B": "Türkiye'yi her alanda çağdaş uygarlık düzeyine çıkarmak", "C": "Batı'yı taklit etmek", "D": "Dini ortadan kaldırmak"},
     "dogru_cevap": "B", "aciklama": "Tüm inkılâplar Türkiye'yi her alanda çağdaş uygarlık düzeyine çıkarmayı hedeflemiştir."},
    {"unite": U4, "konu": "Atatürk İlkeleri", "yil": 2024, "zorluk": "Orta",
     "soru": "Laiklik ilkesi;\nI. Din ve devlet işlerinin ayrılması\nII. Vicdan ve ibadet özgürlüğü\nIII. Dinin siyasi araç olarak kullanılmaması\n\nLaikliğin amacı hangisidir?",
     "siklar": {"A": "Dini yasaklamak", "B": "Din ve devlet işlerini ayırarak din ve vicdan özgürlüğünü güvence altına almak", "C": "Tek din belirlemek", "D": "Dini güçlendirmek"},
     "dogru_cevap": "B", "aciklama": "Laiklik din-devlet ayrımıyla din ve vicdan özgürlüğünü güvence altına alır."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2023, "zorluk": "Orta",
     "soru": "1 Kasım 1928'de Millet Mektepleri açılmıştır.\n\nMillet Mekteplerinin amacı hangisidir?",
     "siklar": {"A": "Sadece çocuklara eğitim vermek", "B": "Yeni Türk harflerini halka öğretmek ve okuryazarlık oranını artırmak", "C": "Üniversiteleri kapatmak", "D": "Dini eğitim vermek"},
     "dogru_cevap": "B", "aciklama": "Millet Mektepleri yeni harfleri halka öğretmek ve okuryazarlığı artırmak amacıyla kurulmuştur."},
    {"unite": U4, "konu": "Atatürk İlkeleri", "yil": 2023, "zorluk": "Zor",
     "soru": "Halkçılık ilkesi;\nI. Kanun önünde eşitlik\nII. Ayrıcalıklı sınıf yok\nIII. Halkın kamu hizmetlerinden eşit yararlanması\n\nHalkçılığın demokratik topluma katkısı hangisidir?",
     "siklar": {"A": "Sınıf ayrımı yapmak", "B": "Toplumsal eşitliği sağlayarak demokratik toplumun temelini oluşturmak", "C": "Sadece zenginlere hizmet etmek", "D": "Vergi muafiyeti sağlamak"},
     "dogru_cevap": "B", "aciklama": "Halkçılık toplumsal eşitliği sağlayarak demokratik toplumun temelini oluşturur."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2022, "zorluk": "Orta",
     "soru": "Türk Tarih Kurumu (1931) ve Türk Dil Kurumu (1932) kurulmuştur.\n\nBu kurumların ortak amacı hangisidir?",
     "siklar": {"A": "Siyasi parti kurmak", "B": "Türk tarihini ve Türk dilini araştırarak millî bilinç oluşturmak", "C": "Yabancı dilleri yasaklamak", "D": "Osmanlı tarihini silmek"},
     "dogru_cevap": "B", "aciklama": "TTK ve TDK Türk tarih ve dilini araştırarak millî bilinç oluşturmayı hedeflemiştir."},

    # Ünite 5 ek
    {"unite": U5, "konu": "Çok Partili Hayata Geçiş Denemeleri", "yil": 2024, "zorluk": "Orta",
     "soru": "Şeyh Sait İsyanı (1925);\nI. İnkılâp karşıtı ve bölücü nitelikte\nII. Takrir-i Sükûn Kanunu'nun çıkarılmasına neden olmuş\nIII. Terakkiperver Cumhuriyet Fırkası kapatılmış\n\nBu isyan hangisini gösterir?",
     "siklar": {"A": "Demokrasinin güçlendiğini", "B": "İnkılâplara karşı ciddi direniş olduğunu ve güvenlik önlemlerinin alınması gerektiğini", "C": "İsyanın başarılı olduğunu", "D": "Halkın memnuniyetini"},
     "dogru_cevap": "B", "aciklama": "Şeyh Sait İsyanı inkılâplara ciddi direniş olduğunu göstermiş ve güvenlik önlemleri alınmıştır."},
    {"unite": U5, "konu": "1946 ve Sonrası Demokratikleşme", "yil": 2023, "zorluk": "Zor",
     "soru": "1961 ve 1982 Anayasaları;\nI. Temel hak ve özgürlükler düzenlenmiş\nII. Yargı bağımsızlığı güçlendirilmiş\nIII. Askeri vesayet unsurları içermiş\n\nBu anayasaların ortak özelliği hangisidir?",
     "siklar": {"A": "Tamamen demokratik olması", "B": "Askeri müdahale sonrası hazırlanmış olmaları", "C": "Halk oyuyla hazırlanmaları", "D": "Tek parti dönemi ürünü olmaları"},
     "dogru_cevap": "B", "aciklama": "1961 ve 1982 anayasaları askeri müdahale sonrası hazırlanmıştır."},
    {"unite": U5, "konu": "1946 ve Sonrası Demokratikleşme", "yil": 2022, "zorluk": "Orta",
     "soru": "14 Mayıs 1950 seçimleri;\n- Demokrat Parti %53 oyla kazanmış\n- CHP barışçıl şekilde iktidarı devretmiş\n\nBu seçimin Türk demokrasi tarihindeki önemi hangisidir?",
     "siklar": {"A": "CHP'nin güçlenmesi", "B": "İktidar değişiminin seçim yoluyla ve barışçıl şekilde gerçekleşmesi", "C": "Tek parti döneminin devam etmesi", "D": "Askeri müdahale yapılması"},
     "dogru_cevap": "B", "aciklama": "1950 seçimleri iktidar değişiminin barışçıl ve seçimle olabileceğini kanıtlamıştır."},
    {"unite": U5, "konu": "Askeri Müdahaleler ve Demokrasi", "yil": 2023, "zorluk": "Orta",
     "soru": "27 Mayıs 1960 askeri müdahalesi;\n- Demokrat Parti kapatılmış\n- Menderes ve arkadaşları yargılanmış\n- 1961 Anayasası hazırlanmış\n\nBu müdahalenin Türk siyasi tarihine uzun vadeli etkisi hangisidir?",
     "siklar": {"A": "Demokrasinin güçlenmesi", "B": "Askeri müdahalelerin bir gelenek haline gelmesi riskinin oluşması", "C": "Ekonominin güçlenmesi", "D": "Barışın sağlanması"},
     "dogru_cevap": "B", "aciklama": "1960 darbesi askeri müdahalelerin tekrarlanma riskini artıran bir emsal oluşturmuştur."},

    # Ünite 6 ek
    {"unite": U6, "konu": "Atatürk Dönemi Dış Politika İlkeleri", "yil": 2024, "zorluk": "Orta",
     "soru": "Atatürk dış politikada;\n- Hukuka dayalı\n- Eşitliğe dayalı\n- Karşılıklı çıkarlara saygılı\nilişkiler kurmuştur.\n\nBu yaklaşım hangisini yansıtır?",
     "siklar": {"A": "Yayılmacılığı", "B": "Bağımsızlık ve onurlu dış politikayı", "C": "İçe kapanmayı", "D": "Sömürgeciliği"},
     "dogru_cevap": "B", "aciklama": "Hukuk, eşitlik ve karşılıklı saygıya dayalı yaklaşım bağımsız ve onurlu dış politikadır."},
    {"unite": U6, "konu": "Montrö Boğazlar Sözleşmesi", "yil": 2023, "zorluk": "Orta",
     "soru": "Montrö öncesi Boğazlar;\n- Uluslararası bir komisyon yönetiyordu\n- Türkiye'nin tam hakimiyeti yoktu\n\nMontrö'den sonra en önemli değişiklik hangisidir?",
     "siklar": {"A": "Boğazların kapatılması", "B": "Komisyonun kaldırılması ve Türkiye'nin Boğazlar üzerinde tam egemenlik kurması", "C": "Savaş gemilerinin serbest geçişi", "D": "Ticaretin durması"},
     "dogru_cevap": "B", "aciklama": "Montrö ile komisyon kaldırılmış ve Türkiye Boğazlarda tam egemenlik kurmuştur."},
    {"unite": U6, "konu": "Hatay Sorunu", "yil": 2023, "zorluk": "Orta",
     "soru": "Hatay sorununun çözüm süreci;\nI. Hatay Meclisi kurulmuş → Bağımsızlık ilan edilmiş → Türkiye'ye katılma kararı\n\nBu süreç hangisini gösterir?",
     "siklar": {"A": "Savaşla çözüm", "B": "Halkın iradesine dayalı demokratik çözüm", "C": "BM müdahalesi", "D": "Fransa'nın hediyesi"},
     "dogru_cevap": "B", "aciklama": "Hatay sorunu halk oylamasına dayalı demokratik bir süreçle çözülmüştür."},
    {"unite": U6, "konu": "Balkan ve Sadabat Paktları", "yil": 2022, "zorluk": "Zor",
     "soru": "Sadabat Paktı (1937);\n- Türkiye, İran, Irak, Afganistan arasında\n- Sınır güvenliği ve barışı koruma amaçlı\n\nBu paktın bölgesel önemi hangisidir?",
     "siklar": {"A": "Savaş hazırlığı", "B": "Ortadoğu'da barış ve istikrarı sağlamak için bölgesel iş birliği kurulması", "C": "Sömürgecilik", "D": "Avrupa ile ittifak"},
     "dogru_cevap": "B", "aciklama": "Sadabat Paktı Ortadoğu'da barış ve istikrar için bölgesel iş birliği kurmayı amaçlamıştır."},
    {"unite": U6, "konu": "Nüfus Mübadelesi", "yil": 2023, "zorluk": "Zor",
     "soru": "Nüfus mübadelesinin insani boyutu;\nI. Yüz binlerce insan yerinden olmuş\nII. Aile bağları kopmuş\nIII. Kültürel kayıplar yaşanmış\n\nMübadelenin zorluğuna rağmen yapılmasının nedeni hangisidir?",
     "siklar": {"A": "İnsanları cezalandırmak", "B": "Kalıcı barış için etnik sorunların köklü çözümünü sağlamak", "C": "Nüfusu azaltmak", "D": "Ekonomik kazanç sağlamak"},
     "dogru_cevap": "B", "aciklama": "Mübadele insani zorluğuna rağmen kalıcı barış için etnik sorunların köklü çözümünü amaçlamıştır."},
]

out = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "parts", "sorular_8_b.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)
print(f"8. Sınıf Batch B (LGS): {len(questions)} soru yazıldı")
