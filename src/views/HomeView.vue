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

<style scoped>
/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  position: relative;
  overflow: hidden;
  width: 100%;
  margin-top: 10px;
  padding: 0;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%23667eea" stop-opacity="0.1"/><stop offset="100%" stop-color="%23667eea" stop-opacity="0"/></radialGradient></defs><circle cx="10" cy="10" r="10" fill="url(%23a)"/><circle cx="90" cy="10" r="10" fill="url(%23a)"/></svg>')
    repeat;
  opacity: 0.1;
}

.hero-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
  width: 100%;
  color: #0b0b0b;
}

.hero-content {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 3rem;
  align-items: center;
  min-height: 85vh;
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1.5rem;
  color: rgb(6, 6, 6);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.gradient-text {
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: none;
}

.hero-subtitle {
  font-size: clamp(1.2rem, 2.5vw, 1.6rem);
  font-weight: 400;
  color: rgba(12, 12, 12, 0.9);
  margin-bottom: 2rem;
}

.hero-description {
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  line-height: 1.7;
  color: rgba(6, 6, 6, 0.8);
  margin-bottom: 3rem;
  max-width: 600px;
}

.hero-buttons {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.hero-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.image-placeholder {
  width: clamp(280px, 25vw, 350px);
  height: clamp(280px, 25vw, 350px);
  border-radius: 25px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0.1) 100%);
  backdrop-filter: blur(20px);
  border: 2px solid rgba(255, 255, 255, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow:
    0 25px 50px rgba(0, 0, 0, 0.15),
    0 10px 25px rgba(255, 171, 160, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3),
    inset 0 -1px 0 rgba(0, 0, 0, 0.1);
  animation: float 6s ease-in-out infinite;
  overflow: visible;
}

.image-placeholder::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transform: rotate(45deg);
  animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
  0% {
    transform: translateX(-100%) translateY(-100%) rotate(45deg);
  }
  50% {
    transform: translateX(100%) translateY(100%) rotate(45deg);
  }
  100% {
    transform: translateX(-100%) translateY(-100%) rotate(45deg);
  }
}

.avatar {
  width: clamp(180px, 18vw, 220px);
  height: clamp(180px, 18vw, 220px);
  border-radius: 50%;
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 4px solid rgba(255, 255, 255, 0.6);
  box-shadow:
    0 15px 35px rgba(0, 0, 0, 0.15),
    0 5px 15px rgba(255, 171, 160, 0.4),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
  position: relative;
  overflow: hidden;
}

.avatar::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  background: linear-gradient(45deg, #ffeaa7, #fab1a0, #667eea, #764ba2);
  border-radius: 50%;
  z-index: -1;
  animation: rotate 3s linear infinite;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.avatar-image {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  object-position: center;
  transition: all 0.3s ease;
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.1)) brightness(1.05) contrast(1.1);
}

.avatar-image:hover {
  transform: scale(1.05);
  filter: drop-shadow(0 8px 16px rgba(0, 0, 0, 0.15)) brightness(1.1) contrast(1.15);
}

.avatar-text {
  font-size: clamp(2.5rem, 8vw, 4rem);
  font-weight: 700;
  color: #2c3e50;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.avatar-text.fallback {
  display: block;
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

.hero-scroll {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
}

.scroll-indicator {
  color: #7f8c8d;
  font-size: 0.9rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: color 0.3s ease;
}

.scroll-indicator:hover {
  color: #667eea;
}

.scroll-arrow {
  width: 20px;
  height: 20px;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  transform: rotate(45deg);
  animation: bounce 2s infinite;
}

@keyframes bounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: rotate(45deg) translateY(0);
  }
  40% {
    transform: rotate(45deg) translateY(-10px);
  }
  60% {
    transform: rotate(45deg) translateY(-5px);
  }
}

/* Quick About Section */
.quick-about {
  padding: 6rem 0;
  background: white;
  width: 100%;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  width: 100%;
}

.section-title {
  font-size: clamp(2rem, 4vw, 3rem);
  font-weight: 700;
  text-align: center;
  margin-bottom: 1rem;
  color: #2c3e50;
}

.section-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #7f8c8d;
  margin-bottom: 4rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.about-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.5rem;
  margin-top: 4rem;
}

.about-item {
  text-align: center;
  padding: 3rem 2rem;
  border-radius: 20px;
  background: #f8f9fa;
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.about-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 1;
}

.about-item:hover::before {
  opacity: 0.05;
}

.about-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
  border-color: #667eea;
}

.about-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 2;
}

.about-item h3 {
  font-size: 1.6rem;
  font-weight: 600;
  margin-bottom: 1.2rem;
  color: #2c3e50;
  position: relative;
  z-index: 2;
}

.about-item p {
  color: #7f8c8d;
  line-height: 1.7;
  font-size: 1.05rem;
  position: relative;
  z-index: 2;
}

/* Experience Section */
.experience {
  padding: 6rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  width: 100%;
}

.experience .section-title {
  color: white;
}

.experience .section-subtitle {
  color: rgba(255, 255, 255, 0.9);
}

.experience-timeline {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.experience-timeline::before {
  content: '';
  position: absolute;
  left: 30px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: rgba(255, 255, 255, 0.3);
}

.experience-item {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 80px;
}

.experience-item::before {
  content: '';
  position: absolute;
  left: 21px;
  top: 8px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  border: 3px solid white;
  box-shadow: 0 0 0 4px rgba(255, 255, 255, 0.2);
}

.experience-date {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.experience-content h3 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 0.3rem;
  color: white;
}

.experience-content h4 {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 1rem;
  font-weight: 500;
}

.experience-content ul {
  list-style: none;
  padding: 0;
}

.experience-content li {
  position: relative;
  padding-left: 20px;
  margin-bottom: 0.5rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}

.experience-content li::before {
  content: '▸';
  position: absolute;
  left: 0;
  color: #ffeaa7;
  font-weight: bold;
}

/* Featured Projects Section */
.featured-projects {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2.5rem;
  margin-bottom: 4rem;
}

.project-card {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(0, 0, 0, 0.05);
}

.project-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

.project-image {
  height: 220px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.project-image::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    45deg,
    transparent 30%,
    rgba(255, 255, 255, 0.1) 50%,
    transparent 70%
  );
  transform: translateX(-100%);
  transition: transform 0.6s ease;
}

.project-card:hover .project-image::before {
  transform: translateX(100%);
}

.project-placeholder {
  font-size: 4.5rem;
  color: white;
  opacity: 0.9;
}

.project-content {
  padding: 2rem;
}

.project-content h3 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 0.8rem;
  color: #2c3e50;
}

.project-content p {
  color: #7f8c8d;
  margin-bottom: 1.5rem;
  line-height: 1.7;
  font-size: 1.05rem;
}

.project-tags {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  transition: transform 0.2s ease;
}

.tag:hover {
  transform: translateY(-2px);
}

.projects-cta {
  text-align: center;
}

/* Skills Preview Section */
.skills-preview {
  padding: 6rem 0;
  background: white;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
  margin-top: 4rem;
}

.skill-category {
  text-align: center;
  padding: 3rem 2rem;
  border-radius: 20px;
  background: #f8f9fa;
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.skill-category::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.skill-category:hover::before {
  opacity: 0.05;
}

.skill-category:hover {
  border-color: #667eea;
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
}

.skill-category h3 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 2rem;
  color: #2c3e50;
  position: relative;
  z-index: 2;
}

.skill-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  justify-content: center;
  position: relative;
  z-index: 2;
}

.skill-item {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.6rem 1.2rem;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  cursor: default;
}

.skill-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

/* Achievements Section */
.achievements {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  width: 100%;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
  margin-top: 4rem;
}

.achievement-item {
  text-align: center;
  padding: 3rem 2rem;
  border-radius: 20px;
  background: white;
  border: 2px solid transparent;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
}

.achievement-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.achievement-item:hover::before {
  opacity: 0.05;
}

.achievement-item:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
  border-color: #667eea;
}

.achievement-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  position: relative;
  z-index: 2;
}

.achievement-item h3 {
  font-size: 1.4rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: #2c3e50;
  position: relative;
  z-index: 2;
}

.achievement-item p {
  font-size: 1.1rem;
  color: #667eea;
  font-weight: 600;
  margin-bottom: 0.5rem;
  position: relative;
  z-index: 2;
}

.achievement-desc {
  font-size: 0.95rem;
  color: #7f8c8d;
  line-height: 1.6;
  position: relative;
  z-index: 2;
}

/* Button Styles */
.btn-primary {
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  color: #2c3e50;
  padding: 1rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: inline-block;
  box-shadow: 0 4px 15px rgba(255, 171, 160, 0.3);
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px rgba(255, 171, 160, 0.4);
  color: #2c3e50;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.1);
  color: white;
  padding: 1rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  display: inline-block;
  border: 2px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
}

.btn-secondary:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
  color: white;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-container {
    padding: 1.5rem 1.5rem;
  }

  .hero-content {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
    min-height: 90vh;
  }

  .hero-title {
    font-size: clamp(2rem, 6vw, 2.8rem);
  }

  .hero-subtitle {
    font-size: clamp(1.1rem, 3vw, 1.4rem);
  }

  .hero-description {
    font-size: 1.1rem;
    max-width: 100%;
  }

  .image-placeholder {
    width: clamp(250px, 60vw, 300px);
    height: clamp(250px, 60vw, 300px);
  }

  .avatar {
    width: clamp(160px, 40vw, 200px);
    height: clamp(160px, 40vw, 200px);
  }

  .avatar-text {
    font-size: clamp(2rem, 12vw, 3rem);
  }

  .about-grid,
  .projects-grid,
  .skills-grid,
  .achievements-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .experience-timeline::before {
    left: 20px;
  }

  .experience-item {
    padding-left: 60px;
  }

  .experience-item::before {
    left: 11px;
  }

  .hero-buttons {
    justify-content: center;
    gap: 1rem;
  }

  .btn-primary,
  .btn-secondary {
    padding: 0.9rem 1.8rem;
    font-size: 1rem;
  }

  .container {
    padding: 0 1.5rem;
  }

  .about-item,
  .skill-category,
  .achievement-item {
    padding: 2.5rem 1.5rem;
  }

  .project-content {
    padding: 1.8rem;
  }
}

@media (max-width: 480px) {
  .hero-container {
    margin-top: 2.5rem;
    padding: 2rem 1rem;
  }

  .hero-title {
    font-size: clamp(1.8rem, 8vw, 2.2rem);
    margin-bottom: 1rem;
  }

  .hero-subtitle {
    font-size: clamp(1rem, 4vw, 1.2rem);
    margin-bottom: 1.5rem;
  }

  .hero-description {
    font-size: 1rem;
    margin-bottom: 2rem;
  }

  .section-title {
    font-size: clamp(1.6rem, 6vw, 2.2rem);
  }

  .about-item,
  .skill-category,
  .achievement-item {
    padding: 2rem 1.2rem;
  }

  .experience-item {
    padding-left: 50px;
  }

  .experience-timeline::before {
    left: 15px;
  }

  .experience-item::before {
    left: 6px;
  }

  .project-content {
    padding: 1.5rem;
  }

  .hero-buttons {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .btn-primary,
  .btn-secondary {
    padding: 0.8rem 1.5rem;
    font-size: 0.95rem;
    width: 100%;
    max-width: 250px;
    text-align: center;
  }

  .container {
    padding: 0 1rem;
  }

  .quick-about,
  .experience,
  .featured-projects,
  .skills-preview,
  .achievements {
    padding: 4rem 0;
  }
}
</style>

<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-container">
        <div class="hero-content">
          <div class="hero-text">
            <h1 class="hero-title">Hi, I'm <span class="gradient-text">Abhishek Yadav</span></h1>
            <h2 class="hero-subtitle">Computer Science Student & Full-Stack Developer</h2>
            <p class="hero-description">
              Results-driven Computer Science student with 2+ years of experience in full-stack web
              development. Specialized in building scalable web applications using modern frameworks
              like Flask and Vue.js, with expertise in database-driven solutions and machine
              learning integration.
            </p>
            <div class="hero-buttons">
              <RouterLink to="/projects" class="btn-primary">View My Work</RouterLink>
              <RouterLink to="/contact" class="btn-secondary">Get In Touch</RouterLink>
            </div>
          </div>
          <div class="hero-image">
            <div class="image-placeholder">
              <div class="avatar">
                <img
                  src="@/assets/images/avatar.png"
                  alt="Abhishek Yadav"
                  class="avatar-image"
                  @error="handleImageError"
                />
                <span class="avatar-text fallback" v-if="showFallback">AY</span>
              </div>
            </div>
          </div>
        </div>
        <div class="hero-scroll">
          <div class="scroll-indicator">
            <span>Scroll Down</span>
            <div class="scroll-arrow"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick About Section -->
    <section class="quick-about">
      <div class="container">
        <h2 class="section-title">About Me</h2>
        <p class="section-subtitle">
          Passionate about creating innovative solutions and continuous learning
        </p>
        <div class="about-grid">
          <div class="about-item">
            <div class="about-icon">🎓</div>
            <h3>Education</h3>
            <p>
              B.E. Computer Science & Engineering at SLIET with 9.18 CGPA, focusing on Deep
              Learning, Machine Learning, and Data Structures
            </p>
          </div>
          <div class="about-item">
            <div class="about-icon">�</div>
            <h3>Experience</h3>
            <p>
              Web Development Manager at BDCI with 2+ years of full-stack development experience,
              increasing enrollment by 40% through UX improvements
            </p>
          </div>
          <div class="about-item">
            <div class="about-icon">🚀</div>
            <h3>Innovation</h3>
            <p>
              GSSoC 2024 Contributor, 2nd Prize winner in TechFest SLIET 2024, and Postman Student
              Expert certified
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Experience Section -->
    <section class="experience">
      <div class="container">
        <h2 class="section-title">Professional Experience</h2>
        <p class="section-subtitle">My journey in the tech industry and leadership roles</p>

        <div class="experience-timeline">
          <div class="experience-item">
            <div class="experience-date">Aug 2023 – Present</div>
            <div class="experience-content">
              <h3>Web Development Manager</h3>
              <h4>BDCI (Part-Time)</h4>
              <ul>
                <li>Designed and deployed websites using GoDaddy hosting</li>
                <li>Increased enrollment by 40% through performance and UX improvements</li>
                <li>Led web development initiatives and optimized user experience</li>
              </ul>
            </div>
          </div>

          <div class="experience-item">
            <div class="experience-date">Present</div>
            <div class="experience-content">
              <h3>Website Head</h3>
              <h4>Mavericks Club, SLIET</h4>
              <ul>
                <li>Managing and updating club's web presence</li>
                <li>Implementing modern web technologies for better engagement</li>
              </ul>
            </div>
          </div>

          <div class="experience-item">
            <div class="experience-date">Present</div>
            <div class="experience-content">
              <h3>Chief Designer</h3>
              <h4>Novine SVIESA (College Magazine)</h4>
              <ul>
                <li>Responsible for layout, design, and visual content</li>
                <li>Leading creative direction for college publication</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Projects Preview -->
    <section class="featured-projects">
      <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <p class="section-subtitle">A selection of my recent work and personal projects</p>
        <div class="projects-grid">
          <div class="project-card">
            <div class="project-image">
              <div class="project-placeholder">🧠</div>
            </div>
            <div class="project-content">
              <h3>Quiz-Master WebApp</h3>
              <p>Multi-user quiz platform with real-time scoring and student/teacher portals</p>
              <div class="project-tags">
                <span class="tag">Python</span>
                <span class="tag">Flask</span>
                <span class="tag">SQLite</span>
                <span class="tag">Bootstrap</span>
              </div>
            </div>
          </div>

          <div class="project-card">
            <div class="project-image">
              <div class="project-placeholder">�</div>
            </div>
            <div class="project-content">
              <h3>Hospital Management System</h3>
              <p>
                Complete admin, patient, and doctor portal for scheduling and profile management
              </p>
              <div class="project-tags">
                <span class="tag">Node.js</span>
                <span class="tag">React</span>
                <span class="tag">Express</span>
                <span class="tag">Tailwind CSS</span>
              </div>
            </div>
          </div>

          <div class="project-card">
            <div class="project-image">
              <div class="project-placeholder">🤖</div>
            </div>
            <div class="project-content">
              <h3>AI Chatbot with Gemini API</h3>
              <p>AI-powered chatbot for real-time conversations using Google's Gemini API</p>
              <div class="project-tags">
                <span class="tag">Node.js</span>
                <span class="tag">React</span>
                <span class="tag">Gemini API</span>
              </div>
            </div>
          </div>
        </div>
        <div class="projects-cta">
          <RouterLink to="/projects" class="btn-primary">View All Projects</RouterLink>
        </div>
      </div>
    </section>

    <!-- Skills Preview -->
    <section class="skills-preview">
      <div class="container">
        <h2 class="section-title">Technical Skills</h2>
        <p class="section-subtitle">Technologies and tools I work with to bring ideas to life</p>
        <div class="skills-grid">
          <div class="skill-category">
            <h3>Languages</h3>
            <div class="skill-list">
              <span class="skill-item">Python</span>
              <span class="skill-item">JavaScript</span>
              <span class="skill-item">C++</span>
              <span class="skill-item">C</span>
            </div>
          </div>
          <div class="skill-category">
            <h3>Frameworks & Tools</h3>
            <div class="skill-list">
              <span class="skill-item">Flask</span>
              <span class="skill-item">Vue.js</span>
              <span class="skill-item">React</span>
              <span class="skill-item">Node.js</span>
              <span class="skill-item">TensorFlow</span>
              <span class="skill-item">FastAPI</span>
            </div>
          </div>
          <div class="skill-category">
            <h3>Databases & Cloud</h3>
            <div class="skill-list">
              <span class="skill-item">PostgreSQL</span>
              <span class="skill-item">MongoDB</span>
              <span class="skill-item">SQLite</span>
              <span class="skill-item">Redis</span>
              <span class="skill-item">Google Cloud</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Achievements Section -->
    <section class="achievements">
      <div class="container">
        <h2 class="section-title">Achievements & Recognition</h2>
        <p class="section-subtitle">Awards, certifications, and notable accomplishments</p>

        <div class="achievements-grid">
          <div class="achievement-item">
            <div class="achievement-icon">🏆</div>
            <h3>2nd Prize in Electronica</h3>
            <p>TechFest SLIET 2024</p>
            <span class="achievement-desc">IoT-based voice-controlled RC car project</span>
          </div>

          <div class="achievement-item">
            <div class="achievement-icon">👩‍💻</div>
            <h3>GSSoC 2024 Contributor</h3>
            <p>GirlScript Summer of Code</p>
            <span class="achievement-desc">Contributed to open-source projects</span>
          </div>

          <div class="achievement-item">
            <div class="achievement-icon">📜</div>
            <h3>Postman Student Expert</h3>
            <p>API Testing Certification</p>
            <span class="achievement-desc">API testing and automation expertise</span>
          </div>

          <div class="achievement-item">
            <div class="achievement-icon">🎓</div>
            <h3>Academic Excellence</h3>
            <p>CGPA: 9.18</p>
            <span class="achievement-desc">B.E. Computer Science & Engineering</span>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
