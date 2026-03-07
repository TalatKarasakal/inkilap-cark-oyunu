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
    wheelAngle: 0
};

// Colors based on theme (approximate values for drawing wheel)
const wheelColors = {
    energy: ["#e8a020", "#cc2200", "#f5d040", "#aa1800", "#ffbe45", "#8b0000", "#ffd060", "#b83000", "#e89000", "#c01500"],
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
        sounds[type].play().catch(e => console.log('Autoplay prevented'));
    }
}

// Navigation
function showView(viewName) {
    Object.values(views).forEach(v => v.classList.remove('active'));
    Object.values(views).forEach(v => v.classList.add('hidden'));

    views[viewName].classList.remove('hidden');
    views[viewName].classList.add('active');
}

// Initialize
function init() {
    drawWheel();
    setupEventListeners();
    updateStatsUI();
}

function setupEventListeners() {
    // Theme toggle
    btnTheme.addEventListener('click', () => {
        currentThemeIdx = (currentThemeIdx + 1) % themes.length;
        document.body.setAttribute('data-theme', themes[currentThemeIdx]);
        drawWheel(); // redraw colors
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
    const w = wheelCanvas.width;
    const h = wheelCanvas.height;
    const cx = w / 2;
    const cy = h / 2;
    const r = cx - 10;
    const themeName = themes[currentThemeIdx];

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(angleOffset);

    let colorIdx = 0;
    for (let i = 0; i < SLICE_COUNT; i++) {
        let val = WHEEL_SLICES[i];
        let isSpecial = typeof val === 'string';
        let color = isSpecial ? specialColors[val] : wheelColors[themeName][colorIdx++ % wheelColors[themeName].length];

        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, r, i * SLICE_ANGLE, (i + 1) * SLICE_ANGLE);
        ctx.fillStyle = color;
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = getComputedStyle(document.body).getPropertyValue('--bg').trim();
        ctx.stroke();

        ctx.save();
        ctx.rotate(i * SLICE_ANGLE + SLICE_ANGLE / 2);
        ctx.textAlign = "center";
        ctx.fillStyle = "#ffffff";
        ctx.font = isSpecial ? "bold 16px 'Segoe UI'" : "bold 20px 'Segoe UI'";
        ctx.translate(r * 0.7, 0);

        if (isSpecial) {
            let t = val === 'İFLAS' ? '💀 İFLAS' : val === 'PAS' ? '⏸ PAS' : '⚡ X2';
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

    // Calculate angle to land exactly in the middle of targetSlice at the top (-90 deg or 270 deg)
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
        state.score = 0;
        updateStatsUI();
        playSound('fail');
        showFeedbackUI("💀 İFLAS!", "Tüm puanlarınız sıfırlandı!", "var(--error)", false, null);
        return;
    }
    if (val === "PAS") {
        showFeedbackUI("⏸ PAS!", "Bu turu geçtiniz. Puan değişmedi.", "var(--fg-dim)", false, null);
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

    document.getElementById('q-unite').textContent = state.currentQ.unite;
    document.getElementById('q-konu').textContent = state.currentQ.konu;
    document.getElementById('q-text').textContent = state.currentQ.soru;

    const optContainer = document.getElementById('options-container');
    optContainer.innerHTML = '';

    // siklar is an object {A: "...", B: "..."}
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
    // deselect all
    document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
    // select clicked
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
    document.getElementById('timer-val').textContent = `🕐 ${state.timer}`;
    const fill = document.getElementById('timer-fill');
    fill.style.width = `${(state.timer / 45) * 100}%`;
    if (state.timer <= 10) fill.style.backgroundColor = 'var(--error)';
    else if (state.timer <= 20) fill.style.backgroundColor = 'var(--warning)';
    else fill.style.backgroundColor = 'var(--accent)';
}
function handleTimeout() {
    stopTimer();
    playSound('fail');
    state.wrong++;
    state.score -= 5;
    state.solved++;
    state.x2Mode = false;
    updateStatsUI();
    showFeedbackUI("Süre Doldu!", `Doğru Cevap: ${state.currentQ.dogru_cevap}`, "var(--error)", false, state.currentQ.aciklama);
}

function submitAnswer() {
    stopTimer();
    let isCorrect = (state.selectedOpt === state.currentQ.dogru_cevap);
    state.solved++;

    if (isCorrect) {
        state.correct++;
        if (state.x2Mode) state.score *= 2;
        else state.score += state.currentPoints + 10; // Bonus
        playSound('win');
    } else {
        state.wrong++;
        state.score -= 5;
        playSound('wrong');
    }

    recordUnit(state.currentQ.unite, isCorrect);

    state.x2Mode = false;
    updateStatsUI();

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
    document.getElementById('total-score').textContent = state.score;
    document.getElementById('stat-correct').textContent = state.correct;
    document.getElementById('stat-wrong').textContent = state.wrong;
    document.getElementById('stat-solved').textContent = state.solved;
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

// Start
init();
