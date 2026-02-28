# LGS İnkılap Tarihi – Çark Oyunu 🏛🎡

Python / Tkinter ile hazırlanmış masaüstü çark oyunu.
Çarkı çevir → puan belirle → LGS çıkmış soruyu cevapla → puan kazan!

## Gereksinimler

- **Python 3.10+** (Tkinter dahil gelir; ek bağımlılık yok)
- Windows, macOS veya Linux

## Çalıştırma

```bash
python cark_oyunu.py
```

> Windows'ta `python` komutu çalışmazsa `py cark_oyunu.py` veya `python3 cark_oyunu.py` deneyin.

## Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🎯 Animasyonlu Çark | Easing ile yavaşlayarak duran çark |
| 📚 35 Soru | 7 üniteyi kapsayan LGS çıkmış soruları |
| 🌙 Koyu / ☀ Açık Tema | Tek tıkla geçiş |
| 📊 İstatistik | Toplam puan, doğru/yanlış/çözülen |
| ⏩ Soru Geçme | Puan kaybetmeden atlama |
| ↻ Sıfırlama | Oyunu baştan başlatma |
| 🔄 Tekrar Kontrolü | Aynı soru tekrar gelmez |

## Soru Ekleme

`sorular.json` dosyasına yeni kayıtlar ekleyebilirsiniz:

```json
{
  "id": 36,
  "unite": "Ünite 4 – Atatürkçülük",
  "konu": "Cumhuriyetçilik İlkesi",
  "yil": 2023,
  "zorluk": "Kolay",
  "soru": "Soru metni buraya...",
  "siklar": {
    "A": "Şık A",
    "B": "Şık B",
    "C": "Şık C",
    "D": "Şık D"
  },
  "dogru_cevap": "B",
  "aciklama": "Opsiyonel açıklama"
}
```

## Dosya Yapısı

```
Çark/
├── cark_oyunu.py    ← Ana uygulama
├── sorular.json     ← Soru havuzu
└── README.md        ← Bu dosya
```
