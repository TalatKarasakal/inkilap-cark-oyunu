data-dc-script="" data-props="{&quot;timerSeconds&quot;:{&quot;editor&quot;:&quot;int&quot;,&quot;default&quot;:45,&quot;tsType&quot;:&quot;number&quot;,&quot;min&quot;:15,&quot;max&quot;:90,&quot;unit&quot;:&quot;sn&quot;,&quot;section&quot;:&quot;Oyun&quot;},&quot;showStreak&quot;:{&quot;editor&quot;:&quot;boolean&quot;,&quot;default&quot;:true,&quot;tsType&quot;:&quot;boolean&quot;,&quot;section&quot;:&quot;Oyun&quot;}}">
const SEGMENTS = [
  { kind: 'points', value: 200 },
  { kind: 'x2' },
  { kind: 'points', value: 300 },
  { kind: 'pas' },
  { kind: 'points', value: 400 },
  { kind: 'iflas' },
  { kind: 'points', value: 500 },
  { kind: 'points', value: 100 },
];

const GRADES = [
  { no: 5, subject: 'Sosyal Bilgiler', units: 6, count: 202, tint: 'var(--color-accent-2-300)', ink: 'var(--color-accent-2-900)' },
  { no: 6, subject: 'Sosyal Bilgiler', units: 6, count: 200, tint: 'var(--color-accent-300)', ink: 'var(--color-accent-900)' },
  { no: 7, subject: 'Sosyal Bilgiler', units: 7, count: 200, tint: 'var(--color-neutral-300)', ink: 'var(--color-neutral-900)' },
  { no: 8, subject: 'İnkılap Tarihi', units: 6, count: 200, tint: 'var(--color-accent)', ink: 'var(--color-bg)' },
];

const UNITS = {
  5: ['Ünite 1 – Birlikte Yaşamak', 'Ünite 2 – Evimiz Dünya', 'Ünite 3 – Ortak Mirasımız', 'Ünite 4 – Yaşayan Demokrasimiz', 'Ünite 5 – Hayatımızdaki Ekonomi', 'Ünite 6 – Teknoloji ve Sosyal Bilimler'],
  6: ['Ünite 1 – Birlikte Yaşamak', 'Ünite 2 – Yeryüzünde Yaşam', 'Ünite 3 – İpek Yolunda Türkler', 'Ünite 4 – Bilim, Teknoloji ve Toplum', 'Ünite 5 – Üretim, Dağıtım ve Tüketim', 'Ünite 6 – Etkin Vatandaşlık'],
  7: ['Ünite 1 – Birey ve Toplum', 'Ünite 2 – Kültür ve Miras', 'Ünite 3 – İnsanlar, Yerler ve Çevreler', 'Ünite 4 – Bilim, Teknoloji ve Toplum', 'Ünite 5 – Ekonomi ve Sosyal Hayat', 'Ünite 6 – Yaşayan Demokrasi', 'Ünite 7 – Küresel Bağlantılar'],
  8: ['Ünite 1 – Bir Kahraman Doğuyor', 'Ünite 2 – Millî Bir Destan: Ya İstiklal Ya Ölüm', 'Ünite 3 – Atatürkçülük ve Çağdaşlaşan Türkiye', 'Ünite 4 – Demokratikleşme Çabaları', 'Ünite 5 – Atatürk Dönemi Dış Politika', 'Ünite 6 – Atatürk’ün Ölümü'],
};

const BANK = {
  8: [
    { unite: 'Ünite 1 – Bir Kahraman Doğuyor', konu: 'Atatürk’ün Öğrenim Hayatı', soru: 'Mustafa Kemal;\nI. Şemsi Efendi İlkokulu\nII. Selanik Askeri Rüştiyesi\nIII. Manastır Askeri İdadisi\nIV. Harp Okulu\n\nBu eğitim süreci Mustafa Kemal hakkında hangisini gösterir?', siklar: { A: 'Sadece askeri eğitim aldığını', B: 'Yalnızca İstanbul’da okuduğunu', C: 'Disiplinli, planlı ve askeri-siyasi alanda yetişen bir lider olduğunu', D: 'Eğitimini yarıda bıraktığını' }, dogru: 'C', aciklama: 'Askeri okullar silsilesinde yetişmesi disiplinli ve donanımlı bir lider olduğunu gösterir.' },
    { unite: 'Ünite 1 – Bir Kahraman Doğuyor', konu: 'Selanik’in Etkisi', soru: 'Mustafa Kemal’in Selanik’te doğup büyümesi;\nI. Farklı kültür ve milletlerle iç içe yaşamış\nII. Batı dünyasını yakından tanımış\nIII. Milliyetçilik akımından etkilenmiş\n\nSelanik’in Mustafa Kemal’e etkisi hangileridir?', siklar: { A: 'I, II ve III', B: 'I ve II', C: 'Yalnız I', D: 'I ve III' }, dogru: 'A', aciklama: 'Selanik çok kültürlü, Batı’ya açık ve milliyetçilik akımlarının yoğun olduğu bir şehirdi.' },
    { unite: 'Ünite 1 – Bir Kahraman Doğuyor', konu: 'Osmanlı’nın Son Dönemi', soru: 'Osmanlı’nın son döneminde;\nI. Osmanlıcılık\nII. İslamcılık\nIII. Türkçülük\nIV. Batıcılık\nfikir akımları uygulanmıştır.\n\nBu fikir akımlarının amacı hangisidir?', siklar: { A: 'Yeni devlet kurmak', B: 'Osmanlı İmparatorluğu’nu çöküşten kurtarmak', C: 'Avrupa’yı taklit etmek', D: 'Farklı siyasi partiler kurmak' }, dogru: 'B', aciklama: 'Tüm fikir akımlarının ortak amacı Osmanlı’yı çöküşten kurtarmaktı.' },
    { unite: 'Ünite 1 – Bir Kahraman Doğuyor', konu: '31 Mart Olayı', soru: '31 Mart Olayı (1909) sonucu;\nI. Hareket Ordusu İstanbul’a gelmiş\nII. II. Abdülhamid tahttan indirilmiş\nIII. Meşrutiyet korunmuş\n\nBu olay hangisini gösterir?', siklar: { A: 'Ordunun siyasete karıştığını', B: 'Padişahın güçlendiğini', C: 'İsyanın başarılı olduğunu', D: 'Meşrutiyet yönetiminin korunması için mücadele edildiğini' }, dogru: 'D', aciklama: '31 Mart Olayı meşrutiyet yönetiminin korunması için bastırılmıştır.' },
  ],
  5: [
    { unite: 'Ünite 1 – Birlikte Yaşamak', konu: 'Gruplar ve Roller', soru: 'Ali, okulda sınıf başkanıdır ve arkadaşlarının sorunlarını öğretmenine iletir. Evde ise ailesine yardım eder ve ablasıyla birlikte ev işlerini paylaşır.\n\nBuna göre Ali’nin farklı gruplarda farklı roller üstlenmesi aşağıdakilerden hangisiyle açıklanabilir?', siklar: { A: 'Roller sadece okul ortamında geçerlidir', B: 'Bireyler bulundukları gruba göre farklı roller üstlenebilir', C: 'Aile içinde herkesin görevi aynıdır', D: 'İnsanlar her ortamda aynı davranışı sergiler' }, dogru: 'B', aciklama: 'Her birey bulunduğu gruba göre farklı roller üstlenir.' },
  ],
  6: [
    { unite: 'Ünite 1 – Birlikte Yaşamak', konu: 'Gruplar ve Roller', soru: 'Bir öğrenci okulda öğrenci, evde çocuk, spor kulübünde takım kaptanıdır.\n\nBu durum hangisini gösterir?', siklar: { A: 'Sadece okuldaki rollerin önemli olduğunu', B: 'Bireylerin bulundukları gruba göre farklı roller üstlendiğini', C: 'Bireylerin her ortamda aynı davrandığını', D: 'Rollerin değiştirilemez olduğunu' }, dogru: 'B', aciklama: 'Bireyler aile, okul, spor kulübü gibi farklı gruplarda farklı roller üstlenir.' },
  ],
  7: [
    { unite: 'Ünite 1 – Birey ve Toplum', konu: 'Olumlu İletişim', soru: 'Karşısındakini dinleyip anladığını belirten ve “benim düşüncem” diyen bir kişi olumlu iletişim kurmaktadır.\n\nBu kişinin kullandığı iletişim unsurları hangileridir?', siklar: { A: 'Görmezden gelme', B: 'Empati ve ben dili', C: 'Otoriter tavır', D: 'Eleştiri ve suçlama' }, dogru: 'B', aciklama: 'Dinleyip anlamak empatiyi, “benim düşüncem” demek ben dilini gösterir.' },
  ],
};

const BADGES = [
  { name: 'İlk Adım', hint: 'İlk soruyu çöz', need: s => s.solved >= 1 },
  { name: 'Seri Başı', hint: '3 doğru üst üste', need: s => s.best >= 3 },
  { name: 'Puan Avcısı', hint: '1000 puan topla', need: s => s.score >= 1000 },
  { name: 'Tarih Dehası', hint: '500’lük soruyu bil', need: s => s.big },
];

class Component extends DCLogic {
  state = {
    screen: 'home', grade: null, unit: null, mode: 'single',
    score: 0, correct: 0, wrong: 0, solved: 0, streakBest: 0, run: 0,
    bigWin: false, multiplier: 1, points: 0, deg: 0, spinning: false,
    special: null, question: null, picked: null, revealed: false,
    timeLeft: 45, fb: null, teamA: 0, teamB: 0, turn: 'A',
    unitScores: {}, tab: 'play',
  };

  componentWillUnmount() { clearInterval(this._t); }

  get secs() { return this.props.timerSeconds ?? 45; }

  startTimer() {
    clearInterval(this._t);
    this.setState({ timeLeft: this.secs });
    this._t = setInterval(() => {
      const t = this.state.timeLeft - 1;
      if (t <= 0) { clearInterval(this._t); this.setState({ timeLeft: 0 }); this.resolve(false, true); }
      else this.setState({ timeLeft: t });
    }, 1000);
  }

  pickGrade(no) { this.setState({ grade: no, screen: 'units' }); }
  pickUnit(name) { this.setState({ unit: name, screen: 'mode' }); }

  begin(mode) { this.setState({ mode, screen: 'wheel', deg: 0, multiplier: 1 }); }

  spin() {
    if (this.state.spinning) return;
    const idx = Math.floor(Math.random() * SEGMENTS.length);
    const target = 360 * 5 + (360 - (idx * 45 + 22.5));
    const deg = this.state.deg + target;
    this.setState({ spinning: true, deg });
    setTimeout(() => {
      const seg = SEGMENTS[idx];
      this.setState({ spinning: false });
      if (seg.kind === 'points') {
        this.setState({ points: seg.value * this.state.multiplier });
        this.openQuestion();
      } else {
        this.setState({ special: seg.kind });
      }
    }, 4200);
  }

  openQuestion() {
    const g = this.state.grade || 8;
    const pool = BANK[g] || BANK[8];
    const q = pool[this.state.solved % pool.length];
    this.setState({ question: q, picked: null, revealed: false, screen: 'question' });
    this.startTimer();
  }

  closeSpecial() {
    const k = this.state.special;
    if (k === 'x2') this.setState({ special: null, multiplier: 2 });
    else if (k === 'iflas') this.setState({ special: null, score: 0, multiplier: 1 });
    else this.setState({ special: null, multiplier: 1 });
  }

  resolve(ok, timeout) {
    clearInterval(this._t);
    const s = this.state;
    const unit = s.unit || (s.question && s.question.unite) || '—';
    const us = Object.assign({}, s.unitScores);
    const cur = us[unit] || { c: 0, w: 0 };
    us[unit] = ok ? { c: cur.c + 1, w: cur.w } : { c: cur.c, w: cur.w + 1 };
    const run = ok ? s.run + 1 : 0;
    this.setState({
      score: ok ? s.score + s.points : s.score,
      correct: ok ? s.correct + 1 : s.correct,
      wrong: ok ? s.wrong : s.wrong + 1,
      solved: s.solved + 1,
      run, streakBest: Math.max(s.streakBest, run),
      bigWin: s.bigWin || (ok && s.points >= 500),
      unitScores: us, multiplier: 1,
      teamA: s.mode === 'team' && s.turn === 'A' && ok ? s.teamA + s.points : s.teamA,
      teamB: s.mode === 'team' && s.turn === 'B' && ok ? s.teamB + s.points : s.teamB,
      turn: s.mode === 'team' ? (s.turn === 'A' ? 'B' : 'A') : s.turn,
      screen: 'feedback',
      fb: ok ? 'ok' : (timeout ? 'time' : 'no'),
    });
  }

  submit() { if (this.state.picked) this.resolve(this.state.picked === this.state.question.dogru, false); }

  renderVals() {
    const s = this.state;
    const q = s.question;
    const showStreak = this.props.showStreak ?? true;
    const chrome = s.screen === 'home' || s.screen === 'units' || s.screen === 'mode' || s.screen === 'karne';

    const tabs = [
      { key: 'play', label: 'Oyna', path: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Zm0 6a3 3 0 1 0 0 6 3 3 0 0 0 0-6Z' },
      { key: 'karne', label: 'Karne', path: 'M5 20V10M12 20V4M19 20v-7' },
    ].map(t => {
      const active = (t.key === 'karne') === (s.screen === 'karne');
      return {
        key: t.key, label: t.label, path: t.path,
        ink: active ? 'var(--color-accent-700)' : 'var(--color-neutral-600)',
        tint: active ? 'var(--color-accent-200)' : 'transparent',
        go: () => this.setState({ screen: t.key === 'karne' ? 'karne' : 'home' }),
      };
    });

    const units = (UNITS[s.grade] || []).map((name, i) => {
      const st = s.unitScores[name] || { c: 0, w: 0 };
      const total = st.c + st.w;
      const pct = total ? Math.round((st.c / total) * 100) : 0;
      return {
        name, pick: () => this.pickUnit(name), pct: pct + '%',
        dash: 100.5 - (100.5 * pct) / 100,
        meta: total ? st.c + ' doğru · ' + st.w + ' yanlış' : 'Henüz çalışılmadı',
      };
    });

    const options = q ? Object.keys(q.siklar).map(k => {
      const picked = s.picked === k;
      let bg = 'var(--color-surface)', border = 'var(--color-divider)', keyBg = 'var(--color-neutral-300)', keyInk = 'var(--color-neutral-800)';
      if (picked) { bg = 'var(--color-accent-200)'; border = 'var(--color-accent)'; keyBg = 'var(--color-accent)'; keyInk = 'var(--color-bg)'; }
      return {
        key: k, text: q.siklar[k], pick: () => this.setState({ picked: k }),
        style: {
          appearance: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 11,
          background: bg, border: '1px solid ' + border, borderRadius: 20, padding: '12px 14px',
          fontFamily: 'var(--font-body)', fontSize: 13.5, lineHeight: 1.4, color: 'var(--color-text)',
          textAlign: 'left', width: '100%',
        },
        keyStyle: {
          width: 26, height: 26, borderRadius: '50%', flex: 'none', display: 'flex',
          alignItems: 'center', justifyContent: 'center', background: keyBg, color: keyInk,
          fontFamily: 'var(--font-heading)', fontSize: 13,
        },
      };
    }) : [];

    const unitStats = Object.keys(s.unitScores).map(name => {
      const st = s.unitScores[name];
      const total = st.c + st.w;
      const pct = total ? Math.round((st.c / total) * 100) : 0;
      return { name, ratio: st.c + '/' + total, width: pct + '%' };
    });
    if (!unitStats.length) unitStats.push({ name: 'Henüz veri yok', ratio: '0/0', width: '0%' });

    const badgeState = { solved: s.solved, best: s.streakBest, score: s.score, big: s.bigWin };
    const badges = BADGES.map(b => {
      const on = b.need(badgeState);
      return {
        name: b.name, hint: b.hint,
        tint: on ? 'var(--color-accent-2-200)' : 'var(--color-neutral-200)',
        dot: on ? 'var(--color-accent-2-500)' : 'var(--color-neutral-400)',
        ink: on ? '#f0fae1' : 'var(--color-neutral-200)',
        op: on ? 1 : 0.55,
      };
    });

    const sp = {
      x2: { title: 'X2 aktif!', msg: 'Sıradaki sorunun puanı iki katına çıktı. Çarkı yeniden çevir.', glyph: '×2', tint: 'var(--color-accent-900)', dot: 'var(--color-accent-300)', ink: 'var(--color-accent-900)', titleInk: 'var(--color-accent-200)', bodyInk: 'var(--color-accent-300)', btn: 'var(--color-accent-300)', btnInk: 'var(--color-accent-900)' },
      pas: { title: 'Pas', msg: 'Bu tur boş geçti. Kaybın yok, çarkı yeniden çevir.', glyph: '›', tint: 'var(--color-surface)', dot: 'var(--color-neutral-300)', ink: 'var(--color-neutral-800)', titleInk: 'var(--color-text)', bodyInk: 'var(--color-neutral-700)', btn: 'var(--color-accent)', btnInk: 'var(--color-bg)' },
      iflas: { title: 'İflas', msg: 'Puanların sıfırlandı. Yeniden toplamaya başla.', glyph: '!', tint: 'var(--color-neutral-900)', dot: 'var(--color-accent-600)', ink: 'var(--color-neutral-100)', titleInk: 'var(--color-neutral-100)', bodyInk: 'var(--color-neutral-300)', btn: 'var(--color-accent)', btnInk: 'var(--color-bg)' },
    }[s.special] || {};

    const fbMap = {
      ok: { title: 'Doğru!', msg: '+' + s.points + ' puan kazandın.', glyph: '✓', tint: 'var(--color-accent-2-300)', ink: 'var(--color-accent-2-900)' },
      no: { title: 'Yanlış', msg: 'Açıklamayı oku, bir dahakine bileceksin.', glyph: '✕', tint: 'var(--color-accent-300)', ink: 'var(--color-accent-900)' },
      time: { title: 'Süre bitti', msg: 'Bu soruda süre yetmedi.', glyph: '⏱', tint: 'var(--color-neutral-300)', ink: 'var(--color-neutral-900)' },
    }[s.fb] || {};

    const gradeMeta = GRADES.find(g => g.no === s.grade) || {};
    const secs = this.secs;

    return {
      showChrome: chrome,
      showHome: s.screen === 'home',
      showUnits: s.screen === 'units',
      showMode: s.screen === 'mode',
      showWheel: s.screen === 'wheel',
      showQuestion: s.screen === 'question',
      showFeedback: s.screen === 'feedback',
      showKarne: s.screen === 'karne',
      showSpecial: !!s.special,

      grades: GRADES.map(g => Object.assign({}, g, { pick: () => this.pickGrade(g.no) })),
      units, options, unitStats, badges, tabs,

      streakLabel: showStreak ? (s.streakBest || 0) + ' seri' : String(s.score),
      questLabel: Math.min(s.correct, 5) + '/5',
      gradeLabel: s.grade ? s.grade + '. Sınıf' : '',
      subjectLabel: gradeMeta.subject || '',
      unitLabel: s.unit || '',
      scoreLabel: s.score + ' P',
      score: s.score, correct: s.correct, wrong: s.wrong,

      isTeam: s.mode === 'team',
      teamAScore: s.teamA, teamBScore: s.teamB,
      teamATint: s.turn === 'A' ? 'var(--color-accent)' : 'var(--color-surface)',
      teamAInk: s.turn === 'A' ? 'var(--color-bg)' : 'var(--color-neutral-700)',
      teamBTint: s.turn === 'B' ? 'var(--color-accent-2-500)' : 'var(--color-surface)',
      teamBInk: s.turn === 'B' ? '#f0fae1' : 'var(--color-neutral-700)',

      wheelHeadline: s.spinning ? 'Çark dönüyor…' : (s.mode === 'team' ? s.turn + ' grubunun sırası' : 'Çarkı çevir'),
      wheelSub: s.spinning ? 'Bakalım hangi puana denk gelecek' : 'Gelen puan, sıradaki sorunun değeri olur',
      wheelStyle: {
        position: 'absolute', inset: 0, borderRadius: '50%', overflow: 'hidden',
        transformOrigin: '50% 50%',
        transform: 'rotate(' + s.deg + 'deg)',
        transition: 'transform 4.1s cubic-bezier(.16,.84,.14,1)',
      },
      spin: () => this.spin(),
      spinDisabled: s.spinning,
      spinLabel: s.spinning ? 'Dönüyor…' : 'Çarkı çevir',

      qUnit: q ? q.unite.split('–')[0].trim() : '',
      qTopic: q ? q.konu : '',
      qText: q ? q.soru : '',
      pointsLabel: s.points + ' puan',
      timeLeft: s.timeLeft,
      timerDash: 157.1 - (157.1 * s.timeLeft) / secs,
      timerColor: s.timeLeft <= 10 ? 'var(--color-accent-600)' : 'var(--color-accent-2-500)',
      submit: () => this.submit(),
      submitDisabled: !s.picked,
      skip: () => this.resolve(false, false),

      fbTitle: fbMap.title, fbMsg: fbMap.msg, fbGlyph: fbMap.glyph,
      fbTint: fbMap.tint, fbInk: fbMap.ink,
      fbCorrectKey: q ? q.dogru : '',
      fbExplain: q ? q.aciklama : '',
      nextSpin: () => this.setState({ screen: 'wheel' }),

      spTitle: sp.title, spMsg: sp.msg, spGlyph: sp.glyph, spTint: sp.tint,
      spDot: sp.dot, spInk: sp.ink, spTitleInk: sp.titleInk, spBodyInk: sp.bodyInk,
      spBtn: sp.btn, spBtnInk: sp.btnInk,
      closeSpecial: () => this.closeSpecial(),

      goHome: () => this.setState({ screen: 'home' }),
      goUnits: () => this.setState({ screen: 'units' }),
      quitGame: () => this.setState({ screen: 'home' }),
      startSingle: () => this.begin('single'),
      startTeam: () => this.begin('team'),
      resetAll: () => this.setState({ score: 0, correct: 0, wrong: 0, solved: 0, run: 0, streakBest: 0, bigWin: false, unitScores: {}, teamA: 0, teamB: 0 }),
    };
  }
}

</script>


