// Elements
const wheelCanvas = document.getElementById('wheelCanvas');
const ctx = wheelCanvas.getContext('2d');
const btnSpin = document.getElementById('btn-spin');
const btnTheme = document.getElementById('btn-theme');
const btnMenu = document.getElementById('btn-menu');
const btnReset = document.getElementById('btn-reset');
const btnStats = document.getElementById('btn-stats');

const views = {
    grade: document.getElementById('view-grade'),
    idle: document.getElementById('view-idle'),
    question: document.getElementById('view-question'),
    feedback: document.getElementById('view-feedback'),
    stats: document.getElementById('view-stats')
};

// Game Rules & State
const WHEEL_SLICES = [10, 20, "PAS", 30, 40, "X2", 50, 60, 70, 80, "İFLAS", 90, 100];
const SLICE_COUNT = WHEEL_SLICES.length;
const SLICE_ANGLE = (Math.PI * 2) / SLICE_COUNT;

const themes = ["energy", "dark", "light"];
let currentThemeIdx = 0;

let wheelLogicalSize = 500;

let state = {
    grade: null,
    score: 0,
    correct: 0,
    wrong: 0,
    solved: 0,
    unitStats: {},
    remainingQuestions: [],
    x2Mode: false,
    currentPoints: 0,
    currentQ: null,
    selectedOpt: null,
    timer: 45,
    timerInterval: null,
    wheelAngle: 0,
    userStreak: 0,
    lastLoginDate: "",
    todaySolvedCount: 0,
    lastSpinWasIflas: false
};

// Colors based on theme
const wheelColors = {
    energy: ["#8b2313", "#5a3c25", "#d4af37", "#1c0e07", "#b8432b", "#70482b", "#ebd076", "#2d1c12", "#8b2313", "#5a3c25"],
    dark: ["#6c8cff", "#ff6b7a", "#4cdf8b", "#ffb347", "#c77dff", "#ff8fab", "#64dfdf", "#ffd166", "#a5b4fc", "#f472b6"],
    light: ["#4f6ef7", "#ef4444", "#22c55e", "#f59e0b", "#a855f7", "#ec4899", "#06b6d4", "#eab308", "#818cf8", "#f472b6"]
};
const specialColors = { "İFLAS": "#0d0000", "PAS": "#0a1a2a", "X2": "#5a4000" };

// Sounds
const sounds = {
    spin: document.getElementById('snd-spin'),
    tick: document.getElementById('snd-tick'),
    win: document.getElementById('snd-win'),
    wrong: document.getElementById('snd-wrong'),
    fail: document.getElementById('snd-fail')
};
function playSound(type) {
    if (sounds[type]) {
        sounds[type].currentTime = 0;
        if (type === 'spin') sounds[type].volume = 0.3;
        if (type === 'tick') sounds[type].volume = 0.5;
        sounds[type].play().catch(() => {});
    }
}

// Navigation
function showView(viewName) {
    Object.values(views).forEach(v => v.classList.remove('active'));
    Object.values(views).forEach(v => v.classList.add('hidden'));

    views[viewName].classList.remove('hidden');
    views[viewName].classList.add('active');
}

// Canvas Resize for High-DPI and Responsive
function handleResize() {
    const container = document.querySelector('.wheel-container');
    if (!container) return;
    const size = Math.min(container.clientWidth, container.clientHeight);
    if (size <= 0) return;
    const dpr = window.devicePixelRatio || 1;

    wheelCanvas.width = size * dpr;
    wheelCanvas.height = size * dpr;
    wheelCanvas.style.width = size + 'px';
    wheelCanvas.style.height = size + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    wheelLogicalSize = size;
    drawWheel();
}

let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(handleResize, 200);
});

// Initialize
function init() {
    loadUserData();
    checkDailyStreak();
    handleResize();
    setupEventListeners();
    updateStatsUI();
}

function setupEventListeners() {
    // Theme toggle
    btnTheme.addEventListener('click', () => {
        currentThemeIdx = (currentThemeIdx + 1) % themes.length;
        document.body.setAttribute('data-theme', themes[currentThemeIdx]);
        handleResize();
    });

    // Menus
    btnMenu.addEventListener('click', () => {
        if (confirm("Sınıf seçimine dönmek istediğinize emin misiniz? Mevcut puanınız sıfırlanacaktır.")) {
            resetGame();
            showView('grade');
        }
    });

    btnReset.addEventListener('click', () => {
        if (confirm("Oyunu sıfırlamak istediğinize emin misiniz?")) resetGame();
    });

    btnStats.addEventListener('click', () => {
        renderStats();
        showView('stats');
    });
    document.getElementById('btn-close-stats').addEventListener('click', () => {
        showView(state.grade ? 'idle' : 'grade');
    });

    // Grade Selection
    document.querySelectorAll('.grade-card').forEach(btn => {
        btn.addEventListener('click', (e) => {
            let g = e.currentTarget.getAttribute('data-grade');
            startGame(g);
        });
    });

    // Spin
    btnSpin.addEventListener('click', spinWheel);

    // Question actions
    document.getElementById('btn-submit').addEventListener('click', submitAnswer);
    document.getElementById('btn-skip').addEventListener('click', skipQuestion);
    document.getElementById('btn-next').addEventListener('click', () => showView('idle'));

    // Close badge popup
    document.getElementById('btn-close-badge').addEventListener('click', () => {
        document.getElementById('badge-popup-container').classList.add('hidden');
        if (badgeTimeout) clearTimeout(badgeTimeout);
    });

    // Share score
    document.getElementById('btn-share').addEventListener('click', () => {
        const template = `🎮 LGS Çark Oyunu'nda tarih yazdım! 🚀\n\n🔥 Günlük Seri: ${state.userStreak} Gün\n🏆 Toplam Puan: ${state.score} Puan\n✅ Doğru Cevap: ${state.correct}\n❌ Yanlış Cevap: ${state.wrong}\n\nHadi sen de gel, çarkı çevir ve bilgini kanıtla! 🏛️✨`;
        navigator.clipboard.writeText(template).then(() => {
            const btn = document.getElementById('btn-share');
            const oldText = btn.textContent;
            btn.textContent = "✓ Kopyalandı! Arkadaşlarına Gönder! 🚀";
            btn.style.backgroundColor = "#2e7d32";
            setTimeout(() => {
                btn.textContent = oldText;
                btn.style.backgroundColor = "";
            }, 2000);
        }).catch(err => {
            console.error("Panoya kopyalama başarısız:", err);
        });
    });
}

function startGame(grade) {
    state.grade = grade;
    state.remainingQuestions = [...SORULAR[grade]].sort(() => Math.random() - 0.5);
    document.getElementById('current-grade-label').textContent = `${grade}. Sınıf`;
    btnSpin.disabled = false;
    showView('idle');
}

function resetGame() {
    state.score = 0;
    state.correct = 0;
    state.wrong = 0;
    state.solved = 0;
    state.unitStats = {};
    if (state.grade) {
        state.remainingQuestions = [...SORULAR[state.grade]].sort(() => Math.random() - 0.5);
        showView('idle');
    } else {
        showView('grade');
    }
    updateStatsUI();
    stopTimer();
}

// Wheel Logic
function drawWheel(angleOffset = state.wheelAngle) {
    const w = wheelLogicalSize;
    const h = wheelLogicalSize;
    const cx = w / 2;
    const cy = h / 2;
    const r = cx - 10;
    const themeName = themes[currentThemeIdx];

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);

    const outerRim = cx - 4;
    const slicesR = themeName === 'energy' ? cx - 22 : cx - 10;

    if (themeName === 'energy') {
        // Outer rim
        ctx.beginPath();
        ctx.arc(0, 0, outerRim, 0, Math.PI * 2);
        ctx.fillStyle = "#3d2314";
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = "#5a381c";
        ctx.stroke();

        // Inner rim
        ctx.beginPath();
        ctx.arc(0, 0, slicesR + 2, 0, Math.PI * 2);
        ctx.fillStyle = "#8c5623";
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = "#3d2314";
        ctx.stroke();
    }

    ctx.rotate(angleOffset);

    let colorIdx = 0;
    for (let i = 0; i < SLICE_COUNT; i++) {
        let val = WHEEL_SLICES[i];
        let isSpecial = typeof val === 'string';
        let color = isSpecial ? specialColors[val] : wheelColors[themeName][colorIdx++ % wheelColors[themeName].length];

        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, slicesR, i * SLICE_ANGLE, (i + 1) * SLICE_ANGLE);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.lineWidth = themeName === 'energy' ? 1 : 2;
        ctx.strokeStyle = themeName === 'energy' ? '#3d2314' : getComputedStyle(document.body).getPropertyValue('--bg').trim();
        ctx.stroke();

        ctx.save();
        ctx.rotate(i * SLICE_ANGLE + SLICE_ANGLE / 2);
        ctx.textAlign = "center";
        ctx.fillStyle = "#ffffff";

        // Scale font based on wheel size
        const baseFontSize = Math.max(10, Math.round(w / 25));
        const specialFontSize = Math.max(8, Math.round(w / 30));
        ctx.font = isSpecial ? `bold ${specialFontSize}px 'Segoe UI'` : `bold ${baseFontSize}px 'Segoe UI'`;
        ctx.translate(slicesR * 0.7, 0);

        if (isSpecial) {
            let t = val === 'İFLAS' ? 'İFLAS' : val === 'PAS' ? 'PAS' : 'X2';
            ctx.fillText(t, 0, 6);
        } else {
            ctx.fillText(val, 0, 6);
        }
        ctx.restore();
    }
    ctx.restore();
}

function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

function spinWheel() {
    btnSpin.disabled = true;
    playSound('spin');

    const duration = 4000;
    const targetSlice = Math.floor(Math.random() * SLICE_COUNT);
    const extraTurns = Math.floor(Math.random() * 5 + 5) * Math.PI * 2;

    const sliceMidPoint = (targetSlice * SLICE_ANGLE) + (SLICE_ANGLE / 2);
    const finalAngle = (Math.PI * 1.5) - sliceMidPoint;

    const startAngle = state.wheelAngle;
    const totalRotation = extraTurns + ((finalAngle - (startAngle % (Math.PI * 2)) + (Math.PI * 2)) % (Math.PI * 2));

    let startTime = null;

    function animate(timestamp) {
        if (!startTime) startTime = timestamp;
        let p = (timestamp - startTime) / duration;
        if (p > 1) p = 1;

        let eased = easeOut(p);
        state.wheelAngle = startAngle + totalRotation * eased;
        drawWheel();

        if (p < 1) {
            requestAnimationFrame(animate);
        } else {
            onSpinComplete(targetSlice);
        }
    }
    requestAnimationFrame(animate);
}

function onSpinComplete(targetSlice) {
    btnSpin.disabled = false;
    let val = WHEEL_SLICES[targetSlice];

    if (val === "İFLAS") {
        state.lastSpinWasIflas = true;
        state.score = 0;
        updateStatsUI();
        playSound('fail');
        showFeedbackUI("İFLAS!", "Tüm puanlarınız sıfırlandı!", "var(--error)", false, null);
        return;
    }
    if (val === "PAS") {
        state.lastSpinWasIflas = false;
        showFeedbackUI("PAS!", "Bu turu geçtiniz. Puan değişmedi.", "var(--fg-dim)", false, null);
        return;
    }

    if (val === "X2") {
        state.x2Mode = true;
        state.currentPoints = 0;
    } else {
        state.x2Mode = false;
        state.currentPoints = parseInt(val);
    }

    loadQuestion();
}

function loadQuestion() {
    if (state.remainingQuestions.length === 0) {
        state.remainingQuestions = [...SORULAR[state.grade]].sort(() => Math.random() - 0.5);
    }
    state.currentQ = state.remainingQuestions.pop();
    state.selectedOpt = null;

    const qImg = document.getElementById('q-img');
    if (state.currentQ.gorsel) {
        let src = state.currentQ.gorsel;
        if (src.startsWith('web/')) {
            src = src.substring(4);
        }
        qImg.src = src;
        qImg.classList.remove('hidden');
    } else {
        qImg.src = "";
        qImg.classList.add('hidden');
    }

    document.getElementById('q-unite').textContent = state.currentQ.unite;
    document.getElementById('q-konu').textContent = state.currentQ.konu;
    document.getElementById('q-text').textContent = state.currentQ.soru;

    const optContainer = document.getElementById('options-container');
    optContainer.innerHTML = '';

    for (let key in state.currentQ.siklar) {
        let btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.innerHTML = `<span class="opt-letter">${key})</span> <span class="opt-text">${state.currentQ.siklar[key]}</span>`;
        btn.onclick = () => selectOption(btn, key);
        optContainer.appendChild(btn);
    }

    document.getElementById('btn-submit').disabled = true;
    showView('question');
    startTimer();
}

function selectOption(btnElem, key) {
    document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
    btnElem.classList.add('selected');
    state.selectedOpt = key;
    document.getElementById('btn-submit').disabled = false;
}

function startTimer() {
    stopTimer();
    state.timer = 45;
    updateTimerUI();
    state.timerInterval = setInterval(() => {
        state.timer--;
        updateTimerUI();
        if (state.timer > 0) {
            playSound('tick');
        } else {
            handleTimeout();
        }
    }, 1000);
}
function stopTimer() {
    clearInterval(state.timerInterval);
}

function updateTimerUI() {
    const progress = document.getElementById('timer-progress');
    const text = document.getElementById('timer-text');
    const container = document.querySelector('.timer-container');
    if (!progress || !text) return;

    const circumference = 2 * Math.PI * 42; // ~264
    const offset = circumference * (1 - state.timer / 45);

    progress.style.strokeDashoffset = offset;
    text.textContent = state.timer;

    container.classList.remove('timer-danger', 'timer-warn');
    if (state.timer <= 10) {
        container.classList.add('timer-danger');
    } else if (state.timer <= 20) {
        container.classList.add('timer-warn');
    }
}

function handleTimeout() {
    stopTimer();
    playSound('fail');
    state.wrong++;
    state.score -= 5;
    state.solved++;
    state.x2Mode = false;
    state.lastSpinWasIflas = false;
    updateStatsUI();
    showFeedbackUI("Süre Doldu!", `Doğru Cevap: ${state.currentQ.dogru_cevap}`, "var(--error)", false, state.currentQ.aciklama);
}

function submitAnswer() {
    if (!state.selectedOpt || !state.currentQ) return;
    stopTimer();
    let isCorrect = (state.selectedOpt === state.currentQ.dogru_cevap);
    state.solved++;

    if (isCorrect) {
        state.correct++;
        if (state.x2Mode) state.score *= 2;
        else state.score += state.currentPoints + 10;
        playSound('win');

        // Award badges
        let badgesEarned = [];
        if (state.grade === "8" && state.currentPoints === 100) {
            badgesEarned.push({
                name: "Tarih Dehası",
                desc: "8. Sınıfta 100 puanlık soruyu doğru bildin! Tarihin gerçek lideri sensin! 👑",
                emoji: "🏆"
            });
        }
        if (state.lastSpinWasIflas) {
            badgesEarned.push({
                name: "Yıkılmadım",
                desc: "İflas ettikten sonra ilk soruyu doğru bildin! Küllerinden doğdun! 🔥",
                emoji: "💪"
            });
        }

        badgesEarned.forEach((badge, idx) => {
            setTimeout(() => {
                showBadgePopup(badge.name, badge.desc, badge.emoji);
            }, idx * 4200);
        });
    } else {
        state.wrong++;
        state.score -= 5;
        playSound('wrong');
    }

    recordUnit(state.currentQ.unite, isCorrect);

    state.x2Mode = false;
    state.lastSpinWasIflas = false;
    updateStatsUI();
    onQuestionSolved();

    let title = isCorrect ? "Tebrikler!" : "Yanlış Cevap!";
    let msg = isCorrect ? "Doğru cevap verdiniz." : `Doğru cevap: ${state.currentQ.dogru_cevap}) ${state.currentQ.siklar[state.currentQ.dogru_cevap]}`;
    let col = isCorrect ? "var(--success)" : "var(--error)";

    showFeedbackUI(title, msg, col, isCorrect, state.currentQ.aciklama);
}

function skipQuestion() {
    stopTimer();
    showView('idle');
}

function showFeedbackUI(title, msg, color, isCorrect, explanation) {
    document.getElementById('feedback-title').textContent = title;
    document.getElementById('feedback-title').style.color = color;
    document.getElementById('feedback-msg').textContent = msg;

    let ic = document.getElementById('feedback-icon');
    ic.textContent = isCorrect ? '✓' : '✗';
    ic.style.color = color;

    let expEl = document.getElementById('feedback-explanation');
    if (explanation) {
        expEl.style.display = 'block';
        expEl.innerText = "Açıklama: " + explanation;
    } else {
        expEl.style.display = 'none';
    }

    showView('feedback');
}

function recordUnit(unitName, isCorrect) {
    if (!state.unitStats[unitName]) state.unitStats[unitName] = { d: 0, y: 0 };
    if (isCorrect) state.unitStats[unitName].d++;
    else state.unitStats[unitName].y++;
}

function updateStatsUI() {
    animateScore(state.score);
    document.getElementById('stat-correct').textContent = state.correct;
    document.getElementById('stat-wrong').textContent = state.wrong;
    document.getElementById('stat-solved').textContent = state.solved;
}

function animateScore(target) {
    const el = document.getElementById('total-score');
    const start = parseInt(el.textContent) || 0;
    if (start === target) return;

    const diff = target - start;
    const duration = 400;
    const startTime = performance.now();

    el.classList.remove('score-pop', 'score-flash-success', 'score-flash-error');
    void el.offsetWidth;
    el.classList.add('score-pop');
    el.classList.add(diff > 0 ? 'score-flash-success' : 'score-flash-error');
    setTimeout(() => {
        el.classList.remove('score-flash-success', 'score-flash-error');
    }, 500);

    function step(now) {
        const p = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(start + diff * eased);
        if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
}

function renderStats() {
    document.getElementById('st-score').textContent = state.score;
    document.getElementById('st-correct').textContent = state.correct;
    document.getElementById('st-wrong').textContent = state.wrong;

    const container = document.getElementById('unit-stats-container');
    container.innerHTML = '';

    if (Object.keys(state.unitStats).length === 0) {
        container.innerHTML = '<p style="text-align:center; color: var(--fg-dim);">Henüz istatistik bulunmuyor.</p>';
        return;
    }

    for (let u in state.unitStats) {
        let st = state.unitStats[u];
        let row = document.createElement('div');
        row.className = 'unit-stat-row';
        row.innerHTML = `
            <div style="flex:1;"><strong>${u}</strong></div>
            <div style="flex:0 0 100px; text-align:right;">
                <span style="color:var(--success);">✓ ${st.d}</span> |
                <span style="color:var(--error);">✗ ${st.y}</span>
            </div>
        `;
        container.appendChild(row);
    }
}

// Streak & Quest helper functions
function loadUserData() {
    const raw = localStorage.getItem('lgs_cark_userdata');
    if (raw) {
        try {
            const data = JSON.parse(raw);
            state.userStreak = data.userStreak || 0;
            state.lastLoginDate = data.lastLoginDate || "";
            state.todaySolvedCount = data.todaySolvedCount || 0;
            const todayStr = getTodayString();
            if (data.todaySolvedDate !== todayStr) {
                state.todaySolvedCount = 0;
            }
        } catch (e) {
            console.error("Kullanıcı verileri yüklenirken hata:", e);
        }
    }
}

function saveUserData() {
    try {
        const data = {
            userStreak: state.userStreak,
            lastLoginDate: state.lastLoginDate,
            todaySolvedCount: state.todaySolvedCount,
            todaySolvedDate: getTodayString()
        };
        localStorage.setItem('lgs_cark_userdata', JSON.stringify(data));
    } catch (e) {
        console.error("Kullanıcı verileri kaydedilirken hata:", e);
    }
}

function getTodayString() {
    const d = new Date();
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function getYesterdayString() {
    const d = new Date();
    d.setDate(d.getDate() - 1);
    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

function checkDailyStreak() {
    const todayStr = getTodayString();
    const yesterdayStr = getYesterdayString();
    
    if (!state.lastLoginDate) {
        state.userStreak = 1;
        state.lastLoginDate = todayStr;
    } else if (state.lastLoginDate === todayStr) {
        // Do nothing
    } else if (state.lastLoginDate === yesterdayStr) {
        state.userStreak += 1;
        state.lastLoginDate = todayStr;
    } else {
        state.userStreak = 1;
        state.lastLoginDate = todayStr;
    }
    saveUserData();
    updateStreakAndQuestUI();
}

function onQuestionSolved() {
    state.todaySolvedCount += 1;
    updateStreakAndQuestUI();
    saveUserData();
}

function updateStreakAndQuestUI() {
    const streakEl = document.getElementById('user-streak');
    const questEl = document.getElementById('user-quest');
    if (streakEl) {
        streakEl.textContent = `🔥 Günlük Seri: ${state.userStreak} Gün`;
    }
    if (questEl) {
        if (state.todaySolvedCount >= 5) {
            questEl.textContent = "🎯 Görev: Bugünün görevi tamamlandı! Harikasın! 🚀";
        } else {
            questEl.textContent = `🎯 Görev: Bugün 5 soru çöz! (${state.todaySolvedCount}/5)`;
        }
    }
}

// Badge Popup helper functions
let badgeTimeout = null;
function showBadgePopup(name, desc, emoji) {
    const container = document.getElementById('badge-popup-container');
    const emEl = document.getElementById('badge-emoji');
    const nameEl = document.getElementById('badge-name');
    const descEl = document.getElementById('badge-desc');
    
    if (container && emEl && nameEl && descEl) {
        emEl.textContent = emoji;
        nameEl.textContent = name;
        descEl.textContent = desc;
        container.classList.remove('hidden');
        
        if (badgeTimeout) clearTimeout(badgeTimeout);
        badgeTimeout = setTimeout(() => {
            container.classList.add('hidden');
        }, 4000);
    }
}

// Start
init();
