"""8. sınıf batch JSON dosyalarını birleştirip sorular_8.json oluşturur."""
import json, os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PARTS_DIR = os.path.join(PROJECT_ROOT, "data", "parts")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
all_q = []

for part in ["sorular_8_a.json", "sorular_8_b.json", "sorular_8_c.json", "sorular_8_d.json"]:
    path = os.path.join(PARTS_DIR, part)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        all_q.extend(data)
        print(f"  {part}: {len(data)} soru")

U1 = "Ünite 1 – Bir Kahraman Doğuyor"
U2 = "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3 = "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4 = "Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5 = "Ünite 5 – Demokratikleşme Çabaları"
U6 = "Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

ek = [
    {"unite": U1, "konu": "Atatürk'ün Çocukluk ve Öğrenim Hayatı", "yil": 2024, "zorluk": "Zor",
     "soru": "Mustafa Kemal'in eğitim hayatı ve askeri kariyeri;\nI. Disiplinli eğitim\nII. Çok yönlü bilgi birikimi\nIII. Siyasi farkındalık\n\nBunlar Kurtuluş Savaşı liderliğine nasıl katkı sağlamıştır?",
     "siklar": {"A": "Hiç katkı sağlamamış", "B": "Askeri strateji, diplomasi ve halk yönetiminde kapsamlı yetkinlik kazandırmış", "C": "Sadece askeri beceri kazandırmış", "D": "Sadece siyasi beceri kazandırmış"},
     "dogru_cevap": "B", "aciklama": "Eğitimi Mustafa Kemal'e askeri strateji, diplomasi ve halk yönetiminde kapsamlı yetkinlik kazandırmıştır."},
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2024, "zorluk": "Orta",
     "soru": "Kanal Cephesi'nde Osmanlı Süveyş Kanalı'nı ele geçirmeye çalışmış ancak başarısız olmuştur.\n\nBu cephenin açılma amacı hangisidir?",
     "siklar": {"A": "Mısır'ı fethetmek", "B": "İngiltere'nin sömürgeleriyle bağlantısını kesmek", "C": "Fransa'yı yenmek", "D": "Rusya'yı desteklemek"},
     "dogru_cevap": "B", "aciklama": "Kanal Cephesi İngiltere'nin Hindistan yolunu ve sömürge bağlantısını kesmeyi hedeflemiştir."},
    {"unite": U1, "konu": "Osmanlı'nın Son Döneminde Yaşanan Gelişmeler", "yil": 2022, "zorluk": "Orta",
     "soru": "İttihat ve Terakki Cemiyeti;\nI. II. Meşrutiyet'in ilanında etkili\nII. I. Dünya Savaşı'na girişte belirleyici\nIII. Osmanlı'nın son dönemine damgasını vurmuş\n\nİttihat ve Terakki'nin en tartışmalı kararı hangisidir?",
     "siklar": {"A": "Meşrutiyet ilanı", "B": "Osmanlı'yı I. Dünya Savaşı'na sokmak", "C": "Meclis açmak", "D": "Basın özgürlüğü"},
     "dogru_cevap": "B", "aciklama": "Osmanlı'yı I. Dünya Savaşı'na sokmak İttihat ve Terakki'nin en tartışmalı kararıdır."},
    {"unite": U2, "konu": "İşgaller ve Tepkiler", "yil": 2024, "zorluk": "Zor",
     "soru": "Zararlı cemiyetler;\nI. Mavri Mira → İstanbul ve Batı Trakya'yı Yunanistan'a katmak\nII. Pontus Rum → Karadeniz'de Rum devleti kurmak\nIII. Hınçak-Taşnaksutyun → Doğu'da Ermeni devleti kurmak\n\nBu cemiyetlerin ortak özelliği hangisidir?",
     "siklar": {"A": "Osmanlı'yı desteklemek", "B": "Osmanlı topraklarını parçalayarak bağımsız devletler kurmak", "C": "Barış istemek", "D": "TBMM'yi desteklemek"},
     "dogru_cevap": "B", "aciklama": "Zararlı cemiyetler Osmanlı topraklarını parçalayarak kendi devletlerini kurmayı amaçlamıştır."},
    {"unite": U2, "konu": "TBMM'nin Açılması", "yil": 2023, "zorluk": "Orta",
     "soru": "TBMM'nin ilk icraatları;\nI. İstiklal Mahkemeleri kurulmuş\nII. İç isyanlar bastırılmış\nIII. Düzenli ordu oluşturulmuş\n\nBu icraatların amacı hangisidir?",
     "siklar": {"A": "Savaştan kaçmak", "B": "TBMM otoritesini güçlendirmek ve millî birliği sağlamak", "C": "Padişahı desteklemek", "D": "Barış yapmak"},
     "dogru_cevap": "B", "aciklama": "TBMM ilk icraatlarıyla otoritesini güçlendirmiş ve millî birliği sağlamıştır."},
    {"unite": U2, "konu": "Kongreler ve Amasya Genelgesi", "yil": 2022, "zorluk": "Zor",
     "soru": "Erzurum ve Sivas Kongreleri karşılaştırması;\nErzurum: Bölgesel toplanış, ulusal kararlar\nSivas: Ulusal toplanış, ulusal kararlar\n\nBu iki kongrenin birlikte değerlendirilmesinin sonucu hangisidir?",
     "siklar": {"A": "Farklı hedefler", "B": "Bölgesel mücadelenin ulusal mücadeleye dönüştüğünü göstermesi", "C": "Çelişkili kararlar", "D": "İşgallerin kabul edilmesi"},
     "dogru_cevap": "B", "aciklama": "Erzurum ve Sivas kongrelerinin süreci bölgesel mücadelenin ulusal mücadeleye dönüşümünü gösterir."},
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2024, "zorluk": "Zor",
     "soru": "Kurtuluş Savaşı'nın aşamaları;\nI. Savunma: İnönü Savaşları\nII. Taarruz: Büyük Taarruz\nIII. Takip: Düşmanın İzmir'e kadar kovalanması\n\nBu aşamaların doğru sıralaması hangisini gösterir?",
     "siklar": {"A": "Rastgele savaşlar", "B": "Planlı, aşamalı bir askeri strateji uygulandığını", "C": "Savunmanın gereksiz olduğunu", "D": "Taarruzun tek önemli adım olduğunu"},
     "dogru_cevap": "B", "aciklama": "Savunma→Taarruz→Takip sıralaması planlı ve aşamalı askeri stratejiyi gösterir."},
    {"unite": U3, "konu": "Mudanya Ateşkesi ve Lozan", "yil": 2023, "zorluk": "Orta",
     "soru": "1 Kasım 1922'de saltanat kaldırılmıştır. Vahdettin İstanbul'u terk etmiştir.\n\nSaltanatın kaldırılmasının anlamı hangisidir?",
     "siklar": {"A": "Padişahlığın güçlenmesi", "B": "Monarşinin sona ermesi ve millî egemenliğe tam geçiş", "C": "İstanbul'un boşaltılması", "D": "Savaşın bitmesi"},
     "dogru_cevap": "B", "aciklama": "Saltanatın kaldırılması monarşiyi sonlandırarak millî egemenliğe tam geçişi sağlamıştır."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2024, "zorluk": "Orta",
     "soru": "Atatürk'ün eğitim alanında yaptığı inkılâplar;\nI. Tevhid-i Tedrisat (eğitim birliği)\nII. Harf İnkılabı (Latin harfleri)\nIII. Millet Mektepleri (yetişkin eğitimi)\nIV. Üniversite reformu\n\nBu inkılâpların ortak hedefi hangisidir?",
     "siklar": {"A": "Eğitimi kısıtlamak", "B": "Çağdaş, laik ve herkese açık bir eğitim sistemi kurmak", "C": "Sadece zenginlere eğitim vermek", "D": "Askeri eğitim sağlamak"},
     "dogru_cevap": "B", "aciklama": "Eğitim inkılâpları çağdaş, laik ve herkese açık eğitim sistemi kurmayı hedeflemiştir."},
    {"unite": U4, "konu": "Cumhuriyetin İlanı", "yil": 2023, "zorluk": "Zor",
     "soru": "Cumhuriyetin temel nitelikleri;\nI. Millî egemenlik\nII. Laiklik\nIII. Hukukun üstünlüğü\nIV. Demokratik yönetim\n\n1923'ten bugüne bu niteliklerin önemi hangisidir?",
     "siklar": {"A": "Sadece tarihî değer", "B": "Türkiye Cumhuriyeti'nin değişmez, koruyucu temel ilkeleri olması", "C": "Geçici kurallar", "D": "Yalnızca sembolik anlam"},
     "dogru_cevap": "B", "aciklama": "Bu nitelikler Cumhuriyet'in değişmez, koruyucu temel ilkeleridir."},
    {"unite": U5, "konu": "1946 ve Sonrası Demokratikleşme", "yil": 2024, "zorluk": "Orta",
     "soru": "Türkiye'de;\n- 1945: Çok partili hayata geçiş kararı\n- 1946: DP kurulması\n- 1950: İktidar değişimi\n\nBu süreç hangisinin göstergesidir?",
     "siklar": {"A": "Tek parti döneminin devamı", "B": "Demokratik olgunlaşma ve barışçıl iktidar değişimi", "C": "Askeri müdahale", "D": "Dış baskı sonucu değişim"},
     "dogru_cevap": "B", "aciklama": "1945-1950 süreci demokratik olgunlaşma ve barışçıl iktidar değişiminin göstergesidir."},
    {"unite": U5, "konu": "Çok Partili Hayata Geçiş Denemeleri", "yil": 2022, "zorluk": "Zor",
     "soru": "Menemen Olayı (1930);\n- İnkılâp karşıtı bir isyan girişimi\n- Asteğmen Kubilay şehit edilmiş\n\nBu olayın Cumhuriyet tarihi açısından önemi hangisidir?",
     "siklar": {"A": "Önemsiz bir olay", "B": "İnkılâplara yönelik tehditlerin devam ettiğini ve korunması gerektiğini göstermesi", "C": "Demokrasinin güçlendiğini", "D": "Ordunun zayıfladığını"},
     "dogru_cevap": "B", "aciklama": "Menemen Olayı inkılâplara yönelik tehditlerin ciddiyetini ve korunması gerektiğini göstermiştir."},
    {"unite": U6, "konu": "Atatürk Dönemi Dış Politika İlkeleri", "yil": 2022, "zorluk": "Orta",
     "soru": "Atatürk döneminde dış borçların düzenli ödenmesi;\n\nBu tutum hangisini gösterir?",
     "siklar": {"A": "Ekonomik zayıflığı", "B": "Uluslararası alanda güvenilirlik ve onurlu duruşu", "C": "Dışa bağımlılığı", "D": "İflası"},
     "dogru_cevap": "B", "aciklama": "Dış borçların düzenli ödenmesi uluslararası güvenilirlik ve onurlu duruşun göstergesidir."},
    {"unite": U6, "konu": "Hatay Sorunu", "yil": 2022, "zorluk": "Zor",
     "soru": "Atatürk Hatay konusunda;\n'40 asırlık Türk yurdu düşman eline bırakılamaz' demiştir.\n\nBu söz hangisini ifade eder?",
     "siklar": {"A": "Savaş tehdidini", "B": "Hatay'ın Türk toprağı olduğu konusundaki kararlılığını", "C": "Fransa ile barış isteğini", "D": "Hatay'dan vazgeçmeyi"},
     "dogru_cevap": "B", "aciklama": "Bu söz Atatürk'ün Hatay'ın Türk vatanı olduğu konusundaki kararlılığını gösterir."},
    {"unite": U1, "konu": "I. Dünya Savaşı", "yil": 2021, "zorluk": "Orta",
     "soru": "Çanakkale Savaşı'nda;\nI. Deniz Savaşı (18 Mart 1915)\nII. Kara Savaşı (25 Nisan - 9 Ocak)\naşamaları yaşanmıştır.\n\n18 Mart Deniz Zaferi'nin önemi hangisidir?",
     "siklar": {"A": "Savaşın bitmesi", "B": "İtilaf donanmasının Boğaz'dan geçememesi ve Türk savunmasının başarısı", "C": "Osmanlı'nın deniz gücünün artması", "D": "Barış yapılması"},
     "dogru_cevap": "B", "aciklama": "18 Mart İtilaf donanmasını durdurarak Türk deniz savunmasının zaferini temsil eder."},
    {"unite": U2, "konu": "İşgaller ve Tepkiler", "yil": 2021, "zorluk": "Zor",
     "soru": "Millî cemiyetler;\nI. Trakya-Paşaeli\nII. İzmir Müdafaa-i Hukuk-ı Osmaniye\nIII. Doğu Anadolu Müdafaa-i Hukuk\nIV. Kilikyalılar\n\nBu cemiyetlerin Sivas Kongresi'yle birleştirilmesinin nedeni hangisidir?",
     "siklar": {"A": "Gereksiz olmaları", "B": "Dağınık mücadelenin tek merkezden yönetilmesini sağlamak", "C": "Padişahın emri", "D": "İtilaf devletlerinin isteği"},
     "dogru_cevap": "B", "aciklama": "Cemiyetlerin birleştirilmesi dağınık mücadeleyi tek merkezden yönetmeyi amaçlamıştır."},
    {"unite": U3, "konu": "Güney ve Doğu Cepheleri", "yil": 2021, "zorluk": "Orta",
     "soru": "Maraş'ta Sütçü İmam'ın direnişi;\n- Fransız askerinin bir Türk kadınının peçesini açmaya çalışmasına karşı ateş açmış\n\nBu olay hangisini simgeler?",
     "siklar": {"A": "Bireysel şiddeti", "B": "Millî onurun korunması ve halkın işgale karşı direniş ruhunu", "C": "Askeri müdahaleyi", "D": "Barış isteğini"},
     "dogru_cevap": "B", "aciklama": "Sütçü İmam'ın direnişi millî onurun korunması ve halkın direniş ruhunu simgeler."},
    {"unite": U4, "konu": "İnkılaplar", "yil": 2021, "zorluk": "Orta",
     "soru": "Kadın hakları kronolojisi;\n- 1930: Belediye seçimlerinde seçme\n- 1934: Milletvekili seçme ve seçilme\n\nTürkiye bu hakları İsviçre (1971), Fransa (1944), İtalya (1945)'den önce vermiştir. Bu ne anlama gelir?",
     "siklar": {"A": "Avrupa'nın geri olduğunu", "B": "Atatürk inkılâplarının kadın hakları konusunda dünyaya öncülük ettiğini", "C": "Kadın haklarının önemsiz olduğunu", "D": "Türkiye'nin Avrupa'dan koptuğunu"},
     "dogru_cevap": "B", "aciklama": "Atatürk inkılâpları kadın hakları konusunda birçok Avrupa ülkesine öncülük etmiştir."},
    {"unite": U5, "konu": "Askeri Müdahaleler ve Demokrasi", "yil": 2021, "zorluk": "Orta",
     "soru": "28 Şubat 1997 süreci;\n- Postmodern darbe olarak nitelenir\n- Askerler doğrudan yönetimi almamış ama siyasi baskı yapmış\n\nBu sürecin demokrasiye etkisi hangisidir?",
     "siklar": {"A": "Demokrasinin güçlenmesi", "B": "Sivil iradenin askeri baskıyla sınırlandırılması", "C": "Barışın sağlanması", "D": "Ekonominin büyümesi"},
     "dogru_cevap": "B", "aciklama": "28 Şubat sivil iradenin askeri baskıyla sınırlandırıldığı postmodern bir müdahaleydi."},
    {"unite": U6, "konu": "Balkan ve Sadabat Paktları", "yil": 2021, "zorluk": "Orta",
     "soru": "Atatürk dönemindeki paktların II. Dünya Savaşı'nda etkisizleşmesi;\n- Balkan ve Sadabat ülkelerinin savaşta farklı taraflarda yer alması\n\nBu durum hangisini gösterir?",
     "siklar": {"A": "Paktların başarısız olduğunu", "B": "Bölgesel ittifakların küresel çatışmalar karşısında sürdürülmesinin zorluğunu", "C": "Atatürk'ün hatalı olduğunu", "D": "Savaşın gereksiz olduğunu"},
     "dogru_cevap": "B", "aciklama": "Bu durum bölgesel ittifakların küresel çatışmalarda sürdürülme zorluğunu gösterir."},
    {"unite": U1, "konu": "Mustafa Kemal'in Askerlik Hayatı", "yil": 2021, "zorluk": "Zor",
     "soru": "Mustafa Kemal'in askeri hayatı boyunca görev yaptığı cepheler;\nI. Trablusgarap → İlk savaş deneyimi\nII. Balkan → Toprak kayıplarının etkisi\nIII. Çanakkale → Dünyaya tanınma\nIV. Kafkas → Doğu cephe deneyimi\nV. Suriye → Son cephe görevi\n\nBu deneyimlerin toplamı hangisini sağlamıştır?",
     "siklar": {"A": "Sadece askeri bilgi", "B": "Geniş coğrafya bilgisi, farklı savaş taktikleri ve stratejik liderlik yetkinliği", "C": "Yorgunluk", "D": "Siyasi bir kariyer"},
     "dogru_cevap": "B", "aciklama": "Farklı cepheler coğrafi bilgi, taktik çeşitliliği ve stratejik liderlik yetkinliği kazandırmıştır."},
    {"unite": U3, "konu": "Batı Cephesi Savaşları", "yil": 2022, "zorluk": "Zor",
     "soru": "İstiklal Marşı 12 Mart 1921'de TBMM tarafından kabul edilmiştir.\n\nİstiklal Marşı'nın savaş döneminde kabulünün önemi hangisidir?",
     "siklar": {"A": "Edebiyat geliştirmek", "B": "Millî birlik ve bağımsızlık ruhunu güçlendirerek morali yükseltmek", "C": "Müzik eğitimi vermek", "D": "Dış politikayı güçlendirmek"},
     "dogru_cevap": "B", "aciklama": "İstiklal Marşı millî birlik ve bağımsızlık ruhunu güçlendirerek savaş moralini yükseltmiştir."},
    {"unite": U4, "konu": "Atatürk İlkeleri", "yil": 2021, "zorluk": "Zor",
     "soru": "Cumhuriyetçilik ilkesi;\n- Devlet başkanı seçimle belirlenir\n- Egemenlik millete aittir\n- Hükümet halka karşı sorumludur\n\nCumhuriyetçilik hangi yönetim biçimine karşıt olarak gelişmiştir?",
     "siklar": {"A": "Demokrasiye", "B": "Monarşi ve saltanata", "C": "Federal sisteme", "D": "Başkanlık sistemine"},
     "dogru_cevap": "B", "aciklama": "Cumhuriyetçilik monarşi ve saltanata karşıt olarak milletin egemenliğini savunur."},
]
all_q.extend(ek)

out = os.path.join(DATA_DIR, "sorular_8.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(all_q, f, ensure_ascii=False, indent=2)
print(f"\n8. Sınıf TOPLAM: {len(all_q)} soru -> sorular_8.json")

units = {}
for q in all_q:
    u = q["unite"]
    units[u] = units.get(u, 0) + 1
for u, c in sorted(units.items()):
    print(f"  {u}: {c} soru")
