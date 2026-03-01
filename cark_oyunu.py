#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LGS İnkılap Tarihi Çark Oyunu
==============================
Python / Tkinter ile çalışan masaüstü çark oyunu.
Çarkı çevir → puan belirle → soruyu cevapla → puan kazan!

Çalıştırma:
    python cark_oyunu.py
"""

import json
import math
import os
import random
import sys
import tkinter as tk
from tkinter import font as tkfont
from typing import Optional, Dict, List


def resource_path(relative_path: str) -> str:
    """PyInstaller --onefile ile uyumlu kaynak dosya yolu döndürür."""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, relative_path)

# ──────────────────────────────────────────────
# TEMA
# ──────────────────────────────────────────────

THEMES = {
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
        "wheel_colors": [
            "#4f6ef7", "#ef4444", "#22c55e", "#f59e0b", "#a855f7",
            "#ec4899", "#06b6d4", "#eab308", "#818cf8", "#f472b6",
        ],
    },
}

# ──────────────────────────────────────────────
# PUAN DİLİMLERİ
# ──────────────────────────────────────────────

POINT_VALUES  = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
SLICE_COUNT   = len(POINT_VALUES)
SLICE_ANGLE   = 360 / SLICE_COUNT          # 36°

# ──────────────────────────────────────────────
# YARDIMCI
# ──────────────────────────────────────────────

def load_questions(path: str) -> list[dict]:
    """sorular.json dosyasını oku."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def ease_out_cubic(t: float) -> float:
    """0-1 arası değer alır, yavaşlayarak durma eğrisi."""
    return 1 - (1 - t) ** 3


# ──────────────────────────────────────────────
# ANA UYGULAMA
# ──────────────────────────────────────────────

class CarkOyunu(tk.Tk):
    """LGS İnkılap Tarihi Çark Oyunu ana pencere."""

    # ── durum sabitleri ──
    STATE_IDLE       = "idle"        # çark döndürülmeyi bekliyor
    STATE_SPINNING   = "spinning"    # çark dönüyor
    STATE_QUESTION   = "question"    # soru gösteriliyor
    STATE_ANSWERED   = "answered"    # cevap verildi

    ANIM_DURATION_MS = 4000          # toplam animasyon süresi (ms)
    ANIM_FPS         = 60

    def __init__(self):
        super().__init__()

        # ── pencereyi yapılandır ──
        self.title("LGS İnkılap Tarihi – Çark Oyunu")
        self.minsize(1100, 700)
        self.geometry("1200x750")
        self.configure(bg="#181c24")

        # ── tema ──
        self.current_theme = "dark"
        self.t = THEMES[self.current_theme]

        # ── fontlar ──
        self.base_family = "Segoe UI" if os.name == "nt" else "Helvetica"
        self.f_title  = tkfont.Font(family=self.base_family, size=18, weight="bold")
        self.f_normal = tkfont.Font(family=self.base_family, size=13)
        self.f_small  = tkfont.Font(family=self.base_family, size=11)
        self.f_big    = tkfont.Font(family=self.base_family, size=15, weight="bold")
        self.f_option = tkfont.Font(family=self.base_family, size=13)
        self.f_score  = tkfont.Font(family=self.base_family, size=22, weight="bold")
        self.f_wheel  = tkfont.Font(family=self.base_family, size=14, weight="bold")
        self.f_icon   = tkfont.Font(family=self.base_family, size=18)

        # ── soru havuzu ──
        self.all_questions = load_questions(resource_path("sorular.json"))
        self.remaining: List[dict] = []
        self._refill_pool()

        # ── oyun durumu ──
        self.state         = self.STATE_IDLE
        self.total_score   = 0
        self.correct_count = 0
        self.wrong_count   = 0
        self.solved_count  = 0
        self.current_q: Optional[dict] = None
        self.current_points = 0
        self.selected_opt: Optional[str] = None

        # ── animasyon ──
        self.anim_id: Optional[str] = None
        self.wheel_angle   = 0.0   # çarkın mevcut açısı (derece)
        self.target_angle  = 0.0
        self.anim_start    = 0.0
        self.anim_elapsed  = 0

        # ── UI kur ──
        self._build_ui()
        self._apply_theme()
        self._draw_wheel()
        self._show_idle_panel()

    # ──────────────────────────────────────────
    # SORU HAVUZU
    # ──────────────────────────────────────────

    def _refill_pool(self):
        self.remaining = list(self.all_questions)
        random.shuffle(self.remaining)

    def _pick_question(self) -> dict:
        if not self.remaining:
            self._refill_pool()
        return self.remaining.pop()

    # ──────────────────────────────────────────
    # UI OLUŞTURMA
    # ──────────────────────────────────────────

    def _build_ui(self):
        # ── Üst bar ──
        self.top_bar = tk.Frame(self, height=52)
        self.top_bar.pack(fill="x", side="top")
        self.top_bar.pack_propagate(False)

        self.lbl_title = tk.Label(
            self.top_bar, text="🏛  LGS İnkılap Tarihi – Çark Oyunu",
            font=self.f_title, anchor="w", padx=18
        )
        self.lbl_title.pack(side="left", fill="y")

        self.btn_theme = tk.Label(
            self.top_bar, text="🌙", font=self.f_icon, cursor="hand2",
            padx=18, pady=6
        )
        self.btn_theme.pack(side="right", fill="y")
        self.btn_theme.bind("<Button-1>", lambda _: self._toggle_theme())

        self.btn_reset = tk.Label(
            self.top_bar, text="↻ Sıfırla", font=self.f_normal, cursor="hand2",
            padx=16, pady=6
        )
        self.btn_reset.pack(side="right", fill="y")
        self.btn_reset.bind("<Button-1>", lambda _: self._reset_game())

        # ── Ana içerik ──
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        # SOL – Çark alanı
        self.left_frame = tk.Frame(self.main_frame, width=460)
        self.left_frame.pack(side="left", fill="both", padx=(0, 8))
        self.left_frame.pack_propagate(False)

        self.canvas_size = 400
        self.wheel_canvas = tk.Canvas(
            self.left_frame, width=self.canvas_size, height=self.canvas_size,
            highlightthickness=0
        )
        self.wheel_canvas.pack(pady=(12, 8), padx=10)

        # İşaretçi (pointer) canvas'ın üstünde
        self.pointer_canvas = tk.Canvas(
            self.left_frame, width=40, height=28, highlightthickness=0
        )
        self.pointer_canvas.place(
            in_=self.wheel_canvas,
            relx=0.5, rely=0.0, anchor="s", y=6
        )

        # Çarkı Çevir butonu
        self.btn_spin = tk.Label(
            self.left_frame, text="🎯  Çarkı Çevir", font=self.f_big,
            cursor="hand2", padx=28, pady=10, relief="flat"
        )
        self.btn_spin.pack(pady=(4, 8))
        self.btn_spin.bind("<Button-1>", lambda _: self._spin_wheel())

        # Puan göstergesi
        self.score_frame = tk.Frame(self.left_frame)
        self.score_frame.pack(fill="x", padx=20, pady=(4, 8))

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
        self.stat_frame.pack(fill="x", padx=20, pady=(0, 6))

        self.lbl_correct = tk.Label(self.stat_frame, text="✓ 0", font=self.f_normal)
        self.lbl_correct.pack(side="left", expand=True)
        self.lbl_wrong = tk.Label(self.stat_frame, text="✗ 0", font=self.f_normal)
        self.lbl_wrong.pack(side="left", expand=True)
        self.lbl_solved = tk.Label(self.stat_frame, text="📝 0", font=self.f_normal)
        self.lbl_solved.pack(side="left", expand=True)

        # SAĞ – Soru paneli
        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side="left", fill="both", expand=True, padx=(8, 0))

        # Sağ panel içi – kaydırılabilir alan yerine basit frame
        self.question_panel = tk.Frame(self.right_frame)
        self.question_panel.pack(fill="both", expand=True, padx=10, pady=10)

    # ──────────────────────────────────────────
    # ÇARK ÇİZİMİ
    # ──────────────────────────────────────────

    def _draw_wheel(self):
        c = self.wheel_canvas
        c.delete("all")
        cx = cy = self.canvas_size / 2
        r = self.canvas_size / 2 - 16

        for i in range(SLICE_COUNT):
            start = i * SLICE_ANGLE + self.wheel_angle
            color = self.t["wheel_colors"][i % len(self.t["wheel_colors"])]
            c.create_arc(
                cx - r, cy - r, cx + r, cy + r,
                start=start, extent=SLICE_ANGLE,
                fill=color, outline=self.t["bg"], width=2,
                style="pieslice"
            )
            # Metin (puan)
            mid = math.radians(start + SLICE_ANGLE / 2)
            tx = cx + (r * 0.65) * math.cos(mid)
            ty = cy - (r * 0.65) * math.sin(mid)
            c.create_text(
                tx, ty, text=str(POINT_VALUES[i]),
                font=self.f_wheel, fill="#ffffff"
            )

        # Merkez daire
        c.create_oval(
            cx - 28, cy - 28, cx + 28, cy + 28,
            fill=self.t["bg_secondary"], outline=self.t["border"], width=2
        )
        c.create_text(cx, cy, text="LGS", font=self.f_small, fill=self.t["fg_dim"])

        # Pointer çiz
        self._draw_pointer()

    def _draw_pointer(self):
        pc = self.pointer_canvas
        pc.delete("all")
        # Aşağı bakan üçgen
        pc.create_polygon(
            8, 2,  32, 2,  20, 26,
            fill=self.t["error"], outline=self.t["bg"], width=1
        )

    # ──────────────────────────────────────────
    # ÇARK ANİMASYONU
    # ──────────────────────────────────────────

    def _spin_wheel(self):
        if self.state != self.STATE_IDLE:
            return

        self.state = self.STATE_SPINNING
        self.btn_spin.config(cursor="arrow")

        # Hedef: en az 5 tur + rastgele dilim
        extra_turns = random.randint(5, 9) * 360
        target_slice = random.randint(0, SLICE_COUNT - 1)
        # Çarkın üstte durması: 90° referans
        # Dilimin ortası: target_slice * SLICE_ANGLE + SLICE_ANGLE/2
        # Çark açısı + dilim ortası = 90 => wheel_angle = 90 - mid
        slice_mid = target_slice * SLICE_ANGLE + SLICE_ANGLE / 2
        final_angle = 90 - slice_mid
        # Toplam dönüş miktarı
        self.anim_start_angle = self.wheel_angle
        self.total_rotation = extra_turns + (final_angle - (self.wheel_angle % 360) + 360) % 360
        self.target_angle = self.anim_start_angle + self.total_rotation
        self.target_slice = target_slice
        self.anim_elapsed = 0

        self._clear_right_panel()
        self._show_spinning_panel()
        self._animate_step()

    def _animate_step(self):
        dt = 1000 / self.ANIM_FPS
        self.anim_elapsed += dt
        progress = min(self.anim_elapsed / self.ANIM_DURATION_MS, 1.0)
        eased = ease_out_cubic(progress)

        self.wheel_angle = self.anim_start_angle + self.total_rotation * eased
        self._draw_wheel()

        if progress < 1.0:
            self.anim_id = self.after(int(dt), self._animate_step)
        else:
            self.anim_id = None
            self.wheel_angle = self.target_angle
            self._draw_wheel()
            self._on_spin_complete()

    def _on_spin_complete(self):
        self.current_points = POINT_VALUES[self.target_slice]
        self.current_q = self._pick_question()
        self.selected_opt = None
        self.state = self.STATE_QUESTION
        self._clear_right_panel()
        self._show_question_panel()
        self.btn_spin.config(cursor="hand2")

    # ──────────────────────────────────────────
    # SAĞ PANEL: DURUMLAR
    # ──────────────────────────────────────────

    def _clear_right_panel(self):
        for w in self.question_panel.winfo_children():
            w.destroy()

    def _show_idle_panel(self):
        """Başlangıç: çark döndürülmemiş."""
        self._clear_right_panel()
        f = self.question_panel
        t = self.t

        spacer = tk.Frame(f, height=80, bg=t["bg_card"])
        spacer.pack()

        icon = tk.Label(f, text="🎡", font=tkfont.Font(size=48), bg=t["bg_card"], fg=t["fg"])
        icon.pack(pady=(10, 4))

        lbl = tk.Label(
            f, text="Çarkı çevirerek\nbir puan belirleyin!",
            font=self.f_big, bg=t["bg_card"], fg=t["fg_dim"],
            justify="center"
        )
        lbl.pack(pady=10)

        hint = tk.Label(
            f, text="Sol taraftaki 'Çarkı Çevir' butonuna tıklayın.",
            font=self.f_small, bg=t["bg_card"], fg=t["fg_dim"]
        )
        hint.pack()

    def _show_spinning_panel(self):
        """Çark dönerken sağda gösterilen mesaj."""
        self._clear_right_panel()
        f = self.question_panel
        t = self.t

        spacer = tk.Frame(f, height=100, bg=t["bg_card"])
        spacer.pack()

        lbl = tk.Label(
            f, text="⏳  Çark dönüyor…",
            font=self.f_big, bg=t["bg_card"], fg=t["accent"]
        )
        lbl.pack(pady=20)

    def _show_question_panel(self):
        """Soru göster: meta + soru + şıklar + butonlar."""
        f = self.question_panel
        t = self.t
        q = self.current_q

        # ── Puan banner ──
        pts_frame = tk.Frame(f, bg=t["accent"], height=40)
        pts_frame.pack(fill="x", pady=(0, 10))
        pts_frame.pack_propagate(False)
        tk.Label(
            pts_frame,
            text=f"🎯  Bu soru  {self.current_points} puan  değerinde!",
            font=self.f_big, bg=t["accent"], fg="#ffffff"
        ).pack(expand=True)

        # ── Meta bilgiler ──
        meta_frame = tk.Frame(f, bg=t["bg_card"])
        meta_frame.pack(fill="x", padx=6, pady=(0, 6))

        meta_texts = [
            ("📚", q["unite"]),
            ("📌", q["konu"]),
            ("📅", str(q["yil"])),
            ("⚡", q["zorluk"]),
        ]
        for icon_c, val in meta_texts:
            row = tk.Frame(meta_frame, bg=t["bg_card"])
            row.pack(fill="x", pady=2, padx=6)
            tk.Label(row, text=icon_c, font=self.f_normal, bg=t["bg_card"], fg=t["fg_dim"], width=3).pack(side="left")
            tk.Label(row, text=val, font=self.f_normal, bg=t["bg_card"], fg=t["fg"], anchor="w").pack(side="left", fill="x")

        # ── Ayırıcı ──
        sep = tk.Frame(f, height=1, bg=t["border"])
        sep.pack(fill="x", padx=10, pady=6)

        # ── Soru metni ──
        q_lbl = tk.Label(
            f, text=q["soru"], font=self.f_normal,
            bg=t["bg_card"], fg=t["fg"], wraplength=500,
            justify="left", anchor="nw", padx=12, pady=10
        )
        q_lbl.pack(fill="x")

        # ── Şıklar ──
        self.option_widgets: Dict[str, tk.Frame] = {}
        self.option_labels: Dict[str, tk.Label] = {}

        for key in ["A", "B", "C", "D"]:
            opt_frame = tk.Frame(
                f, bg=t["option_bg"], cursor="hand2",
                highlightbackground=t["border"], highlightthickness=1,
                padx=16, pady=12
            )
            opt_frame.pack(fill="x", padx=10, pady=4)

            opt_lbl = tk.Label(
                opt_frame,
                text=f"{key})  {q['siklar'][key]}",
                font=self.f_option, bg=t["option_bg"], fg=t["option_fg"],
                anchor="w", wraplength=460, justify="left"
            )
            opt_lbl.pack(fill="x", pady=2)

            # Tıklama
            for w in (opt_frame, opt_lbl):
                w.bind("<Button-1>", lambda e, k=key: self._select_option(k))

            self.option_widgets[key] = opt_frame
            self.option_labels[key] = opt_lbl

        # ── Alt butonlar ──
        btn_row = tk.Frame(f, bg=t["bg_card"])
        btn_row.pack(fill="x", padx=10, pady=(12, 4))

        self.btn_answer = tk.Label(
            btn_row, text="✓  Cevapla", font=self.f_big,
            bg=t["btn_bg"], fg=t["btn_fg"],
            padx=28, pady=11, cursor="hand2"
        )
        self.btn_answer.pack(side="left", expand=True, fill="x", padx=(0, 6))
        self.btn_answer.bind("<Button-1>", lambda _: self._submit_answer())

        self.btn_skip = tk.Label(
            btn_row, text="⏩  Geç", font=self.f_normal,
            bg=t["skip_bg"], fg=t["skip_fg"],
            padx=24, pady=11, cursor="hand2"
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
                frm.config(bg=t["option_sel"], highlightbackground=t["option_sel_border"], highlightthickness=2)
                self.option_labels[k].config(bg=t["option_sel"])
            else:
                frm.config(bg=t["option_bg"], highlightbackground=t["border"], highlightthickness=1)
                self.option_labels[k].config(bg=t["option_bg"])

    def _submit_answer(self):
        if self.state != self.STATE_QUESTION or self.selected_opt is None:
            return

        self.state = self.STATE_ANSWERED
        q = self.current_q
        correct = q["dogru_cevap"]
        is_correct = self.selected_opt == correct

        self.solved_count += 1
        if is_correct:
            self.correct_count += 1
            self.total_score += self.current_points
        else:
            self.wrong_count += 1

        self._update_stats()
        self._show_feedback(is_correct, correct)

    def _skip_question(self):
        if self.state not in (self.STATE_QUESTION, self.STATE_ANSWERED):
            return
        self.state = self.STATE_IDLE
        self._clear_right_panel()
        self._show_idle_panel()

    def _show_feedback(self, is_correct: bool, correct_key: str):
        t = self.t
        q = self.current_q

        # Renklendirme: doğru yeşil, yanlış kırmızı
        for k, frm in self.option_widgets.items():
            if k == correct_key:
                frm.config(bg=t["success"], highlightbackground=t["success"], highlightthickness=2)
                self.option_labels[k].config(bg=t["success"], fg="#ffffff")
            elif k == self.selected_opt and not is_correct:
                frm.config(bg=t["error"], highlightbackground=t["error"], highlightthickness=2)
                self.option_labels[k].config(bg=t["error"], fg="#ffffff")
            # Tıklamayı devre dışı bırak
            for w in (frm, self.option_labels[k]):
                w.unbind("<Button-1>")
                w.config(cursor="arrow")

        # Cevapla butonunu devre dışı bırak
        self.btn_answer.unbind("<Button-1>")
        self.btn_answer.config(bg=t["border"], cursor="arrow")

        # Sonuç mesajı ekle (en alta)
        f = self.question_panel

        result_frame = tk.Frame(f, bg=t["bg_card"])
        result_frame.pack(fill="x", padx=10, pady=(6, 2))

        if is_correct:
            msg = f"🎉  Doğru!  +{self.current_points} puan kazandınız!"
            msg_color = t["success"]
        else:
            msg = f"❌  Yanlış!  Doğru cevap: {correct_key}"
            msg_color = t["error"]

        tk.Label(
            result_frame, text=msg, font=self.f_big,
            bg=t["bg_card"], fg=msg_color
        ).pack(pady=4)

        # Açıklama
        if q.get("aciklama"):
            tk.Label(
                result_frame,
                text=f"💡  {q['aciklama']}",
                font=self.f_normal, bg=t["bg_card"], fg=t["fg_dim"],
                wraplength=500, justify="left", anchor="nw"
            ).pack(fill="x", padx=4, pady=(2, 4))

        # Devam butonu
        self.btn_skip.config(text="▶  Devam Et")

    # ──────────────────────────────────────────
    # İSTATİSTİK & SIFIRLAMA
    # ──────────────────────────────────────────

    def _update_stats(self):
        t = self.t
        self.lbl_score.config(text=str(self.total_score))
        self.lbl_correct.config(text=f"✓ {self.correct_count}", fg=t["success"])
        self.lbl_wrong.config(text=f"✗ {self.wrong_count}", fg=t["error"])
        self.lbl_solved.config(text=f"📝 {self.solved_count}")

    def _reset_game(self):
        if self.anim_id:
            self.after_cancel(self.anim_id)
            self.anim_id = None

        self.state = self.STATE_IDLE
        self.total_score = 0
        self.correct_count = 0
        self.wrong_count = 0
        self.solved_count = 0
        self.current_q = None
        self.current_points = 0
        self.selected_opt = None
        self.wheel_angle = 0.0

        self._refill_pool()
        self._update_stats()
        self._draw_wheel()
        self._show_idle_panel()

    # ──────────────────────────────────────────
    # TEMA DEĞİŞTİRME
    # ──────────────────────────────────────────

    def _toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        self.t = THEMES[self.current_theme]
        self._apply_theme()
        self._draw_wheel()

        # Sağ paneli yeniden çiz (durum korunarak)
        if self.state == self.STATE_IDLE:
            self._show_idle_panel()
        elif self.state == self.STATE_QUESTION:
            self._clear_right_panel()
            self._show_question_panel()
            # Seçili şıkkı yeniden işaretle
            if self.selected_opt:
                self._select_option(self.selected_opt)
        elif self.state == self.STATE_SPINNING:
            self._show_spinning_panel()

    def _apply_theme(self):
        t = self.t
        self.configure(bg=t["bg"])
        self.top_bar.config(bg=t["bg_secondary"])
        self.lbl_title.config(bg=t["bg_secondary"], fg=t["fg"])
        self.btn_theme.config(
            bg=t["bg_secondary"], fg=t["fg"],
            text="☀" if self.current_theme == "dark" else "🌙"
        )
        self.btn_reset.config(bg=t["bg_secondary"], fg=t["fg_dim"])

        self.main_frame.config(bg=t["bg"])
        self.left_frame.config(bg=t["bg"])
        self.wheel_canvas.config(bg=t["bg"])
        self.pointer_canvas.config(bg=t["bg"])

        self.btn_spin.config(bg=t["btn_bg"], fg=t["btn_fg"])

        self.score_frame.config(bg=t["score_bg"])
        self.lbl_score_title.config(bg=t["score_bg"], fg=t["fg_dim"])
        self.lbl_score.config(bg=t["score_bg"], fg=t["accent"])

        self.stat_frame.config(bg=t["bg"])
        self.lbl_correct.config(bg=t["bg"], fg=t["success"])
        self.lbl_wrong.config(bg=t["bg"], fg=t["error"])
        self.lbl_solved.config(bg=t["bg"], fg=t["fg_dim"])

        self.right_frame.config(bg=t["bg_card"])
        self.question_panel.config(bg=t["bg_card"])


# ──────────────────────────────────────────────
# GİRİŞ
# ──────────────────────────────────────────────

if __name__ == "__main__":
    app = CarkOyunu()
    app.mainloop()
