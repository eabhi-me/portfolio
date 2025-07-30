<template>
  <div class="skills">
    <!-- Hero Section -->
    <section class="skills-hero">
      <div class="container">
        <div class="hero-content">
          <h1 class="section-title">Technical Skills</h1>
          <p class="hero-subtitle">
            A comprehensive overview of my technical expertise and proficiency levels
          </p>
        </div>
      </div>
    </section>

    <!-- Skills Overview -->
    <section class="skills-overview">
      <div class="container">
        <div class="overview-grid">
          <div class="overview-item">
            <div class="overview-icon">💻</div>
            <h3>Programming Languages</h3>
            <p>
              Proficient in C++, Python, JavaScript, and C with strong problem-solving foundations
            </p>
            <span class="skill-count">4+ Languages</span>
          </div>

          <div class="overview-item">
            <div class="overview-icon">🚀</div>
            <h3>Frameworks & Libraries</h3>
            <p>
              Experience with Flask, Vue.js, React, Node.js, TensorFlow, and machine learning tools
            </p>
            <span class="skill-count">10+ Technologies</span>
          </div>

          <div class="overview-item">
            <div class="overview-icon">🛠️</div>
            <h3>Tools & Platforms</h3>
            <p>
              Proficient with Git, Linux, Google Cloud, Bootstrap, Tailwind CSS, and development
              tools
            </p>
            <span class="skill-count">15+ Tools</span>
          </div>

          <div class="overview-item">
            <div class="overview-icon">📊</div>
            <h3>Databases & Analytics</h3>
            <p>Experience with PostgreSQL, MongoDB, SQLite, Redis, and data analysis libraries</p>
            <span class="skill-count">6+ Systems</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Technical Skills -->
    <section class="technical-skills">
      <div class="container">
        <h2 class="section-subtitle">Technical Proficiency</h2>

        <div class="skills-tabs">
          <button
            v-for="category in skillCategories"
            :key="category.id"
            class="skill-tab"
            :class="{ active: activeCategory === category.id }"
            @click="setActiveCategory(category.id)"
          >
            <span class="tab-icon">{{ category.icon }}</span>
            {{ category.name }}
          </button>
        </div>

        <div class="skills-content">
          <div
            v-for="category in skillCategories"
            :key="category.id"
            class="skill-category"
            :class="{ active: activeCategory === category.id }"
          >
            <div class="category-header">
              <h3>{{ category.name }}</h3>
              <p>{{ category.description }}</p>
            </div>

            <div class="skills-grid">
              <div v-for="skill in category.skills" :key="skill.name" class="skill-item">
                <div class="skill-header">
                  <div class="skill-info">
                    <span class="skill-name">{{ skill.name }}</span>
                    <span class="skill-level">{{ skill.level }}%</span>
                  </div>
                  <div class="skill-experience">{{ skill.experience }}</div>
                </div>

                <div class="skill-bar">
                  <div
                    class="skill-progress"
                    :style="{ width: skill.level + '%' }"
                    :class="getSkillClass(skill.level)"
                  ></div>
                </div>

                <div class="skill-description">
                  {{ skill.description }}
                </div>

                <div v-if="skill.projects" class="skill-projects">
                  <span class="projects-label">Used in:</span>
                  <div class="project-tags">
                    <span v-for="project in skill.projects" :key="project" class="project-tag">
                      {{ project }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Certifications & Learning -->
    <section class="certifications">
      <div class="container">
        <h2 class="section-subtitle">Certifications & Learning</h2>

        <div class="cert-grid">
          <div class="cert-item">
            <div class="cert-icon">🏆</div>
            <h3>Competition Achievements</h3>
            <ul>
              <li>2nd Prize in Electronica, TechFest SLIET 2024</li>
              <li>IoT-based voice-controlled RC car project</li>
              <li>Academic Excellence - CGPA: 9.18</li>
            </ul>
          </div>

          <div class="cert-item">
            <div class="cert-icon">📜</div>
            <h3>Professional Certifications</h3>
            <ul>
              <li>Postman Student Expert - API Testing</li>
              <li>GSSoC 2024 Contributor Certificate</li>
              <li>Open Source Contribution Recognition</li>
            </ul>
          </div>

          <div class="cert-item">
            <div class="cert-icon">📚</div>
            <h3>Continuous Learning</h3>
            <ul>
              <li>Machine Learning Specialization</li>
              <li>DevOps and CI/CD Practices</li>
              <li>Modern JavaScript Frameworks</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Development Timeline -->
    <section class="skills-timeline">
      <div class="container">
        <h2 class="section-subtitle">Learning Journey</h2>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
              <h3>Foundation Building</h3>
              <span class="timeline-period">2022-2023</span>
              <p>
                Started with programming fundamentals, data structures, and core computer science
                concepts
              </p>
              <div class="timeline-skills">
                <span class="timeline-skill">C++</span>
                <span class="timeline-skill">C</span>
                <span class="timeline-skill">Python</span>
                <span class="timeline-skill">DSA</span>
              </div>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
              <h3>Web Development Mastery</h3>
              <span class="timeline-period">2023-2024</span>
              <p>
                Expanded into full-stack development, modern frameworks, and database management
              </p>
              <div class="timeline-skills">
                <span class="timeline-skill">Flask</span>
                <span class="timeline-skill">JavaScript</span>
                <span class="timeline-skill">Vue.js</span>
                <span class="timeline-skill">PostgreSQL</span>
              </div>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
              <h3>Advanced Technologies & AI</h3>
              <span class="timeline-period">2024-Present</span>
              <p>
                Specialized in machine learning, cloud technologies, and modern development
                practices
              </p>
              <div class="timeline-skills">
                <span class="timeline-skill">TensorFlow</span>
                <span class="timeline-skill">React</span>
                <span class="timeline-skill">Google Cloud</span>
                <span class="timeline-skill">FastAPI</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'SkillsView',
  data() {
    return {
      activeCategory: 'programming',
      skillCategories: [
        {
          id: 'programming',
          name: 'Programming Languages',
          icon: '💻',
          description: 'Core programming languages with varying levels of expertise',
          skills: [
            {
              name: 'Python',
              level: 90,
              experience: '2+ years',
              description:
                'Expert in Flask, FastAPI, machine learning libraries, and data analysis',
              projects: ['Quiz-Master WebApp', 'Object Detection YOLO', 'UAV System'],
            },
            {
              name: 'JavaScript',
              level: 85,
              experience: '2+ years',
              description: 'Proficient in ES6+, async programming, Vue.js, React, and Node.js',
              projects: ['Hospital Management', 'AI Chatbot', 'Web Platforms'],
            },
            {
              name: 'C++',
              level: 80,
              experience: '2+ years',
              description:
                'Fundamental programming, data structures, algorithms, and competitive programming',
              projects: ['DSA Challenges', 'System Programming', 'IoT RC Car Project'],
            },
            {
              name: 'C',
              level: 75,
              experience: '2+ years',
              description: 'System programming, embedded systems, and low-level programming',
              projects: ['System Tools', 'Embedded Projects', 'Algorithm Implementation'],
            },
          ],
        },
        {
          id: 'frontend',
          name: 'Frontend Development',
          icon: '🎨',
          description: 'Modern frontend frameworks and libraries for creating user interfaces',
          skills: [
            {
              name: 'Vue.js',
              level: 90,
              experience: '2+ years',
              description: 'Advanced component development, state management, and routing',
              projects: ['Portfolio Website', 'Quiz-Master Frontend', 'Web Platforms'],
            },
            {
              name: 'React',
              level: 85,
              experience: '1+ years',
              description: 'Hooks, context API, and modern React patterns',
              projects: ['Hospital Management', 'AI Chatbot Interface', 'Admin Portals'],
            },
            {
              name: 'Bootstrap',
              level: 90,
              experience: '2+ years',
              description: 'Semantic markup, modern CSS features, and responsive design',
              projects: ['All Web Projects', 'Landing Pages', 'UI Components'],
            },
            {
              name: 'Sass/SCSS',
              level: 80,
              experience: '2+ years',
              description: 'Advanced CSS preprocessing and maintainable stylesheets',
              projects: ['Component Libraries', 'Theme Systems'],
            },
            {
              name: 'Bootstrap',
              level: 85,
              experience: '2+ years',
              description: 'Rapid prototyping and responsive grid systems',
              projects: ['Admin Dashboards', 'Landing Pages'],
            },
            {
              name: 'Tailwind CSS',
              level: 85,
              experience: '1+ years',
              description: 'Utility-first CSS framework for modern, responsive designs',
              projects: ['Hospital Management UI', 'Modern Web Apps', 'Component Systems'],
            },
          ],
        },
        {
          id: 'backend',
          name: 'Backend Development',
          icon: '⚙️',
          description: 'Server-side technologies and database management',
          skills: [
            {
              name: 'Flask',
              level: 90,
              experience: '2+ years',
              description: 'Python web framework, RESTful APIs, and database integration',
              projects: ['Quiz-Master WebApp', 'API Development', 'Web Services'],
            },
            {
              name: 'Node.js',
              level: 85,
              experience: '1+ years',
              description: 'Server-side JavaScript, Express.js, and real-time applications',
              projects: ['Hospital Management', 'AI Chatbot Backend', 'API Services'],
            },
            {
              name: 'FastAPI',
              level: 80,
              experience: '1+ years',
              description: 'Modern Python framework for building APIs with automatic documentation',
              projects: ['ML Model APIs', 'High-performance backends', 'Microservices'],
            },
            {
              name: 'PostgreSQL',
              level: 85,
              experience: '2+ years',
              description: 'Advanced SQL queries, database design, and performance optimization',
              projects: ['Quiz-Master Database', 'User Management', 'Data Analytics'],
            },
            {
              name: 'MongoDB',
              level: 80,
              experience: '1+ years',
              description: 'NoSQL database design, aggregation, and document-based storage',
              projects: ['Hospital Management', 'Content Management', 'User Systems'],
            },
            {
              name: 'SQLite',
              level: 85,
              experience: '2+ years',
              description: 'Lightweight database for applications and local storage',
              projects: ['Quiz-Master WebApp', 'Desktop Apps', 'Mobile Storage'],
            },
            {
              name: 'Redis',
              level: 70,
              experience: '1+ years',
              description: 'In-memory data structure store for caching and sessions',
              projects: ['Web Applications', 'Performance Optimization', 'Session Management'],
            },
          ],
        },
        {
          id: 'ml',
          name: 'Machine Learning & AI',
          icon: '🤖',
          description: 'Machine learning frameworks and artificial intelligence tools',
          skills: [
            {
              name: 'TensorFlow',
              level: 80,
              experience: '1+ years',
              description: 'Deep learning models, neural networks, and model deployment',
              projects: ['Object Detection YOLO', 'Image Classification', 'ML Models'],
            },
            {
              name: 'Keras',
              level: 75,
              experience: '1+ years',
              description: 'High-level neural networks API and model building',
              projects: ['Deep Learning Projects', 'Neural Networks', 'Model Training'],
            },
            {
              name: 'Scikit-learn',
              level: 80,
              experience: '1+ years',
              description: 'Machine learning algorithms and data preprocessing',
              projects: ['Data Analysis', 'Classification Models', 'Predictive Analytics'],
            },
            {
              name: 'OpenCV',
              level: 75,
              experience: '1+ years',
              description: 'Computer vision, image processing, and real-time detection',
              projects: ['Object Detection System', 'Image Processing', 'Computer Vision'],
            },
          ],
        },
        {
          id: 'mobile',
          name: 'Development Tools',
          icon: '📱',
          description: 'Development tools, libraries, and data analysis frameworks',
          skills: [
            {
              name: 'NumPy',
              level: 85,
              experience: '2+ years',
              description: 'Numerical computing and array operations for data science',
              projects: ['Data Analysis', 'Machine Learning', 'Scientific Computing'],
            },
            {
              name: 'Pandas',
              level: 80,
              experience: '2+ years',
              description: 'Data manipulation and analysis library for Python',
              projects: ['Data Processing', 'Analytics Dashboard', 'Data Cleaning'],
            },
            {
              name: 'Matplotlib',
              level: 75,
              experience: '1+ years',
              description: 'Data visualization and plotting library for Python',
              projects: ['Data Visualization', 'Analytics Reports', 'Scientific Plots'],
            },
            {
              name: 'Seaborn',
              level: 75,
              experience: '1+ years',
              description: 'Statistical data visualization built on matplotlib',
              projects: ['Data Analysis', 'Statistical Plots', 'Exploratory Data Analysis'],
            },
            {
              name: 'Celery',
              level: 70,
              experience: '1+ years',
              description: 'Distributed task queue for Python applications',
              projects: ['Background Tasks', 'Asynchronous Processing', 'Job Scheduling'],
            },
          ],
        },
        {
          id: 'tools',
          name: 'Tools & Cloud',
          icon: '🛠️',
          description: 'Development tools, version control, and cloud platforms',
          skills: [
            {
              name: 'Git',
              level: 90,
              experience: '2+ years',
              description: 'Version control, branching strategies, and collaborative development',
              projects: ['All Development Projects', 'Team Collaboration', 'Open Source'],
            },
            {
              name: 'Linux (Ubuntu)',
              level: 85,
              experience: '2+ years',
              description: 'System administration, shell scripting, and server management',
              projects: ['UAV System', 'Server Deployment', 'Development Environment'],
            },
            {
              name: 'Google Cloud Console',
              level: 80,
              experience: '1+ years',
              description: 'Cloud services, deployment, and infrastructure management',
              projects: ['Web Hosting', 'API Deployment', 'Cloud Storage'],
            },
            {
              name: 'Render',
              level: 75,
              experience: '1+ years',
              description: 'Cloud platform for deploying web applications and APIs',
              projects: ['Quiz-Master Deployment', 'Web Services', 'API Hosting'],
            },
          ],
        },
      ],
    }
  },
  methods: {
    setActiveCategory(categoryId) {
      this.activeCategory = categoryId
    },
    getSkillClass(level) {
      if (level >= 80) return 'expert'
      if (level >= 60) return 'intermediate'
      return 'beginner'
    },
  },
}
</script>

<style scoped>
.skills {
  padding-top: 80px;
}

/* Hero Section */
.skills-hero {
  padding: 4rem 0;
  color: black;
  text-align: center;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  font-weight: 300;
  opacity: 0.9;
  margin-top: 1rem;
}

.section-subtitle {
  font-size: 2rem;
  font-weight: 600;
  text-align: center;
  margin-bottom: 3rem;
  color: #2c3e50;
}

/* Skills Overview */
.skills-overview {
  padding: 5rem 0;
  background: white;
}

.overview-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.overview-item {
  text-align: center;
  padding: 2rem;
  border-radius: 15px;
  background: #f8f9fa;
  border: 2px solid transparent;
  transition: all 0.3s ease;
}

.overview-item:hover {
  border-color: #667eea;
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.overview-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.overview-item h3 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.overview-item p {
  color: #5a6c7d;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.skill-count {
  display: inline-block;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 500;
  font-size: 0.9rem;
}

/* Technical Skills */
.technical-skills {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.skills-tabs {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 3rem;
  flex-wrap: wrap;
}

.skill-tab {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
  padding: 1rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.skill-tab.active,
.skill-tab:hover {
  background: #667eea;
  color: white;
}

.tab-icon {
  font-size: 1.2rem;
}

.skills-content {
  position: relative;
}

.skill-category {
  display: none;
}

.skill-category.active {
  display: block;
}

.category-header {
  text-align: center;
  margin-bottom: 3rem;
}

.category-header h3 {
  font-size: 1.8rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.category-header p {
  color: #5a6c7d;
  font-size: 1.1rem;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
}

.skill-item {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.skill-item:hover {
  transform: translateY(-5px);
}

.skill-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.skill-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.skill-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
}

.skill-level {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.85rem;
  font-weight: 500;
}

.skill-experience {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-weight: 500;
}

.skill-bar {
  height: 8px;
  background: #e9ecef;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 1rem;
}

.skill-progress {
  height: 100%;
  border-radius: 10px;
  transition: width 1s ease;
}

.skill-progress.expert {
  background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
}

.skill-progress.intermediate {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.skill-progress.beginner {
  background: linear-gradient(135deg, #ffc107 0%, #fd7e14 100%);
}

.skill-description {
  color: #5a6c7d;
  line-height: 1.6;
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.skill-projects {
  border-top: 1px solid #e9ecef;
  padding-top: 1rem;
}

.projects-label {
  color: #7f8c8d;
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 0.5rem;
  display: block;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.project-tag {
  background: #e9ecef;
  color: #495057;
  padding: 0.25rem 0.5rem;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 500;
}

/* Certifications */
.certifications {
  padding: 5rem 0;
  background: white;
}

.cert-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.cert-item {
  text-align: center;
  padding: 2rem;
  border-radius: 15px;
  background: #f8f9fa;
  transition: transform 0.3s ease;
}

.cert-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.cert-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.cert-item h3 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.cert-item ul {
  list-style: none;
  padding: 0;
  text-align: left;
}

.cert-item li {
  padding: 0.5rem 0;
  color: #5a6c7d;
  position: relative;
  padding-left: 1.5rem;
}

.cert-item li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #667eea;
  font-weight: bold;
}

/* Skills Timeline */
.skills-timeline {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.timeline {
  max-width: 1200px;
  margin: 3rem auto 0;
  position: relative;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 30px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.timeline-item {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 80px;
}

.timeline-marker {
  position: absolute;
  left: 20px;
  top: 0;
  width: 20px;
  height: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 50%;
  border: 4px solid white;
  box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.2);
}

.timeline-content {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.timeline-content h3 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.timeline-period {
  color: #667eea;
  font-weight: 500;
  font-size: 0.9rem;
  margin-bottom: 1rem;
  display: block;
}

.timeline-content p {
  color: #5a6c7d;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.timeline-skills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.timeline-skill {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.85rem;
  font-weight: 500;
}

/* Responsive Design */
@media (max-width: 768px) {
  .skills-tabs {
    flex-direction: column;
    align-items: center;
  }

  .skill-tab {
    width: 100%;
    max-width: 300px;
    justify-content: center;
  }

  .skills-grid {
    grid-template-columns: 1fr;
  }

  .timeline {
    margin-left: 1rem;
  }

  .timeline::before {
    left: 15px;
  }

  .timeline-marker {
    left: 5px;
  }

  .timeline-item {
    padding-left: 50px;
  }
}

@media (max-width: 480px) {
  .skills {
    padding-top: 70px;
  }

  .skills-hero {
    padding: 2rem 0;
  }

  .technical-skills,
  .skills-overview,
  .certifications,
  .skills-timeline {
    padding: 3rem 0;
  }

  .skill-item {
    padding: 1.5rem;
  }

  .skill-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }
}
</style>
