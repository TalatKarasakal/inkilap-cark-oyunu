"""8. sınıfa son 14 LGS sorusu ekler, dengeler, birleştirir, exe yapar."""
import json, os, random
random.seed(777)
BASE = os.path.dirname(os.path.abspath(__file__))
U1="Ünite 1 – Bir Kahraman Doğuyor"
U2="Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar"
U3="Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!"
U4="Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye"
U5="Ünite 5 – Demokratikleşme Çabaları"
U6="Ünite 6 – Atatürk Dönemi Türk Dış Politikası"

ek=[
 {"unite":U1,"konu":"I. Dünya Savaşı","yil":2024,"zorluk":"Zor",
  "soru":"Irak Cephesi'nde İngilizler Kut'ül Amare'de yenilmiş ancak sonunda Bağdat'ı ele geçirmiştir.\n\nKut'ül Amare Zaferi'nin önemi aşağıdakilerden hangisidir?",
  "siklar":{"A":"Irak'ın kurtarılması","B":"Osmanlı'nın I. Dünya Savaşı'ndaki önemli savunma başarılarından biri olması","C":"İngiltere'nin teslim olması","D":"Savaşın bitmesi"},
  "dogru_cevap":"B","aciklama":"Kut'ül Amare Osmanlı'nın I. Dünya Savaşı'ndaki önemli savunma zaferlerindendir."},
 {"unite":U1,"konu":"Mustafa Kemal","yil":2023,"zorluk":"Orta",
  "soru":"Mustafa Kemal Suriye Cephesi'nde Yıldırım Orduları komutanlığı yapmıştır.\n\nBu görev aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Savaştan kaçındığını","B":"I. Dünya Savaşı'nın son döneminde üst düzey komutanlık yetkisi aldığını","C":"Savaşa katılmadığını","D":"Sadece savunma yaptığını"},
  "dogru_cevap":"B","aciklama":"Yıldırım Orduları komutanlığı üst düzey askeri yetki göstergesidir."},
 {"unite":U2,"konu":"İşgaller","yil":2024,"zorluk":"Zor",
  "soru":"Bir öğrenci işgallerin haritasını incelemiş:\n- İngilizler: İstanbul, Musul, Antep\n- Fransızlar: Adana, Maraş, Urfa\n- İtalyanlar: Antalya, Konya\n- Yunanlılar: İzmir\n\nBu haritaya göre aşağıdakilerden hangisi söylenebilir?",
  "siklar":{"A":"İşgaller sınırlı alana yapılmıştır","B":"Anadolu'nun her bölgesi farklı devletlerce işgal edilmiştir","C":"Sadece kıyılar işgal edilmiştir","D":"İşgalciler iş birliği yapmamıştır"},
  "dogru_cevap":"B","aciklama":"Harita Anadolu'nun farklı bölgelerinin farklı devletlerce işgal edildiğini gösterir."},
 {"unite":U3,"konu":"Batı Cephesi","yil":2024,"zorluk":"Orta",
  "soru":"Büyük Taarruz öncesi Mustafa Kemal;\n- Güçlü bir ordu hazırlamış\n- Taarruz planını gizli tutmuş\n- Diplomatik ortamı hazırlamış\n\nBu hazırlıklar aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Askeri ve diplomatik hazırlığın birlikte yürütüldüğünü","B":"Sadece askeri güce güvenildiğini","C":"Barış arayışında olunduğunu","D":"Taarruzdan vazgeçildiğini"},
  "dogru_cevap":"A","aciklama":"Askeri hazırlık ve diplomatik ortamın birlikte hazırlanması kapsamlı stratejiyi gösterir."},
 {"unite":U3,"konu":"Lozan","yil":2023,"zorluk":"Zor",
  "soru":"Lozan'da;\nI. Kapitülasyonlar kaldırılmış\nII. Borçlar taksitlendirilmiş\nIII. Boğazlar komisyon yönetiminde kalmış\nIV. Sınırlar belirlenmiş\n\nLozan'da Türkiye'nin tam başarı sağlayamadığı konu hangisidir?",
  "siklar":{"A":"I","B":"II","C":"III","D":"IV"},
  "dogru_cevap":"C","aciklama":"Boğazlar Lozan'da komisyon yönetiminde kalmış, tam egemenlik ancak 1936 Montrö ile sağlanmıştır."},
 {"unite":U4,"konu":"İnkılaplar","yil":2024,"zorluk":"Orta",
  "soru":"Aşağıdaki inkılâplardan hangisi toplumsal alanda yapılan değişikliklerden biridir?",
  "siklar":{"A":"Cumhuriyet'in ilanı","B":"Şapka İnkılabı ve kılık kıyafet düzenlemesi","C":"Türk Medeni Kanunu","D":"TBMM'nin açılması"},
  "dogru_cevap":"B","aciklama":"Şapka İnkılabı ve kılık kıyafet düzenlemesi toplumsal alanda yapılan değişikliktir."},
 {"unite":U4,"konu":"Atatürk İlkeleri","yil":2023,"zorluk":"Zor",
  "soru":"Öğretmen sınıfa şu soruyu sormuştur:\n'Atatürk Nutuk'u neden yazmıştır?'\n\nBu sorunun en doğru cevabı aşağıdakilerden hangisidir?",
  "siklar":{"A":"Roman yazmak istemiş","B":"Millî Mücadele ve Cumhuriyet'in kuruluş sürecini gelecek nesillere aktarmak istemiş","C":"Siyasi rakiplerini eleştirmek istemiş","D":"Anılarını kaleme almak istemiş"},
  "dogru_cevap":"B","aciklama":"Nutuk Millî Mücadele ve Cumhuriyet'in kuruluşunu gelecek nesillere aktarmak için yazılmıştır."},
 {"unite":U5,"konu":"Demokratikleşme","yil":2024,"zorluk":"Orta",
  "soru":"Türkiye'de kadınlara verilen haklar:\n1930: Belediye seçimlerine katılma\n1933: Muhtar seçilme\n1934: Milletvekili seçilme\n\nBu kronolojik gelişme aşağıdakilerden hangisini gösterir?",
  "siklar":{"A":"Haklarının daraltıldığını","B":"Kadın haklerının aşamalı olarak genişletildiğini","C":"Tüm hakların aynı anda verildiğini","D":"Hakların geri alındığını"},
  "dogru_cevap":"B","aciklama":"Kronolojik sıralama kadın haklarının aşamalı genişletildiğini gösterir."},
 {"unite":U5,"konu":"Askeri Müdahaleler","yil":2023,"zorluk":"Zor",
  "soru":"Aşağıdaki anayasalar ve hazırlanış biçimleri eşleştirilmiştir:\n\n1921: TBMM tarafından\n1924: TBMM tarafından\n1961: Askeri müdahale sonrası\n1982: Askeri müdahale sonrası\n\nBu tabloya göre aşağıdakilerden hangisi söylenebilir?",
  "siklar":{"A":"Tüm anayasalar demokratik süreçte hazırlanmıştır","B":"Son iki anayasa askeri vesayet altında hazırlanmıştır","C":"Anayasalar hiç değişmemiştir","D":"1921 Anayasası en kapsamlısıdır"},
  "dogru_cevap":"B","aciklama":"1961 ve 1982 anayasaları askeri müdahale sonrası hazırlanmıştır."},
 {"unite":U6,"konu":"Dış Politika","yil":2024,"zorluk":"Orta",
  "soru":"Türkiye'nin Milletler Cemiyeti'ne 1932'de davet yoluyla katılması aşağıdakilerden hangisinin sonucudur?",
  "siklar":{"A":"Savaş tehdidinin","B":"Barışçıl dış politikanın uluslararası alanda güven oluşturmasının","C":"Dış baskının","D":"İç sorunların"},
  "dogru_cevap":"B","aciklama":"Davet yoluyla katılım barışçıl politikanın uluslararası güven oluşturduğunu gösterir."},
 {"unite":U2,"konu":"Kongreler","yil":2022,"zorluk":"Orta",
  "soru":"Sivas Kongresi'nde alınan 'Manda ve himaye kabul edilemez' kararı aşağıdakilerden hangisiyle ilgilidir?",
  "siklar":{"A":"Ekonomik bağımsızlıkla","B":"Tam bağımsızlık ilkesiyle","C":"Askeri güçle","D":"Eğitim reformuyla"},
  "dogru_cevap":"B","aciklama":"Manda ve himaye reddi tam bağımsızlık ilkesinin kararlı savunusudur."},
 {"unite":U4,"konu":"İnkılaplar","yil":2022,"zorluk":"Orta",
  "soru":"Aşar vergisinin kaldırılması (1925) aşağıdakilerden hangisini amaçlamıştır?",
  "siklar":{"A":"Devlet gelirini artırmak","B":"Köylünün üzerindeki ağır vergi yükünü hafifletmek","C":"Tarımı durdurmak","D":"Sanayiyi desteklemek"},
  "dogru_cevap":"B","aciklama":"Aşar vergisinin kaldırılması köylünün ağır vergi yükünü hafifletmeyi amaçlamıştır."},
 {"unite":U3,"konu":"Doğu Cephesi","yil":2022,"zorluk":"Zor",
  "soru":"Moskova Antlaşması (1921) ile Sovyet Rusya TBMM'yi tanımıştır.\n\nBu antlaşmanın Millî Mücadele açısından önemi aşağıdakilerden hangisidir?",
  "siklar":{"A":"Sovyetlerle savaş başlaması","B":"Doğu sınırının güvence altına alınması ve uluslararası destek kazanılması","C":"Batı cephesinin kapanması","D":"İşgallerin sona ermesi"},
  "dogru_cevap":"B","aciklama":"Moskova Antlaşması doğu güvenliği sağlamış ve uluslararası destek kazandırmıştır."},
 {"unite":U6,"konu":"Hatay","yil":2022,"zorluk":"Zor",
  "soru":"Atatürk son hastalık döneminde bile Hatay meselesiyle yakından ilgilenmiştir.\n\nBu durum Atatürk'ün hangi özelliğini yansıtır?",
  "siklar":{"A":"Savaşçılığını","B":"Millî dava konusundaki kararlılığını ve vatanseverliğini","C":"Dış politikadan uzaklığını","D":"Kişisel çıkarını"},
  "dogru_cevap":"B","aciklama":"Hasta yatağında bile Hatay'la ilgilenmesi vatanseverlik ve kararlılığı yansıtır."},
]

fn=os.path.join(BASE,"sorular_8.json")
with open(fn,"r",encoding="utf-8") as f: qs=json.load(f)
qs.extend(ek)
# Balance
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
with open(fn,"w",encoding="utf-8") as f: json.dump(qs,f,ensure_ascii=False,indent=2)
d={k:sum(1 for q in qs if q["dogru_cevap"]==k) for k in keys}
print(f"8. Sinif: {len(qs)} soru | A={d['A']} B={d['B']} C={d['C']} D={d['D']}")
