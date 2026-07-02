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
    unit: document.getElementById('view-unit'),
    mode: document.getElementById('view-mode'),
    wheel: document.getElementById('view-wheel'),
    question: document.getElementById('view-question'),
    feedback: document.getElementById('view-feedback'),
    stats: document.getElementById('view-stats')
};

// HUD Elements
const hudScore = document.getElementById('hud-score');
const hudStreak = document.getElementById('hud-streak');
const hudCorrect = document.getElementById('hud-correct');
const hudWrong = document.getElementById('hud-wrong');
const hudSolved = document.getElementById('hud-solved');
const hudQuest = document.getElementById('hud-quest');
const hudBar = document.getElementById('hud-bar');

// Game Rules & State
const WHEEL_SLICES = [10, 20, "PAS", 30, 40, "X2", 50, 60, 70, 80, "İFLAS", 90, 100];
const SLICE_COUNT = WHEEL_SLICES.length;
const SLICE_ANGLE = (Math.PI * 2) / SLICE_COUNT;

const themes = ["energy", "dark", "light"];
let currentThemeIdx = 0;

let wheelLogicalSize = 700;

let state = {
    grade: null,
    selectedUnit: null,
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
    lastSpinWasIflas: false,
    earnedBadges: [],
    isTeamMode: false,
    teamScores: { A: 0, B: 0 },
    activeTeam: 'A',
    teamCorrect: 0,
    teamWrong: 0
};

// Colors based on theme
const wheelColors = {
    energy: ["#3b82f6", "#1d1e3a", "#8b5cf6", "#0b0c16", "#2563eb", "#2a2b54", "#6366f1", "#121324", "#3b82f6", "#1d1e3a"],
    dark: ["#6c8cff", "#ff6b7a", "#4cdf8b", "#ffb347", "#c77dff", "#ff8fab", "#64dfdf", "#ffd166", "#a5b4fc", "#f472b6"],
    light: ["#4f6ef7", "#ef4444", "#22c55e", "#f59e0b", "#a855f7", "#ec4899", "#06b6d4", "#eab308", "#818cf8", "#f472b6"]
};
const specialColors = { "İFLAS": "#ff1744", "PAS": "#1f2041", "X2": "#ffd54f" };


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
    Object.values(views).forEach(v => {
        if (v) {
            v.classList.remove('active');
            v.classList.add('hidden');
        }
    });

    if (views[viewName]) {
        views[viewName].classList.remove('hidden');
        views[viewName].classList.add('active');
    }

    // Toggle HUD visibility
    if (hudBar) {
        if (viewName === 'grade' || viewName === 'unit' || !state.grade) {
            hudBar.style.visibility = 'hidden';
        } else {
            hudBar.style.visibility = 'visible';
        }
    }

    // Re-trigger handleResize when switching to wheel stage
    if (viewName === 'wheel') {
        setTimeout(handleResize, 50);
    }
}

// Canvas Resize for High-DPI and Responsive
function handleResize() {
    const container = document.querySelector('.wheel-container');
    if (!container) return;
    let size = Math.min(container.clientWidth, container.clientHeight);
    if (size <= 0) {
        // Fallback calculation if hidden
        size = Math.min(window.innerWidth - 60, window.innerHeight - 250, 450);
    }
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
    
    document.getElementById('btn-print-report').addEventListener('click', printReportCard);
    
    document.getElementById('btn-close-stats').addEventListener('click', () => {
        showView(state.grade ? 'wheel' : 'grade');
    });

    // Grade Selection
    document.querySelectorAll('.grade-card').forEach(btn => {
        btn.addEventListener('click', (e) => {
            let g = e.currentTarget.getAttribute('data-grade');
            startGame(g);
        });
    });

    // Unit selection back button
    document.getElementById('btn-unit-back').addEventListener('click', () => {
        showView('grade');
    });

    // Mode Selection
    document.getElementById('btn-mode-single').addEventListener('click', () => selectMode(false));
    document.getElementById('btn-mode-team').addEventListener('click', () => selectMode(true));
    document.getElementById('btn-mode-back').addEventListener('click', () => showView('unit'));

    // Spin
    btnSpin.addEventListener('click', spinWheel);

    // Question actions
    document.getElementById('btn-submit').addEventListener('click', submitAnswer);
    document.getElementById('btn-skip').addEventListener('click', skipQuestion);
    document.getElementById('btn-next').addEventListener('click', () => {
        if (state.isTeamMode) {
            state.activeTeam = state.activeTeam === 'A' ? 'B' : 'A';
            updateStatsUI();
        }
        showView('wheel');
    });

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
    state.selectedUnit = null;
    document.getElementById('unit-grade-label').textContent = `${grade}. Sınıf`;

    // Extract unique units for this grade
    const units = [...new Set(SORULAR[grade].map(q => q.unite))].sort();

    const container = document.getElementById('unit-list-container');
    container.innerHTML = '';

    // Add "All Units" card
    const allBtn = document.createElement('button');
    allBtn.className = 'unit-card mix-card';
    allBtn.innerHTML = `<span>📚 Tüm Ünitelerden Karışık</span> <span class="unit-qcount">${SORULAR[grade].length} Soru</span>`;
    allBtn.onclick = () => selectUnit('ALL');
    container.appendChild(allBtn);

    // Add specific unit cards
    units.forEach(u => {
        const uCount = SORULAR[grade].filter(q => q.unite === u).length;
        const btn = document.createElement('button');
        btn.className = 'unit-card';
        btn.innerHTML = `<span>📖 ${u}</span> <span class="unit-qcount">${uCount} Soru</span>`;
        btn.onclick = () => selectUnit(u);
        container.appendChild(btn);
    });

    showView('unit');
}

function selectUnit(unit) {
    state.selectedUnit = unit;
    if (unit === 'ALL') {
        state.remainingQuestions = [...SORULAR[state.grade]].sort(() => Math.random() - 0.5);
    } else {
        state.remainingQuestions = SORULAR[state.grade].filter(q => q.unite === unit).sort(() => Math.random() - 0.5);
    }
    showView('mode');
}

function selectMode(isTeam) {
    state.isTeamMode = isTeam;
    state.teamScores = { A: 0, B: 0 };
    state.activeTeam = 'A';
    state.teamCorrect = 0;
    state.teamWrong = 0;
    state.score = 0;
    state.correct = 0;
    state.wrong = 0;
    state.solved = 0;

    // Toggle HUD display
    const indHud = document.getElementById('hud-individual');
    const teamHud = document.getElementById('hud-team');
    if (indHud && teamHud) {
        if (state.isTeamMode) {
            indHud.style.display = 'none';
            teamHud.style.display = 'flex';
        } else {
            indHud.style.display = 'flex';
            teamHud.style.display = 'none';
        }
    }

    updateStatsUI();
    btnSpin.disabled = false;
    showView('wheel');
}

function resetGame() {
    state.score = 0;
    state.correct = 0;
    state.wrong = 0;
    state.solved = 0;
    state.unitStats = {};
    if (state.grade) {
        selectUnit(state.selectedUnit || 'ALL');
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
    const themeName = 'energy';

    ctx.clearRect(0, 0, w, h);
    ctx.save();
    ctx.translate(cx, cy);

    const outerRim = cx - 4;
    const slicesR = cx - 22;

    // Outer rim (glowing cyan/purple gradient)
    ctx.beginPath();
    ctx.arc(0, 0, outerRim, 0, Math.PI * 2);
    let rimGrad = ctx.createLinearGradient(-outerRim, -outerRim, outerRim, outerRim);
    rimGrad.addColorStop(0, "#00e5ff");
    rimGrad.addColorStop(0.5, "#651fff");
    rimGrad.addColorStop(1, "#00e5ff");
    ctx.strokeStyle = rimGrad;
    ctx.lineWidth = 5;
    ctx.stroke();

    // Inner rim
    ctx.beginPath();
    ctx.arc(0, 0, slicesR + 2, 0, Math.PI * 2);
    ctx.fillStyle = "#0b0c16";
    ctx.fill();
    ctx.lineWidth = 2;
    ctx.strokeStyle = "#121324";
    ctx.stroke();

    ctx.rotate(angleOffset);

    let colorIdx = 0;
    for (let i = 0; i < SLICE_COUNT; i++) {
        let val = WHEEL_SLICES[i];
        let isSpecial = typeof val === 'string';
        let color = isSpecial ? specialColors[val] : wheelColors[themeName][colorIdx++ % wheelColors[themeName].length];

        ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.arc(0, 0, slicesR, i * SLICE_ANGLE, (i + 1) * SLICE_ANGLE);
        
        let sliceGrad = ctx.createRadialGradient(0, 0, slicesR * 0.2, 0, 0, slicesR);
        sliceGrad.addColorStop(0, "#121324");
        sliceGrad.addColorStop(0.85, color);
        sliceGrad.addColorStop(1, "rgba(255, 255, 255, 0.15)");
        
        ctx.fillStyle = sliceGrad;
        ctx.fill();
        ctx.lineWidth = 1.5;
        ctx.strokeStyle = '#121324';
        ctx.stroke();

        ctx.save();
        ctx.rotate(i * SLICE_ANGLE + SLICE_ANGLE / 2);
        ctx.textAlign = "center";
        ctx.fillStyle = "#ffffff";

        // Scale font based on wheel size
        const baseFontSize = Math.max(10, Math.round(w / 25));
        const specialFontSize = Math.max(8, Math.round(w / 30));
        ctx.font = isSpecial ? `bold ${specialFontSize}px 'Outfit'` : `bold ${baseFontSize}px 'Outfit'`;
        ctx.translate(slicesR * 0.7, 0);

        if (isSpecial) {
            let t = val === 'İFLAS' ? 'İFLAS' : val === 'PAS' ? 'PAS' : 'X2';
            ctx.fillText(t, 0, 6);
        } else {
            ctx.fillText(val, 0, 6);
        }
        ctx.restore();
    }
    
    // Central cap (holographic blue orb)
    ctx.beginPath();
    ctx.arc(0, 0, slicesR * 0.22, 0, Math.PI * 2);
    let centerGrad = ctx.createRadialGradient(0, 0, 2, 0, 0, slicesR * 0.22);
    centerGrad.addColorStop(0, "#ffffff");
    centerGrad.addColorStop(0.3, "#00e5ff");
    centerGrad.addColorStop(1, "#121324");
    ctx.fillStyle = centerGrad;
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
    ctx.stroke();

    // Center icon
    ctx.fillStyle = "#ffffff";
    ctx.font = `bold ${Math.max(16, Math.round(slicesR * 0.15))}px 'Outfit'`;
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText("🏛", 0, 0);

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

let specialParticlesInterval = null;

function showSpecial3DModal(type, title, message, onCloseCallback) {
    const modal = document.getElementById('special-3d-modal');
    const card = document.getElementById('special-3d-card');
    const icon = document.getElementById('special-3d-icon');
    const titleEl = document.getElementById('special-3d-title');
    const msgEl = document.getElementById('special-3d-message');
    const closeBtn = document.getElementById('btn-special-3d-close');
    const particlesContainer = document.getElementById('special-3d-particles');

    if (!modal || !card || !icon || !titleEl || !msgEl || !closeBtn || !particlesContainer) return;

    // Reset card classes
    card.className = "special-3d-card";
    card.classList.add(`glow-${type}`);

    // Set content
    let iconEmoji = "⚡";
    let particleColor = "#ffd54f"; // Gold
    if (type === 'iflas') {
        iconEmoji = "💀";
        particleColor = "#ff1744"; // Red
    } else if (type === 'pas') {
        iconEmoji = "🛡️";
        particleColor = "#90a4ae"; // Silver/Blue
    }
    icon.textContent = iconEmoji;
    icon.style.color = particleColor;
    titleEl.textContent = title;
    msgEl.textContent = message;

    // Clear previous particles
    particlesContainer.innerHTML = '';
    if (specialParticlesInterval) clearInterval(specialParticlesInterval);

    // Spawn particles
    specialParticlesInterval = setInterval(() => {
        const p = document.createElement('div');
        p.className = 'special-particle';
        p.style.backgroundColor = particleColor;
        p.style.boxShadow = `0 0 8px ${particleColor}`;
        p.style.left = `${Math.random() * 100}vw`;
        p.style.width = `${Math.random() * 8 + 4}px`;
        p.style.height = p.style.width;
        p.style.animationDuration = `${Math.random() * 2 + 2}s`;
        particlesContainer.appendChild(p);

        // Remove particle after animation
        setTimeout(() => p.remove(), 4000);
    }, 120);

    // Close handler
    const closeHandler = () => {
        modal.classList.add('hidden');
        clearInterval(specialParticlesInterval);
        particlesContainer.innerHTML = '';
        closeBtn.removeEventListener('click', closeHandler);
        if (onCloseCallback) onCloseCallback();
    };
    closeBtn.addEventListener('click', closeHandler);

    // Show modal
    modal.classList.remove('hidden');
}

function onSpinComplete(targetSlice) {
    btnSpin.disabled = false;
    let val = WHEEL_SLICES[targetSlice];

    const currentTeamName = state.activeTeam === 'A' ? 'A Grubu' : 'B Grubu';

    if (val === "İFLAS") {
        state.lastSpinWasIflas = true;
        playSound('fail');
        if (state.isTeamMode) {
            state.teamScores[state.activeTeam] = 0;
            updateStatsUI();
            showSpecial3DModal('iflas', 'İFLAS!', `${currentTeamName} puanı sıfırlandı!`, () => {
                state.activeTeam = state.activeTeam === 'A' ? 'B' : 'A';
                updateStatsUI();
                showView('wheel');
            });
        } else {
            state.score = 0;
            updateStatsUI();
            showSpecial3DModal('iflas', 'İFLAS!', 'Tüm puanlarınız sıfırlandı!', () => {
                showView('wheel');
            });
        }
        return;
    }
    if (val === "PAS") {
        state.lastSpinWasIflas = false;
        if (state.isTeamMode) {
            showSpecial3DModal('pas', 'PAS!', `${currentTeamName} bu turu pas geçti!`, () => {
                state.activeTeam = state.activeTeam === 'A' ? 'B' : 'A';
                updateStatsUI();
                showView('wheel');
            });
        } else {
            showSpecial3DModal('pas', 'PAS!', 'Bu turu geçtiniz. Puan değişmedi.', () => {
                showView('wheel');
            });
        }
        return;
    }

    if (val === "X2") {
        state.x2Mode = true;
        state.currentPoints = 0;
        if (state.isTeamMode) {
            showSpecial3DModal('x2', 'X2 KATLAYICI!', `${currentTeamName} için X2 aktif! Doğru cevaplarsa puanı ikiye katlanacak!`, () => {
                loadQuestion();
            });
        } else {
            showSpecial3DModal('x2', 'X2 KATLAYICI!', 'X2 aktif! Doğru cevaplarsanız toplam puanınız 2 katına çıkacak!', () => {
                loadQuestion();
            });
        }
    } else {
        state.x2Mode = false;
        state.currentPoints = parseInt(val);
        loadQuestion();
    }
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
    state.solved++;
    
    if (state.isTeamMode) {
        state.teamWrong++;
        state.teamScores[state.activeTeam] -= 5;
    } else {
        state.wrong++;
        state.score -= 5;
    }
    
    state.x2Mode = false;
    state.lastSpinWasIflas = false;
    updateStatsUI();
    onQuestionSolved();
    
    const currentTeamName = state.activeTeam === 'A' ? 'A Grubu' : 'B Grubu';
    let msg = "";
    if (state.isTeamMode) {
        msg = `${currentTeamName} süre sınırını aştı ve puan kaybetti. Devam et'e basınca sıra diğer takıma geçecek. Doğru Cevap: ${state.currentQ.dogru_cevap}`;
    } else {
        msg = `Doğru Cevap: ${state.currentQ.dogru_cevap}`;
    }
    showFeedbackUI("Süre Doldu!", msg, "var(--error)", false, state.currentQ.aciklama);
}

function submitAnswer() {
    if (!state.selectedOpt || !state.currentQ) return;
    stopTimer();
    let isCorrect = (state.selectedOpt === state.currentQ.dogru_cevap);
    state.solved++;

    if (state.isTeamMode) {
        if (isCorrect) {
            state.teamCorrect++;
            let earned = state.x2Mode ? state.teamScores[state.activeTeam] : (state.currentPoints + 10);
            state.teamScores[state.activeTeam] += earned;
            playSound('win');
        } else {
            state.teamWrong++;
            state.teamScores[state.activeTeam] -= 5;
            playSound('wrong');
        }
    } else {
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
                if (!state.earnedBadges.some(b => b.name === badge.name)) {
                    state.earnedBadges.push(badge);
                    saveUserData();
                }
                setTimeout(() => {
                    showBadgePopup(badge.name, badge.desc, badge.emoji);
                }, idx * 4200);
            });
        } else {
            state.wrong++;
            state.score -= 5;
            playSound('wrong');
        }
    }

    recordUnit(state.currentQ.unite, isCorrect);

    state.x2Mode = false;
    state.lastSpinWasIflas = false;
    updateStatsUI();
    onQuestionSolved();

    const currentTeamName = state.activeTeam === 'A' ? 'A Grubu' : 'B Grubu';
    let title = isCorrect ? "Tebrikler!" : "Yanlış Cevap!";
    let msg = "";
    if (state.isTeamMode) {
        msg = isCorrect 
            ? `${currentTeamName} doğru cevap verdi ve puan kazandı! Devam et'e basınca sıra diğer takıma geçecek.` 
            : `Yanlış cevap! Doğru cevap: ${state.currentQ.dogru_cevap}) ${state.currentQ.siklar[state.currentQ.dogru_cevap]}. Devam et'e basınca sıra diğer takıma geçecek.`;
    } else {
        msg = isCorrect ? "Doğru cevap verdiniz." : `Doğru cevap: ${state.currentQ.dogru_cevap}) ${state.currentQ.siklar[state.currentQ.dogru_cevap]}`;
    }
    let col = isCorrect ? "var(--success)" : "var(--error)";

    showFeedbackUI(title, msg, col, isCorrect, state.currentQ.aciklama);
}

function skipQuestion() {
    stopTimer();
    if (state.isTeamMode) {
        state.activeTeam = state.activeTeam === 'A' ? 'B' : 'A';
        updateStatsUI();
    }
    showView('wheel');
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
    if (state.isTeamMode) {
        const teamAScoreEl = document.getElementById('hud-team-a-score');
        const teamBScoreEl = document.getElementById('hud-team-b-score');
        const teamCorrectEl = document.getElementById('hud-team-correct');
        const teamWrongEl = document.getElementById('hud-team-wrong');
        const teamTurnEl = document.getElementById('hud-team-turn');

        if (teamAScoreEl) teamAScoreEl.textContent = state.teamScores.A;
        if (teamBScoreEl) teamBScoreEl.textContent = state.teamScores.B;
        if (teamCorrectEl) teamCorrectEl.textContent = state.teamCorrect;
        if (teamWrongEl) teamWrongEl.textContent = state.teamWrong;

        if (teamTurnEl) {
            teamTurnEl.textContent = `📢 Sıra: ${state.activeTeam} Grubunda`;
            teamTurnEl.className = "hud-item team-turn-indicator";
            if (state.activeTeam === 'A') {
                teamTurnEl.classList.add('team-turn-active-a');
            } else {
                teamTurnEl.classList.add('team-turn-active-b');
            }
        }
    } else {
        animateScore(state.score);
        if (hudCorrect) hudCorrect.textContent = state.correct;
        if (hudWrong) hudWrong.textContent = state.wrong;
        if (hudSolved) hudSolved.textContent = state.solved;
    }
}

function animateScore(target) {
    const el = hudScore;
    if (!el) return;
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
        document.getElementById('ai-guidance-box').style.display = 'none';
        return;
    }

    for (let u in state.unitStats) {
        let st = state.unitStats[u];
        let total = st.d + st.y;
        let pct = total > 0 ? Math.round((st.d / total) * 100) : 0;
        let row = document.createElement('div');
        row.className = 'unit-stat-row';
        row.innerHTML = `
            <div style="flex:1;"><strong>${u}</strong></div>
            <div style="flex:0 0 160px; text-align:right; display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">
                <span style="color:var(--success);">✓ ${st.d}</span> |
                <span style="color:var(--error);">✗ ${st.y}</span> |
                <span style="color:${pct >= 70 ? 'var(--success)' : 'var(--warning)'}; font-weight: bold;">%${pct}</span>
            </div>
        `;
        container.appendChild(row);
    }
    
    generateAIRecommendations();
}

const STUDY_RECS = {
    // 5. Sınıf
    "Ünite 1 – Birlikte Yaşamak": "Sosyal roller, hak ve sorumluluklarımız ile çocuk hakları konularına tekrar çalışmalısınız.",
    "Ünite 2 – Evimiz Dünya": "Türkiye'nin fiziki yeryüzü şekilleri, iklim tipleri, bitki örtüsü ve beşerî coğrafya özelliklerini gözden geçirmelisiniz.",
    "Ünite 3 – Ortak Mirasımız": "Anadolu and Mezopotamya'nın kadim uygarlıkları ile ülkemizin somut/somut olmayan kültürel miras varlıklarını tekrar etmelisiniz.",
    "Ünite 4 – Yaşayan Demokrasimiz": "Demokrasinin temel ilkeleri, devletin yönetim organları ve katılım hakkının önemi konularını çalışmalısınız.",
    "Ünite 5 – Hayatımızda Ekonomi": "Ekonomik faaliyetler, meslek grupları, bütçe hazırlama ve bilinçli bir tüketicinin yapması gerekenler konularına bakmalısınız.",
    "Ünite 6 – Teknoloji ve Sosyal Bilimler": "Teknolojinin sosyal hayatımız üzerindeki etkileri, sosyal bilimlerin dalları ve bilimsel çalışma etiği konularını tekrar etmelisiniz.",
    
    // 6. Sınıf
    "Ünite 1 – Birlikte Yaşamak": "Sosyal roller, toplumsal yardımlaşma ve dayanışma ile ön yargıları kırma konularını incelemelisiniz.",
    "Ünite 2 – Evimiz Dünya": "Dünya'nın paralel/meridyen yapısı, kıtalar ve okyanuslar ile ülkemizin coğrafi konumunu tekrar etmelisiniz.",
    "Ünite 3 – Ortak Mirasımız": "İlk Türk devletlerinin kültürel özellikleri, İslamiyetin doğuşu ve Türklerin İslamiyete geçişini çalışmalısınız.",
    "Ünite 4 – Yaşayan Demokrasimiz": "Demokratik yönetim şekilleri, kadın hakları ve Türk tarihindeki yönetim yapılarını gözden geçirmelisiniz.",
    "Ünite 5 – Hayatımızdaki Ekonomi": "Üretim kaynaklarımız, yatırım ve girişimcilik fikirleri ile vergilerimizin önemi konularını çalışmalısınız.",
    "Ünite 6 – Teknoloji ve Sosyal Bilimler": "Bilim ve teknolojideki gelişmeler ile telif/patent haklarının önemi konularını çalışmalısınız.",
    
    // 7. Sınıf
    "Ünite 1 – Birey ve Toplum": "Olumlu ve etkili iletişim becerileri, medya okuryazarlığı, RTÜK ve iletişim özgürlüğü (sansür, basın özgürlüğü vb.) konularını tekrar etmelisiniz.",
    "Ünite 2 – Kültür ve Miras": "Osmanlı Devleti'nin kuruluş süreci, uyguladığı iskân ve istimâlet politikaları, denizlerdeki fetihler ve Avrupa'daki uyanışın (Rönesans, Reform vb.) Osmanlı'ye etkilerini incelemelisiniz.",
    "Ünite 3 – İnsanlar, Yerler ve Çevreler": "Nüfusun dağılışını etkileyen faktörler, Türkiye'deki göç dalgaları ve göçün nedenleri/sonuçları konularını gözden geçirmelisiniz.",
    "Ünite 4 – Bilim, Teknoloji ve Toplum": "Tarih boyunca bilginin korunması/yayılması (kil tabletler, matbaa) ve ünlü Türk-İslam bilginleri (İbn-i Sina, Farabi vb.) konularını çalışmalısınız.",
    "Ünite 5 – Üretim, Dağıtım ve Tüketim": "Toprağın yönetimde ve üretimdeki önemi, Ahilik/Lonca teşkilatı, mesleki yönlendirme ve dijital çağın getirdiği yeni meslekleri incelemelisiniz.",
    "Ünite 6 – Etkin Vatandaşlık": "Demokratik yönetimlerin tarihi gelişimi, Türkiye Cumhuriyeti anayasasının temel nitelikleri ve sivil toplum örgütlerinin (STK) faaliyetlerine odaklanmalısınız.",
    "Ünite 7 – Küresel Bağlantılar": "Ülkemizin üye olduğu uluslararası siyasi/ekonomik kuruluşlar (BM, NATO vb.) ve küresel çevre/iklim sorunlarına karşı alınabilecek tedbirleri tekrar etmelisiniz.",
    
    // 8. Sınıf
    "Ünite 1 – Bir Kahraman Doğuyor": "Mustafa Kemal'in çocukluk dönemi, okuduğu okullar, Selanik şehrinin sosyal/kültürel yapısı ve askerlik hayatı (Trablusgarp Savaşı, Balkan Savaşları, Çanakkale Cephesi) konularını tekrar etmelisiniz.",
    "Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar": "I. Dünya Savaşı'nın nedenleri ve cepheleri, Mondros Ateşkes Antlaşması, Havza ve Amasya Genelgeleri, Erzurum ve Sivas Kongreleri ile Misak-ı Milli kararlarına tekrar çalışmalısınız.",
    "Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!": "Doğu ve Güney cepheleri, Batı cephesindeki düzenli ordu savaşları (I. ve II. İnönü, Kütahya-Eskişehir, Sakarya Meydan Muharebesi, Büyük Taarruz) ve ülkemizin bağımsızlık belgesi olan Lozan Antlaşması konularını çalışmalısınız.",
    "Ünite 4 – Atatürkçülük ve Çağdaşlaşan Türkiye": "Siyasi alandaki inkılaplar (Saltanatın kaldırılması, Ankara'nın başkent oluşu, Cumhuriyetin ilanı, Halifeliğin kaldırılması), eğitim/kültür inkılapları ve Atatürk ilkeleri (Cumhuriyetçilik, Milliyetçilik, Halkçılık, Devletçilik, Laiklik, İnkılapçılık) konularına odaklanın.",
    "Ünite 5 – Demokratikleşme Çabaları": "Çok partili hayata geçiş denemeleri, Terakkiperver Cumhuriyet Fırkası, Serbest Cumhuriyet Fırkası ve Şeyh Said İsyanı gibi laik cumhuriyete karşı çıkan isyanları çalışmalısınız.",
    "Ünite 6 – Atatürk Dönemi Türk Dış Politikası": "Atatürk dönemi dış politikanın temel ilkeleri, Lozan'dan kalan sorunlar (Nüfus mübadelesi, Yabancı okullar, Musul sorunu, Boğazlar konusu, Hatay meselesi) ve barış paktlarını (Balkan Antantı, Sadabat Paktı) tekrar edin."
};

function generateAIRecommendations() {
    const box = document.getElementById('ai-guidance-box');
    const content = document.getElementById('ai-guidance-content');
    
    if (!box || !content) return;
    
    let weakUnits = [];
    let hasData = false;
    
    for (let u in state.unitStats) {
        let st = state.unitStats[u];
        let total = st.d + st.y;
        if (total > 0) {
            hasData = true;
            let pct = st.d / total;
            if (pct < 0.70) {
                weakUnits.push({ name: u, pct: Math.round(pct * 100) });
            }
        }
    }
    
    if (!hasData) {
        content.innerHTML = "💡 Henüz analiz edilecek bir soru çözmediniz. Soruları çözdükçe size özel tavsiyeler burada görünecektir.";
        box.style.display = 'block';
        return;
    }
    
    if (weakUnits.length === 0) {
        content.innerHTML = "🎯 <strong>Tebrikler!</strong> Çalıştığınız tüm ünitelerde %70'in üzerinde yüksek bir başarı oranına sahipsiniz. LGS hazırlığınız harika gidiyor! Bu şekilde çalışmaya devam edin. 🚀";
    } else {
        let html = "<p>Konu başarı analizinize göre aşağıdaki ünitelerde eksikleriniz tespit edildi. Rehberlik servisi tavsiyelerini dikkatle inceleyin:</p><ul style='margin-left: 1.5rem; margin-top: 0.5rem;'>";
        weakUnits.forEach(u => {
            let rec = STUDY_RECS[u.name] || `${u.name} ünitesiyle ilgili konu özetlerini tekrar gözden geçirmelisiniz.`;
            html += `<li style='margin-bottom: 0.75rem;'><strong>${u.name} (Başarı: %${u.pct}):</strong> ${rec}</li>`;
        });
        html += "</ul>";
        content.innerHTML = html;
    }
    box.style.display = 'block';
}

function printReportCard() {
    document.getElementById('print-date').textContent = `Tarih: ${new Date().toLocaleDateString('tr-TR')}`;
    
    const gradeInfoMap = {
        "5": "5. Sınıf Sosyal Bilgiler",
        "6": "6. Sınıf Sosyal Bilgiler",
        "7": "7. Sınıf Sosyal Bilgiler",
        "8": "8. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük"
    };
    
    document.getElementById('print-grade').textContent = gradeInfoMap[state.grade] || `${state.grade}. Sınıf`;
    document.getElementById('print-unit').textContent = state.selectedUnit === 'ALL' ? 'Tüm Üniteler' : state.selectedUnit;
    
    document.getElementById('print-score').textContent = state.score;
    document.getElementById('print-solved').textContent = state.solved;
    document.getElementById('print-correct').textContent = state.correct;
    document.getElementById('print-wrong').textContent = state.wrong;
    
    const tableBody = document.getElementById('print-table-body');
    tableBody.innerHTML = '';
    
    if (Object.keys(state.unitStats).length === 0) {
        tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:#555;">Henüz çözülmüş soru bulunmuyor.</td></tr>`;
    } else {
        for (let u in state.unitStats) {
            let st = state.unitStats[u];
            let total = st.d + st.y;
            let pct = total > 0 ? Math.round((st.d / total) * 100) : 0;
            let tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${u}</strong></td>
                <td style="text-align:center; color:#2e7d32; font-weight:bold;">${st.d}</td>
                <td style="text-align:center; color:#c62828; font-weight:bold;">${st.y}</td>
                <td style="text-align:center; font-weight:bold; color:${pct >= 70 ? '#2e7d32' : '#d4af37'}">%${pct}</td>
            `;
            tableBody.appendChild(tr);
        }
    }
    
    const adviceContent = document.getElementById('print-guidance-content');
    let weakUnits = [];
    let hasData = false;
    for (let u in state.unitStats) {
        let st = state.unitStats[u];
        let total = st.d + st.y;
        if (total > 0) {
            hasData = true;
            if (st.d / total < 0.70) {
                weakUnits.push({ name: u, pct: Math.round((st.d / total) * 100) });
            }
        }
    }
    
    if (!hasData) {
        adviceContent.innerHTML = "💡 Henüz analiz edilecek bir soru çözülmedi.";
    } else if (weakUnits.length === 0) {
        adviceContent.innerHTML = "🎯 Tebrikler! Tüm konularda %70'in üzerinde başarı sağladınız. LGS sınavına harika bir şekilde hazırlanıyorsunuz! 🚀";
    } else {
        let html = "<ul style='margin-left: 1.2rem; padding: 0;'>";
        weakUnits.forEach(u => {
            let rec = STUDY_RECS[u.name] || "Bu üniteyle ilgili konu özetlerini tekrar çalışmalısınız.";
            html += `<li style='margin-bottom: 0.5rem;'><strong>${u.name} (Başarı: %${u.pct}):</strong> ${rec}</li>`;
        });
        html += "</ul>";
        adviceContent.innerHTML = html;
    }
    
    const badgesSection = document.getElementById('print-badges-section');
    const badgesList = document.getElementById('print-badges-list');
    badgesList.innerHTML = '';
    
    if (!state.earnedBadges || state.earnedBadges.length === 0) {
        badgesSection.style.display = 'none';
    } else {
        badgesSection.style.display = 'block';
        state.earnedBadges.forEach(b => {
            let div = document.createElement('div');
            div.className = 'print-badge-card';
            div.innerHTML = `
                <span class="print-badge-emoji">${b.emoji}</span>
                <div class="print-badge-info">
                    <h4>${b.name}</h4>
                    <p>${b.desc}</p>
                </div>
            `;
            badgesList.appendChild(div);
        });
    }
    
    window.print();
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
            state.earnedBadges = data.earnedBadges || [];
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
            todaySolvedDate: getTodayString(),
            earnedBadges: state.earnedBadges || []
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
    const streakEl = hudStreak;
    const questEl = hudQuest;
    if (streakEl) {
        streakEl.textContent = `${state.userStreak} Gün`;
    }
    if (questEl) {
        if (state.todaySolvedCount >= 5) {
            questEl.textContent = "🎯 Görev Tamam! 🚀";
        } else {
            questEl.textContent = `🎯 Görev: ${state.todaySolvedCount}/5`;
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
