<template>
  <div class="projects">
    <!-- Hero Section -->
    <section class="projects-hero">
      <div class="hero-content">
        <h1 class="section-title">My Projects</h1>
        <p class="hero-subtitle">
          A collection of projects that showcase my skills, creativity, and passion for technology
        </p>
      </div>
    </section>

    <!-- Featured Projects -->
    <section class="featured-projects">
      <div class="featured-container">
        <h2 class="section-subtitle">Featured Projects</h2>

        <div class="featured-grid">
          <div class="featured-project">
            <div class="project-image">
              <div class="project-placeholder">🧠</div>
              <div class="project-overlay">
                <div class="project-links">
                  <a href="#" class="project-link">Live Demo</a>
                  <a href="#" class="project-link">GitHub</a>
                </div>
              </div>
            </div>
            <div class="project-content">
              <h3>Quiz-Master WebApp</h3>
              <p>
                A comprehensive multi-user quiz platform with real-time scoring and separate portals
                for students and teachers. Built with Python Flask and featuring database-driven
                question management and analytics.
              </p>
              <div class="project-tech">
                <span class="tech-tag">Python</span>
                <span class="tech-tag">Flask</span>
                <span class="tech-tag">SQLite</span>
                <span class="tech-tag">JavaScript</span>
                <span class="tech-tag">Bootstrap</span>
              </div>
              <div class="project-features">
                <h4>Key Features:</h4>
                <ul>
                  <li>Multi-user authentication system</li>
                  <li>Real-time quiz scoring and feedback</li>
                  <li>Teacher dashboard for question management</li>
                  <li>Student progress tracking and analytics</li>
                </ul>
              </div>
            </div>
          </div>

          <div class="featured-project reverse">
            <div class="project-image">
              <div class="project-placeholder">🏥</div>
              <div class="project-overlay">
                <div class="project-links">
                  <a href="#" class="project-link">Live Demo</a>
                  <a href="#" class="project-link">GitHub</a>
                </div>
              </div>
            </div>
            <div class="project-content">
              <h3>Hospital Management System</h3>
              <p>
                A complete healthcare management platform with dedicated portals for admins,
                patients, and doctors. Features appointment scheduling, profile management, and
                medical record tracking.
              </p>
              <div class="project-tech">
                <span class="tech-tag">Node.js</span>
                <span class="tech-tag">Express</span>
                <span class="tech-tag">React</span>
                <span class="tech-tag">Tailwind CSS</span>
                <span class="tech-tag">MongoDB</span>
              </div>
              <div class="project-features">
                <h4>Key Features:</h4>
                <ul>
                  <li>Role-based access control system</li>
                  <li>Appointment scheduling and management</li>
                  <li>Medical record digitization</li>
                  <li>Real-time doctor-patient communication</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- All Projects -->
    <section class="all-projects">
      <div class="all-projects-container">
        <h2 class="section-subtitle">All Projects</h2>

        <div class="filter-tabs">
          <button
            class="filter-tab"
            :class="{ active: activeFilter === 'all' }"
            @click="setFilter('all')"
          >
            All
          </button>
          <button
            class="filter-tab"
            :class="{ active: activeFilter === 'web' }"
            @click="setFilter('web')"
          >
            Web Development
          </button>
          <button
            class="filter-tab"
            :class="{ active: activeFilter === 'mobile' }"
            @click="setFilter('mobile')"
          >
            Mobile Apps
          </button>
          <button
            class="filter-tab"
            :class="{ active: activeFilter === 'ai' }"
            @click="setFilter('ai')"
          >
            AI/ML
          </button>
        </div>

        <div class="projects-grid">
          <div
            v-for="project in filteredProjects"
            :key="project.id"
            class="project-card"
            :class="project.category"
          >
            <div class="card-image">
              <div class="image-placeholder">{{ project.emoji }}</div>
              <div class="card-overlay">
                <div class="overlay-content">
                  <a :href="project.demo" class="overlay-link">View Details</a>
                  <a :href="project.github" class="overlay-link">Source Code</a>
                </div>
              </div>
            </div>
            <div class="card-content">
              <h3>{{ project.title }}</h3>
              <p>{{ project.description }}</p>
              <div class="card-tech">
                <span v-for="tech in project.technologies" :key="tech" class="tech-badge">
                  {{ tech }}
                </span>
              </div>
              <div class="card-status">
                <span :class="['status-badge', project.status]">
                  {{ project.status }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action -->
    <section class="projects-cta">
      <div class="cta-content">
        <h2>Interested in Collaborating?</h2>
        <p>
          I'm always open to discussing new projects, creative ideas, or opportunities to be part of
          your vision.
        </p>
        <RouterLink to="/contact" class="btn-primary">Get In Touch</RouterLink>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ProjectsView',
  data() {
    return {
      activeFilter: 'all',
      projects: [
          {
            id: 1,
            title: 'Quiz-Master WebApp',
            description:
              'Dynamic multi-user quiz platform with real-time scoring and dedicated teacher/student portals.',
            emoji: '🧠',
            category: 'web',
            technologies: ['Python', 'Flask', 'SQLite', 'JavaScript', 'Bootstrap'],
            status: 'completed',
            github: 'https://github.com/eabhi-me/quiz-master-prep',
            demo: 'https://quiz-master-dot-velvety-ring-456112-u3.el.r.appspot.com/',
        },
        {
          id: 2,
          title: 'Hospital Management System',
          description:
            'Full-stack web application for managing hospital operations including appointments and patient profiles.',
          emoji: '🏥',
          category: 'web',
          technologies: ['Node.js', 'Express', 'React', 'Tailwind CSS'],
          status: 'completed',
          github: 'https://github.com/eabhi-me/medecro-health-hack',
          demo: 'https://medecro-health-hack.vercel.app/',
        },
        {
          id: 3,
          title: 'AI Chatbot with Gemini API',
          description:
            'Conversational chatbot powered by Gemini API for real-time interactions and responses.',
          emoji: '🤖',
          category: 'ai',
          technologies: ['Node.js', 'Express', 'React', 'Gemini API'],
          status: 'completed',
          github: 'https://github.com/eabhi-me/mini-chatbot',
          demo: 'https://mini-chatbot-8gul.onrender.com/',
        },
        {
          id: 4,
          title: 'Object Detection using YOLO and OpenCV',
          description:
            'Real-time object detection system for automation and surveillance using YOLOv8 and OpenCV.',
          emoji: '🎯',
          category: 'ml',
          technologies: ['Python', 'YOLOv8', 'OpenCV'],
          status: 'completed',
          github: 'https://github.com/eabhi-me/ai-ml-block/tree/main/object-detection',
          demo: '#',
        },
        {
          id: 5,
          title: 'Unmanned Aerial Vehicle (UAV) – IoT',
          description:
            'Autonomous UAV for smart agriculture with LIDAR, ML-based object detection, and ROS-based control.',
          emoji: '🚁',
          category: 'iot',
          technologies: ['Linux (ROS)', 'Python', 'LIDAR', 'Machine Learning'],
          status: 'ongoing',
          github: '#',
          demo: '#',
        },
        {
          id: 6,
          title: 'Multi-User To-Do App',
          description:
            'Task management web app allowing users to create, update, and delete tasks with a clean UI.',
          emoji: '📝',
          category: 'web',
          technologies: ['Python', 'Flask', 'Jinja2', 'Bootstrap'],
          status: 'completed',
          github: 'https://github.com/eabhi-me/todo-app',
          demo: 'https://todo-app-u4k5.onrender.com/',
        },
        {
          id: 7,
          title: 'Line Following Robot Car',
          description:
            'A robotic car that follows a predefined path using IR sensors and microcontroller logic.',
          emoji: '🚗',
          category: 'iot',
          technologies: ['Arduino', 'C++', 'IR Sensors', 'L293D'],
          status: 'completed',
          github: '#',
          demo: '#',
        },
        {
          id: 8,
          title: 'Audio Transmission via RF Modules',
          description:
            'Wireless audio transmission system using RF transmitter and receiver for short-range communication.',
          emoji: '📡',
          category: 'iot',
          technologies: ['Arduino', 'RF Modules', 'LM386', 'Analog Signal Processing'],
          status: 'completed',
          github: '#',
          demo: '#',
        },
        {
          id: 9,
          title: 'SMS Spam Classifier',
          description:
            'Machine learning model to classify SMS messages as spam or not using text vectorization and Naive Bayes.',
          emoji: '📨',
          category: 'ml',
          technologies: ['Python', 'scikit-learn', 'TfidfVectorizer', 'MultinomialNB'],
          status: 'completed',
          github: 'https://github.com/eabhi-me/sms-spam-classifier',
          demo: '#',
        },
      ],
    }
  },
  computed: {
    filteredProjects() {
      if (this.activeFilter === 'all') {
        return this.projects
      }
      return this.projects.filter((project) => project.category === this.activeFilter)
    },
  },
  methods: {
    setFilter(filter) {
      this.activeFilter = filter
    },
  },
}
</script>

<style scoped>
.projects {
  padding-top: 80px;
  width: 100%;
  overflow-x: hidden;
}

/* Hero Section */
.projects-hero {
  padding: 6rem 0;

  color: rgb(5, 5, 5);
  text-align: center;
  width: 100%;
  min-height: 60vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.projects-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 20"><defs><radialGradient id="a" cx="50%" cy="50%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><circle cx="10" cy="10" r="10" fill="url(%23a)"/><circle cx="90" cy="10" r="10" fill="url(%23a)"/></svg>')
    repeat;
  opacity: 0.3;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 3rem;
  position: relative;
  z-index: 1;
}

.hero-subtitle {
  font-size: 1.4rem;
  font-weight: 300;
  opacity: 0.95;
  margin-top: 1.5rem;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 1.5rem;
}

.section-subtitle {
  font-size: 3rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 4rem;
  color: #2c3e50;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Featured Projects */
.featured-projects {
  padding: 7rem 0;
  background: white;
  width: 100%;
}

.featured-container {
  width: 100%;
  max-width: 1600px;
  margin: 0 auto;
  padding: 0 3rem;
}

.featured-grid {
  display: flex;
  flex-direction: column;
  gap: 8rem;
  width: 100%;
}

.featured-project {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: center;
  width: 100%;
  padding: 2rem 0;
}

.featured-project.reverse {
  direction: rtl;
}

.featured-project.reverse > * {
  direction: ltr;
}

.project-image {
  position: relative;
  height: 400px;
  width: 100%;
  border-radius: 25px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  cursor: pointer;
  box-shadow: 0 20px 60px rgba(102, 126, 234, 0.25);
  transition: all 0.4s ease;
}

.project-image:hover {
  transform: translateY(-15px) scale(1.02);
  box-shadow: 0 30px 80px rgba(102, 126, 234, 0.35);
}

.project-placeholder {
  font-size: 10rem;
  color: rgba(255, 255, 255, 0.95);
  text-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-image:hover .project-overlay {
  opacity: 1;
}

.project-links {
  display: flex;
  gap: 1rem;
}

.project-link {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 500;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.project-link:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
}

.project-content {
  padding: 3rem 0;
  width: 100%;
}

.project-content h3 {
  font-size: 2.8rem;
  font-weight: 800;
  color: #2c3e50;
  margin-bottom: 2rem;
  line-height: 1.2;
}

.project-content p {
  font-size: 1.3rem;
  line-height: 1.9;
  color: #5a6c7d;
  margin-bottom: 2.5rem;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-bottom: 2rem;
}

.tech-tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  font-size: 1rem;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
  transition: all 0.3s ease;
}

.tech-tag:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.project-features {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 15px;
  border-left: 4px solid #667eea;
}

.project-features h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.project-features ul {
  list-style: none;
  padding: 0;
}

.project-features li {
  padding: 0.75rem 0;
  color: #5a6c7d;
  position: relative;
  padding-left: 2rem;
  font-size: 1.05rem;
  line-height: 1.6;
  border-bottom: 1px solid #e9ecef;
}

.project-features li:last-child {
  border-bottom: none;
}

.project-features li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #667eea;
  font-weight: bold;
  font-size: 1.2rem;
  width: 1.5rem;
  height: 1.5rem;
  background: rgba(102, 126, 234, 0.1);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* All Projects */
.all-projects {
  padding: 8rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  width: 100%;
}

.all-projects-container {
  width: 100%;
  max-width: 1800px;
  margin: 0 auto;
  padding: 0 3rem;
}

.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 5rem;
  flex-wrap: wrap;
  width: 100%;
}

.filter-tab {
  background: white;
  color: #667eea;
  border: 3px solid #667eea;
  padding: 1.2rem 2.5rem;
  border-radius: 35px;
  cursor: pointer;
  font-weight: 700;
  font-size: 1.1rem;
  transition: all 0.4s ease;
  box-shadow: 0 6px 20px rgba(102, 126, 234, 0.15);
  min-width: 140px;
  text-align: center;
}

.filter-tab.active,
.filter-tab:hover {
  background: #667eea;
  color: white;
  transform: translateY(-5px);
  box-shadow: 0 12px 35px rgba(102, 126, 234, 0.4);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 3rem;
  width: 100%;
}

.project-card {
  background: white;
  border-radius: 25px;
  overflow: hidden;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: all 0.4s ease;
  position: relative;
  height: 100%;
}

.project-card:hover {
  transform: translateY(-20px);
  box-shadow: 0 35px 70px rgba(0, 0, 0, 0.2);
}

.card-image {
  position: relative;
  height: 250px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.image-placeholder {
  font-size: 5rem;
  color: rgba(255, 255, 255, 0.95);
  text-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.card-image:hover .card-overlay {
  opacity: 1;
}

.overlay-content {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.overlay-link {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  text-decoration: none;
  font-size: 0.9rem;
  text-align: center;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.overlay-link:hover {
  background: rgba(255, 255, 255, 0.3);
}

.card-content {
  padding: 2.5rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.card-content h3 {
  font-size: 1.6rem;
  font-weight: 800;
  color: #2c3e50;
  margin-bottom: 1.2rem;
  line-height: 1.3;
}

.card-content p {
  color: #5a6c7d;
  line-height: 1.8;
  margin-bottom: 1.8rem;
  font-size: 1.05rem;
  flex-grow: 1;
}

.card-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tech-badge {
  background: linear-gradient(135deg, #e9ecef 0%, #f8f9fa 100%);
  color: #495057;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  border: 1px solid #dee2e6;
  transition: all 0.3s ease;
}

.tech-badge:hover {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  transform: translateY(-2px);
}

.card-status {
  text-align: right;
}

.status-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 500;
  text-transform: uppercase;
}

.status-badge.completed {
  background: #d4edda;
  color: #155724;
}

.status-badge.in-progress {
  background: #fff3cd;
  color: #856404;
}

.status-badge.planning {
  background: #d1ecf1;
  color: #0c5460;
}

/* Call to Action */
.projects-cta {
  padding: 6rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-align: center;
}

.cta-content {
  max-width: 700px;
  margin: 0 auto;
  padding: 0 2rem;
}

.cta-content h2 {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  margin-bottom: 1.5rem;
}

.cta-content p {
  font-size: 1.3rem;
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.8;
  margin-bottom: 2.5rem;
}

.cta-content .btn-primary {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 30px;
  transition: all 0.3s ease;
}

.cta-content .btn-primary:hover {
  background: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

/* Responsive Design */
@media (max-width: 1200px) {
  .featured-grid {
    max-width: 1000px;
  }

  .projects-grid {
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2rem;
    padding: 0 1.5rem;
  }
}

@media (max-width: 768px) {
  .featured-project {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 3rem;
  }

  .featured-project.reverse {
    direction: ltr;
  }

  .project-image {
    height: 280px;
    max-width: 500px;
    margin: 0 auto;
  }

  .project-placeholder {
    font-size: 6rem;
  }

  .project-content {
    max-width: 600px;
    margin: 0 auto;
  }

  .project-content h3 {
    font-size: 1.8rem;
  }

  .projects-grid {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    padding: 0 1rem;
  }

  .filter-tabs {
    gap: 1rem;
    padding: 0 1rem;
  }

  .filter-tab {
    flex: 1;
    min-width: 0;
    padding: 0.75rem 1rem;
    font-size: 0.95rem;
  }

  .all-projects {
    padding: 4rem 0;
  }

  .featured-projects {
    padding: 4rem 0;
  }
}

@media (max-width: 480px) {
  .projects {
    padding-top: 70px;
  }

  .projects-hero {
    padding: 2rem 0;
  }

  .hero-subtitle {
    font-size: 1.1rem;
  }

  .featured-projects,
  .all-projects,
  .projects-cta {
    padding: 3rem 0;
  }

  .featured-grid {
    gap: 3rem;
  }

  .project-image {
    height: 220px;
  }

  .project-placeholder {
    font-size: 4rem;
  }

  .project-content h3 {
    font-size: 1.5rem;
  }

  .project-content p {
    font-size: 1.1rem;
  }

  .tech-tag {
    padding: 0.5rem 1rem;
    font-size: 0.9rem;
  }

  .project-features {
    padding: 1.5rem;
  }

  .project-features li {
    font-size: 1rem;
    padding: 0.5rem 0;
  }

  .projects-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    padding: 0 0.5rem;
  }

  .card-content {
    padding: 1.5rem;
  }

  .card-content h3 {
    font-size: 1.2rem;
  }

  .filter-tabs {
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    max-width: 300px;
  }

  .filter-tab {
    width: 100%;
    padding: 0.75rem 1.5rem;
  }

  .section-subtitle {
    font-size: 1.8rem;
  }
}

@media (max-width: 360px) {
  .projects-grid {
    padding: 0 0.25rem;
  }

  .card-content {
    padding: 1.25rem;
  }

  .project-features {
    padding: 1.25rem;
  }

  .filter-tabs {
    padding: 0 0.5rem;
  }
}
</style>
