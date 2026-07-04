<template>
  <div class="about">
    <section class="about-hero">
      <div class="container">
        <div class="hero-content">
          <h1 class="section-title">About Me</h1>
          <p class="section-subtitle">Get to know more about my journey, passion, and vision as an engineering student</p>
        </div>
      </div>
    </section>

    <section class="about-content">
      <div class="container">
        <div class="about-grid">
          <div class="about-text">
            <div class="about-section">
              <h2>Hello, I'm Abhishek Yadav</h2>
              <p>I am a passionate Backend Developer and Machine Learning enthusiast with hands-on experience in building RESTful APIs, scalable web applications, and AI-powered solutions. Currently pursuing my B.E. in Computer Science Engineering at SLIET with a CGPA of 9.12, I combine strong academic foundations with practical industry experience.</p>
              <p>My journey in software development began during my college years and has evolved through various roles, including my recent position as a Backend Developer Intern at Novem Controls (May 2025 - Jul 2025). I specialize in creating scalable backend systems using Flask and FastAPI, database design with PostgreSQL and Redis, and have successfully developed multiple production-ready systems including quiz platforms, sentiment analysis tools, and IoT-based autonomous UAVs.</p>
            </div>
            <div class="about-section">
              <h3>What Drives Me</h3>
              <ul class="motivation-list">
                <li><span class="drive-icon">🚀</span> <strong>Innovation:</strong> Developing AI-powered solutions that transform traditional workflows</li>
                <li><span class="drive-icon">� Wiring</span> <strong>Learning:</strong> Continuously expanding skills in emerging technologies</li>
                <li><span class="drive-icon">🤝</span> <strong>Leadership:</strong> Mentoring teams and contributing to open-source communities</li>
              </ul>
            </div>
          </div>
          <div class="about-stats">
            <div class="stat-card glass">
              <div class="stat-icon">🎓</div>
              <div class="stat-content">
                <h3>Education</h3>
                <p>B.E. CSE - 9.12 CGPA</p>
                <span class="stat-detail">Computer Science Engineering at SLIET</span>
              </div>
            </div>
            <div class="stat-card glass">
              <div class="stat-icon">💼</div>
              <div class="stat-content">
                <h3>Experience</h3>
                <p>Backend &amp; Full-Stack</p>
                <span class="stat-detail">Intern at Novem Controls, Freelance at BDCI</span>
              </div>
            </div>
            <div class="stat-card glass">
              <div class="stat-icon">🏆</div>
              <div class="stat-content">
                <h3>Achievements</h3>
                <p>GATE Qualified</p>
                <span class="stat-detail">GATE 2026, 3rd Rank IIT BHU, GSSoC</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">Technical Skills</h2>
        <p class="section-subtitle">Proficiency levels across technologies</p>
        <div class="skills-categories">
          <div class="skill-category glass">
            <h3>Programming Languages</h3>
            <div class="skills-list">
              <div class="skill-item"><span class="skill-name">Python</span><div class="skill-bar"><div class="skill-progress" style="width: 90%"></div></div></div>
              <div class="skill-item"><span class="skill-name">JavaScript</span><div class="skill-bar"><div class="skill-progress" style="width: 85%"></div></div></div>
              <div class="skill-item"><span class="skill-name">C++</span><div class="skill-bar"><div class="skill-progress" style="width: 80%"></div></div></div>
              <div class="skill-item"><span class="skill-name">C</span><div class="skill-bar"><div class="skill-progress" style="width: 75%"></div></div></div>
            </div>
          </div>
          <div class="skill-category glass">
            <h3>Web Technologies</h3>
            <div class="skills-list">
              <div class="skill-item"><span class="skill-name">Flask</span><div class="skill-bar"><div class="skill-progress" style="width: 92%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Vue.js</span><div class="skill-bar"><div class="skill-progress" style="width: 85%"></div></div></div>
              <div class="skill-item"><span class="skill-name">FastAPI</span><div class="skill-bar"><div class="skill-progress" style="width: 80%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Node.js</span><div class="skill-bar"><div class="skill-progress" style="width: 78%"></div></div></div>
            </div>
          </div>
          <div class="skill-category glass">
            <h3>Data &amp; ML</h3>
            <div class="skills-list">
              <div class="skill-item"><span class="skill-name">PostgreSQL</span><div class="skill-bar"><div class="skill-progress" style="width: 85%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Redis</span><div class="skill-bar"><div class="skill-progress" style="width: 70%"></div></div></div>
              <div class="skill-item"><span class="skill-name">PyTorch</span><div class="skill-bar"><div class="skill-progress" style="width: 75%"></div></div></div>
              <div class="skill-item"><span class="skill-name">MongoDB</span><div class="skill-bar"><div class="skill-progress" style="width: 72%"></div></div></div>
            </div>
          </div>
          <div class="skill-category glass">
            <h3>Tools &amp; Platforms</h3>
            <div class="skills-list">
              <div class="skill-item"><span class="skill-name">Git</span><div class="skill-bar"><div class="skill-progress" style="width: 88%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Docker</span><div class="skill-bar"><div class="skill-progress" style="width: 70%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Linux</span><div class="skill-bar"><div class="skill-progress" style="width: 82%"></div></div></div>
              <div class="skill-item"><span class="skill-name">Celery</span><div class="skill-bar"><div class="skill-progress" style="width: 68%"></div></div></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default { name: 'AboutView' };
</script>

<style scoped>
.about { padding-top: 80px; }
.about-hero { padding: 5rem 0; text-align: center; position: relative; overflow: hidden; }
.about-hero::before {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 50%, rgba(124,58,237,0.1), transparent 60%);
  pointer-events: none;
}
.about-content { padding: 5rem 0; }
.about-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start; }
.about-section { margin-bottom: 3rem; }
.about-section h2 { font-size: 2rem; font-weight: 700; background: var(--grad-main); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 1.5rem; }
.about-section h3 { font-size: 1.5rem; font-weight: 600; color: #fff; margin-bottom: 1rem; }
.about-section p { font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary); margin-bottom: 1.5rem; }
.motivation-list { list-style: none; padding: 0; }
.motivation-list li { padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 1rem; line-height: 1.6; color: var(--text-secondary); display: flex; align-items: center; gap: 0.8rem; }
.motivation-list li:last-child { border-bottom: none; }
.drive-icon { font-size: 1.4rem; flex-shrink: 0; }
.about-stats { display: flex; flex-direction: column; gap: 1.5rem; }
.stat-card { display: flex; align-items: center; padding: 1.5rem; border-radius: 16px; transition: transform 0.3s var(--ease-out); }
.stat-card:hover { transform: translateY(-5px); }
.stat-icon { font-size: 2.2rem; margin-right: 1rem; flex-shrink: 0; }
.stat-content h3 { font-size: 1.1rem; font-weight: 600; color: #fff; margin-bottom: 0.3rem; }
.stat-content p { font-size: 0.95rem; font-weight: 600; color: #a78bfa; margin-bottom: 0.2rem; }
.stat-detail { font-size: 0.85rem; color: var(--text-muted); }
.skills-section { padding: 5rem 0; background: linear-gradient(180deg, var(--bg-deep), rgba(124,58,237,0.03)); }
.skills-categories { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; margin-top: 3rem; }
.skill-category { padding: 2rem; border-radius: 20px; }
.skill-category h3 { font-size: 1.2rem; font-weight: 600; color: #fff; margin-bottom: 1.5rem; text-align: center; }
.skills-list { display: flex; flex-direction: column; gap: 1rem; }
.skill-item { display: flex; flex-direction: column; gap: 0.4rem; }
.skill-name { font-weight: 500; color: var(--text-secondary); font-size: 0.95rem; }
.skill-bar { height: 8px; background: rgba(255,255,255,0.06); border-radius: 10px; overflow: hidden; }
.skill-progress { height: 100%; border-radius: 10px; background: var(--grad-main); box-shadow: 0 0 12px rgba(124,58,237,0.3); transition: width 1s ease; }
.glass { background: rgba(255,255,255,0.03); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.06); }

@media (max-width: 768px) {
  .about-grid { grid-template-columns: 1fr; gap: 2rem; }
  .about-stats { order: -1; }
  .skills-categories { grid-template-columns: 1fr; }
}
</style>