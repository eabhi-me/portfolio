<script>
export default {
  name: 'HomeView',
  data() {
    return {
      showFallback: false,
    }
  },
  methods: {
    handleImageError() {
      this.showFallback = true
    },
  },
}
</script>

<template>
  <div class="home">
    <!-- Animated Background -->
    <div class="hero-bg">
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>
    </div>

    <!-- ── HERO ── -->
    <section class="hero">
      <div class="hero-container">
        <div class="hero-text">
          <div class="hero-badge">
            <span class="badge-pulse"></span>
            <span class="badge-text">Open to opportunities</span>
          </div>
          <h1 class="hero-title">
            Hi, I'm <span class="gradient-text">Abhishek Yadav</span>
          </h1>
          <h2 class="hero-subtitle">Backend Developer &amp; ML Enthusiast</h2>
          <p class="hero-desc">
            CS undergraduate focused on Backend Development and Machine Learning.
            Skilled in building RESTful APIs with Flask and FastAPI. Passionate about
            AI/ML and competitive programming with <span class="hl">500+ DSA</span> problems solved.
          </p>
          <div class="hero-buttons">
            <RouterLink to="/projects" class="btn-primary">View My Work</RouterLink>
            <a href="https://github.com/eabhi-me" target="_blank" rel="noopener" class="btn-secondary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.374 0 12c0 5.302 3.438 9.8 8.207 11.387.6.111.82-.261.82-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>
              GitHub
            </a>
          </div>
        </div>

        <div class="hero-image">
          <div class="avatar-wrap">
            <div class="avatar-ring"></div>
            <div class="avatar">
              <img src="@/assets/images/avatar.png" alt="Abhishek Yadav" class="avatar-img" @error="handleImageError" />
              <span v-if="showFallback" class="avatar-fallback">AY</span>
            </div>
          </div>
        </div>
      </div>

      <div class="scroll-down">
        <span>Scroll</span>
        <div class="scroll-arrow"></div>
      </div>
    </section>

    <!-- ── QUICK ABOUT ── -->
    <section class="quick-about">
      <div class="container">
        <h2 class="section-title">About Me</h2>
        <p class="section-subtitle">A snapshot of who I am and what drives me</p>
        <div class="about-grid">
          <div class="about-card" v-for="n in 3" :key="n">
            <div class="card-glow"></div>
            <div class="card-icon" v-if="n===1">🎓</div>
            <div class="card-icon" v-if="n===2">💼</div>
            <div class="card-icon" v-if="n===3">🚀</div>
            <h3 v-if="n===1">Education</h3>
            <h3 v-if="n===2">Experience</h3>
            <h3 v-if="n===3">Achievements</h3>
            <p v-if="n===1">B.E. Computer Science at SLIET with <span class="hl">9.12 CGPA</span>. Focused on Backend Development, ML, and Data Structures.</p>
            <p v-if="n===2">Backend Intern at Novem Controls &amp; Freelance Full-Stack Developer at BDCI, building scalable web apps.</p>
            <p v-if="n===3">GATE 2026, 3rd Rank IIT BHU Trading Competition, GSSoC 2024, TechFest Winner, Postman Expert.</p>
          </div>
        </div>
        <div class="cta-row">
          <RouterLink to="/about" class="btn-primary">Full Bio</RouterLink>
        </div>
      </div>
    </section>

    <!-- ── TIMELINE ── -->
    <section class="experience">
      <div class="container">
        <h2 class="section-title">Professional Experience</h2>
        <p class="section-subtitle">My journey from internships to freelance development</p>
        <div class="timeline">
          <div class="timeline-item">
            <div class="tl-dot"></div>
            <div class="tl-content">
              <span class="tl-date">May 2025 – Jul 2025</span>
              <h3>Backend Developer Intern</h3>
              <h4>Novem Controls Pvt. Ltd., Mohali</h4>
              <ul>
                <li>Developed admin dashboard using Flask and PostgreSQL</li>
                <li>Built CRUD operations, backend APIs, and DB management</li>
                <li>Assisted in testing, debugging, and deployment</li>
              </ul>
            </div>
          </div>
          <div class="timeline-item">
            <div class="tl-dot"></div>
            <div class="tl-content">
              <span class="tl-date">Aug 2023 – Present</span>
              <h3>Freelance Full-Stack Developer</h3>
              <h4>BDCI (Part-Time, Remote)</h4>
              <ul>
                <li>Built institute management platform with Flask, Vue.js, and MySQL</li>
                <li>Developed RESTful APIs for auth, courses, and branch management</li>
                <li>Deployed and maintained production apps on cPanel</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ── FEATURED PROJECTS ── -->
    <section class="featured-projects">
      <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <p class="section-subtitle">A selection of recent work and experiments</p>
        <div class="projects-grid">

          <div class="project-card">
            <!-- QuizMaster V2 -->
            <div class="card-top">
              <div class="card-icon">🧠</div>
              <h3>QuizMaster V2</h3>
              <p class="card-dscr">Full-stack quiz platform with analytics, JWT auth, Celery async tasks, and Docker deployment.</p>
              <div class="card-tags">
                <span>Flask</span><span>Vue.js</span><span>PostgreSQL</span><span>Redis</span><span>Docker</span>
              </div>
            </div>
            <div class="card-links">
              <a href="#" class="link-live">Live</a>
              <a href="https://github.com/eabhi-me" class="link-code">GitHub</a>
            </div>
          </div>

          <div class="project-card">
            <div class="card-top">
              <div class="card-icon">😊</div>
              <h3>Sentiment Analysis</h3>
              <p class="card-dscr">Real-time NLP classification using a pre-trained DistilBERT model with a Gradio web interface.</p>
              <div class="card-tags">
                <span>Python</span><span>HuggingFace</span><span>PyTorch</span><span>Gradio</span>
              </div>
            </div>
            <div class="card-links">
              <a href="#" class="link-live">Live</a>
              <a href="https://github.com/eabhi-me" class="link-code">GitHub</a>
            </div>
          </div>

          <div class="project-card">
            <div class="card-top">
              <div class="card-icon">🚁</div>
              <h3>Autonomous UAV</h3>
              <p class="card-dscr">IoT-based UAV for agriculture with ML plant health detection and ROS LIDAR integration.</p>
              <div class="card-tags">
                <span>Python</span><span>ROS</span><span>LIDAR</span><span>ML</span>
              </div>
            </div>
            <div class="card-links">
              <a href="#" class="link-live">Live</a>
              <a href="https://github.com/eabhi-me" class="link-code">GitHub</a>
            </div>
          </div>
        </div>
        <div class="cta-row">
          <RouterLink to="/projects" class="btn-primary">All Projects</RouterLink>
        </div>
      </div>
    </section>

    <!-- ── TECH STACK ── -->
    <section class="skills-preview">
      <div class="container">
        <h2 class="section-title">Tech Stack</h2>
        <p class="section-subtitle">Languages, frameworks, and tools I use daily</p>
        <div class="skills-grid">
          <div class="skill-block">
            <h3>Languages</h3>
            <div class="skill-tags">
              <span>Python</span><span>C++</span><span>C</span><span>JavaScript</span>
            </div>
          </div>
          <div class="skill-block">
            <h3>Frameworks</h3>
            <div class="skill-tags">
              <span>Flask</span><span>Vue.js</span><span>FastAPI</span><span>React</span>
            </div>
          </div>
          <div class="skill-block">
            <h3>Data &amp; ML</h3>
            <div class="skill-tags">
              <span>PostgreSQL</span><span>MongoDB</span><span>Redis</span><span>PyTorch</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ── ACHIEVEMENTS ── -->
    <section class="achievements">
      <div class="container">
        <h2 class="section-title">Achievements</h2>
        <p class="section-subtitle">Milestones that define my journey</p>
        <div class="awards-grid">
          <div class="award-card" v-for="i in 8" :key="i">
            <div class="award-icon" v-if="i===1">🎓</div>
            <div class="award-icon" v-if="i===2">🏆</div>
            <div class="award-icon" v-if="i===3">🚀</div>
            <div class="award-icon" v-if="i===4">🎯</div>
            <div class="award-icon" v-if="i===5">👩‍💻</div>
            <div class="award-icon" v-if="i===6">📜</div>
            <div class="award-icon" v-if="i===7">🎓</div>
            <div class="award-icon" v-if="i===8">💻</div>
            <h4 v-if="i===1">GATE CSE 2026</h4>
            <h4 v-if="i===2">3rd Rank IIT BHU</h4>
            <h4 v-if="i===3">Antariksh Hackathon</h4>
            <h4 v-if="i===4">2nd Prize TechFest</h4>
            <h4 v-if="i===5">GSSoC 2024</h4>
            <h4 v-if="i===6">Postman Expert</h4>
            <h4 v-if="i===7">CGPA 9.12</h4>
            <h4 v-if="i===8">500+ DSA</h4>
            <p v-if="i===1">Qualified</p>
            <p v-if="i===2">Trading Algo Comp</p>
            <p v-if="i===3">Finalist</p>
            <p v-if="i===4">IoT RC Car</p>
            <p v-if="i===5">Open Source</p>
            <p v-if="i===6">API Expert</p>
            <p v-if="i===7">SLIET</p>
            <p v-if="i===8">Problems Solved</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ============================================================
   HOME  (modern glass theme 2026)
   ============================================================ */

/* ── UTILS ── */
.hl { background: var(--grad-main); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; }

/* ── HERO ── */
.hero {
  min-height: 100vh; display: flex; flex-direction: column;
  align-items: center; justify-content: center; position: relative;
  padding: 8rem 0 4rem; overflow: hidden;
}

.hero-bg { position: absolute; inset: 0; pointer-events: none; z-index: 0; }
.orb { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.45; animation: orbFloat 8s ease-in-out infinite; }
.orb-1 { width: 480px; height: 480px; background: rgba(124,58,237,0.35); top: -10%; left: -5%; animation-delay: 0s; }
.orb-2 { width: 360px; height: 360px; background: rgba(6,182,212,0.25); bottom: 10%; right: -5%; animation-delay: -3s; }
.orb-3 { width: 260px; height: 260px; background: rgba(245,158,11,0.15); top: 40%; left: 45%; animation-delay: -5s; }
@keyframes orbFloat { 0%, 100% { transform: translate(0,0) scale(1); } 50% { transform: translate(30px,-30px) scale(1.05); } }

.hero-container { display: grid; grid-template-columns: 1.3fr 1fr; gap: 4rem; align-items: center; max-width: 1200px; width: 100%; padding: 0 2.4rem; position: relative; z-index: 1; }

/* Text */
.hero-text { max-width: 620px; }
.hero-badge { display: inline-flex; align-items: center; gap: 0.6rem; padding: 0.4rem 1rem; border-radius: 50px; background: rgba(124,58,237,0.12); border: 1px solid rgba(124,58,237,0.2); margin-bottom: 2rem; font-size: 0.85rem; color: #c4b5fd; }
.badge-pulse { width: 8px; height: 8px; border-radius: 50%; background: #7c3aed; animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0 tasks.4; transform: scale(1.3); } }

.hero-title { font-size: clamp(2.6rem, 6vw, 4.5rem); font-weight: 800; line-height: 1.1; color: #fff; letter-spacing: -0.03em; margin-bottom: 1.2rem; }
.gradient-text { background: var(--grad-main); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

.hero-subtitle { font-size: clamp(1.2rem, 2.4vw, 1.7rem); font-weight: 500; color: var(--text-secondary); margin-bottom: 1.5rem; }
.hero-desc { font-size: clamp(0.95rem, 1.5vw, 1.1rem); line-height: 1.8; color: var(--text-secondary); margin-bottom: 2.5rem; }

.hero-buttons { display: flex; gap: 1.2rem; flex-wrap: wrap; }

/* Avatar */
.hero-image { display: flex; align-items: center; justify-content: center; }
.avatar-wrap { position: relative; width: 280px; height: 280px; }
.avatar-ring { position: absolute; inset: -20px; border-radius: 50%; background: conic-gradient(from 0deg, #4d44ad, #7c3aed, #06b6d4, #4d44ad); opacity: 0.6; animation: spin 8s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.avatar { position: relative; width: 100%; height: 100%; border-radius: 50%; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.5); }
.avatar-img { width: 100%; height: 100%; object-fit: cover; }
.avatar-fallback { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 4rem; font-weight: 800; background: linear-gradient(135deg,#4d44ad,#7c3aed); }

/* Scroll */
  .scroll-down { position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; gap: 0.5rem; color: var(--text-muted); font-size: 0.85rem; }
.scroll-arrow { width: 20px; height: 20px; border-right: 2px solid; border-bottom: 2px solid; transform: rotate(45deg); animation: bounceArrow 2s infinite; }
@keyframes bounceArrow { 0%,20%,50%,80%,100% { transform: rotate(45deg) translate(0,0); } 40% { transform: rotate(45deg) translateY(-8px); } 60% { transform: rotate(45deg) translateY(-4px); } }

/* ── SECTION SHARED ── */
.quick-about, .experience, .featured-projects, .skills-preview, .achievements { padding: 7rem 0; position: relative; }

/* ── QUICK ABOUT ── */
.quick-about { background: linear-gradient(180deg,transparent, rgba(124,58,237,0.03)); }
.about-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.8rem; margin-top: 3rem; }
.about-card { position: relative; padding: 2.2rem 1.8rem; border-radius: 20px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); transition: transform 0.4s var(--ease-out), box-shadow 0.4s var(--ease-out); backdrop-filter: blur(12px); }
.about-card:hover { transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.2), 0 0 30px rgba(124,58,237,0.06); border-color: rgba(124,58,237,0.2); }
.card-glow { position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, rgba(124,58,237,0.08), transparent 60%); opacity: 0; transition: opacity 0.4s; }
.about-card:hover .card-glow { opacity: 1; }
.card-icon { font-size: 2.8rem; margin-bottom: 1rem; }
.about-card h3 { font-size: 1.2rem; font-weight: 600; color: #fff; margin-bottom: 0.8rem; }
.about-card p { font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary); }

/* ── TIMELINE ── */
.experience { background: var(--bg-deep); }
.timeline { position: relative; max-width: 800px; margin: 2rem auto 0; padding-left: 2rem; }
.timeline::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, #7c3aed, #06b6d4); border-radius: 2px; }
.timeline-item { position: relative; padding: 0 0 0 2rem; margin-bottom: 3rem; }
.tl-dot { position: absolute; left: -8px; top: 2px; width: 16px; height: 16px; border-radius: 50%; background: #7c3aed; border: 3px solid var(--bg-deep); box-shadow: 0 0 12px rgba(124,58,237,0.4); }
.tl-date { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }
.tl-content h3 { font-size: 1.3rem; font-weight: 600; color: #fff; margin: 0.3rem 0 0.3rem; }
.tl-content h4 { font-size: 1rem; font-weight: 400; color: var(--text-secondary); margin-bottom: 1rem; }
.tl-content ul { list-style: none; padding: 0; }
.tl-content li {position: relative; padding-left: 1.2rem; margin-bottom: 0.6rem; color: var(--text-secondary); font-size: 0.95rem; }
.tl-content li::before { content: '➜'; position: absolute; left: 0; color: #7c3aed; font-size: 0.8rem; }

/* ── PROJECTS ── */
.featured-projects { background: linear-gradient(180deg, var(--bg-deep), rgba(124,58,237,0.04), var(--bg-deep)); }
.projects-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.8rem; margin-top: 3rem; }
.project-card { display: flex; flex-direction: column; border-radius: 24px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); overflow: hidden; transition: all 0.4s var(--ease-out); position: relative; }
.project-card:hover { transform: translateY(-10px) scale(1.01); box-shadow: 0 30px 60px rgba(0,0,0,0.3), 0 0 40px rgba(124,58,237,0.06); border-color: rgba(124,58,237,0.15); }
.card-top { padding: 2rem; flex: 1; }
.card-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.project-card h3 { font-size: 1.25rem; font-weight: 600; color: #fff; margin-bottom: 0.6rem; }
.card-dscr { font-size: 0.95rem; color: var(--text-secondary); line-height: 1.65; margin-bottom: 1.2rem; }
.card-tags { display: flex; flex-wrap: wrap; gap: 0.4rem; }
.card-tags span { padding: 0.25rem 0.7rem; border-radius: 50px; font-size: 0.8rem; background: rgba(124,58,237,0.1); color: #c4b5fd; border: 1px solid rgba(124,58,237,0.15); }
.card-links { display: flex; padding: 0 2rem 1.5rem; gap: 1rem; }
.link-live, .link-code { padding: 0.5rem 1.2rem; border-radius: 50px; font-size: 0.85rem; font-weight: 500; text-decoration: none; transition: all 0.25s ease; }
.link-live { background: var(--grad-main); color: #fff; box-shadow: 0 4px 16px rgba(124,58,237,0.35); }
.link-live:hover { transform: scale(1.05); box-shadow: 0 6px 24px rgba(124,58,237,0.45); }
.link-code { background: rgba(255,255,255,0.05); color: var(--text-secondary); border: 1px solid rgba(255,255,255,0.1); }
.link-code:hover { border-color: rgba(255,255,255,0.25); color: #fff; }

/* ── SKILLS ── */
.skills-preview { background: var(--bg-deep); }
.skills-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 1.8rem; margin-top: 3rem; }
.skill-block { padding: 2rem; border-radius: 20px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); text-align: center; transition: all 0.35s var(--ease-out); }
  .skill-block:hover { transform: translateY(-6px); border-color: rgba(124,58,237,0.15); box-shadow: 0 15px 40px rgba(0,0,0,0.2); }
.skill-block h3 { font-size: 1.1rem; font-weight: 600; color: #fff; margin-bottom: 1rem; }
.skill-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; justify-content: center; }
.skill-tags span { padding: 0.35rem 0.9rem; border-radius: 50px; font-size: 0.85rem; background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(6,182,212,0.1)); color: #c4b5fd; border: 1px solid rgba(124,58,237,0.15); }

/* ── ACHIEVEMENTS ── */
.achievements { background: linear-gradient(180deg, var(--bg-deep), rgba(124,58,237,0.03)); }
.awards-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 1.2rem; margin-top: 3rem; }
  .award-card { padding: 1.8rem 1rem; border-radius: 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); text-align: center; transition: all 0.35s var(--ease-out); }
.award-card:hover { transform: translateY(-5px); border-color: rgba(124,58,237,0.2); box-shadow: 0 12px 32px rgba(0,0,0,0.2); }
.award-icon { font-size: 2.2rem; margin-bottom: 0.8rem; }
.award-card h4 { font-size: 1rem; font-weight: 600; color: #fff; margin-bottom: 0.3rem; }
.award-card p { font-size: 0.8rem; color: var(--text-muted); }

/* ── CTA ROW ── */
.cta-row { display: flex; justify-content: center; margin-top: 3rem; }

/* ── RESPONSIVE ── */
@media (max-width: 1024px) {
  .hero-container { grid-template-columns: 1fr; text-align: center; gap: 3rem; }
  .hero-image { order: -1; }
  .avatar-wrap { width: 220px; height: 220px; margin: 0 auto; }
  .hero-buttons { justify-content: center; }
  .about-grid, .skills-grid { grid-template-columns: repeat(2,1fr); }
  .projects-grid { grid-template-columns: repeat(2,1fr); }
  .awards-grid { grid-template-columns: repeat(2,1fr); }
}

@media (max-width: 640px) {
  .hero-container { padding: 0 1.2rem; }
  .about-grid, .projects-grid, .skills-grid, .awards-grid { grid-template-columns: 1fr; }
  .timeline { padding-left: 1.2rem; }
}
</style>