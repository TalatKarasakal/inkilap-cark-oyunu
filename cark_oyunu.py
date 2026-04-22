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

# ──────────────────────────────────────────────
# TEMALAR
# ──────────────────────────────────────────────

THEMES = {
    "energy": {
        "bg":            "#1a0a00",
        "bg_secondary":  "#2b1200",
        "bg_card":       "#1f1008",
        "fg":            "#fff8ee",
        "fg_dim":        "#c8a97a",
        "accent":        "#e8a020",
        "accent_hover":  "#ffbe45",
        "success":       "#39d068",
        "error":         "#ff3b3b",
        "warning":       "#ff8800",
        "border":        "#4a2800",
        "btn_bg":        "#cc2200",
        "btn_fg":        "#ffffff",
        "btn_hover":     "#ff3a1a",
        "skip_bg":       "#3a1a00",
        "skip_fg":       "#c8a97a",
        "option_bg":     "#251205",
        "option_fg":     "#fff8ee",
        "option_hover":  "#3a1e08",
        "option_sel":    "#4a2200",
        "option_sel_border": "#e8a020",
        "score_bg":      "#130800",
        "timer_normal":  "#e8a020",
        "timer_warn":    "#ff8800",
        "timer_danger":  "#ff3b3b",
        "wheel_colors": [
            "#e8a020", "#cc2200", "#f5d040", "#aa1800",
            "#ffbe45", "#8b0000", "#ffd060", "#b83000",
            "#e89000", "#c01500",
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
    "İFLAS": "#0d0000",   # siyaha yakın kırmızı
    "PAS":   "#0a1a2a",   # koyu çelik mavi
    "X2":    "#5a4000",   # koyu altın
}
SLICE_SPECIAL_LABEL = {
    "İFLAS": "💀\nİFLAS",
    "PAS":   "⏸\nPAS",
    "X2":    "⚡\nX2",
}

TIMER_SECONDS   = 60
BONUS_CORRECT   = 10
PENALTY_WRONG   = 5

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

def ease_out_cubic(t: float) -> float:
    return 1 - (1 - t) ** 3

# ──────────────────────────────────────────────
# ANA UYGULAMA
# ──────────────────────────────────────────────

class CarkOyunu(tk.Tk):
    STATE_GRADE_SELECT = "grade_select"
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
        self.current_q: Optional[dict] = None
        self.current_points = 0
        self.selected_opt: Optional[str] = None
        self.x2_mode      = False   # X2 dilimi aktif mi?

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

        self.lbl_title = tk.Label(
            self.top_bar, text="🏛  LGS Sosyal Bilgiler – Çark Oyunu",
            font=self.f_title, anchor="w", padx=int(18 * s)
        )
        self.lbl_title.pack(side="left", fill="y")

        # Tema döngüsü butonu
        self.btn_theme = tk.Label(
            self.top_bar, text="🎨", font=self.f_icon,
            cursor="hand2", padx=int(14 * s), pady=6
        )
        self.btn_theme.pack(side="right", fill="y")
        self.btn_theme.bind("<Button-1>", lambda _: self._cycle_theme())

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

        # Ana içerik
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=pad, pady=(0, pad))

        # SOL – Çark alanı (genişlik pencereye göre ayarlanacak)
        self._left_width = int(480 * s)
        self.left_frame = tk.Frame(self.main_frame, width=self._left_width)
        self.left_frame.pack(side="left", fill="both", padx=(0, int(8 * s)))
        self.left_frame.pack_propagate(False)

        self.canvas_size = int(420 * s)
        self.wheel_canvas = tk.Canvas(
            self.left_frame, width=self.canvas_size, height=self.canvas_size,
            highlightthickness=0
        )
        self.wheel_canvas.pack(pady=(int(10 * s), int(6 * s)), padx=int(10 * s))

        self.pointer_canvas = tk.Canvas(
            self.left_frame, width=int(40 * s), height=int(28 * s), highlightthickness=0
        )
        self.pointer_canvas.place(
            in_=self.wheel_canvas,
            relx=0.5, rely=0.0, anchor="s", y=6
        )

        self.btn_spin = tk.Frame(self.left_frame, cursor="hand2", padx=int(28 * s), pady=int(10 * s))
        self.btn_spin.pack(pady=(int(4 * s), int(6 * s)))

        self.btn_spin_icon = tk.Label(self.btn_spin, text="🎯", font=self.f_big, cursor="hand2")
        self.btn_spin_icon.pack(side="left", padx=(0, 6))

        self.btn_spin_text = tk.Label(self.btn_spin, text="Çarkı Çevir", font=self.f_big, cursor="hand2")
        self.btn_spin_text.pack(side="left")

        for w in (self.btn_spin, self.btn_spin_icon, self.btn_spin_text):
            w.bind("<Button-1>", lambda _: self._spin_wheel())

        # Puan göstergesi
        self.score_frame = tk.Frame(self.left_frame)
        self.score_frame.pack(fill="x", padx=int(16 * s), pady=(2, 4))

        self.lbl_score_title = tk.Label(
            self.score_frame, text="TOPLAM PUAN", font=self.f_small
        )
        self.lbl_score_title.pack()
        self.lbl_score = tk.Label(
            self.score_frame, text="0", font=self.f_score
        )
        self.lbl_score.pack()

        # İstatistik satırı
        self.stat_frame = tk.Frame(self.left_frame)
        self.stat_frame.pack(fill="x", padx=int(16 * s), pady=(0, 4))

        self.lbl_correct = tk.Label(self.stat_frame, text="✓ 0", font=self.f_normal)
        self.lbl_correct.pack(side="left", expand=True)
        self.lbl_wrong = tk.Label(self.stat_frame, text="✗ 0", font=self.f_normal)
        self.lbl_wrong.pack(side="left", expand=True)
        self.lbl_solved = tk.Label(self.stat_frame, text="📝 0", font=self.f_normal)
        self.lbl_solved.pack(side="left", expand=True)

        # SAĞ – Soru paneli (kaydırılabilir)
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=(int(8 * s), 0))

        self.q_canvas = tk.Canvas(self.right_frame, highlightthickness=0)
        self.q_canvas.pack(side="left", fill="both", expand=True)

        self.question_panel = tk.Frame(self.q_canvas)
        self._qp_window = self.q_canvas.create_window(
            (0, 0), window=self.question_panel, anchor="nw"
        )
        self.question_panel.bind("<Configure>", self._on_qpanel_configure)
        self.q_canvas.bind("<Configure>", self._on_qcanvas_configure)
        # Mouse wheel scroll
        self.q_canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _on_qpanel_configure(self, _):
        self.q_canvas.configure(scrollregion=self.q_canvas.bbox("all"))

    def _on_qcanvas_configure(self, event):
        self.q_canvas.itemconfig(self._qp_window, width=event.width)

    def _on_mousewheel(self, event):
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

        # Sol paneli pencere genişliğinin ~%35'i yap
        new_left_w = max(300, int(w * 0.35))
        new_left_w = min(new_left_w, 600)
        self.left_frame.config(width=new_left_w)

        # Çark boyutunu sol panele göre ayarla
        new_canvas = min(new_left_w - 60, h - 280)
        new_canvas = max(200, new_canvas)
        if abs(new_canvas - self.canvas_size) > 10:
            self.canvas_size = new_canvas
            self.wheel_canvas.config(width=new_canvas, height=new_canvas)
            self._draw_wheel()

        # Sağ paneldeki wraplength'leri güncelle
        right_w = max(300, w - new_left_w - 60)
        self._current_wraplength = right_w - 60
        self._current_opt_wraplength = right_w - 100

    def _get_wraplength(self):
        return getattr(self, '_current_wraplength', int(520 * self.scale))

    def _get_opt_wraplength(self):
        return getattr(self, '_current_opt_wraplength', int(480 * self.scale))

    # ─────────────────────────────────────────
    # ÇARK ÇİZİMİ
    # ─────────────────────────────────────────

    def _draw_wheel(self):
        c = self.wheel_canvas
        c.delete("all")
        cx = cy = self.canvas_size / 2
        r = self.canvas_size / 2 - 14

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
                cx - r, cy - r, cx + r, cy + r,
                start=start, extent=SLICE_ANGLE,
                fill=color, outline=self.t["bg"], width=2,
                style="pieslice"
            )
            mid = math.radians(start + SLICE_ANGLE / 2)
            tx = cx + (r * 0.65) * math.cos(mid)
            ty = cy - (r * 0.65) * math.sin(mid)
            if is_special:
                label = SLICE_SPECIAL_LABEL[sv]
                c.create_text(tx, ty, text=label,
                              font=self.f_small, fill="#ffffff",
                              justify="center")
            else:
                c.create_text(tx, ty, text=str(sv),
                              font=self.f_wheel, fill="#ffffff")

        c.create_oval(
            cx - 30, cy - 30, cx + 30, cy + 30,
            fill=self.t["bg_secondary"], outline=self.t["accent"], width=2
        )
        c.create_text(cx, cy, text="LGS", font=self.f_normal, fill=self.t["accent"])
        self._draw_pointer()

    def _draw_pointer(self):
        pc = self.pointer_canvas
        pc.delete("all")
        pc.create_polygon(8, 2, 32, 2, 20, 26,
                          fill=self.t["error"], outline=self.t["bg"], width=1)

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
            # Tüm puanı sıfırla
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
            # Soru yok, puan değişmiyor
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
        else:
            self.x2_mode        = False
            self.current_points = sv

        self.current_q    = self._pick_question()
        self.selected_opt = None
        self.state        = self.STATE_QUESTION
        self._clear_right_panel()
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
            # Ortadaki sayı (Beyaz renk ile okunabilirliği artırıldı)
            tc.create_text(cx, cy, text=f"{secs}", font=self.f_timer, fill="#ffffff")

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

        self.wrong_count  += 1
        self.solved_count += 1
        self.total_score  -= PENALTY_WRONG
        self._record_unite(q["unite"], False)
        self._update_stats()
        self._show_feedback(False, q["dogru_cevap"], timeout=True)

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

    def _show_grade_selection(self):
        """Sınıf seçim ekranını gösterir."""
        self.state = self.STATE_GRADE_SELECT
        self.selected_grade = None
        self._clear_right_panel()
        f = self.question_panel
        t = self.t

        # Başlık
        tk.Frame(f, height=30, bg=t["bg_card"]).pack()
        tk.Label(f, text="📚", font=tkfont.Font(size=42),
                 bg=t["bg_card"], fg=t["accent"]).pack(pady=(10, 4))
        tk.Label(f, text="Sınıf Düzeyini Seçiniz",
                 font=self.f_title, bg=t["bg_card"], fg=t["fg"]).pack(pady=(4, 6))
        tk.Label(f, text="Oynamak istediğiniz sınıf düzeyine tıklayın",
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(0, 12))

        # Sınıf butonları 2x2 grid
        grid_frame = tk.Frame(f, bg=t["bg_card"])
        grid_frame.pack(padx=20, pady=4)

        for i, (grade, info) in enumerate(GRADE_INFO.items()):
            if grade not in self.questions_db:
                continue
            q_count = len(self.questions_db[grade])
            unites = set(q["unite"] for q in self.questions_db[grade])

            row, col = divmod(i, 2)
            btn_frame = tk.Frame(grid_frame, bg=info["color"], cursor="hand2",
                                 padx=16, pady=14,
                                 highlightbackground=t["border"], highlightthickness=1)
            btn_frame.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

            emoji_lbl = tk.Label(btn_frame, text=info["emoji"],
                                 font=tkfont.Font(size=28), bg=info["color"], fg="#ffffff")
            emoji_lbl.pack(pady=(2, 4))

            name_lbl = tk.Label(btn_frame, text=info["label"],
                                font=self.f_big, bg=info["color"], fg="#ffffff")
            name_lbl.pack()

            desc_lbl = tk.Label(btn_frame, text=info["desc"],
                                font=self.f_small, bg=info["color"], fg="#f3f4f6")
            desc_lbl.pack()

            count_lbl = tk.Label(btn_frame, text=f"{q_count} soru | {len(unites)} unite",
                                 font=self.f_small, bg=info["color"], fg="#e5e7eb")
            count_lbl.pack(pady=(2, 0))

            # Bind click
            for w in (btn_frame, emoji_lbl, name_lbl, desc_lbl, count_lbl):
                w.bind("<Button-1>", lambda e, g=grade: self._select_grade(g))
                # Hover effect
                w.bind("<Enter>", lambda e, bf=btn_frame, c=info["hover"]: bf.config(bg=c) or [ch.config(bg=c) for ch in bf.winfo_children()])
                w.bind("<Leave>", lambda e, bf=btn_frame, c=info["color"]: bf.config(bg=c) or [ch.config(bg=c) for ch in bf.winfo_children()])

        grid_frame.columnconfigure(0, weight=1)
        grid_frame.columnconfigure(1, weight=1)

        # Alt bilgi
        total = sum(len(v) for v in self.questions_db.values())
        tk.Label(f, text=f"Toplam {total} soru | 4 sinif duzeyi",
                 font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]).pack(pady=(14, 4))

    def _select_grade(self, grade: str):
        """Kullanıcı sınıf seçti → soruları yükle ve oyuna başla."""
        self.selected_grade = grade
        self.all_questions = list(self.questions_db[grade])
        self._refill_pool()

        # Başlığı güncelle
        info = GRADE_INFO[grade]
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
        if is_correct:
            self.correct_count += 1
            if was_x2:
                self.total_score = self.total_score * 2
            else:
                self.total_score += self.current_points + BONUS_CORRECT
        else:
            self.wrong_count   += 1
            self.total_score   -= PENALTY_WRONG
        self.x2_mode = False

        self._record_unite(q["unite"], is_correct)
        self._update_stats()
        self._show_feedback(is_correct, correct, was_x2=was_x2)

    def _skip_question(self):
        if self.state not in (self.STATE_QUESTION, self.STATE_ANSWERED):
            return
        self._stop_timer()
        self.state = self.STATE_IDLE
        self._clear_right_panel()
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
        if self.state == self.STATE_ANSWERED:
            self._show_idle_panel()
            self.state = self.STATE_IDLE
        elif self.state == self.STATE_IDLE:
            self._show_idle_panel()
        elif self.state == self.STATE_QUESTION:
            self._clear_right_panel()
            self._show_question_panel()
        else:
            self._show_idle_panel()
            self.state = self.STATE_IDLE

    # ─────────────────────────────────────────
    # İSTATİSTİK & SIFIRLAMA
    # ─────────────────────────────────────────

    def _update_stats(self):
        t = self.t
        old_score = self.lbl_score.cget("text")
        new_score = str(self.total_score)
        self.lbl_score.config(text=new_score)
        self.lbl_correct.config(text=f"✓ {self.correct_count}", fg=t["success"])
        self.lbl_wrong.config(text=f"✗ {self.wrong_count}", fg=t["error"])
        self.lbl_solved.config(text=f"📝 {self.solved_count}")

        # Puan animasyonu (bounce + flash)
        if old_score != new_score:
            try:
                diff = int(new_score) - int(old_score)
                flash_color = t["success"] if diff > 0 else t["error"]
            except ValueError:
                flash_color = t["accent"]
            big_size = max(18, int(26 * self.scale))
            normal_size = max(16, int(22 * self.scale))
            self.lbl_score.config(fg=flash_color)
            self.f_score.config(size=big_size)
            self.after(250, lambda: self.f_score.config(size=normal_size))
            self.after(500, lambda: self.lbl_score.config(fg=t["accent"]))

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

        self._refill_pool()
        self._update_stats()
        self._draw_wheel()
        self._show_idle_panel()

    # ─────────────────────────────────────────
    # TEMA
    # ─────────────────────────────────────────

    _theme_cycle = ["energy", "dark", "light"]

    def _cycle_theme(self):
        idx = self._theme_cycle.index(self.current_theme)
        self.current_theme = self._theme_cycle[(idx + 1) % len(self._theme_cycle)]
        self.t = THEMES[self.current_theme]
        self._apply_theme()
        self._draw_wheel()
        if   self.state == self.STATE_GRADE_SELECT:
            self._show_grade_selection()
        elif self.state == self.STATE_IDLE:
            self._show_idle_panel()
        elif self.state == self.STATE_QUESTION:
            self._clear_right_panel()
            self._show_question_panel()
            if self.selected_opt:
                self._select_option(self.selected_opt)
        elif self.state == self.STATE_SPINNING:
            self._show_spinning_panel()

    def _apply_theme(self):
        t = self.t
        self.configure(bg=t["bg"])
        self.top_bar.config(bg=t["bg_secondary"])
        self.lbl_title.config(bg=t["bg_secondary"], fg=t["fg"])
        self.btn_theme.config(bg=t["bg_secondary"], fg=t["accent"])
        self.btn_main_menu.config(bg=t["bg_secondary"], fg=t["fg_dim"])
        self.btn_reset.config(bg=t["bg_secondary"], fg=t["fg_dim"])
        self.btn_stats.config(bg=t["bg_secondary"], fg=t["fg_dim"])
        self.main_frame.config(bg=t["bg"])
        self.left_frame.config(bg=t["bg"])
        self.wheel_canvas.config(bg=t["bg"])
        self.pointer_canvas.config(bg=t["bg"])
        self.btn_spin.config(bg=t["btn_bg"])
        self.btn_spin_icon.config(bg=t["btn_bg"], fg=t["btn_fg"])
        self.btn_spin_text.config(bg=t["btn_bg"], fg=t["btn_fg"])
        self.score_frame.config(bg=t["score_bg"])
        self.lbl_score_title.config(bg=t["score_bg"], fg=t["fg_dim"])
        self.lbl_score.config(bg=t["score_bg"], fg=t["accent"])
        self.stat_frame.config(bg=t["bg"])
        self.lbl_correct.config(bg=t["bg"], fg=t["success"])
        self.lbl_wrong.config(bg=t["bg"], fg=t["error"])
        self.lbl_solved.config(bg=t["bg"], fg=t["fg_dim"])
        self.right_frame.config(bg=t["bg_card"])
        self.q_canvas.config(bg=t["bg_card"])
        self.question_panel.config(bg=t["bg_card"])


# ──────────────────────────────────────────────
# GİRİŞ
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app = CarkOyunu()
    app.mainloop()
