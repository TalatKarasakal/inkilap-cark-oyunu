#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LGS Sosyal Bilgiler Çark Oyunu  –  v3.0
========================================
Yenilikler:
  • 5. 6. 7. ve 8. Sınıf desteği (sınıf seçim ekranı)
  • 130+ Soru (her sınıf için ayrı soru bankası)
  • 45 saniyelik geri sayım zamanlayıcısı
  • Puanlama: Doğru +çark+10 bonus / Yanlış veya süre dolunca -5
  • Ünite bazlı istatistik / özet ekranı
  • Enerji Teması (Sarı / Kırmızı / Lacivert)
"""

import json
import math
import os
import random
import sys
import tkinter as tk
from tkinter import font as tkfont
from typing import Optional, Dict, List
from datetime import datetime, timedelta

try:
    from PIL import Image as PILImage, ImageTk as PILImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# Pygame ses için (başlangıcı hızlandırmak için sadece tanım, import sonradan)
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
pygame = None

import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    try:
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass

# ──────────────────────────────────────────────
# KAYNAK YOLU
# ──────────────────────────────────────────────

def resource_path(relative_path: str) -> str:
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

def get_user_data_path() -> str:
    app_dir = os.path.join(os.path.expanduser("~"), ".lgscarkoyunu")
    if not os.path.exists(app_dir):
        try:
            os.makedirs(app_dir)
        except Exception:
            return "streak_data.json"
    return os.path.join(app_dir, "streak_data.json")

# ──────────────────────────────────────────────
# TEMALAR
# ──────────────────────────────────────────────

THEMES = {
    "energy": {
        "bg":            "#0d0e15",
        "bg_secondary":  "#121324",
        "bg_card":       "#16172e",
        "fg":            "#f3f4f6",
        "fg_dim":        "#9ca3af",
        "accent":        "#ffd54f",
        "accent_hover":  "#ffe082",
        "success":       "#00e676",
        "error":         "#ff1744",
        "warning":       "#ff9100",
        "border":        "#1d1e3a",
        "btn_bg":        "#4f46e5",
        "btn_fg":        "#ffffff",
        "btn_hover":     "#6366f1",
        "skip_bg":       "#1f2041",
        "skip_fg":       "#9ca3af",
        "option_bg":     "#121324",
        "option_fg":     "#f3f4f6",
        "option_hover":  "#242650",
        "option_sel":    "#2e316a",
        "option_sel_border": "#00e5ff",
        "score_bg":      "#121324",
        "timer_normal":  "#00e5ff",
        "timer_warn":    "#ff9100",
        "timer_danger":  "#ff1744",
        "wheel_colors": [
            "#3b82f6", "#1d1e3a", "#8b5cf6", "#0b0c16",
            "#2563eb", "#2a2b54", "#6366f1", "#121324",
            "#3b82f6", "#1d1e3a"
        ],
    },
    "dark": {
        "bg":            "#181c24",
        "bg_secondary":  "#232830",
        "bg_card":       "#2a303a",
        "fg":            "#f0f4fc",
        "fg_dim":        "#a0aabe",
        "accent":        "#6c8cff",
        "accent_hover":  "#8ba4ff",
        "success":       "#4cdf8b",
        "error":         "#ff6b7a",
        "warning":       "#ffb347",
        "border":        "#353c4a",
        "btn_bg":        "#6c8cff",
        "btn_fg":        "#ffffff",
        "btn_hover":     "#8ba4ff",
        "skip_bg":       "#3a4150",
        "skip_fg":       "#c4ccda",
        "option_bg":     "#2a303a",
        "option_fg":     "#f0f4fc",
        "option_hover":  "#353c4a",
        "option_sel":    "#3d4a6a",
        "option_sel_border": "#6c8cff",
        "score_bg":      "#1e2430",
        "timer_normal":  "#6c8cff",
        "timer_warn":    "#ffb347",
        "timer_danger":  "#ff6b7a",
        "wheel_colors": [
            "#6c8cff", "#ff6b7a", "#4cdf8b", "#ffb347", "#c77dff",
            "#ff8fab", "#64dfdf", "#ffd166", "#a5b4fc", "#f472b6",
        ],
    },
    "light": {
        "bg":            "#f0f2f5",
        "bg_secondary":  "#ffffff",
        "bg_card":       "#ffffff",
        "fg":            "#1a1f2e",
        "fg_dim":        "#6b7280",
        "accent":        "#4f6ef7",
        "accent_hover":  "#3b5be0",
        "success":       "#16a34a",
        "error":         "#dc2626",
        "warning":       "#d97706",
        "border":        "#d1d5db",
        "btn_bg":        "#4f6ef7",
        "btn_fg":        "#ffffff",
        "btn_hover":     "#3b5be0",
        "skip_bg":       "#e5e7eb",
        "skip_fg":       "#6b7280",
        "option_bg":     "#f9fafb",
        "option_fg":     "#1a1f2e",
        "option_hover":  "#e5e7eb",
        "option_sel":    "#dbe4ff",
        "option_sel_border": "#4f6ef7",
        "score_bg":      "#e8ecf4",
        "timer_normal":  "#4f6ef7",
        "timer_warn":    "#d97706",
        "timer_danger":  "#dc2626",
        "wheel_colors": [
            "#4f6ef7", "#ef4444", "#22c55e", "#f59e0b", "#a855f7",
            "#ec4899", "#06b6d4", "#eab308", "#818cf8", "#f472b6",
        ],
    },
}

# ──────────────────────────────────────────────
# ÇARK DİLİMLERİ  (int = puan, str = özel)
# ──────────────────────────────────────────────

# 13 dilim: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 + 1 İFLAS + 1 PAS + 1 X2
WHEEL_SLICES = [10, 20, "PAS", 30, 40, "X2", 50, 60, 70, 80, "İFLAS", 90, 100]
SLICE_COUNT  = len(WHEEL_SLICES)
SLICE_ANGLE  = 360 / SLICE_COUNT          # ~27.69° per slice

# Özel dilim renkleri (tema bağımsız)
SLICE_SPECIAL_COLOR = {
    "İFLAS": "#ff1744",   # Neon kırmızı
    "PAS":   "#1f2041",   # Koyu cam
    "X2":    "#ffd54f",   # Neon altın sarısı
}
SLICE_SPECIAL_LABEL = {
    "İFLAS": "💀\nİFLAS",
    "PAS":   "⏸\nPAS",
    "X2":    "⚡\nX2",
}

TIMER_SECONDS   = 45
BONUS_CORRECT   = 10
PENALTY_WRONG   = 5

# Web (index) versiyonundaki sınıf kartı görselleri
GRADE_IMAGES = {
    "5": "web/assets/grade_5.png",
    "6": "web/assets/grade_6.png",
    "7": "web/assets/grade_7.png",
    "8": "web/assets/grade_8.png",
}

# ──────────────────────────────────────────────
# YARDIMCI
# ──────────────────────────────────────────────

def load_questions(path: str) -> dict:
    """Sınıf bazlı soru sözlüğü döndürür: {'5': [...], '6': [...], ...}"""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Eski format (düz liste) ise 8. sınıf olarak sar
    if isinstance(data, list):
        return {"8": data}
    return data

# Sınıf bilgileri
GRADE_INFO = {
    "5": {"label": "5. Sınıf", "desc": "Sosyal Bilgiler", "emoji": "📗", "color": "#22c55e", "hover": "#16a34a"},
    "6": {"label": "6. Sınıf", "desc": "Sosyal Bilgiler", "emoji": "📘", "color": "#3b82f6", "hover": "#2563eb"},
    "7": {"label": "7. Sınıf", "desc": "Sosyal Bilgiler", "emoji": "📙", "color": "#f59e0b", "hover": "#d97706"},
    "8": {"label": "8. Sınıf", "desc": "İnkılap Tarihi", "emoji": "📕", "color": "#ef4444", "hover": "#dc2626"},
}

PYTHON_STUDY_RECS = {
    # 5. Sınıf
    "Ünite 1 – Birlikte Yaşamak": "Sosyal roller, hak ve sorumluluklarımız ile çocuk hakları konularına tekrar çalışmalısınız.",
    "Ünite 2 – Evimiz Dünya": "Türkiye'nin fiziki yeryüzü şekilleri, iklim tipleri, bitki örtüsü ve beşerî coğrafya özelliklerini gözden geçirmelisiniz.",
    "Ünite 3 – Ortak Mirasımız": "Anadolu ve Mezopotamya'nın kadim uygarlıkları ile ülkemizin somut/somut olmayan kültürel miras varlıklarını tekrar etmelisiniz.",
    "Ünite 4 – Yaşayan Demokrasimiz": "Demokrasinin temel ilkeleri, devletin yönetim organları ve katılım hakkının önemi konularını çalışmalısınız.",
    "Ünite 5 – Hayatımızda Ekonomi": "Ekonomik faaliyetler, meslek grupları, bütçe hazırlama ve bilinçli bir tüketicinin yapması gerekenler konularına bakmalısınız.",
    "Ünite 6 – Teknoloji ve Sosyal Bilimler": "Teknolojinin sosyal hayatımız üzerindeki etkileri, sosyal bilimlerin dalları ve bilimsel çalışma etiği konularını tekrar etmelisiniz.",
    
    # 6. Sınıf
    "Ünite 1 – Birlikte Yaşamak": "Sosyal roller, toplumsal yardımlaşma ve dayanışma ile ön yargıları kırma konularını incelemelisiniz.",
    "Ünite 2 – Evimiz Dünya": "Dünya'nın paralel/meridyen yapısı, kıtalar ve okyanuslar ile ülkemizin coğrafi konumunu tekrar etmelisiniz.",
    "Ünite 3 – Ortak Mirasımız": "İlk Türk devletlerinin kültürel özellikleri, İslamiyetin doğuşu ve Türklerin İslamiyete geçişini çalışmalısınız.",
    "Ünite 4 – Yaşayan Demokrasimiz": "Demokratik yönetim şekilleri, kadın hakları ve Türk tarihindeki yönetim yapılarını gözden geçirmelisiniz.",
    "Ünite 5 – Hayatımızdaki Ekonomi": "Üretim kaynaklarımız, yatırım ve girişimcilik fikirleri ile vergilerimizin önemi konularını çalışmalısınız.",
    "Ünite 6 – Teknoloji ve Sosyal Bilimler": "Bilim ve teknolojideki gelişmeler ile telif/patent haklarının önemi konularını çalışmalısınız.",
    
    # 7. Sınıf
    "Ünite 1 – Birey ve Toplum": "Olumlu ve etkili iletişim becerileri, medya okuryazarlığı, RTÜK ve iletişim özgürlüğü (sansür, basın özgürlüğü vb.) konularını tekrar etmelisiniz.",
    "Ünite 2 – Kültür ve Miras": "Osmanlı Devleti'nin kuruluş süreci, uyguladığı iskân ve istimâlet politikaları, denizlerdeki fetihler ve Avrupa'daki uyanışın (Rönesans, Reform vb.) Osmanlı'ya etkilerini incelemelisiniz.",
    "Ünite 3 – İnsanlar, Yerler ve Çevreler": "Nüfusun dağılışını etkileyen faktörler, Türkiye'deki göç dalgaları ve göçün nedenleri/sonuçları konularını gözden geçirmelisiniz.",
    "Ünite 4 – Bilim, Teknoloji ve Toplum": "Tarih boyunca bilginin korunması/yayılması (kil tabletler, matbaa) ve ünlü Türk-İslam bilginleri (İbn-i Sina, Farabi vb.) konularını çalışmalısınız.",
    "Ünite 5 – Üretim, Dağıtım ve Tüketim": "Toprağın yönetimde ve üretimdeki önemi, Ahilik/Lonca teşkilatı, mesleki yönlendirme ve dijital çağın getirdiği yeni meslekleri incelemelisiniz.",
    "Ünite 6 – Etkin Vatandaşlık": "Demokratik yönetimlerin tarihi gelişimi, Türkiye Cumhuriyeti anayasasının temel nitelikleri ve sivil toplum örgütlerinin (STK) faaliyetlerine odaklanmalısınız.",
    "Ünite 7 – Küresel Bağlantılar": "Ülkemizin üye olduğu uluslararası siyasi/ekonomik kuruluşlar (BM, NATO vb.) ve küresel çevre/iklim sorunlarına karşı alınabilecek tedbirleri tekrar etmelisiniz.",
    
    # 8. Sınıf
    "Ünite 1 – Bir Kahraman Doğuyor": "Mustafa Kemal'in çocukluk dönemi, okuduğu okullar, Selanik şehrinin sosyal/kültürel yapısı ve askerlik hayatı (Trablusgarp Savaşı, Balkan Savaşları, Çanakkale Cephesi) konularını tekrar etmelisiniz.",
    "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar": "I. Dünya Savaşı'nın nedenleri ve cepheleri, Mondros Ateşkes Antlaşması, Havza ve Amasya Genelgeleri, Erzurum ve Sivas Kongreleri ile Misak-ı Milli kararlarına tekrar çalışmalısınız.",
    "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!": "Doğu ve Güney cepheleri, Batı cephesindeki düzenli ordu savaşları (I. ve II. İnönü, Kütahya-Eskişehir, Sakarya Meydan Muharebesi, Büyük Taarruz) ve ülkemizin bağımsızlık belgesi olan Lozan Antlaşması konularını çalışmalısınız.",
    "Ünite 4 – Atatürkçülük ve Çağdaşlaşan Türkiye": "Siyasi alandaki inkılaplar (Saltanatın kaldırılması, Ankara'nın başkent oluşu, Cumhuriyetin ilanı, Halifeliğin kaldırılması), eğitim/kültür inkılapları ve Atatürk ilkeleri (Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılapçılık) konularına odaklanın.",
    "Ünite 5 – Demokratikleşme Çabaları": "Çok partili hayata geçiş denemeleri, Terakkiperver Cumhuriyet Fırkası, Serbest Cumhuriyet Fırkası ve Şeyh Said İsyanı gibi laik cumhuriyete karşı çıkan isyanları çalışmalısınız.",
    "Ünite 6 – Atatürk Dönemi Türk Dış Politikası": "Atatürk dönemi dış politikanın temel ilkeleri, Lozan'dan kalan sorunlar (Nüfus mübadelesi, Yabancı okullar, Musul sorunu, Boğazlar konusu, Hatay meselesi) ve barış paktlarını (Balkan Antantı, Sadabat Paktı) tekrar edin."
}


def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3

# ──────────────────────────────────────────────
# ANA UYGULAMA
# ──────────────────────────────────────────────

class CarkOyunu(tk.Tk):
    STATE_GRADE_SELECT = "grade_select"
    STATE_UNIT_SELECT = "unit_select"
    STATE_MODE_SELECT = "mode_select"
    STATE_IDLE      = "idle"
    STATE_SPINNING  = "spinning"
    STATE_QUESTION  = "question"
    STATE_ANSWERED  = "answered"

    ANIM_DURATION_MS = 4000
    ANIM_FPS         = 60

    def __init__(self):
        super().__init__()

        # Ensure icon appears in taskbar on Windows
        try:
            import ctypes
            myappid = 'com.talatkarasakal.carkoyunu.v3'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

        self.title("LGS Sosyal Bilgiler – Çark Oyunu  v3")

        # ── Ekran boyutuna göre dinamik ölçeklendirme ──
        self.update_idletasks()
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        self.scale = max(0.6, min(screen_w / 1920, screen_h / 1080, 1.5))

        base_w = int(1240 * self.scale)
        base_h = int(950 * self.scale)
        min_w  = int(900 * self.scale)
        min_h  = int(680 * self.scale)
        self.minsize(min_w, min_h)
        self.geometry(f"{base_w}x{base_h}")

        # Simgesi
        try:
            icon_img = tk.PhotoImage(file=resource_path("icon.png"))
            self.iconphoto(False, icon_img)
        except Exception as e:
            print("İkon yüklenemedi:", e)

        self.configure(bg="#1a0a00")

        # --- SES (Audio) KURULUMU (Lazy init - hızlı açılış) ---
        self.audio_enabled = False
        self.audio_initialized = False
        self.sounds = {}

        # Tema
        self.current_theme = "energy"
        self.t = THEMES[self.current_theme]

        # Fontlar (ölçeklendirilmiş)
        s = self.scale
        fam = "Segoe UI" if os.name == "nt" else "Helvetica"
        self.f_title  = tkfont.Font(family=fam, size=max(12, int(17 * s)), weight="bold")
        self.f_normal = tkfont.Font(family=fam, size=max(10, int(13 * s)))
        self.f_small  = tkfont.Font(family=fam, size=max(9, int(11 * s)))
        self.f_big    = tkfont.Font(family=fam, size=max(11, int(14 * s)), weight="bold")
        self.f_option = tkfont.Font(family=fam, size=max(10, int(12 * s)))
        self.f_score  = tkfont.Font(family=fam, size=max(16, int(22 * s)), weight="bold")
        self.f_wheel  = tkfont.Font(family=fam, size=max(10, int(14 * s)), weight="bold")
        self.f_icon   = tkfont.Font(family=fam, size=max(14, int(18 * s)))
        self.f_timer  = tkfont.Font(family=fam, size=max(14, int(18 * s)), weight="bold")

        # Resize debounce
        self._resize_id = None

        # Görsel önbelleği (parşömen / ahşap / sınıf kartları)
        self._img_cache: Dict[tuple, "PILImageTk.PhotoImage"] = {}

        # Soru havuzu (sınıf bazlı)
        self.questions_db = load_questions(resource_path("sorular.json"))
        self.selected_grade: Optional[str] = None
        self.all_questions: List[dict] = []
        self.remaining: List[dict] = []

        # Oyun durumu
        self.state          = self.STATE_IDLE
        self.total_score    = 0
        self.correct_count  = 0
        self.wrong_count    = 0
        self.solved_count   = 0
        
        # Team Mode variables
        self.is_team_mode   = False
        self.team_scores    = {"A": 0, "B": 0}
        self.active_team    = "A"
        self.team_correct   = 0
        self.team_wrong     = 0
        
        # Streak & Quest data
        self.user_streak = 0
        self.last_login_date = ""
        self.today_solved_count = 0
        self.last_spin_was_iflas = False
        self._load_userdata()
        self._check_daily_streak()
        self.current_q: Optional[dict] = None
        self.current_points = 0
        self.selected_opt: Optional[str] = None
        self.x2_mode      = False   # X2 dilimi aktif mi?
        self.special_is_x2 = False

        # Ünite istatistikleri  {unite_adi: {"d": dogru_sayisi, "y": yanlis_sayisi}}
        self.unite_stats: Dict[str, Dict[str, int]] = {}

        # Animasyon
        self.anim_id: Optional[str]  = None
        self.wheel_angle  = 0.0
        self.target_angle = 0.0
        self.anim_start_angle = 0.0
        self.total_rotation   = 0.0
        self.anim_elapsed     = 0

        # Zamanlayıcı
        self.timer_id: Optional[str] = None
        self.timer_remaining = TIMER_SECONDS

        # UI
        self._build_ui()
        self._apply_theme()
        self._draw_wheel()
        self._show_grade_selection()

        # Pencere yeniden boyutlandırma
        self.bind("<Configure>", self._on_window_resize)
        


    # ─────────────────────────────────────────
    # SES - LAZY INIT (ilk sesle birlikte başlatılır)
    # ─────────────────────────────────────────

    def _init_audio(self):
        """Sesi ilk ihtiyaçta yükler – açılışı hızlandırır."""
        if self.audio_initialized:
            return
        self.audio_initialized = True
        try:
            global pygame
            import pygame
            pygame.mixer.init()
            self.audio_enabled = True
            sp = resource_path("sounds")
            s_dict = {
                "spin": "spin.wav", "tick": "tick.wav",
                "win": "win.wav", "wrong": "wrong.wav", "fail": "fail.wav"
            }
            for k, v in s_dict.items():
                fp = os.path.join(sp, v)
                if os.path.exists(fp):
                    self.sounds[k] = pygame.mixer.Sound(fp)
            if "spin" in self.sounds:
                self.sounds["spin"].set_volume(0.3)
            if "tick" in self.sounds:
                self.sounds["tick"].set_volume(0.5)
        except Exception as e:
            print("Ses sistemi başlatılamadı:", e)

    def _play_sound(self, name: str):
        """Sesi çalar, gerekiyorsa önce audio başlatır."""
        if not self.audio_initialized:
            self._init_audio()
        if self.audio_enabled and name in self.sounds:
            self.sounds[name].play()

    # ─────────────────────────────────────────
    # SORU HAVUZU
    # ─────────────────────────────────────────

    def _refill_pool(self):
        self.remaining = list(self.all_questions)
        random.shuffle(self.remaining)

    def _pick_question(self) -> dict:
        """Soru seçer, uzun şık bug'ını önler ve harf dağılımını homojen yapar."""
        if not self.remaining:
            self._refill_pool()

        q_orijinal = self.remaining.pop()
        q = q_orijinal.copy()
        
        # 1. EN UZUN ŞIK BUG'INI ÖNLEME (Anti-Exploit Çeldirici)
        # Orijinal veriyi bozmamak için dict() ile kopyalıyoruz
        orijinal_siklar = dict(q_orijinal["siklar"])
        dogru_metin = orijinal_siklar[q_orijinal["dogru_cevap"]]
        
        # Şıkların uzunluklarını kontrol et
        max_len = max(len(str(v)) for v in orijinal_siklar.values())
        
        # Eğer doğru cevap en uzun şıksa (ve makul bir uzunluktaysa), bir yanlış şıkkı devasa yaparak öğrencileri yanılt
        if len(str(dogru_metin)) == max_len and max_len > 30:
            yanlis_harfler = [k for k in orijinal_siklar.keys() if k != q_orijinal["dogru_cevap"]]
            hedef_yanlis = random.choice(yanlis_harfler)
            
            uzatici_ifadeler = [
                " ve bu durumun tarihteki bütün olaylarda kesin, değişmez bir kural olarak her zaman aynı şekilde yaşanması",
                " ile birlikte toplumdaki tüm bireylerin istisnasız olarak tamamen aynı ve tek tip tepkiyi göstermesi",
                " gerçeğinin her dönemde tek ve en önemli etken olarak kabul edilmesinin kesinlikle zorunlu olması",
                " gibi gelişmelerin hiçbir şekilde değiştirilemez ve dış güçlerce engellenemez sonuçları beraberinde getirmesi",
                " durumunun yalnızca o döneme ait olması ve dünya tarihinde başka hiçbir zaman diliminde kesinlikle görülmemesi",
                " ve bu sürecin tamamen dış güçlerin kontrolünde, yerel halkın hiçbir iradesi olmadan zorla gerçekleştirilmesi",
                " olgusunun ekonomik, siyasi ve sosyal tüm alanlarda diğer tüm etkenleri yok sayarak tek başına belirleyici olması",
                " sonucunda devletin tüm askeri ve sivil kurumlarının tamamen ve bir daha geri dönülemez şekilde yok olması"
            ]
            
            ek_ifade = random.choice(uzatici_ifadeler)
            orijinal_siklar[hedef_yanlis] = str(orijinal_siklar[hedef_yanlis]) + ek_ifade

        # 2. ŞIK DAĞILIMINI HOMOJEN YAPMA (Aynı harf üst üste gelmesin)
        secenekler = list(orijinal_siklar.values())
        last_correct = getattr(self, '_last_correct_key', None)
        yeni_dogru_harf = "A"
        
        for _ in range(10):
            random.shuffle(secenekler)
            dogru_index = secenekler.index(dogru_metin)
            yeni_dogru_harf = ["A", "B", "C", "D"][dogru_index]
            if yeni_dogru_harf != last_correct:
                break
                
        yeni_siklar = {}
        harfler = ["A", "B", "C", "D"]
        for i, harf in enumerate(harfler):
            yeni_siklar[harf] = secenekler[i]
            
        q["siklar"] = yeni_siklar
        q["dogru_cevap"] = yeni_dogru_harf
        self._last_correct_key = yeni_dogru_harf
        
        return q

    # ─────────────────────────────────────────
    # UI OLUŞTURMA
    # ─────────────────────────────────────────

    def _build_ui(self):
        s = self.scale
        pad = max(6, int(12 * s))

        # Üst bar
        self.top_bar = tk.Frame(self, height=max(40, int(54 * s)))
        self.top_bar.pack(fill="x", side="top")
        self.top_bar.pack_propagate(False)

        # Ahşap doku arka planı (enerji teması) – diğer widget'ların arkasında durur
        self.top_bar_bg = tk.Label(self.top_bar, bd=0, highlightthickness=0)

        self.lbl_title = tk.Label(
            self.top_bar, text="🏛  LGS Sosyal Bilgiler – Çark Oyunu",
            font=self.f_title, anchor="w", padx=int(18 * s)
        )
        self.lbl_title.pack(side="left", fill="y")



        # Ana Menü (Sınıf Seçimi)
        self.btn_main_menu = tk.Label(
            self.top_bar, text="🏠 Sınıf Seçimi", font=self.f_normal,
            cursor="hand2", padx=int(14 * s), pady=6
        )
        self.btn_main_menu.pack(side="right", fill="y")
        self.btn_main_menu.bind("<Button-1>", lambda _: self._return_to_main_menu())

        # Sıfırla
        self.btn_reset = tk.Label(
            self.top_bar, text="↻ Sıfırla", font=self.f_normal,
            cursor="hand2", padx=int(14 * s), pady=6
        )
        self.btn_reset.pack(side="right", fill="y")
        self.btn_reset.bind("<Button-1>", lambda _: self._reset_game())

        # İstatistik
        self.btn_stats = tk.Label(
            self.top_bar, text="📊 İstatistik", font=self.f_normal,
            cursor="hand2", padx=int(14 * s), pady=6
        )
        self.btn_stats.pack(side="right", fill="y")
        self.btn_stats.bind("<Button-1>", lambda _: self._show_stats_panel())

        # HUD Durum Çubuğu (Status Bar)
        self.status_bar = tk.Frame(self, height=max(32, int(42 * s)))
        self.status_hud_frame = tk.Frame(self.status_bar)
        self.status_hud_frame.pack(expand=True, fill="both", padx=10)
        
        self.lbl_score_hud = tk.Label(self.status_hud_frame, text="🏆 Puan: 0", font=self.f_big)
        self.lbl_score_hud.pack(side="left", padx=12, expand=True)
        
        self.lbl_streak_hud = tk.Label(self.status_hud_frame, text="🔥 Seri: 0 Gün", font=self.f_normal)
        self.lbl_streak_hud.pack(side="left", padx=12, expand=True)
        
        self.lbl_correct_hud = tk.Label(self.status_hud_frame, text="✓ 0", font=self.f_normal)
        self.lbl_correct_hud.pack(side="left", padx=12, expand=True)
        
        self.lbl_wrong_hud = tk.Label(self.status_hud_frame, text="✗ 0", font=self.f_normal)
        self.lbl_wrong_hud.pack(side="left", padx=12, expand=True)
        
        self.lbl_solved_hud = tk.Label(self.status_hud_frame, text="📝 0", font=self.f_normal)
        self.lbl_solved_hud.pack(side="left", padx=12, expand=True)
        
        self.lbl_quest_hud = tk.Label(self.status_hud_frame, text="🎯 Görev: 0/5", font=self.f_normal)
        self.lbl_quest_hud.pack(side="left", padx=12, expand=True)

        # Ana içerik alanı
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=pad, pady=(0, pad))

        # Parşömen doku arka planı (enerji teması) – panellerin arkasında durur
        self.main_bg = tk.Label(self.main_frame, bd=0, highlightthickness=0)

        # 1. Sınıf & Ünite Seçim Alanı
        self.grade_unit_frame = tk.Frame(self.main_frame)
        self.grade_unit_canvas = tk.Canvas(self.grade_unit_frame, highlightthickness=0)
        self.grade_unit_canvas.pack(side="left", fill="both", expand=True)
        self.grade_unit_panel = tk.Frame(self.grade_unit_canvas)
        self._gup_window = self.grade_unit_canvas.create_window(
            (0, 0), window=self.grade_unit_panel, anchor="nw"
        )
        self.grade_unit_panel.bind("<Configure>", lambda e: self.grade_unit_canvas.configure(scrollregion=self.grade_unit_canvas.bbox("all")))
        self.grade_unit_canvas.bind("<Configure>", lambda e: self.grade_unit_canvas.itemconfig(self._gup_window, width=e.width))

        # 2. Çark Alanı (Wheel View Container - Centered)
        self.wheel_frame = tk.Frame(self.main_frame)
        self.wheel_content = tk.Frame(self.wheel_frame) # For centering
        self.wheel_content.place(relx=0.5, rely=0.5, anchor="center")

        self.canvas_size = int(420 * s)
        self.wheel_canvas = tk.Canvas(
            self.wheel_content, width=self.canvas_size, height=self.canvas_size,
            highlightthickness=0
        )
        self.wheel_canvas.pack(pady=10)

        self.pointer_canvas = tk.Canvas(
            self.wheel_content, width=int(40 * s), height=int(28 * s), highlightthickness=0
        )
        self.pointer_canvas.place(
            in_=self.wheel_canvas,
            relx=0.5, rely=0.0, anchor="s", y=6
        )

        self.btn_spin = tk.Frame(self.wheel_content, cursor="hand2", padx=int(28 * s), pady=int(10 * s))
        self.btn_spin.pack(pady=10)

        self.btn_spin_icon = tk.Label(self.btn_spin, text="🎯", font=self.f_big, cursor="hand2")
        self.btn_spin_icon.pack(side="left", padx=(0, 6))

        self.btn_spin_text = tk.Label(self.btn_spin, text="Çarkı Çevir", font=self.f_big, cursor="hand2")
        self.btn_spin_text.pack(side="left")

        for w in (self.btn_spin, self.btn_spin_icon, self.btn_spin_text):
            w.bind("<Button-1>", lambda _: self._spin_wheel())

        # 3. Soru Alanı (Question View Container)
        self.question_frame = tk.Frame(self.main_frame)
        self.q_canvas = tk.Canvas(self.question_frame, highlightthickness=0)
        self.q_canvas.pack(side="left", fill="both", expand=True)

        self.question_panel = tk.Frame(self.q_canvas)
        self._qp_window = self.q_canvas.create_window(
            (0, 0), window=self.question_panel, anchor="nw"
        )
        self.question_panel.bind("<Configure>", lambda e: self.q_canvas.configure(scrollregion=self.q_canvas.bbox("all")))
        self.q_canvas.bind("<Configure>", lambda e: self.q_canvas.itemconfig(self._qp_window, width=e.width))

    def _on_mousewheel(self, event):
        if self.state in (self.STATE_GRADE_SELECT, self.STATE_UNIT_SELECT):
            self.grade_unit_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            self.q_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ─────────────────────────────────────────
    # PENCERE YENİDEN BOYUTLANDIRMA
    # ─────────────────────────────────────────

    def _on_window_resize(self, event):
        if event.widget != self:
            return
        if self._resize_id:
            self.after_cancel(self._resize_id)
        self._resize_id = self.after(250, self._handle_resize)

    def _handle_resize(self):
        self._resize_id = None
        w = self.winfo_width()
        h = self.winfo_height()

        # Update text wrap lengths based on full window width
        self._current_wraplength = max(300, w - 80)
        self._current_opt_wraplength = max(300, w - 120)

        # Scale wheel canvas size based on window dimensions
        new_canvas = min(w - 100, h - 240)
        new_canvas = max(250, min(new_canvas, 750))
        
        if hasattr(self, "wheel_canvas") and self.wheel_canvas.winfo_exists():
            if abs(new_canvas - self.canvas_size) > 10:
                self.canvas_size = new_canvas
                self.wheel_canvas.config(width=new_canvas, height=new_canvas)
                self._draw_wheel()

        # Doku arka planlarını yeni boyuta göre yenile (enerji teması)
        self._update_header_bg()
        self._update_main_bg()

    def _get_wraplength(self):
        return getattr(self, '_current_wraplength', int(520 * self.scale))

    def _get_opt_wraplength(self):
        return getattr(self, '_current_opt_wraplength', int(480 * self.scale))

    # ─────────────────────────────────────────
    # GÖRSEL YARDIMCILARI (parşömen / ahşap / kartlar)
    # ─────────────────────────────────────────

    def _update_header_bg(self):
        """Disable image background for modern clean layout."""
        if hasattr(self, "top_bar_bg"):
            self.top_bar_bg.place_forget()

    def _update_main_bg(self):
        """Disable image background for modern clean layout."""
        if hasattr(self, "main_bg"):
            self.main_bg.place_forget()

    def _get_image(self, rel_path: str, width: int, height: int):
        """PIL ile yeniden boyutlandırılmış PhotoImage döndürür (önbellekli)."""
        if not HAS_PIL:
            return None
        width = max(1, int(width))
        height = max(1, int(height))
        key = (rel_path, width, height)
        if key in self._img_cache:
            return self._img_cache[key]
        try:
            path = resource_path(rel_path)
            if not os.path.exists(path):
                return None
            pil = PILImage.open(path)
            resample = PILImage.Resampling.LANCZOS if hasattr(PILImage, "Resampling") else PILImage.ANTIALIAS
            pil = pil.resize((width, height), resample)
            img = PILImageTk.PhotoImage(pil)
            self._img_cache[key] = img
            return img
        except Exception as e:
            print("Resim yüklenemedi:", rel_path, e)
            return None



    # ─────────────────────────────────────────
    # ÇARK ÇİZİMİ
    # ─────────────────────────────────────────

    def _draw_wheel(self):
        c = self.wheel_canvas
        c.delete("all")
        cx = cy = self.canvas_size / 2
        
        # Stand-free floating neon style
        pass

        # Outer rim radius
        outer_rim = self.canvas_size / 2 - 4
        slices_r = self.canvas_size / 2 - 22
        
        # Draw outer neon glowing rim
        c.create_oval(cx - outer_rim, cy - outer_rim, cx + outer_rim, cy + outer_rim,
                      fill="#121324", outline="#00e5ff", width=4)
        c.create_oval(cx - slices_r - 2, cy - slices_r - 2, cx + slices_r + 2, cy + slices_r + 2,
                      fill="#0b0c16", outline="#8b5cf6", width=2)

        num_color_idx = 0  # sadece puan dilimleri için renk döngüsü
        for i, sv in enumerate(WHEEL_SLICES):
            start = i * SLICE_ANGLE + self.wheel_angle
            is_special = isinstance(sv, str)
            if is_special:
                color = SLICE_SPECIAL_COLOR[sv]
            else:
                color = self.t["wheel_colors"][num_color_idx % len(self.t["wheel_colors"])]
                num_color_idx += 1
            c.create_arc(
                cx - slices_r, cy - slices_r, cx + slices_r, cy + slices_r,
                start=start, extent=SLICE_ANGLE,
                fill=color, outline="#121324", width=1,
                style="pieslice"
            )
            mid = math.radians(start + SLICE_ANGLE / 2)
            tx = cx + (slices_r * 0.65) * math.cos(mid)
            ty = cy - (slices_r * 0.65) * math.sin(mid)
            if is_special:
                label = SLICE_SPECIAL_LABEL[sv]
                c.create_text(tx, ty, text=label,
                              font=self.f_small, fill="#ffffff",
                              justify="center")
            else:
                c.create_text(tx, ty, text=str(sv),
                              font=self.f_wheel, fill="#ffffff")

        # Neon center cap
        c.create_oval(
            cx - 32, cy - 32, cx + 32, cy + 32,
            fill="#121324", outline="#00e5ff", width=3
        )
        c.create_text(cx, cy, text="🏛", font=self.f_big, fill="#00e5ff")
        self._draw_pointer()

    def _draw_pointer(self):
        pc = self.pointer_canvas
        pc.delete("all")
        s = self.scale
        w = int(32 * s)
        h = int(44 * s)
        
        # Draw neon pointer
        x1, y1 = 4, 2
        x2, y2 = w - 4, 2
        x3, y3 = w - 4, int(h * 0.7)
        x4, y4 = int(w * 0.5), h - 2
        x5, y5 = 4, int(h * 0.7)
        
        pc.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5,
                           fill="#ff1744", outline="#ffffff", width=2)

    # ─────────────────────────────────────────
    # ÇARK ANİMASYONU
    # ─────────────────────────────────────────

    def _spin_wheel(self):
        if self.state != self.STATE_IDLE or self.selected_grade is None:
            return
        self.state = self.STATE_SPINNING
        for w in (self.btn_spin, self.btn_spin_icon, self.btn_spin_text):
            w.config(cursor="arrow")

        extra_turns    = random.randint(5, 9) * 360
        target_slice   = random.randint(0, SLICE_COUNT - 1)
        # İflas gelme olasılığını azalt (%75 ihtimalle tekrar kura çek)
        if WHEEL_SLICES[target_slice] == "İFLAS" and random.random() < 0.75:
            target_slice = random.choice([i for i, s in enumerate(WHEEL_SLICES) if s != "İFLAS"])
        slice_mid      = target_slice * SLICE_ANGLE + SLICE_ANGLE / 2
        final_angle    = 90 - slice_mid
        self.anim_start_angle = self.wheel_angle
        self.total_rotation   = extra_turns + (final_angle - (self.wheel_angle % 360) + 360) % 360
        self.target_angle     = self.anim_start_angle + self.total_rotation
        self.target_slice     = target_slice
        self.anim_elapsed     = 0
        self.last_played_angle = self.wheel_angle

        self._clear_right_panel()
        self._show_spinning_panel()
        self._animate_step()

    def _animate_step(self):
        dt = 1000 / self.ANIM_FPS
        self.anim_elapsed += dt
        progress = min(self.anim_elapsed / self.ANIM_DURATION_MS, 1.0)
        eased    = ease_out_cubic(progress)
        
        current_angle = self.anim_start_angle + self.total_rotation * eased
        self.wheel_angle = current_angle
        self._draw_wheel()

        pieces_crossed = int((current_angle - self.last_played_angle) / SLICE_ANGLE)
        if pieces_crossed >= 1:
            self.last_played_angle += pieces_crossed * SLICE_ANGLE
            self._play_sound("spin")

        if progress < 1.0:
            self.anim_id = self.after(int(dt), self._animate_step)
        else:
            self.anim_id = None
            self.wheel_angle = self.target_angle
            self._draw_wheel()
            self._on_spin_complete()

    def _on_spin_complete(self):
        for w in (self.btn_spin, self.btn_spin_icon, self.btn_spin_text):
            w.config(cursor="hand2")
        sv = WHEEL_SLICES[self.target_slice]

        if sv == "İFLAS":
            self.last_spin_was_iflas = True
            if self.is_team_mode:
                self.team_scores[self.active_team] = 0
                current_team_name = f"{self.active_team} Grubu"
                self.active_team = "B" if self.active_team == "A" else "A"
                self._update_stats()
                self.state = self.STATE_IDLE
                self._clear_right_panel()
                self._show_special_panel(
                    "💀  İFLAS!",
                    f"{current_team_name} puanı sıfırlandı ve sıra diğer takıma geçti!",
                    self.t["error"]
                )
            else:
                self.total_score = 0
                self._update_stats()
                self.state = self.STATE_IDLE
                self._clear_right_panel()
                self._show_special_panel(
                    "💀  İFLAS!",
                    "Tüm puanlarınız sıfırlandı!",
                    self.t["error"]
                )
            return

        if sv == "PAS":
            self.last_spin_was_iflas = False
            if self.is_team_mode:
                current_team_name = f"{self.active_team} Grubu"
                self.active_team = "B" if self.active_team == "A" else "A"
                self._update_stats()
                self.state = self.STATE_IDLE
                self._clear_right_panel()
                self._show_special_panel(
                    "⏸  PAS!",
                    f"{current_team_name} bu turu pas geçti. Sıra diğer takıma geçti.",
                    self.t["fg_dim"]
                )
            else:
                self.state = self.STATE_IDLE
                self._clear_right_panel()
                self._show_special_panel(
                    "⏸  PAS!",
                    "Bu turu geçtiniz. Puan değişmedi.",
                    self.t["fg_dim"]
                )
            return

        # X2 veya normal puan
        if sv == "X2":
            self.x2_mode        = True
            self.current_points = 0   # X2'de çark puanı kullanılmaz
            self.current_q    = self._pick_question()
            self.selected_opt = None
            self.special_is_x2 = True
            
            if self.is_team_mode:
                current_team_name = f"{self.active_team} Grubu"
                msg = f"{current_team_name} için X2 aktif! Doğru cevaplarsa toplam puanı ikiye katlanacak!"
            else:
                msg = "X2 aktif! Doğru cevaplarsan toplam puanın 2 katına çıkacak!"
                
            self._show_special_panel(
                "⚡  X2 AKTİF!",
                msg,
                "#ffd54f"
            )
            return
        else:
            self.x2_mode        = False
            self.current_points = sv
            self.special_is_x2  = False

        self.current_q    = self._pick_question()
        self.selected_opt = None
        self.state        = self.STATE_QUESTION
        self._clear_right_panel()
        self._switch_stage(self.STATE_QUESTION)
        self._show_question_panel()
        self._start_timer()

    # ─────────────────────────────────────────
    # ZAMANLAYICI
    # ─────────────────────────────────────────

    def _start_timer(self):
        self._stop_timer()
        self.timer_remaining = TIMER_SECONDS
        self._update_timer_display()
        self.timer_id = self.after(1000, self._tick_timer)

    def _tick_timer(self):
        if self.state != self.STATE_QUESTION:
            return
        self.timer_remaining -= 1
        self._update_timer_display()

        if self.timer_remaining > 0:
            self._play_sound("tick")

        if self.timer_remaining <= 0:
            self._time_expired()
        else:
            self.timer_id = self.after(1000, self._tick_timer)

    def _stop_timer(self):
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

    def _update_timer_display(self):
        secs = self.timer_remaining
        t = self.t
        if secs > 20:
            color = t["timer_normal"]
        elif secs > 10:
            color = t["timer_warn"]
        else:
            color = t["timer_danger"]

        # Dairesel timer çizimi
        if hasattr(self, "timer_canvas") and self.timer_canvas.winfo_exists():
            tc = self.timer_canvas
            tc.delete("all")
            sz = self._timer_size
            cx, cy = sz / 2, sz / 2
            r = sz / 2 - 6

            # Pulsing size & text color changes for last 10 seconds
            if secs <= 10 and secs > 0:
                pulse_factor = 1.15 if (secs % 2 == 0) else 0.9
                r = (sz / 2 - 6) * pulse_factor
                pulse_font_size = max(16, int(22 * self.scale)) if (secs % 2 == 0) else max(12, int(15 * self.scale))
                self.f_timer.config(size=pulse_font_size)
                text_color = color  # Force red (timer_danger) text color
            else:
                self.f_timer.config(size=max(14, int(18 * self.scale)))
                text_color = "#ffffff"

            # Arka plan halkası
            tc.create_oval(cx - r, cy - r, cx + r, cy + r,
                           outline=t["border"], width=5, fill="")
            # İlerleme yayı
            pct = secs / TIMER_SECONDS
            if pct > 0:
                extent = 360 * pct
                tc.create_arc(cx - r, cy - r, cx + r, cy + r,
                              start=90, extent=extent,
                              outline=color, width=5, style="arc")
            # Ortadaki sayı (Beyaz renk yerine son 10 saniyede danger rengi)
            tc.create_text(cx, cy, text=f"{secs}", font=self.f_timer, fill=text_color)

            # ≤10 saniyede titreşim efekti
            if secs <= 10 and secs > 0 and secs % 2 == 0:
                tc.create_oval(cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2,
                               outline=color, width=2, fill="")

        # Linear progress bar
        if hasattr(self, "timer_bar_fill") and self.timer_bar_fill.winfo_exists():
            pct = secs / TIMER_SECONDS
            bar_w = int(self.timer_bar_bg.winfo_width() * pct)
            if bar_w > 0:
                self.timer_bar_fill.place(relx=0, rely=0, relheight=1, width=bar_w)
            self.timer_bar_fill.config(bg=color)

    def _time_expired(self):
        """Süre doldu → yanlış say, ceza ver."""
        self._stop_timer()
        self.state = self.STATE_ANSWERED
        q = self.current_q

        if self.is_team_mode:
            self.team_wrong += 1
            self.team_scores[self.active_team] -= PENALTY_WRONG
        else:
            self.wrong_count  += 1
            self.total_score  -= PENALTY_WRONG

        self.solved_count += 1
        self.last_spin_was_iflas = False
        self._record_unite(q["unite"], False)
        self._update_stats()
        self._show_feedback(False, q["dogru_cevap"], timeout=True)
        self._on_question_solved()

    # ─────────────────────────────────────────
    # ÜNİTE KAYIT
    # ─────────────────────────────────────────

    def _record_unite(self, unite: str, correct: bool):
        if unite not in self.unite_stats:
            self.unite_stats[unite] = {"d": 0, "y": 0}
        if correct:
            self.unite_stats[unite]["d"] += 1
        else:
            self.unite_stats[unite]["y"] += 1

    # ─────────────────────────────────────────
    # SAĞ PANEL: DURUMLAR
    # ─────────────────────────────────────────

    def _clear_right_panel(self):
        for w in self.question_panel.winfo_children():
            w.destroy()
        self.q_canvas.yview_moveto(0)

    def _animate_slide_in(self, frame):
        # Forget layout managers first
        frame.pack_forget()
        frame.place_forget()
        
        # Start offscreen bottom
        frame.place(relx=0.0, rely=1.0, relwidth=1.0, relheight=1.0)
        frame.lift()
        
        steps = 15
        delay = 12
        
        def step(i):
            if not frame.winfo_exists():
                return
            if i > steps:
                frame.place_forget()
                frame.pack(fill="both", expand=True)
                return
            progress = i / steps
            eased = 1.0 - (1.0 - progress) ** 3  # cubic ease-out
            rely = 1.0 - eased
            frame.place(rely=rely)
            self.after(delay, lambda: step(i + 1))
            
        step(0)

    def _switch_stage(self, stage: str):
        # Unpack all main views first
        self.grade_unit_frame.pack_forget()
        self.wheel_frame.pack_forget()
        self.question_frame.pack_forget()
        self.grade_unit_frame.place_forget()
        self.wheel_frame.place_forget()
        self.question_frame.place_forget()
        
        # HUD Status Bar visibility management
        if stage in (self.STATE_GRADE_SELECT, self.STATE_UNIT_SELECT, self.STATE_MODE_SELECT):
            self.status_bar.pack_forget()
        else:
            self.status_bar.pack(fill="x", side="top", after=self.top_bar)
            
        # Target frame selection
        target_frame = None
        if stage in (self.STATE_GRADE_SELECT, self.STATE_UNIT_SELECT, self.STATE_MODE_SELECT):
            target_frame = self.grade_unit_frame
        elif stage in (self.STATE_IDLE, self.STATE_SPINNING):
            target_frame = self.wheel_frame
            self._handle_resize()
        elif stage in (self.STATE_QUESTION, self.STATE_ANSWERED):
            target_frame = self.question_frame
            
        if target_frame:
            self._animate_slide_in(target_frame)

    def _clear_grade_unit_panel(self):
        for w in self.grade_unit_panel.winfo_children():
            w.destroy()
        self.grade_unit_canvas.yview_moveto(0)

    def _show_grade_selection(self):
        """Sınıf seçim ekranını gösterir."""
        self.state = self.STATE_GRADE_SELECT
        self.selected_grade = None
        self._clear_grade_unit_panel()
        self._switch_stage(self.STATE_GRADE_SELECT)
        f = self.grade_unit_panel
        t = self.t

        # Başlık
        tk.Frame(f, height=30, bg=t["bg_card"]).pack()
        tk.Label(f, text="📚", font=tkfont.Font(size=42),
                 bg=t["bg_card"], fg=t["accent"]).pack(pady=(10, 4))
        tk.Label(f, text="Sınıf Düzeyini Seçiniz",
                 font=self.f_title, bg=t["bg_card"], fg=t["fg"]).pack(pady=(4, 6))
        tk.Label(f, text="Oynamak istediğiniz sınıf düzeyine tıklayın",
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(0, 12))

        # Sınıf butonları 2x2 grid (web versiyonundaki 3D resimli kartlar)
        grid_frame = tk.Frame(f, bg=t["bg_card"])
        grid_frame.pack(padx=20, pady=4)

        # Kart arka planı: parşömen üzerinde koyu kart
        card_bg = "#241208" if self.current_theme == "energy" else t["option_bg"]
        card_fg = t["fg"]
        card_dim = t["fg_dim"]
        img_size = max(56, int(86 * self.scale))

        for i, (grade, info) in enumerate(GRADE_INFO.items()):
            if grade not in self.questions_db:
                continue
            q_count = len(self.questions_db[grade])
            unites = set(q["unite"] for q in self.questions_db[grade])

            row, col = divmod(i, 2)
            btn_frame = tk.Frame(grid_frame, bg=card_bg, cursor="hand2",
                                 padx=18, pady=16,
                                 highlightbackground=info["color"],
                                 highlightcolor=info["color"], highlightthickness=2)
            btn_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            children = []

            # 3D sınıf görseli (web/assets/grade_X.png) – yoksa emoji'ye düş
            grade_img = self._get_image(GRADE_IMAGES.get(grade, ""), img_size, img_size) if grade in GRADE_IMAGES else None
            if grade_img is not None:
                img_lbl = tk.Label(btn_frame, image=grade_img, bg=card_bg)
                img_lbl.image = grade_img
                img_lbl.pack(pady=(2, 8))
                children.append(img_lbl)
            else:
                emoji_lbl = tk.Label(btn_frame, text=info["emoji"],
                                     font=tkfont.Font(size=max(20, int(30 * self.scale))),
                                     bg=card_bg, fg=info["color"])
                emoji_lbl.pack(pady=(2, 6))
                children.append(emoji_lbl)

            name_lbl = tk.Label(btn_frame, text=info["label"],
                                font=self.f_big, bg=card_bg, fg=card_fg)
            name_lbl.pack()
            children.append(name_lbl)

            desc_lbl = tk.Label(btn_frame, text=info["desc"],
                                font=self.f_small, bg=card_bg, fg=card_dim)
            desc_lbl.pack()
            children.append(desc_lbl)

            count_lbl = tk.Label(btn_frame, text=f"{q_count} soru | {len(unites)} ünite",
                                 font=self.f_small, bg=card_bg, fg=card_dim)
            count_lbl.pack(pady=(4, 0))
            children.append(count_lbl)

            # Tıklama + hover (kenarlık vurgusu)
            for w in (btn_frame, *children):
                w.bind("<Button-1>", lambda e, g=grade: self._select_grade(g))
                w.bind("<Enter>", lambda e, bf=btn_frame, c=info["hover"]:
                       bf.config(highlightbackground=c, highlightcolor=c, highlightthickness=3))
                w.bind("<Leave>", lambda e, bf=btn_frame, c=info["color"]:
                       bf.config(highlightbackground=c, highlightcolor=c, highlightthickness=2))

        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)

        # Alt bilgi
        total = sum(len(v) for v in self.questions_db.values())
        tk.Label(f, text=f"Toplam {total} soru | 4 sınıf düzeyi",
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(14, 4))

    def _select_grade(self, grade: str):
        """Kullanıcı sınıf seçti → Ünite Seçim ekranını göster."""
        self.selected_grade = grade
        self.state = self.STATE_UNIT_SELECT
        self._show_unit_selection()

    def _show_unit_selection(self):
        self._clear_grade_unit_panel()
        self._switch_stage(self.STATE_UNIT_SELECT)
        f = self.grade_unit_panel
        t = self.t
        grade = self.selected_grade
        info = GRADE_INFO[grade]
        
        # Başlık
        tk.Frame(f, height=20, bg=t["bg_card"]).pack()
        tk.Label(f, text="📖", font=tkfont.Font(size=36),
                 bg=t["bg_card"], fg=info["color"]).pack(pady=(10, 4))
        tk.Label(f, text="Çalışmak İstediğiniz Üniteyi Seçin",
                 font=self.f_title, bg=t["bg_card"], fg=t["fg"]).pack(pady=(4, 6))
        tk.Label(f, text=f"Sınıf: {info['label']} {info['desc']}",
                 font=self.f_normal, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(0, 12))
                 
        # Üniteleri listele
        questions = self.questions_db[grade]
        unites = sorted(list(set(q["unite"] for q in questions)))
        
        # Liste çerçevesi
        scroll_frame = tk.Frame(f, bg=t["bg_card"])
        scroll_frame.pack(padx=20, pady=4, fill="both", expand=True)
        
        # Tüm Üniteler Butonu (Öncelikli)
        all_btn_frame = tk.Frame(scroll_frame, bg="#2d1c12" if self.current_theme == "energy" else t["option_bg"],
                                 cursor="hand2", padx=16, pady=12,
                                 highlightbackground=t["accent"], highlightthickness=2)
        all_btn_frame.pack(fill="x", pady=6)
        
        all_lbl_title = tk.Label(all_btn_frame, text="📚 Tüm Ünitelerden Karışık Oyna",
                                 font=self.f_big, bg=all_btn_frame.cget("bg"), fg=t["fg"])
        all_lbl_title.pack(side="left")
        all_lbl_count = tk.Label(all_btn_frame, text=f"{len(questions)} Soru",
                                 font=self.f_small, bg=all_btn_frame.cget("bg"), fg=t["fg_dim"])
        all_lbl_count.pack(side="right")
        
        # Bind click
        for w in (all_btn_frame, all_lbl_title, all_lbl_count):
            w.bind("<Button-1>", lambda e: self._start_game_with_unit("ALL"))
            
        # Her bir ünite için buton oluştur
        for unite in unites:
            u_questions = [q for q in questions if q["unite"] == unite]
            u_btn_frame = tk.Frame(scroll_frame, bg="#241208" if self.current_theme == "energy" else t["option_bg"],
                                     cursor="hand2", padx=16, pady=10,
                                     highlightbackground=t["border"], highlightthickness=1)
            u_btn_frame.pack(fill="x", pady=4)
            
            u_lbl_title = tk.Label(u_btn_frame, text=f"📖 {unite}",
                                     font=self.f_normal, bg=u_btn_frame.cget("bg"), fg=t["fg"],
                                     wraplength=int(600 * self.scale), justify="left")
            u_lbl_title.pack(side="left", anchor="w")
            u_lbl_count = tk.Label(u_btn_frame, text=f"{len(u_questions)} Soru",
                                     font=self.f_small, bg=u_btn_frame.cget("bg"), fg=t["fg_dim"])
            u_lbl_count.pack(side="right")
            
            # Bind
            for w in (u_btn_frame, u_lbl_title, u_lbl_count):
                w.bind("<Button-1>", lambda e, u=unite: self._start_game_with_unit(u))
                w.bind("<Enter>", lambda e, bf=u_btn_frame: bf.config(highlightbackground=t["accent"], highlightthickness=2))
                w.bind("<Leave>", lambda e, bf=u_btn_frame: bf.config(highlightbackground=t["border"], highlightthickness=1))

        # Geri Dön butonu
        back_btn = tk.Label(f, text="← Sınıf Seçimine Dön", font=self.f_normal,
                            bg=t["skip_bg"], fg=t["skip_fg"], cursor="hand2", padx=20, pady=8)
        back_btn.pack(pady=10)
        back_btn.bind("<Button-1>", lambda e: self._return_to_main_menu())

    def _start_game_with_unit(self, unit: str):
        self.selected_unit = unit
        if unit == "ALL":
            self.all_questions = list(self.questions_db[self.selected_grade])
        else:
            self.all_questions = [q for q in self.questions_db[self.selected_grade] if q["unite"] == unit]
            
        self._refill_pool()
        
        # Başlığı güncelle
        info = GRADE_INFO[self.selected_grade]
        self.title(f"LGS {info['label']} {info['desc']} – Çark Oyunu  v3")
        self.lbl_title.config(text=f"🏛  {info['label']} {info['desc']} – Çark Oyunu")
        
        # Oyun durumunu sıfırla
        self.state          = self.STATE_IDLE
        self.total_score    = 0
        self.correct_count  = 0
        self.wrong_count    = 0
        self.solved_count   = 0
        self.current_q      = None
        self.current_points = 0
        self.selected_opt   = None
        self.wheel_angle    = 0.0
        self.unite_stats    = {}
        self._update_stats()
        self._draw_wheel()
        
        # Oyun modu seçim ekranını göster
        self._show_mode_selection_panel()

    def _show_mode_selection_panel(self):
        self.state = self.STATE_MODE_SELECT
        self._clear_grade_unit_panel()
        self._switch_stage(self.STATE_MODE_SELECT)
        
        f = self.grade_unit_panel
        t = self.t
        
        # Üst Bilgi
        tk.Label(f, text="Oyun Modunu Seçiniz", font=self.f_title,
                 bg=t["bg_card"], fg=t["accent"]).pack(pady=(15, 2))
        tk.Label(f, text="Oyunu tek kişi mi, yoksa sınıfta iki grup halinde mi oynamak istersiniz?",
                 font=self.f_normal, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(0, 15))
                 
        card_w = max(280, int(350 * self.scale))
        card_h = max(160, int(200 * self.scale))
        
        # Kartlar için container
        grid_frame = tk.Frame(f, bg=t["bg_card"])
        grid_frame.pack(pady=10)
        
        # Bireysel Mod Kartı
        b_frame = tk.Frame(grid_frame, bg=t["bg_card"], highlightbackground=t["border"],
                           highlightthickness=1, width=card_w, height=card_h)
        b_frame.pack_propagate(False)
        b_frame.grid(row=0, column=0, padx=15, pady=10)
        
        tk.Label(b_frame, text="👤", font=tkfont.Font(size=40), bg=t["bg_card"], fg="#ffd54f").pack(pady=(15, 5))
        tk.Label(b_frame, text="Bireysel Mod", font=self.f_big, bg=t["bg_card"], fg=t["fg"]).pack()
        tk.Label(b_frame, text="Tek oyunculu klasik LGS hazırlık modu", font=self.f_small,
                 bg=t["bg_card"], fg=t["fg_dim"], wraplength=card_w - 40, justify="center").pack(pady=(5, 10))
                 
        # Grup Modu Kartı
        g_frame = tk.Frame(grid_frame, bg=t["bg_card"], highlightbackground=t["border"],
                           highlightthickness=1, width=card_w, height=card_h)
        g_frame.pack_propagate(False)
        g_frame.grid(row=0, column=1, padx=15, pady=10)
        
        tk.Label(g_frame, text="👥", font=tkfont.Font(size=40), bg=t["bg_card"], fg="#00e5ff").pack(pady=(15, 5))
        tk.Label(g_frame, text="Grup Modu (Sınıf)", font=self.f_big, bg=t["bg_card"], fg=t["fg"]).pack()
        tk.Label(g_frame, text="Sınıfı 2 takıma (A vs B) bölerek yarışma modu", font=self.f_small,
                 bg=t["bg_card"], fg=t["fg_dim"], wraplength=card_w - 40, justify="center").pack(pady=(5, 10))

        # Hover ve Klik Efektleri
        for frm, is_team in [(b_frame, False), (g_frame, True)]:
            for w in (frm, *frm.winfo_children()):
                w.bind("<Button-1>", lambda e, it=is_team: self._select_mode(it))
                w.config(cursor="hand2")
                w.bind("<Enter>", lambda e, bf=frm: bf.config(highlightbackground=t["accent"], highlightthickness=2))
                w.bind("<Leave>", lambda e, bf=frm: bf.config(highlightbackground=t["border"], highlightthickness=1))

        # Geri Dön butonu
        back_btn = tk.Label(f, text="← Ünite Seçimine Dön", font=self.f_normal,
                             bg=t["skip_bg"], fg=t["skip_fg"], cursor="hand2", padx=20, pady=8)
        back_btn.pack(pady=20)
        back_btn.bind("<Button-1>", lambda e: self._show_unit_selection())

    def _select_mode(self, is_team: bool):
        self.is_team_mode = is_team
        self.team_scores = {"A": 0, "B": 0}
        self.active_team = "A"
        self.team_correct = 0
        self.team_wrong = 0
        self.total_score = 0
        self.correct_count = 0
        self.wrong_count = 0
        self.solved_count = 0
        
        self._update_stats()
        self._draw_wheel()
        
        # Çark ekranına geç
        self.state = self.STATE_IDLE
        self._switch_stage(self.STATE_IDLE)
        self._clear_right_panel()
        self._show_idle_panel()

    def _show_special_panel(self, title: str, msg: str, color: str):
        self._switch_stage(self.STATE_QUESTION) # Soru çerçevesini göster
        f = self.question_panel
        t = self.t
        
        # 3D Canvas
        canvas_w, canvas_h = 350, 220
        self.special_3d_canvas = tk.Canvas(f, width=canvas_w, height=canvas_h,
                                           bg=t["bg_card"], highlightthickness=0)
        self.special_3d_canvas.pack(pady=(15, 5))
        
        # 3D Math parameters
        self.vertices_3d = [
            [0, -60, 0],   # Top
            [0, 60, 0],    # Bottom
            [-45, 0, -45], # Mid front-left
            [45, 0, -45],  # Mid front-right
            [45, 0, 45],   # Mid back-right
            [-45, 0, 45]   # Mid back-left
        ]
        self.edges_3d = [
            (0, 2), (0, 3), (0, 4), (0, 5),
            (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 3), (3, 4), (4, 5), (5, 2)
        ]
        
        # Set rotation speed based on event type
        self.rot_x, self.rot_y, self.rot_z = 0.0, 0.0, 0.0
        self.rot_speed_x = 1.2
        self.rot_speed_y = 2.4
        self.rot_speed_z = 0.8
        
        if "İFLAS" in title:
            self.rot_speed_x, self.rot_speed_y = 2.0, 4.0
        elif "X2" in title:
            self.rot_speed_x, self.rot_speed_y = 3.0, 1.5
            
        # Start animation loop
        self._animate_special_3d(color)
        
        # Text and button
        tk.Label(f, text=title, font=tkfont.Font(size=36, weight="bold"), bg=t["bg_card"], fg=color).pack(pady=2)
        tk.Label(f, text=msg, font=self.f_big, bg=t["bg_card"], fg=t["fg"], justify="center", wraplength=380).pack(pady=5)
        
        # Devam et butonu
        btn_text = "Oyuna Başla ▶" if (hasattr(self, "special_is_x2") and self.special_is_x2) else "Devam Et (Çarkı Çevir) ▶"
        btn_cont = tk.Label(f, text=btn_text, font=self.f_big, bg=t["btn_bg"], fg=t["btn_fg"], padx=20, pady=10, cursor="hand2")
        btn_cont.pack(pady=(10, 15))
        btn_cont.bind("<Button-1>", lambda e: self._continue_from_special())

    def _animate_special_3d(self, color: str):
        if not hasattr(self, "special_3d_canvas") or not self.special_3d_canvas.winfo_exists():
            return
            
        canvas = self.special_3d_canvas
        canvas.delete("all")
        
        # Increment angles
        self.rot_x += self.rot_speed_x
        self.rot_y += self.rot_speed_y
        self.rot_z += self.rot_speed_z
        
        # Math helper for rotation
        import math
        rx, ry, rz = math.radians(self.rot_x), math.radians(self.rot_y), math.radians(self.rot_z)
        
        cx, cy = 175, 110 # Canvas center
        distance = 250
        
        # Projected 2D points
        proj_points = []
        for x, y, z in self.vertices_3d:
            # Rotate X
            cos_x, sin_x = math.cos(rx), math.sin(rx)
            y1, z1 = y * cos_x - z * sin_x, y * sin_x + z * cos_x
            # Rotate Y
            cos_y, sin_y = math.cos(ry), math.sin(ry)
            x2, z2 = x * cos_y + z1 * sin_y, -x * sin_y + z1 * cos_y
            # Rotate Z
            cos_z, sin_z = math.cos(rz), math.sin(rz)
            x3, y3 = x2 * cos_z - y1 * sin_z, x2 * sin_z + y1 * cos_z
            
            # Perspective projection
            factor = distance / (z2 + distance)
            px = int(x3 * factor + cx)
            py = int(y3 * factor + cy)
            proj_points.append((px, py))
            
        # Draw edges with glowing shadow lines
        for u, v in self.edges_3d:
            p1, p2 = proj_points[u], proj_points[v]
            # Shadow glow line
            canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=color, width=4)
            # Solid line
            canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#ffffff", width=2)
            
        # Draw small neon vertex nodes
        for px, py in proj_points:
            canvas.create_oval(px - 4, py - 4, px + 4, py + 4, fill=color, outline="#ffffff", width=1)
            
        # Call next frame at 60fps (~16ms)
        self.after(16, lambda: self._animate_special_3d(color))
        
    def _continue_from_special(self):
        if hasattr(self, "special_is_x2") and self.special_is_x2:
            self.state = self.STATE_QUESTION
            self._clear_right_panel()
            self._switch_stage(self.STATE_QUESTION)
            self._show_question_panel()
            self._start_timer()
        else:
            self.state = self.STATE_IDLE
            if self.is_team_mode:
                self.active_team = "B" if self.active_team == "A" else "A"
            self._update_stats()
            self._switch_stage(self.STATE_IDLE)
            self._clear_right_panel()
            self._show_idle_panel()

    def _show_idle_panel(self):
        self._clear_right_panel()
        f = self.question_panel
        t = self.t

        tk.Frame(f, height=80, bg=t["bg_card"]).pack()
        tk.Label(f, text="🎡", font=tkfont.Font(size=52),
                 bg=t["bg_card"], fg=t["accent"]).pack(pady=(10, 4))
        tk.Label(f, text="Çarkı çevirerek\nbir puan belirleyin!",
                 font=self.f_big, bg=t["bg_card"], fg=t["fg"], justify="center").pack(pady=10)

        grade_info_text = ""
        if self.selected_grade and self.selected_grade in GRADE_INFO:
            info = GRADE_INFO[self.selected_grade]
            unites = set(q["unite"] for q in self.all_questions)
            grade_info_text = f"{info['emoji']} {info['label']} {info['desc']}  |  {len(self.all_questions)} soru  |  {len(unites)} unite"
        else:
            grade_info_text = f"Soru havuzu: {len(self.all_questions)} soru"

        tk.Label(f, text=grade_info_text,
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack()
        tk.Label(f, text="Doğru: +çark puanı +10  |  Yanlış/Süre: −5",
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(4, 0))

    def _show_spinning_panel(self):
        self._clear_right_panel()
        f = self.question_panel
        t = self.t
        tk.Frame(f, height=120, bg=t["bg_card"]).pack()
        tk.Label(f, text="⏳  Çark dönüyor…",
                 font=self.f_big, bg=t["bg_card"], fg=t["accent"]).pack(pady=20)

    def _show_question_panel(self):
        f = self.question_panel
        t = self.t
        q = self.current_q

        # ── Puan + Timer banner ──
        if self.x2_mode:
            banner_bg  = "#7a5a00"
            banner_txt = "⚡  X2 – Doğru cevaplarsan TOPLAM PUANIN 2 KATINA çıkar!"
        else:
            banner_bg  = t["btn_bg"]
            banner_txt = f"🎯  Bu soru  {self.current_points}  puan değerinde!"

        # Dairesel timer (Canvas tabanlı)
        timer_size = max(56, int(76 * self.scale))
        
        banner = tk.Frame(f, bg=banner_bg, height=timer_size + 8)
        banner.pack(fill="x")
        banner.pack_propagate(False)

        tk.Label(banner,
                 text=banner_txt,
                 font=self.f_big, bg=banner_bg, fg="#ffffff").pack(side="left", padx=int(14 * self.scale), expand=True)

        self.timer_canvas = tk.Canvas(banner, width=timer_size, height=timer_size,
                                       highlightthickness=0, bg=banner_bg)
        self.timer_canvas.pack(side="right", padx=int(10 * self.scale))
        self._timer_size = timer_size

        # Timer progress bar (linear - daha belirgin)
        self.timer_bar_bg = tk.Frame(f, bg=t["border"], height=max(6, int(8 * self.scale)))
        self.timer_bar_bg.pack(fill="x")
        self.timer_bar_fill = tk.Frame(self.timer_bar_bg, bg=t["timer_normal"],
                                        height=max(6, int(8 * self.scale)))
        self.timer_bar_fill.place(relx=0, rely=0, relwidth=1, relheight=1)

        # ── Meta ──
        meta_frame = tk.Frame(f, bg=t["bg_card"])
        meta_frame.pack(fill="x", padx=6, pady=(6, 4))
        for icon_c, val in [("📚", q["unite"]), ("📌", q["konu"]),
                             ("⚡", q["zorluk"])]:
            row = tk.Frame(meta_frame, bg=t["bg_card"])
            row.pack(fill="x", pady=1, padx=6)
            tk.Label(row, text=icon_c, font=self.f_normal,
                     bg=t["bg_card"], fg=t["fg_dim"], width=3).pack(side="left")
            tk.Label(row, text=val, font=self.f_small,
                     bg=t["bg_card"], fg=t["fg_dim"], anchor="w").pack(side="left")

        # ── Ayırıcı ──
        tk.Frame(f, height=1, bg=t["border"]).pack(fill="x", padx=10, pady=4)

        # ── Görsel Soru Desteği ──
        if HAS_PIL and q.get("gorsel"):
            try:
                img_path = resource_path(q["gorsel"])
                if os.path.exists(img_path):
                    pil_img = PILImage.open(img_path)
                    # 350x180 px safely resized
                    resized = pil_img.resize((350, 180), PILImage.Resampling.LANCZOS if hasattr(PILImage, "Resampling") else PILImage.ANTIALIAS)
                    self._tk_q_img = PILImageTk.PhotoImage(resized)
                    
                    img_lbl = tk.Label(f, image=self._tk_q_img, bg=t["bg_card"])
                    img_lbl.pack(pady=8)
                else:
                    print(f"Görsel bulunamadı (Safe Fallback): {img_path}")
            except Exception as e:
                print("Görsel yüklenirken hata oluştu (Safe Fallback):", e)

        # ── Soru metni ──
        tk.Label(f, text=q["soru"], font=self.f_big,
                 bg=t["bg_card"], fg=t["fg"], wraplength=self._get_wraplength(),
                 justify="left", anchor="nw", padx=int(12 * self.scale),
                 pady=int(10 * self.scale)).pack(fill="x")

        # ── Şıklar ──
        self.option_widgets: Dict[str, tk.Frame] = {}
        self.option_labels:  Dict[str, tk.Label] = {}

        for key in ["A", "B", "C", "D"]:
            frm = tk.Frame(f, bg=t["option_bg"], cursor="hand2",
                           highlightbackground=t["border"], highlightthickness=1,
                           padx=14, pady=10)
            frm.pack(fill="x", padx=10, pady=3)
            
            lbl = tk.Label(frm,
                           text=f"{key})  {q['siklar'][key]}",
                           font=self.f_option, bg=t["option_bg"], fg=t["option_fg"],
                           anchor="w", wraplength=self._get_opt_wraplength(), justify="left")
            lbl.pack(fill="x", pady=1)
            for w in (frm, lbl):
                w.bind("<Button-1>", lambda e, k=key: self._select_option(k))
                w.bind("<Enter>", lambda e, fr=frm, lb=lbl: (
                    fr.config(bg=t["option_hover"]),
                    lb.config(bg=t["option_hover"])
                ))
                w.bind("<Leave>", lambda e, fr=frm, lb=lbl, k=key: (
                    fr.config(bg=t["option_sel"] if self.selected_opt == k else t["option_bg"]),
                    lb.config(bg=t["option_sel"] if self.selected_opt == k else t["option_bg"])
                ))
            self.option_widgets[key] = frm
            self.option_labels[key]  = lbl

        # ── Alt butonlar ──
        btn_row = tk.Frame(f, bg=t["bg_card"])
        btn_row.pack(fill="x", padx=10, pady=(10, 6))

        self.btn_answer = tk.Label(
            btn_row, text="✓  Cevapla", font=self.f_big,
            bg=t["btn_bg"], fg=t["btn_fg"],
            padx=28, pady=10, cursor="hand2"
        )
        self.btn_answer.pack(side="left", expand=True, fill="x", padx=(0, 6))
        self.btn_answer.bind("<Button-1>", lambda _: self._submit_answer())

        self.btn_skip = tk.Label(
            btn_row, text="⏩  Geç", font=self.f_normal,
            bg=t["skip_bg"], fg=t["skip_fg"],
            padx=22, pady=10, cursor="hand2"
        )
        self.btn_skip.pack(side="left", padx=(4, 0))
        self.btn_skip.bind("<Button-1>", lambda _: self._skip_question())

    def _select_option(self, key: str):
        if self.state != self.STATE_QUESTION:
            return
        self.selected_opt = key
        t = self.t
        for k, frm in self.option_widgets.items():
            if k == key:
                frm.config(bg=t["option_sel"],
                           highlightbackground=t["option_sel_border"],
                           highlightthickness=2)
                self.option_labels[k].config(bg=t["option_sel"])
            else:
                frm.config(bg=t["option_bg"],
                           highlightbackground=t["border"],
                           highlightthickness=1)
                self.option_labels[k].config(bg=t["option_bg"])

    def _submit_answer(self):
        if self.state != self.STATE_QUESTION or self.selected_opt is None:
            return
        self._stop_timer()
        self.state = self.STATE_ANSWERED
        q = self.current_q
        correct     = q["dogru_cevap"]
        is_correct  = self.selected_opt == correct

        self.solved_count += 1
        was_x2 = self.x2_mode
        if self.is_team_mode:
            if is_correct:
                self.team_correct += 1
                if was_x2:
                    earned = self.team_scores[self.active_team]
                else:
                    earned = self.current_points + BONUS_CORRECT
                self.team_scores[self.active_team] += earned
            else:
                self.team_wrong += 1
                self.team_scores[self.active_team] -= PENALTY_WRONG
        else:
            if is_correct:
                self.correct_count += 1
                if was_x2:
                    self.total_score = self.total_score * 2
                else:
                    self.total_score += self.current_points + BONUS_CORRECT
                    
                # --- Rozet Sistemi ---
                badges_earned = []
                if self.selected_grade == "8" and self.current_points == 100:
                    badges_earned.append({
                        "name": "Tarih Dehası",
                        "desc": "8. Sınıfta 100 puanlık soruyu doğru bildin! Tarihin gerçek lideri sensin! 👑",
                        "emoji": "🎓"
                    })
                if self.last_spin_was_iflas:
                    badges_earned.append({
                        "name": "Yıkılmadım",
                        "desc": "İflas ettikten sonra ilk soruyu doğru bildin! Küllerinden doğdun! 🔥",
                        "emoji": "🦅"
                    })
                
                # Rozet pop-up'larını göster
                for i, badge in enumerate(badges_earned):
                    self.after(i * 4200, lambda b=badge: self._show_badge_popup(b["name"], b["desc"], b["emoji"]))
            else:
                self.wrong_count   += 1
                self.total_score   -= PENALTY_WRONG
        self.x2_mode = False
        self.last_spin_was_iflas = False

        self._record_unite(q["unite"], is_correct)
        self._update_stats()
        self._show_feedback(is_correct, correct, was_x2=was_x2)
        self._on_question_solved()

    def _skip_question(self):
        if self.state not in (self.STATE_QUESTION, self.STATE_ANSWERED):
            return
        self._stop_timer()
        self.state = self.STATE_IDLE
        if self.is_team_mode:
            self.active_team = "B" if self.active_team == "A" else "A"
        self._update_stats()
        self._clear_right_panel()
        self._switch_stage(self.STATE_IDLE)
        self._show_idle_panel()

    def _show_feedback(self, is_correct: bool, correct_key: str, timeout: bool = False, was_x2: bool = False):
        self._stop_timer()
        t = self.t
        q = self.current_q

        # Renklendirme
        for k, frm in self.option_widgets.items():
            if k == correct_key:
                frm.config(bg=t["success"], highlightbackground=t["success"], highlightthickness=2)
                self.option_labels[k].config(bg=t["success"], fg="#ffffff")
            elif k == self.selected_opt and not is_correct:
                frm.config(bg=t["error"], highlightbackground=t["error"], highlightthickness=2)
                self.option_labels[k].config(bg=t["error"], fg="#ffffff")
            for w in (frm, self.option_labels[k]):
                w.unbind("<Button-1>")
                w.config(cursor="arrow")

        self.btn_answer.unbind("<Button-1>")
        self.btn_answer.config(bg=t["border"], cursor="arrow")

        # Timer bar → sıfır veya dolu
        if hasattr(self, "timer_bar_fill") and self.timer_bar_fill.winfo_exists():
            self.timer_bar_fill.config(bg=t["error"] if not is_correct else t["success"])
            self.timer_bar_fill.place(relx=0, rely=0, relheight=1,
                                      width=0 if timeout else None,
                                      relwidth=None if timeout else 1)

        # Sonuç mesajı
        f = self.question_panel
        rf = tk.Frame(f, bg=t["bg_card"])
        rf.pack(fill="x", padx=10, pady=(4, 2))

        if timeout:
            msg       = f"⏰  Süre Doldu!  −{PENALTY_WRONG} puan"
            msg_color = t["error"]
            self._play_sound("fail")
        elif is_correct:
            self._play_sound("win")
            if was_x2:
                msg = f"🎉  Doğru!  Toplam puanın 2 katına çıktı → {self.total_score}"
            else:
                bonus = self.current_points + BONUS_CORRECT
                msg   = f"🎉  Doğru!  +{bonus} puan kazandınız!"
            msg_color = t["success"]
        else:
            msg   = f"❌  Yanlış!  Doğru cevap: {correct_key}  −{PENALTY_WRONG} puan"
            msg_color = t["error"]
            self._play_sound("wrong")

        tk.Label(rf, text=msg, font=self.f_big,
                 bg=t["bg_card"], fg=msg_color).pack(pady=4)

        # Açıklama
        if q.get("aciklama"):
            tk.Label(rf,
                     text=f"💡  {q['aciklama']}",
                     font=self.f_normal, bg=t["bg_card"], fg=t["fg_dim"],
                     wraplength=self._get_wraplength(), justify="left", anchor="nw"
                     ).pack(fill="x", padx=4, pady=(2, 6))

        self.btn_skip.config(text="▶  Devam Et")

    # ─────────────────────────────────────────
    # İSTATİSTİK EKRANI
    # ─────────────────────────────────────────

    def _show_stats_panel(self):
        self._stop_timer()
        self._clear_right_panel()
        self._switch_stage(self.STATE_QUESTION)
        f = self.question_panel
        t = self.t

        # Başlık
        hdr = tk.Frame(f, bg=t["accent"], height=46)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        tk.Label(hdr, text="📊  Ünite Bazlı İstatistik",
                 font=self.f_big, bg=t["accent"], fg="#ffffff"
                 ).pack(expand=True)

        # Genel özet
        total = self.correct_count + self.wrong_count
        pct   = int(100 * self.correct_count / total) if total else 0

        ozet = tk.Frame(f, bg=t["bg_card"])
        ozet.pack(fill="x", padx=10, pady=8)
        for txt, val, col in [
            ("Toplam Soru", str(total), t["fg"]),
            ("Doğru", str(self.correct_count), t["success"]),
            ("Yanlış", str(self.wrong_count), t["error"]),
            ("Puan", str(self.total_score), t["accent"]),
            ("Başarı", f"%{pct}", t["warning"]),
        ]:
            col_f = tk.Frame(ozet, bg=t["bg_card"])
            col_f.pack(side="left", expand=True)
            tk.Label(col_f, text=val, font=self.f_score, bg=t["bg_card"], fg=col).pack()
            tk.Label(col_f, text=txt, font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack()

        tk.Frame(f, height=1, bg=t["border"]).pack(fill="x", padx=10, pady=4)

        # Ünite tablosu başlığı
        header_frame = tk.Frame(f, bg=t["border"])
        header_frame.pack(fill="x", padx=10, pady=(0, 2))
        for col_txt, w in [("Ünite", 38), ("✓", 8), ("✗", 8), ("%", 8)]:
            tk.Label(header_frame, text=col_txt, font=self.f_small,
                     bg=t["border"], fg=t["fg"], width=w, anchor="w"
                     ).pack(side="left", padx=2)

        # Ünite satırları
        all_unites = sorted(set(q["unite"] for q in self.all_questions))
        for unite in all_unites:
            stats = self.unite_stats.get(unite, {"d": 0, "y": 0})
            d, y  = stats["d"], stats["y"]
            tot   = d + y
            p     = int(100 * d / tot) if tot else 0
            short = unite.split("–")[-1].strip() if "–" in unite else unite

            row = tk.Frame(f, bg=t["bg_card"],
                           highlightbackground=t["border"], highlightthickness=1)
            row.pack(fill="x", padx=10, pady=2)
            tk.Label(row, text=short, font=self.f_small,
                     bg=t["bg_card"], fg=t["fg"], anchor="w", width=38
                     ).pack(side="left", padx=(6, 2), pady=4)
            tk.Label(row, text=str(d), font=self.f_small,
                     bg=t["bg_card"], fg=t["success"], width=8).pack(side="left")
            tk.Label(row, text=str(y), font=self.f_small,
                     bg=t["bg_card"], fg=t["error"], width=8).pack(side="left")
            tk.Label(row, text=f"%{p}", font=self.f_small,
                     bg=t["bg_card"], fg=t["warning"], width=8).pack(side="left")

            # Mini bar
            if tot > 0:
                bar_frame = tk.Frame(row, bg=t["border"], height=6, width=120)
                bar_frame.pack(side="left", padx=8, pady=4)
                bar_frame.pack_propagate(False)
                filled = tk.Frame(bar_frame, bg=t["success"] if p > 50 else t["error"],
                                  height=6)
                filled.place(relx=0, rely=0, relheight=1, relwidth=p/100)

        tk.Frame(f, height=1, bg=t["border"]).pack(fill="x", padx=10, pady=8)

        # AI Guidance Box
        weak_units = []
        has_data = False
        for unite in all_unites:
            stats = self.unite_stats.get(unite, {"d": 0, "y": 0})
            d, y = stats["d"], stats["y"]
            tot = d + y
            if tot > 0:
                has_data = True
                if d / tot < 0.70:
                    weak_units.append((unite, int(100 * d / tot)))
                    
        ai_frame = tk.Frame(f, bg="#241208" if self.current_theme == "energy" else t["bg_card"],
                            highlightcolor=t["accent"], highlightthickness=1, padx=12, pady=10)
        ai_frame.pack(fill="x", padx=10, pady=8)
        
        tk.Label(ai_frame, text="🧠  Rehber Öğretmen Yapay Zeka Tavsiyesi", font=self.f_big,
                 bg=ai_frame.cget("bg"), fg=t["accent"], anchor="w").pack(fill="x")
                 
        if not has_data:
            rec_text = "💡 Henüz analiz edilecek bir soru çözmediniz. Soruları çözdükçe size özel tavsiyeler burada görünecektir."
        elif not weak_units:
            rec_text = "🎯 Tebrikler! Çalıştığınız tüm ünitelerde %70'in üzerinde yüksek bir başarı oranına sahipsiniz. LGS hazırlığınız harika gidiyor! 🚀"
        else:
            rec_text = "Konu başarı analizinize göre eksik olduğunuz konular tespit edildi:\n"
            for u_name, u_pct in weak_units:
                rec = PYTHON_STUDY_RECS.get(u_name, "Bu üniteyle ilgili konu özetlerini tekrar çalışmalısınız.")
                rec_text += f"\n• {u_name} (Başarı: %{u_pct}): {rec}\n"
                
        tk.Label(ai_frame, text=rec_text, font=self.f_small, bg=ai_frame.cget("bg"), fg=t["fg"],
                 justify="left", anchor="nw", wraplength=int(600 * self.scale)).pack(fill="x", pady=4)

        # Sosyal Paylaşım Butonu
        share_btn = tk.Label(
            f, text="✨ Skorunu Kopyala ve Paylaş", font=self.f_big,
            bg="#aa382c", fg="#ffffff", padx=20, pady=10, cursor="hand2"
        )
        share_btn.pack(fill="x", padx=10, pady=(0, 8))
        share_btn.bind("<Button-1>", lambda _: self._share_score(share_btn))

        # Yazdır (Karne Al) butonu
        print_btn = tk.Label(
            f, text="📄 Karnemi İndir (PDF Al)", font=self.f_big,
            bg="#2e7d32", fg="#ffffff", padx=20, pady=10, cursor="hand2"
        )
        print_btn.pack(fill="x", padx=10, pady=(0, 8))
        print_btn.bind("<Button-1>", lambda _: self._export_pdf_report())

        # Butonlar
        btn_row = tk.Frame(f, bg=t["bg_card"])
        btn_row.pack(fill="x", padx=10, pady=(0, 8))

        cont = tk.Label(btn_row, text="▶  Oyuna Devam Et",
                        font=self.f_big, bg=t["btn_bg"], fg=t["btn_fg"],
                        padx=22, pady=10, cursor="hand2")
        cont.pack(side="left", expand=True, fill="x", padx=(0, 6))
        cont.bind("<Button-1>", lambda _: self._continue_from_stats())

        reset = tk.Label(btn_row, text="↻  Yeni Oyun",
                         font=self.f_normal, bg=t["skip_bg"], fg=t["skip_fg"],
                         padx=18, pady=10, cursor="hand2")
        reset.pack(side="left", padx=(4, 0))
        reset.bind("<Button-1>", lambda _: self._reset_game())

    def _continue_from_stats(self):
        if self.state == self.STATE_QUESTION:
            self._clear_right_panel()
            self._switch_stage(self.STATE_QUESTION)
            self._show_question_panel()
        else:
            self.state = self.STATE_IDLE
            self._switch_stage(self.STATE_IDLE)
            self._clear_right_panel()
            self._show_idle_panel()

    def _export_pdf_report(self):
        import datetime
        import webbrowser
        import os

        date_str = datetime.date.today().strftime('%d.%m.%Y')
        info = GRADE_INFO.get(self.selected_grade, {"label": "", "desc": ""})
        grade_label = f"LGS {info['label']} {info['desc']}"
        unit_label = "Tüm Üniteler" if self.selected_unit == "ALL" else self.selected_unit

        total = self.correct_count + self.wrong_count

        # Build table rows
        rows_html = ""
        all_unites = sorted(set(q["unite"] for q in self.all_questions))
        for unite in all_unites:
            stats = self.unite_stats.get(unite, {"d": 0, "y": 0})
            d, y = stats["d"], stats["y"]
            tot = d + y
            p = int(100 * d / tot) if tot else 0
            rows_html += f"""
            <tr>
                <td><strong>{unite}</strong></td>
                <td style="text-align:center; color:#2e7d32; font-weight:bold;">{d}</td>
                <td style="text-align:center; color:#c62828; font-weight:bold;">{y}</td>
                <td style="text-align:center; font-weight:bold; color:{'#2e7d32' if p >= 70 else '#d4af37'};">%{p}</td>
            </tr>
            """

        # AI Recommendations
        weak_units = []
        has_data = False
        for unite in all_unites:
            stats = self.unite_stats.get(unite, {"d": 0, "y": 0})
            d, y = stats["d"], stats["y"]
            tot = d + y
            if tot > 0:
                has_data = True
                if d / tot < 0.70:
                    weak_units.append((unite, int(100 * d / tot)))

        if not has_data:
            rec_html = "💡 Henüz analiz edilecek bir soru çözülmedi."
        elif not weak_units:
            rec_html = "🎯 Tebrikler! Tüm konularda %70'in üzerinde başarı sağladınız. LGS sınavına harika bir şekilde hazırlanıyorsunuz! 🚀"
        else:
            rec_html = "<ul style='margin-left: 1.2rem; padding: 0;'>"
            for u_name, u_pct in weak_units:
                rec = PYTHON_STUDY_RECS.get(u_name, "Bu üniteyle ilgili konu özetlerini tekrar çalışmalısınız.")
                rec_html += f"<li style='margin-bottom: 0.5rem;'><strong>{u_name} (Başarı: %{u_pct}):</strong> {rec}</li>"
            rec_html += "</ul>"

        # HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>LGS Başarı Karnesi</title>
    <style>
        body {{
            background: #ffffff;
            color: #111;
            font-family: 'Segoe UI', Arial, sans-serif;
            margin: 0;
            padding: 30px;
        }}
        .print-only-report {{
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
        }}
        .print-header {{
            text-align: center;
            border-bottom: 3px double #333;
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }}
        .print-logo {{
            font-size: 1.1rem;
            font-weight: bold;
            color: #555;
            letter-spacing: 2px;
        }}
        .print-header h1 {{
            font-size: 2.2rem;
            margin-top: 0.5rem;
            color: #000;
            text-transform: uppercase;
        }}
        .print-date {{
            font-size: 0.95rem;
            color: #555;
            margin-top: 0.5rem;
        }}
        .print-student-info {{
            display: flex;
            justify-content: space-between;
            font-size: 1.15rem;
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 2rem;
            border: 1px solid #ddd;
        }}
        .print-student-info p {{
            margin: 0;
        }}
        .print-stats-summary {{
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 2rem;
        }}
        .print-stat-item {{
            flex: 1;
            text-align: center;
            background: #fafafa;
            padding: 1rem;
            border: 1px solid #eee;
            border-radius: 6px;
        }}
        .print-stat-item .label {{
            display: block;
            font-size: 0.85rem;
            color: #555;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }}
        .print-stat-item .value {{
            font-size: 1.6rem;
            font-weight: bold;
            color: #111;
        }}
        .print-section {{
            margin-bottom: 2rem;
        }}
        .print-section h2 {{
            font-size: 1.3rem;
            border-bottom: 2px solid #333;
            padding-bottom: 0.5rem;
            margin-bottom: 1rem;
        }}
        .print-table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
        }}
        .print-table th, .print-table td {{
            border: 1px solid #ddd;
            padding: 8px 10px;
            font-size: 1rem;
        }}
        .print-table th {{
            background: #f0f0f0;
            font-weight: bold;
        }}
        .print-guidance-content {{
            background: #f9f9f9;
            padding: 1.25rem;
            border-left: 5px solid #d4af37;
            font-size: 1.05rem;
            line-height: 1.6;
            border-radius: 0 6px 6px 0;
        }}
        .print-footer {{
            text-align: center;
            margin-top: 3rem;
            border-top: 1px solid #ddd;
            padding-top: 1rem;
            color: #777;
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>
    <div class="print-only-report">
        <div class="print-header">
            <div class="print-logo">🏛 LGS ÇARK OYUNU</div>
            <h1>🏆 LGS BAŞARI KARNESİ 🏆</h1>
            <div class="print-date">Tarih: {date_str}</div>
        </div>
        <div class="print-student-info">
            <p><strong>Sınıf Seviyesi:</strong> {grade_label}</p>
            <p><strong>Çalışılan Ünite:</strong> {unit_label}</p>
        </div>
        <div class="print-stats-summary">
            <div class="print-stat-item">
                <span class="label">Toplam Puan</span>
                <span class="value">{self.total_score}</span>
            </div>
            <div class="print-stat-item">
                <span class="label">Çözülen Soru</span>
                <span class="value">{total}</span>
            </div>
            <div class="print-stat-item">
                <span class="label">Doğru Cevap</span>
                <span class="value" style="color: #2e7d32;">{self.correct_count}</span>
            </div>
            <div class="print-stat-item">
                <span class="label">Yanlış Cevap</span>
                <span class="value" style="color: #c62828;">{self.wrong_count}</span>
            </div>
        </div>
        <div class="print-section">
            <h2>📊 Ünite Bazlı Başarı Durumu</h2>
            <table class="print-table">
                <thead>
                    <tr>
                        <th style="text-align: left;">Ünite Adı</th>
                        <th style="width: 80px; text-align: center;">Doğru</th>
                        <th style="width: 80px; text-align: center;">Yanlış</th>
                        <th style="width: 100px; text-align: center;">Başarı Oranı</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        <div class="print-section">
            <h2>🧠 Rehber Öğretmen Yapay Zeka Tavsiyeleri</h2>
            <div class="print-guidance-content">
                {rec_html}
            </div>
        </div>
        <div class="print-footer">
            <p>LGS Çark Oyunu – Başarıya Giden Eğlenceli Yol!</p>
        </div>
    </div>
    <script>
        window.onload = function() {{
            window.print();
        }}
    </script>
</body>
</html>
"""
        try:
            with open("karne.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            webbrowser.open("file:///" + os.path.abspath("karne.html"))
        except Exception as e:
            print("HTML karne yazılırken hata:", e)

    # ─────────────────────────────────────────
    # İSTATİSTİK & SIFIRLAMA
    # ─────────────────────────────────────────

    def _update_stats(self):
        t = self.t
        if hasattr(self, "is_team_mode") and self.is_team_mode:
            # Grup Modu HUD Güncellemesi
            if hasattr(self, "lbl_score_hud") and self.lbl_score_hud.winfo_exists():
                self.lbl_score_hud.config(text=f"📢 Sıra: {self.active_team} Grubunda", fg="#ffd54f")
            if hasattr(self, "lbl_streak_hud") and self.lbl_streak_hud.winfo_exists():
                self.lbl_streak_hud.config(text=f"🏆 A Grubu: {self.team_scores['A']}", fg="#00e5ff")
            if hasattr(self, "lbl_quest_hud") and self.lbl_quest_hud.winfo_exists():
                self.lbl_quest_hud.config(text=f"🏆 B Grubu: {self.team_scores['B']}", fg="#ff1744")
            if hasattr(self, "lbl_correct_hud") and self.lbl_correct_hud.winfo_exists():
                self.lbl_correct_hud.config(text=f"✓ {self.team_correct}", fg=t["success"])
            if hasattr(self, "lbl_wrong_hud") and self.lbl_wrong_hud.winfo_exists():
                self.lbl_wrong_hud.config(text=f"✗ {self.team_wrong}", fg=t["error"])
            if hasattr(self, "lbl_solved_hud") and self.lbl_solved_hud.winfo_exists():
                self.lbl_solved_hud.config(text=f"📝 {self.solved_count}", fg=t["fg_dim"])
        else:
            # Bireysel Mod HUD Güncellemesi
            old_score = self.lbl_score_hud.cget("text").replace("🏆 Puan: ", "") if hasattr(self, "lbl_score_hud") else "0"
            new_score = str(self.total_score)
            
            if hasattr(self, "lbl_score_hud") and self.lbl_score_hud.winfo_exists():
                self.lbl_score_hud.config(text=f"🏆 Puan: {new_score}", fg=t["accent"])
            if hasattr(self, "lbl_streak_hud") and self.lbl_streak_hud.winfo_exists():
                self.lbl_streak_hud.config(text=f"🔥 Seri: {self.user_streak} Gün", fg=t["fg"])
            if hasattr(self, "lbl_correct_hud") and self.lbl_correct_hud.winfo_exists():
                self.lbl_correct_hud.config(text=f"✓ {self.correct_count}", fg=t["success"])
            if hasattr(self, "lbl_wrong_hud") and self.lbl_wrong_hud.winfo_exists():
                self.lbl_wrong_hud.config(text=f"✗ {self.wrong_count}", fg=t["error"])
            if hasattr(self, "lbl_solved_hud") and self.lbl_solved_hud.winfo_exists():
                self.lbl_solved_hud.config(text=f"📝 {self.solved_count}", fg=t["fg_dim"])
            if hasattr(self, "lbl_quest_hud") and self.lbl_quest_hud.winfo_exists():
                q_text = "🎯 Görev: Tamam! 🚀" if self.today_solved_count >= 5 else f"🎯 Görev: {self.today_solved_count}/5"
                self.lbl_quest_hud.config(text=q_text, fg=t["accent"] if self.today_solved_count >= 5 else t["fg"])

            # Puan animasyonu (bounce + flash)
            if old_score != new_score and hasattr(self, "lbl_score_hud"):
                try:
                    diff = int(new_score) - int(old_score)
                    flash_color = t["success"] if diff > 0 else t["error"]
                except ValueError:
                    flash_color = t["accent"]
                big_size = max(18, int(26 * self.scale))
                normal_size = max(16, int(22 * self.scale))
                self.lbl_score_hud.config(fg=flash_color)
                self.f_score.config(size=big_size)
                self.after(250, lambda: self.f_score.config(size=normal_size) if self.f_score.winfo_exists() else None)
                self.after(500, lambda: self.lbl_score_hud.config(fg=t["accent"]) if self.lbl_score_hud.winfo_exists() else None)

    def _return_to_main_menu(self):
        """Ana sınıfların seçildiği ekrana dön."""
        self._stop_timer()
        if self.anim_id:
            self.after_cancel(self.anim_id)
            self.anim_id = None

        self.state         = self.STATE_GRADE_SELECT
        self.total_score   = 0
        self.correct_count = 0
        self.wrong_count   = 0
        self.solved_count  = 0
        self.current_q     = None
        self.current_points = 0
        self.selected_opt  = None
        self.wheel_angle   = 0.0
        self.unite_stats   = {}
        self.selected_grade = None
        self.all_questions  = []
        self.remaining      = []

        self.title("LGS Sosyal Bilgiler – Çark Oyunu  v3")
        self.lbl_title.config(text="🏛  LGS Sosyal Bilgiler – Çark Oyunu")

        self._update_stats()
        self._draw_wheel()
        self._show_grade_selection()

    def _reset_game(self):
        """Mevcut oyunu en baştan (şu anki sınıf düzeyiyle) başlatır."""
        if self.state == self.STATE_GRADE_SELECT:
            return
            
        self._stop_timer()
        if self.anim_id:
            self.after_cancel(self.anim_id)
            self.anim_id = None

        self.state         = self.STATE_IDLE
        self.total_score   = 0
        self.correct_count = 0
        self.wrong_count   = 0
        self.solved_count  = 0
        self.current_q     = None
        self.current_points = 0
        self.selected_opt  = None
        self.wheel_angle   = 0.0
        self.unite_stats   = {}
        
        # Reset team variables
        self.team_scores    = {"A": 0, "B": 0}
        self.active_team    = "A"
        self.team_correct   = 0
        self.team_wrong     = 0

        self._refill_pool()
        self._update_stats()
        self._draw_wheel()
        self._switch_stage(self.STATE_IDLE)
        self._show_idle_panel()

    # ─────────────────────────────────────────
    # KULLANICI VERİLERİ VE SERİ SİSTEMİ
    # ─────────────────────────────────────────

    def _load_userdata(self):
        path = get_user_data_path()
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.user_streak = data.get("user_streak", 0)
                    self.last_login_date = data.get("last_login_date", "")
                    self.today_solved_count = data.get("today_solved_count", 0)
                    saved_date = data.get("today_solved_date", "")
                    today_str = datetime.now().strftime("%Y-%m-%d")
                    if saved_date != today_str:
                        self.today_solved_count = 0
            except Exception as e:
                print("Kullanıcı verileri yüklenirken hata:", e)

    def _save_userdata(self):
        path = get_user_data_path()
        try:
            data = {
                "user_streak": self.user_streak,
                "last_login_date": self.last_login_date,
                "today_solved_count": self.today_solved_count,
                "today_solved_date": datetime.now().strftime("%Y-%m-%d")
            }
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Kullanıcı verileri kaydedilirken hata:", e)

    def _check_daily_streak(self):
        today_str = datetime.now().strftime("%Y-%m-%d")
        yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        if not self.last_login_date:
            self.user_streak = 1
            self.last_login_date = today_str
        elif self.last_login_date == today_str:
            pass
        elif self.last_login_date == yesterday_str:
            self.user_streak += 1
            self.last_login_date = today_str
        else:
            self.user_streak = 1
            self.last_login_date = today_str
            
        self._save_userdata()
        self._update_streak_and_quest_ui()

    def _on_question_solved(self):
        self.today_solved_count += 1
        self._update_streak_and_quest_ui()
        self._save_userdata()

    def _update_streak_and_quest_ui(self):
        if hasattr(self, "lbl_streak_hud") and self.lbl_streak_hud.winfo_exists():
            self.lbl_streak_hud.config(text=f"🔥 Seri: {self.user_streak} Gün")
        if hasattr(self, "lbl_quest_hud") and self.lbl_quest_hud.winfo_exists():
            if self.today_solved_count >= 5:
                quest_text = "🎯 Görev Tamam! 🚀"
            else:
                quest_text = f"🎯 Görev: {self.today_solved_count}/5"
            self.lbl_quest_hud.config(text=quest_text)

    # ─────────────────────────────────────────
    # ROZETLER VE PAYLAŞIM
    # ─────────────────────────────────────────

    def _show_badge_popup(self, name: str, desc: str, emoji: str):
        popup = tk.Frame(self.main_frame, bg="#3d2314", highlightbackground="#aa382c", highlightthickness=3, padx=20, pady=20)
        popup.place(relx=0.5, rely=0.4, anchor="center")
        
        lbl_emoji = tk.Label(popup, text=emoji, font=tkfont.Font(size=48), bg="#3d2314")
        lbl_emoji.pack(pady=5)
        
        lbl_title = tk.Label(popup, text="🏆 ROZET KAZANDIN! 🏆", font=self.f_big, bg="#3d2314", fg="#ffe5a3")
        lbl_title.pack(pady=5)
        
        lbl_name = tk.Label(popup, text=name, font=tkfont.Font(family="Segoe UI" if os.name == "nt" else "Helvetica", size=18, weight="bold"), bg="#3d2314", fg="#ffffff")
        lbl_name.pack(pady=5)
        
        lbl_desc = tk.Label(popup, text=desc, font=self.f_normal, bg="#3d2314", fg="#e2d4ba", wraplength=300, justify="center")
        lbl_desc.pack(pady=5)
        
        btn_close = tk.Label(popup, text="Harika! 🚀", font=self.f_big, bg="#aa382c", fg="#ffffff", padx=15, pady=8, cursor="hand2")
        btn_close.pack(pady=10)
        btn_close.bind("<Button-1>", lambda e: popup.destroy())
        
        self.after(4000, lambda: popup.destroy() if popup.winfo_exists() else None)

    def _share_score(self, button):
        template = (
            f"🎮 LGS Çark Oyunu'nda tarih yazdım! 🚀\n\n"
            f"🔥 Günlük Seri: {self.user_streak} Gün\n"
            f"🏆 Toplam Puan: {self.total_score} Puan\n"
            f"✅ Doğru Cevap: {self.correct_count}\n"
            f"❌ Yanlış Cevap: {self.wrong_count}\n\n"
            f"Hadi sen de gel, çarkı çevir ve bilgini kanıtla! 🏛️✨"
        )
        self.clipboard_clear()
        self.clipboard_append(template)
        self.update()
        
        button.config(text="✓ Kopyalandı! Arkadaşlarına Gönder! 🚀", bg="#2e7d32")
        self.after(2000, lambda: button.config(text="✨ Skorunu Kopyala ve Paylaş", bg="#aa382c") if button.winfo_exists() else None)

    # ─────────────────────────────────────────
    # TEMA SABİTLENDİ (Energy)
    # ─────────────────────────────────────────


    def _apply_theme(self):
        t = self.t
        self.configure(bg=t["bg"])
        self.top_bar.config(bg=t["bg_secondary"])

        top_fg = t["fg"]
        top_btn_fg = t["fg_dim"]

        title_bg = t["bg_secondary"]
        btn_plaque = t["bg_secondary"]

        self.lbl_title.config(bg=title_bg, fg=top_fg)
        self.btn_main_menu.config(bg=btn_plaque, fg=top_btn_fg)
        self.btn_reset.config(bg=btn_plaque, fg=top_btn_fg)
        self.btn_stats.config(bg=btn_plaque, fg=top_btn_fg)
        self.top_bar_bg.config(bg=t["bg_secondary"])
        self._update_header_bg()

        # Apply theme colors to views
        bg_card = t["bg_card"]
        bg_main = t["bg"]
        
        self.main_frame.config(bg=bg_main)
        self.main_bg.config(bg=bg_main)
        self._update_main_bg()

        # Grade & Unit selection styling
        self.grade_unit_frame.config(bg=bg_card)
        self.grade_unit_canvas.config(bg=bg_card)
        self.grade_unit_panel.config(bg=bg_card)

        # Wheel view styling
        self.wheel_frame.config(bg=bg_main)
        self.wheel_content.config(bg=bg_main)
        self.wheel_canvas.config(bg=bg_main)
        self.pointer_canvas.config(bg=bg_main)
        self.btn_spin.config(bg=t["btn_bg"])
        self.btn_spin_icon.config(bg=t["btn_bg"], fg=t["btn_fg"])
        self.btn_spin_text.config(bg=t["btn_bg"], fg=t["btn_fg"])

        # HUD styling
        stat_bg = t["score_bg"]
        self.status_bar.config(bg=stat_bg)
        self.status_hud_frame.config(bg=stat_bg)
        self.lbl_score_hud.config(bg=stat_bg, fg=t["accent"])
        self.lbl_streak_hud.config(bg=stat_bg, fg=t["accent"])
        self.lbl_correct_hud.config(bg=stat_bg, fg=t["success"])
        self.lbl_wrong_hud.config(bg=stat_bg, fg=t["error"])
        self.lbl_solved_hud.config(bg=stat_bg, fg=t["fg_dim"])
        self.lbl_quest_hud.config(bg=stat_bg, fg=t["fg"])

        # Question view styling
        self.question_frame.config(bg=bg_card)
        self.q_canvas.config(bg=bg_card)
        self.question_panel.config(bg=bg_card)


# ──────────────────────────────────────────────
# GİRİŞ
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app = CarkOyunu()
    app.mainloop()
