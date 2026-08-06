/* ==========================================================================
   ÇARK OYUNU — LGS Sosyal Bilgiler
   Tasarım: "Organic" sistemi (Alfa Slab One + Figtree, toprak/kağıt paleti)
   ========================================================================== */

// ————— Sabitler —————

// Çark dilimleri, saat yönünde tepeden başlayarak (SVG çizimiyle birebir aynı sıra)
const SEGMENTS = [
    { kind: 'points', value: 200 },
    { kind: 'x2' },
    { kind: 'points', value: 300 },
    { kind: 'pas' },
    { kind: 'points', value: 400 },
    { kind: 'iflas' },
    { kind: 'points', value: 500 },
    { kind: 'points', value: 100 }
];
const SEG_ANGLE = 360 / SEGMENTS.length;
const SPIN_MS = 4200;
const QUESTION_SECONDS = 45;
const TIMER_CIRC = 157.1; // 2πr, r = 25

const GRADE_META = {
    '5': { subject: 'Sosyal Bilgiler', tint: 'var(--color-accent-2-300)', ink: 'var(--color-accent-2-900)' },
    '6': { subject: 'Sosyal Bilgiler', tint: 'var(--color-accent-300)', ink: 'var(--color-accent-900)' },
    '7': { subject: 'Sosyal Bilgiler', tint: 'var(--color-neutral-300)', ink: 'var(--color-neutral-900)' },
    '8': { subject: 'İnkılap Tarihi', tint: 'var(--color-accent)', ink: 'var(--color-bg)' }
};

const BADGES = [
    { name: 'İlk Adım', hint: 'İlk soruyu çöz', emoji: '👣', need: s => s.solved >= 1 },
    { name: 'Seri Başı', hint: '3 doğru üst üste', emoji: '🔥', need: s => s.best >= 3 },
    { name: 'Puan Avcısı', hint: '1000 puan topla', emoji: '🎯', need: s => s.score >= 1000 },
    { name: 'Tarih Dehası', hint: '500’lük soruyu bil', emoji: '🏆', need: s => s.big }
];

const SPECIALS = {
    x2: {
        title: 'X2 aktif!',
        msg: 'Sıradaki sorunun puanı iki katına çıktı. Çarkı yeniden çevir.',
        glyph: '×2',
        tint: 'var(--color-accent-900)',
        dot: 'var(--color-accent-300)',
        ink: 'var(--color-accent-900)',
        titleInk: 'var(--color-accent-200)',
        bodyInk: 'var(--color-accent-300)',
        btn: 'var(--color-accent-300)',
        btnInk: 'var(--color-accent-900)'
    },
    pas: {
        title: 'Pas',
        msg: 'Bu tur boş geçti. Kaybın yok, çarkı yeniden çevir.',
        glyph: '›',
        tint: 'var(--color-surface)',
        dot: 'var(--color-neutral-300)',
        ink: 'var(--color-neutral-800)',
        titleInk: 'var(--color-text)',
        bodyInk: 'var(--color-neutral-700)',
        btn: 'var(--color-accent)',
        btnInk: 'var(--color-bg)'
    },
    iflas: {
        title: 'İflas',
        msg: 'Puanların sıfırlandı. Yeniden toplamaya başla.',
        glyph: '!',
        tint: 'var(--color-neutral-900)',
        dot: 'var(--color-accent-600)',
        ink: 'var(--color-neutral-100)',
        titleInk: 'var(--color-neutral-100)',
        bodyInk: 'var(--color-neutral-300)',
        btn: 'var(--color-accent)',
        btnInk: 'var(--color-bg)'
    }
};

const FEEDBACK = {
    ok: { title: 'Doğru!', glyph: '✓', tint: 'var(--color-accent-2-300)', ink: 'var(--color-accent-2-900)' },
    no: { title: 'Yanlış', glyph: '✕', tint: 'var(--color-accent-300)', ink: 'var(--color-accent-900)' },
    time: { title: 'Süre bitti', glyph: '⏱', tint: 'var(--color-neutral-300)', ink: 'var(--color-neutral-900)' }
};

// ————— Durum —————

const state = {
    screen: 'grade',
    grade: null,
    selectedUnit: null,
    isTeamMode: false,
    score: 0,
    correct: 0,
    wrong: 0,
    solved: 0,
    run: 0,
    streakBest: 0,
    bigWin: false,
    multiplier: 1,
    currentPoints: 0,
    currentQ: null,
    selectedOpt: null,
    remainingQuestions: [],
    unitStats: {},
    deg: 0,
    spinning: false,
    special: null,
    timer: QUESTION_SECONDS,
    timerInterval: null,
    teamScores: { A: 0, B: 0 },
    activeTeam: 'A',
    userStreak: 0,
    lastLoginDate: '',
    todaySolvedCount: 0,
    earnedBadges: []
};

// ————— Kısa yollar —————

const $ = id => document.getElementById(id);

const views = {
    grade: $('view-grade'),
    unit: $('view-unit'),
    mode: $('view-mode'),
    wheel: $('view-wheel'),
    question: $('view-question'),
    feedback: $('view-feedback'),
    karne: $('view-karne')
};

const CHROME_SCREENS = ['grade', 'unit', 'mode', 'karne'];

const sounds = {
    spin: $('snd-spin'),
    tick: $('snd-tick'),
    win: $('snd-win'),
    wrong: $('snd-wrong'),
    fail: $('snd-fail')
};

function playSound(type) {
    const el = sounds[type];
    if (!el) return;
    el.currentTime = 0;
    if (type === 'spin') el.volume = 0.3;
    if (type === 'tick') el.volume = 0.5;
    el.play().catch(() => { });
}

function triggerHaptic(type = 'light') {
    if (typeof navigator === 'undefined' || !navigator.vibrate) return;
    try {
        if (type === 'light') navigator.vibrate(15);
        else if (type === 'medium') navigator.vibrate(35);
        else if (type === 'heavy') navigator.vibrate([50, 30, 50]);
        else if (type === 'error') navigator.vibrate([100, 50, 100]);
        else if (type === 'success') navigator.vibrate([30, 40, 80]);
    } catch (e) { /* yok sayılır */ }
}

// ————— Gezinme —————

function showView(name) {
    state.screen = name;
    Object.keys(views).forEach(k => {
        if (views[k]) views[k].classList.toggle('hidden', k !== name);
    });

    const chrome = CHROME_SCREENS.includes(name);
    $('app-header').classList.toggle('hidden', !chrome);
    $('tab-bar').classList.toggle('hidden', !chrome);

    $('tab-play').classList.toggle('active', name !== 'karne');
    $('tab-karne').classList.toggle('active', name === 'karne');

    if (name === 'karne') renderKarne();
    if (name === 'wheel') renderWheelScreen();
}

// ————— Ekran 1: Sınıf seçimi —————

function renderGrades() {
    const grid = $('grade-grid');
    grid.innerHTML = '';

    ['5', '6', '7', '8'].forEach(g => {
        const meta = GRADE_META[g];
        const list = (typeof SORULAR !== 'undefined' && SORULAR[g]) ? SORULAR[g] : [];
        const unitCount = new Set(list.map(q => q.unite)).size;

        const btn = document.createElement('button');
        btn.className = 'grade-card';
        btn.innerHTML = `
            <div class="grade-card-dot" style="background:${meta.tint}">
                <span style="color:${meta.ink}">${g}</span>
            </div>
            <div class="grade-card-name">${g}. Sınıf</div>
            <div class="grade-card-subject">${meta.subject}</div>
            <div class="grade-card-meta">
                <span>${unitCount} ünite</span><span>·</span><span>${list.length} soru</span>
            </div>`;
        btn.onclick = () => pickGrade(g);
        grid.appendChild(btn);
    });
}

function pickGrade(grade) {
    state.grade = grade;
    state.selectedUnit = null;
    renderUnits();
    showView('unit');
}

// ————— Ekran 2: Ünite seçimi —————

function renderUnits() {
    const g = state.grade;
    const meta = GRADE_META[g] || {};
    $('unit-grade-label').textContent = `${g}. Sınıf`;
    $('unit-subject-label').textContent = meta.subject || '';

    const all = (typeof SORULAR !== 'undefined' && SORULAR[g]) ? SORULAR[g] : [];
    const units = [...new Set(all.map(q => q.unite))].sort();

    const container = $('unit-list-container');
    container.innerHTML = '';

    container.appendChild(buildUnitCard({
        name: 'Tüm ünitelerden karışık',
        meta: `${all.length} soru · her üniteden`,
        stats: null,
        mix: true,
        onPick: () => pickUnit('ALL')
    }));

    units.forEach(u => {
        const count = all.filter(q => q.unite === u).length;
        const st = state.unitStats[u];
        const total = st ? st.d + st.y : 0;
        container.appendChild(buildUnitCard({
            name: u,
            meta: total ? `${st.d} doğru · ${st.y} yanlış` : `${count} soru · henüz çalışılmadı`,
            stats: st,
            mix: false,
            onPick: () => pickUnit(u)
        }));
    });
}

function buildUnitCard({ name, meta, stats, mix, onPick }) {
    const total = stats ? stats.d + stats.y : 0;
    const pct = total ? Math.round((stats.d / total) * 100) : 0;
    const dash = 100.5 - (100.5 * pct) / 100;

    const btn = document.createElement('button');
    btn.className = 'unit-card' + (mix ? ' mix-card' : '');
    btn.innerHTML = `
        <div class="unit-ring">
            <svg width="38" height="38" viewBox="0 0 38 38">
                <circle cx="19" cy="19" r="16" fill="none" stroke="var(--color-neutral-300)" stroke-width="4"></circle>
                <circle cx="19" cy="19" r="16" fill="none" stroke="var(--color-accent)" stroke-width="4"
                    stroke-linecap="round" stroke-dasharray="100.5" stroke-dashoffset="${dash}"
                    transform="rotate(-90 19 19)"></circle>
            </svg>
            <span class="unit-ring-pct">${pct}%</span>
        </div>
        <div class="unit-card-body">
            <div class="unit-card-name">${name}</div>
            <div class="unit-card-meta">${meta}</div>
        </div>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--color-accent)" stroke-width="2.75"
            stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"></path></svg>`;
    btn.onclick = onPick;
    return btn;
}

function pickUnit(unit) {
    state.selectedUnit = unit;
    refillQuestionPool();
    $('mode-unit-label').textContent = unitLabel();
    showView('mode');
}

function unitLabel() {
    if (!state.selectedUnit || state.selectedUnit === 'ALL') return 'Tüm ünitelerden karışık';
    return state.selectedUnit;
}

function refillQuestionPool() {
    const all = (typeof SORULAR !== 'undefined' && SORULAR[state.grade]) ? SORULAR[state.grade] : [];
    const pool = state.selectedUnit === 'ALL' ? [...all] : all.filter(q => q.unite === state.selectedUnit);
    state.remainingQuestions = pool.sort(() => Math.random() - 0.5);
}

// ————— Ekran 3: Oyun modu —————

function beginGame(isTeam) {
    state.isTeamMode = isTeam;
    state.teamScores = { A: 0, B: 0 };
    state.activeTeam = 'A';
    state.score = 0;
    state.correct = 0;
    state.wrong = 0;
    state.solved = 0;
    state.run = 0;
    state.multiplier = 1;
    state.deg = 0;
    $('wheel-rotor').style.transition = 'none';
    $('wheel-rotor').style.transform = 'rotate(0deg)';
    void $('wheel-rotor').offsetWidth;
    $('wheel-rotor').style.transition = '';
    showView('wheel');
}

// ————— Ekran 4: Çark —————

function renderWheelScreen() {
    $('wheel-grade-label').textContent = state.grade ? `${state.grade}. Sınıf` : '';
    $('wheel-unit-label').textContent = unitLabel();
    $('wheel-score-pill').textContent = `${state.score} P`;

    const teamRow = $('team-row');
    teamRow.classList.toggle('hidden', !state.isTeamMode);
    if (state.isTeamMode) {
        $('team-a-score').textContent = state.teamScores.A;
        $('team-b-score').textContent = state.teamScores.B;
        $('team-chip-a').className = 'team-chip' + (state.activeTeam === 'A' ? ' active-a' : '');
        $('team-chip-b').className = 'team-chip' + (state.activeTeam === 'B' ? ' active-b' : '');
    }

    updateWheelCopy();
}

function updateWheelCopy() {
    const headline = state.spinning
        ? 'Çark dönüyor…'
        : (state.isTeamMode ? `${state.activeTeam} grubunun sırası` : 'Çarkı çevir');
    const sub = state.spinning
        ? 'Bakalım hangi puana denk gelecek'
        : 'Gelen puan, sıradaki sorunun değeri olur';

    $('wheel-headline').textContent = headline;
    $('wheel-sub').textContent = sub;
    $('btn-spin').textContent = state.spinning ? 'Dönüyor…' : 'Çarkı çevir';
    $('btn-spin').disabled = state.spinning;
}

function spin() {
    if (state.spinning) return;
    state.spinning = true;
    updateWheelCopy();
    playSound('spin');
    triggerHaptic('heavy');

    const idx = Math.floor(Math.random() * SEGMENTS.length);
    // Dilim ortası göstergenin (tepe) altına gelecek şekilde döndür.
    // Hedef mutlak açı üzerinden hesaplanır; aksi hâlde her çevirişte kayma birikir.
    const target = (360 - (idx * SEG_ANGLE + SEG_ANGLE / 2)) % 360;
    const current = ((state.deg % 360) + 360) % 360;
    state.deg += 360 * 5 + ((target - current + 360) % 360);
    $('wheel-rotor').style.transform = `rotate(${state.deg}deg)`;

    setTimeout(() => {
        state.spinning = false;
        updateWheelCopy();
        onSpinComplete(SEGMENTS[idx]);
    }, SPIN_MS);
}

function onSpinComplete(seg) {
    if (seg.kind === 'points') {
        state.currentPoints = seg.value * state.multiplier;
        loadQuestion();
        return;
    }

    if (seg.kind === 'iflas') {
        playSound('fail');
        if (state.isTeamMode) state.teamScores[state.activeTeam] = 0;
        else state.score = 0;
        state.multiplier = 1;
        renderWheelScreen();
    }

    openSpecial(seg.kind);
}

function openSpecial(kind) {
    state.special = kind;
    const sp = SPECIALS[kind];

    $('special-card').style.background = sp.tint;
    $('special-dot').style.background = sp.dot;
    $('special-glyph').textContent = sp.glyph;
    $('special-glyph').style.color = sp.ink;
    $('special-title').textContent = sp.title;
    $('special-title').style.color = sp.titleInk;

    let msg = sp.msg;
    if (state.isTeamMode) {
        const team = `${state.activeTeam} grubu`;
        if (kind === 'iflas') msg = `${team} iflas etti, puanı sıfırlandı. Sıra diğer gruba geçiyor.`;
        else if (kind === 'pas') msg = `${team} bu turu pas geçti. Sıra diğer gruba geçiyor.`;
        else msg = `${team} için X2 aktif! Sıradaki sorunun puanı iki katına çıktı.`;
    }
    $('special-msg').textContent = msg;
    $('special-msg').style.color = sp.bodyInk;

    $('btn-special-close').style.background = sp.btn;
    $('btn-special-close').style.color = sp.btnInk;

    $('special-overlay').classList.remove('hidden');
}

function closeSpecial() {
    const kind = state.special;
    state.special = null;
    $('special-overlay').classList.add('hidden');

    if (kind === 'x2') {
        state.multiplier = 2;
    } else {
        state.multiplier = 1;
        if (state.isTeamMode) switchTeam();
    }
    renderWheelScreen();
}

function switchTeam() {
    state.activeTeam = state.activeTeam === 'A' ? 'B' : 'A';
}

// ————— Ekran 5: Soru —————

function loadQuestion() {
    if (!state.remainingQuestions.length) refillQuestionPool();
    state.currentQ = state.remainingQuestions.pop();
    if (!state.currentQ) return;

    state.selectedOpt = null;

    const q = state.currentQ;
    $('q-unite').textContent = q.unite.split('–')[0].trim();
    $('q-konu').textContent = q.konu || '';
    $('q-points').textContent = `${state.currentPoints} puan`;

    const img = $('q-img');
    if (q.gorsel) {
        img.src = q.gorsel.startsWith('web/') ? q.gorsel.substring(4) : q.gorsel;
        img.classList.remove('hidden');
    } else {
        img.removeAttribute('src');
        img.classList.add('hidden');
    }
    $('q-card').classList.toggle('has-img', !!q.gorsel);
    $('q-text').textContent = q.soru;

    const opts = $('options-container');
    opts.innerHTML = '';
    Object.keys(q.siklar).forEach(key => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.innerHTML = `<span class="opt-letter">${key}</span><span class="opt-text">${q.siklar[key]}</span>`;
        btn.onclick = () => selectOption(btn, key);
        opts.appendChild(btn);
    });
    opts.scrollTop = 0;
    $('q-card').scrollTop = 0;

    $('btn-submit').disabled = true;
    showView('question');
    startTimer();
}

function selectOption(btn, key) {
    document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    state.selectedOpt = key;
    $('btn-submit').disabled = false;
    triggerHaptic('light');
}

function startTimer() {
    stopTimer();
    state.timer = QUESTION_SECONDS;
    updateTimerUI();
    state.timerInterval = setInterval(() => {
        state.timer--;
        updateTimerUI();
        if (state.timer > 0) playSound('tick');
        else resolve(false, true);
    }, 1000);
}

function stopTimer() {
    clearInterval(state.timerInterval);
    state.timerInterval = null;
}

function updateTimerUI() {
    const ring = $('timer-progress');
    ring.style.strokeDashoffset = TIMER_CIRC - (TIMER_CIRC * state.timer) / QUESTION_SECONDS;
    ring.setAttribute('stroke', state.timer <= 10 ? 'var(--color-accent-600)' : 'var(--color-accent-2-500)');
    $('timer-text').textContent = state.timer;
}

function submitAnswer() {
    if (!state.selectedOpt || !state.currentQ) return;
    resolve(state.selectedOpt === state.currentQ.dogru_cevap, false);
}

function skipQuestion() {
    stopTimer();
    state.multiplier = 1;
    if (state.isTeamMode) switchTeam();
    showView('wheel');
}

// ————— Sonuç ve geri bildirim —————

function resolve(isCorrect, timedOut) {
    stopTimer();

    const q = state.currentQ;
    const unit = (q && q.unite) || state.selectedUnit || '—';
    if (!state.unitStats[unit]) state.unitStats[unit] = { d: 0, y: 0 };
    if (isCorrect) state.unitStats[unit].d++;
    else state.unitStats[unit].y++;

    state.solved++;
    state.run = isCorrect ? state.run + 1 : 0;
    state.streakBest = Math.max(state.streakBest, state.run);

    if (isCorrect) {
        state.correct++;
        state.score += state.currentPoints;
        if (state.isTeamMode) state.teamScores[state.activeTeam] += state.currentPoints;
        if (state.currentPoints >= 500) state.bigWin = true;
        playSound('win');
        triggerHaptic('success');
        triggerConfetti();
    } else {
        state.wrong++;
        playSound(timedOut ? 'fail' : 'wrong');
        triggerHaptic('error');
    }

    state.multiplier = 1;
    if (state.isTeamMode) switchTeam();

    onQuestionSolved();
    checkBadges();
    showFeedback(isCorrect ? 'ok' : (timedOut ? 'time' : 'no'));
}

function showFeedback(kind) {
    const fb = FEEDBACK[kind];
    const q = state.currentQ;

    const glyph = $('fb-glyph');
    glyph.textContent = fb.glyph;
    glyph.style.background = fb.tint;
    glyph.style.color = fb.ink;

    $('fb-title').textContent = fb.title;

    let msg;
    if (kind === 'ok') msg = `+${state.currentPoints} puan kazandın.`;
    else if (kind === 'time') msg = 'Bu soruda süre yetmedi.';
    else msg = 'Açıklamayı oku, bir dahakine bileceksin.';
    if (state.isTeamMode) msg += ` Sıra ${state.activeTeam} grubunda.`;
    $('fb-msg').textContent = msg;

    $('fb-correct-key').textContent = q ? q.dogru_cevap : '';
    $('fb-explain-text').textContent = q ? (q.aciklama || q.siklar[q.dogru_cevap]) : '';

    $('fb-correct').textContent = state.correct;
    $('fb-wrong').textContent = state.wrong;
    $('fb-score').textContent = state.score;

    showView('feedback');
}

// ————— Ekran 7: Karne —————

function renderKarne() {
    $('st-score').textContent = state.score;
    $('st-correct').textContent = state.correct;
    $('st-wrong').textContent = state.wrong;

    const container = $('unit-stats-container');
    container.innerHTML = '';

    const names = Object.keys(state.unitStats);
    if (!names.length) {
        container.innerHTML = `
            <div>
                <div class="unit-bar-head"><span class="unit-bar-name">Henüz veri yok</span><span class="unit-bar-ratio">0/0</span></div>
                <div class="unit-bar-track"><div class="unit-bar-fill" style="width:0%"></div></div>
            </div>`;
    } else {
        names.forEach(name => {
            const st = state.unitStats[name];
            const total = st.d + st.y;
            const pct = total ? Math.round((st.d / total) * 100) : 0;
            const row = document.createElement('div');
            row.innerHTML = `
                <div class="unit-bar-head">
                    <span class="unit-bar-name">${name}</span>
                    <span class="unit-bar-ratio">${st.d}/${total}</span>
                </div>
                <div class="unit-bar-track"><div class="unit-bar-fill" style="width:${pct}%"></div></div>`;
            container.appendChild(row);
        });
    }

    renderBadgeGrid();
    generateAIRecommendations();
}

function badgeState() {
    return { solved: state.solved, best: state.streakBest, score: state.score, big: state.bigWin };
}

function renderBadgeGrid() {
    const grid = $('badge-grid');
    grid.innerHTML = '';
    const s = badgeState();

    BADGES.forEach(b => {
        const on = b.need(s);
        const div = document.createElement('div');
        div.className = 'badge-item' + (on ? ' on' : '');
        div.innerHTML = `
            <div class="badge-dot">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none"
                    stroke="${on ? '#f0fae1' : 'var(--color-neutral-200)'}" stroke-width="2.75"
                    stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="12" cy="9" r="5.5"></circle>
                    <path d="M8.5 14L7 21l5-2.5L17 21l-1.5-7"></path>
                </svg>
            </div>
            <div style="min-width:0">
                <div class="badge-name">${b.name}</div>
                <div class="badge-hint">${b.hint}</div>
            </div>`;
        grid.appendChild(div);
    });
}

function checkBadges() {
    const s = badgeState();
    BADGES.forEach(b => {
        if (!b.need(s)) return;
        if (state.earnedBadges.some(e => e.name === b.name)) return;
        state.earnedBadges.push({ name: b.name, desc: b.hint, emoji: b.emoji });
        saveUserData();
        showBadgePopup(b.name, b.hint, b.emoji);
    });
}

let badgeTimeout = null;
function showBadgePopup(name, desc, emoji) {
    $('badge-emoji').textContent = emoji;
    $('badge-name').textContent = name;
    $('badge-desc').textContent = desc;
    $('badge-popup-container').classList.remove('hidden');

    if (badgeTimeout) clearTimeout(badgeTimeout);
    badgeTimeout = setTimeout(() => $('badge-popup-container').classList.add('hidden'), 4500);
}

function resetStats() {
    state.score = 0;
    state.correct = 0;
    state.wrong = 0;
    state.solved = 0;
    state.run = 0;
    state.streakBest = 0;
    state.bigWin = false;
    state.unitStats = {};
    state.teamScores = { A: 0, B: 0 };
    state.multiplier = 1;
    renderKarne();
    updateChrome();
}

// ————— Rehberlik tavsiyeleri —————

// Anahtarlar data.js'teki ünite adlarıyla birebir aynı olmalı.
const STUDY_RECS = {
    // 5. ve 6. Sınıf (ortak ünite adları)
    'Ünite 1 – Birlikte Yaşamak': 'Sosyal roller, hak ve sorumluluklarımız, çocuk hakları ile toplumsal dayanışma konularına tekrar çalışmalısın.',
    'Ünite 2 – Evimiz Dünya': "Dünya'nın konumu, kıtalar ve okyanuslar, Türkiye'nin yeryüzü şekilleri, iklim ve bitki örtüsü konularını gözden geçirmelisin.",
    'Ünite 3 – Ortak Mirasımız': "Anadolu ve Mezopotamya uygarlıkları, ilk Türk devletleri ile somut/somut olmayan kültürel miras varlıklarını tekrar etmelisin.",
    'Ünite 4 – Yaşayan Demokrasimiz': 'Demokrasinin temel ilkeleri, devletin yönetim organları ve katılım hakkının önemi konularını çalışmalısın.',
    'Ünite 5 – Hayatımızda Ekonomi': 'Ekonomik faaliyetler, meslek grupları, bütçe hazırlama ve bilinçli tüketicilik konularına bakmalısın.',
    'Ünite 5 – Hayatımızdaki Ekonomi': 'Üretim kaynaklarımız, yatırım ve girişimcilik fikirleri ile vergilerin önemi konularını çalışmalısın.',
    'Ünite 6 – Teknoloji ve Sosyal Bilimler': 'Teknolojinin sosyal hayata etkileri, sosyal bilimlerin dalları, telif/patent hakları ve bilim etiği konularını tekrar etmelisin.',

    // 7. Sınıf
    'Ünite 1 – Birey ve Toplum': 'Olumlu ve etkili iletişim becerileri, medya okuryazarlığı, RTÜK ve iletişim özgürlüğü konularını tekrar etmelisin.',
    'Ünite 2 – Kültür ve Miras': "Osmanlı'nın kuruluş süreci, iskân ve istimâlet politikaları, denizlerdeki fetihler ve Avrupa'daki uyanışın etkilerini incelemelisin.",
    'Ünite 3 – İnsanlar, Yerler ve Çevreler': "Nüfusun dağılışını etkileyen faktörler, Türkiye'deki göç dalgaları ve göçün nedenleri/sonuçlarını gözden geçirmelisin.",
    'Ünite 4 – Bilim, Teknoloji ve Toplum': 'Tarih boyunca bilginin korunması/yayılması ve ünlü Türk-İslam bilginleri konularını çalışmalısın.',
    'Ünite 5 – Üretim, Dağıtım ve Tüketim': 'Toprağın üretimdeki yeri, Ahilik/Lonca teşkilatı, mesleki yönlendirme ve dijital çağın meslekleri konularını incelemelisin.',
    'Ünite 6 – Etkin Vatandaşlık': 'Demokratik yönetimlerin tarihî gelişimi, anayasanın temel nitelikleri ve sivil toplum örgütlerine odaklanmalısın.',
    'Ünite 7 – Küresel Bağlantılar': 'Ülkemizin üye olduğu uluslararası kuruluşlar ve küresel çevre/iklim sorunlarına karşı alınabilecek tedbirleri tekrar etmelisin.',

    // 8. Sınıf
    'Ünite 1 – Bir Kahraman Doğuyor': "Mustafa Kemal'in çocukluğu, okuduğu okullar, Selanik'in sosyal yapısı ve askerlik hayatı konularını tekrar etmelisin.",
    'Ünite 2 – Millî Uyanış: Bağımsızlık Yolunda Atılan Adımlar': "I. Dünya Savaşı'nın nedenleri ve cepheleri, Mondros, Havza ve Amasya Genelgeleri, kongreler ile Misak-ı Millî kararlarına çalışmalısın.",
    'Ünite 3 – Millî Bir Destan: Ya İstiklal Ya Ölüm!': 'Doğu ve Güney cepheleri, düzenli ordu savaşları (İnönü, Sakarya, Büyük Taarruz) ve Lozan Antlaşması konularını çalışmalısın.',
    'Ünite 4 – Atatürk ve Çağdaşlaşan Türkiye': 'Siyasi, eğitim ve kültür inkılapları ile Atatürk ilkelerine odaklanmalısın.',
    'Ünite 5 – Demokratikleşme Çabaları': 'Çok partili hayata geçiş denemeleri ve laik cumhuriyete karşı çıkan isyanları çalışmalısın.',
    'Ünite 6 – Atatürk Dönemi Türk Dış Politikası': "Dış politikanın temel ilkeleri, Lozan'dan kalan sorunlar (Musul, Boğazlar, Hatay) ve barış paktlarını tekrar etmelisin."
};

function weakUnits() {
    const weak = [];
    Object.keys(state.unitStats).forEach(u => {
        const st = state.unitStats[u];
        const total = st.d + st.y;
        if (total > 0 && st.d / total < 0.7) weak.push({ name: u, pct: Math.round((st.d / total) * 100) });
    });
    return weak;
}

function adviceHTML() {
    if (!Object.keys(state.unitStats).length) {
        return 'Henüz analiz edilecek bir soru çözmedin. Soruları çözdükçe sana özel tavsiyeler burada görünecek.';
    }
    const weak = weakUnits();
    if (!weak.length) {
        return 'Çalıştığın tüm ünitelerde %70’in üzerinde başarı oranın var. LGS hazırlığın harika gidiyor, aynen devam!';
    }
    let html = 'Başarı analizine göre şu ünitelerde eksiklerin var:<ul>';
    weak.forEach(u => {
        const rec = STUDY_RECS[u.name] || `${u.name} ünitesiyle ilgili konu özetlerini tekrar gözden geçirmelisin.`;
        html += `<li><strong>${u.name} (%${u.pct}):</strong> ${rec}</li>`;
    });
    return html + '</ul>';
}

function generateAIRecommendations() {
    $('ai-guidance-content').innerHTML = adviceHTML();
}

// ————— PDF karne —————

function printReportCard() {
    const gradeInfoMap = {
        '5': '5. Sınıf Sosyal Bilgiler',
        '6': '6. Sınıf Sosyal Bilgiler',
        '7': '7. Sınıf Sosyal Bilgiler',
        '8': '8. Sınıf T.C. İnkılap Tarihi ve Atatürkçülük'
    };

    $('print-date').textContent = `Tarih: ${new Date().toLocaleDateString('tr-TR')}`;
    $('print-grade').textContent = gradeInfoMap[state.grade] || (state.grade ? `${state.grade}. Sınıf` : '-');
    $('print-unit').textContent = unitLabel();
    $('print-score').textContent = state.score;
    $('print-solved').textContent = state.solved;
    $('print-correct').textContent = state.correct;
    $('print-wrong').textContent = state.wrong;

    const tbody = $('print-table-body');
    tbody.innerHTML = '';
    const names = Object.keys(state.unitStats);
    if (!names.length) {
        tbody.innerHTML = '<tr><td colspan="4" style="text-align:center; color:#555;">Henüz çözülmüş soru bulunmuyor.</td></tr>';
    } else {
        names.forEach(u => {
            const st = state.unitStats[u];
            const total = st.d + st.y;
            const pct = total ? Math.round((st.d / total) * 100) : 0;
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><strong>${u}</strong></td>
                <td style="text-align:center; color:#2e7d32; font-weight:bold;">${st.d}</td>
                <td style="text-align:center; color:#c62828; font-weight:bold;">${st.y}</td>
                <td style="text-align:center; font-weight:bold; color:${pct >= 70 ? '#2e7d32' : '#b2622d'}">%${pct}</td>`;
            tbody.appendChild(tr);
        });
    }

    $('print-guidance-content').innerHTML = adviceHTML();

    const section = $('print-badges-section');
    const list = $('print-badges-list');
    list.innerHTML = '';
    if (!state.earnedBadges.length) {
        section.style.display = 'none';
    } else {
        section.style.display = 'block';
        state.earnedBadges.forEach(b => {
            const div = document.createElement('div');
            div.className = 'print-badge-card';
            div.innerHTML = `
                <span class="print-badge-emoji">${b.emoji}</span>
                <div class="print-badge-info"><h4>${b.name}</h4><p>${b.desc}</p></div>`;
            list.appendChild(div);
        });
    }

    window.print();
}

// ————— Kalıcı veri —————

function loadUserData() {
    const raw = localStorage.getItem('lgs_cark_userdata');
    if (!raw) return;
    try {
        const data = JSON.parse(raw);
        state.userStreak = data.userStreak || 0;
        state.lastLoginDate = data.lastLoginDate || '';
        state.todaySolvedCount = data.todaySolvedDate === getTodayString() ? (data.todaySolvedCount || 0) : 0;
        state.earnedBadges = data.earnedBadges || [];
    } catch (e) {
        console.error('Kullanıcı verileri yüklenirken hata:', e);
    }
}

function saveUserData() {
    try {
        localStorage.setItem('lgs_cark_userdata', JSON.stringify({
            userStreak: state.userStreak,
            lastLoginDate: state.lastLoginDate,
            todaySolvedCount: state.todaySolvedCount,
            todaySolvedDate: getTodayString(),
            earnedBadges: state.earnedBadges
        }));
    } catch (e) {
        console.error('Kullanıcı verileri kaydedilirken hata:', e);
    }
}

function dateString(offsetDays = 0) {
    const d = new Date();
    d.setDate(d.getDate() + offsetDays);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

function getTodayString() { return dateString(0); }

function checkDailyStreak() {
    const today = dateString(0);
    const yesterday = dateString(-1);

    if (!state.lastLoginDate) {
        state.userStreak = 1;
        state.lastLoginDate = today;
    } else if (state.lastLoginDate === yesterday) {
        state.userStreak += 1;
        state.lastLoginDate = today;
    } else if (state.lastLoginDate !== today) {
        state.userStreak = 1;
        state.lastLoginDate = today;
    }
    saveUserData();
}

function onQuestionSolved() {
    state.todaySolvedCount += 1;
    saveUserData();
    updateChrome();
}

function updateChrome() {
    $('streak-label').textContent = `${state.streakBest} seri`;
    $('quest-label').textContent = state.todaySolvedCount >= 5 ? '5/5' : `${state.todaySolvedCount}/5`;
}

// ————— Konfeti —————

function triggerConfetti() {
    const canvas = $('confettiCanvas');
    if (!canvas) return;
    const c = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const colors = ['#c67139', '#7a8a5e', '#f6a06b', '#402310', '#ccdbb2', '#ffe1d0'];
    const particles = [];
    for (let i = 0; i < 75; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height * 0.4,
            r: Math.random() * 6 + 4,
            d: Math.random() * 25 + 10,
            color: colors[Math.floor(Math.random() * colors.length)],
            tilt: Math.floor(Math.random() * 10) - 10,
            tiltAngleIncremental: Math.random() * 0.07 + 0.05,
            tiltAngle: 0
        });
    }

    let frame;
    let opacity = 1;
    const startTime = Date.now();

    function draw() {
        c.clearRect(0, 0, canvas.width, canvas.height);
        if (Date.now() - startTime > 2200) opacity -= 0.05;
        if (opacity <= 0) {
            c.clearRect(0, 0, canvas.width, canvas.height);
            cancelAnimationFrame(frame);
            return;
        }

        c.globalAlpha = opacity;
        particles.forEach(p => {
            p.tiltAngle += p.tiltAngleIncremental;
            p.y += (Math.cos(p.d) + 3 + p.r / 2) / 2;
            p.x += Math.sin(p.d);
            p.tilt = Math.sin(p.tiltAngle) * 15;

            c.beginPath();
            c.lineWidth = p.r;
            c.strokeStyle = p.color;
            c.moveTo(p.x + p.tilt + p.r / 2, p.y);
            c.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
            c.stroke();
        });

        frame = requestAnimationFrame(draw);
    }
    draw();
}

// ————— Olay bağlantıları —————

function setupEventListeners() {
    $('btn-unit-back').onclick = () => showView('grade');
    $('btn-mode-back').onclick = () => showView('unit');

    $('btn-mode-single').onclick = () => beginGame(false);
    $('btn-mode-team').onclick = () => beginGame(true);

    $('btn-spin').onclick = spin;
    $('wheel-wrap').onclick = spin;

    $('btn-submit').onclick = submitAnswer;
    $('btn-skip').onclick = skipQuestion;
    $('btn-next').onclick = () => showView('wheel');

    $('btn-quit-game').onclick = () => {
        stopTimer();
        showView('grade');
    };

    $('btn-special-close').onclick = closeSpecial;
    $('btn-close-badge').onclick = () => {
        $('badge-popup-container').classList.add('hidden');
        if (badgeTimeout) clearTimeout(badgeTimeout);
    };

    $('tab-play').onclick = () => showView(state.grade && state.selectedUnit ? 'wheel' : 'grade');
    $('tab-karne').onclick = () => showView('karne');

    $('btn-print-report').onclick = printReportCard;
    $('btn-reset').onclick = () => {
        if (confirm('Tüm istatistikleri sıfırlamak istediğine emin misin?')) resetStats();
    };

    $('btn-share').onclick = () => {
        const text = `Çark Oyunu’nda tarih yazdım!\n\nGünlük seri: ${state.userStreak} gün\nToplam puan: ${state.score}\nDoğru: ${state.correct} · Yanlış: ${state.wrong}\n\nHadi sen de gel, çarkı çevir!`;
        navigator.clipboard.writeText(text).then(() => {
            const btn = $('btn-share');
            const old = btn.textContent;
            btn.textContent = 'Kopyalandı!';
            setTimeout(() => { btn.textContent = old; }, 2000);
        }).catch(err => console.error('Panoya kopyalama başarısız:', err));
    };
}

// ————— Başlangıç —————

function init() {
    loadUserData();
    checkDailyStreak();
    renderGrades();
    setupEventListeners();
    updateChrome();
    showView('grade');
}

init();
