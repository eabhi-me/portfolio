<template>
  <div class="resume">
    <!-- Header Section -->
    <section class="resume-header">
      <div class="container">
        <h1 class="section-title">Resume</h1>
        <p class="section-subtitle">Download my resume or view the LaTeX source code</p>
        <div class="resume-actions">
          <button @click="downloadResume" class="btn-primary" :disabled="isLoading">
            📄 Download LaTeX File
          </button>
          <button @click="toggleLatex" class="btn-secondary" :disabled="isLoading">
            {{ showLatex ? '👁️ Hide LaTeX' : '📝 Show LaTeX Code' }}
          </button>
        </div>
      </div>
    </section>

    <!-- LaTeX Code Section -->
    <section v-if="showLatex" class="latex-section">
      <div class="container">
        <div class="latex-container">
          <div class="latex-header">
            <h3>LaTeX Source Code</h3>
            <button
              @click="copyLatex"
              class="copy-btn"
              :class="{ copied: isCopied }"
              :disabled="isLoading"
            >
              {{ isCopied ? '✅ Copied!' : '📋 Copy Code' }}
            </button>
          </div>

          <!-- Loading State -->
          <div v-if="isLoading" class="latex-loading">
            <div class="loading-spinner"></div>
            <p>Loading LaTeX file...</p>
          </div>

          <!-- Error State -->
          <div v-else-if="loadError" class="latex-error">
            <p>⚠️ {{ loadError }}</p>
            <button @click="loadLatexFile" class="retry-btn">🔄 Retry</button>
          </div>

          <!-- LaTeX Code -->
          <pre v-else><code class="latex-code">{{ latexCode }}</code></pre>
        </div>
      </div>
    </section>

    <!-- Resume Preview Section -->
    <section class="resume-preview">
      <div class="container">
        <h2 class="section-title">Resume Preview</h2>
        <div class="preview-container">
          <div class="resume-document">
            <!-- Header -->
            <div class="resume-doc-header">
              <h1>Abhishek Yadav</h1>
              <div class="contact-info">
                <span>📧 abhishek@example.com</span>
                <span>📱 +91-XXXXX-XXXXX</span>
                <span>🌐 portfolio.abhishek.dev</span>
                <span>💼 LinkedIn: /in/abhishek-yadav</span>
              </div>
            </div>

            <!-- Education -->
            <div class="resume-section">
              <h2>Education</h2>
              <div class="resume-item">
                <div class="item-header">
                  <strong>BS in Data Science and Applications</strong>
                  <span class="date">2022 - 2026</span>
                </div>
                <div class="item-details">IIT Madras</div>
                <ul>
                  <li>Focus on statistical analysis, machine learning, and data visualization</li>
                  <li>
                    Coursework: Statistics, Data Analytics, Python Programming, Machine Learning
                  </li>
                </ul>
              </div>
              <div class="resume-item">
                <div class="item-header">
                  <strong>B.Tech in Computer Science Engineering</strong>
                  <span class="date">2023 - 2027</span>
                </div>
                <div class="item-details">CGPA: 9.18</div>
                <ul>
                  <li>Specialization in software development and AI/ML applications</li>
                  <li>
                    Coursework: Data Structures, Machine Learning, Web Development, Computer Vision
                  </li>
                </ul>
              </div>
            </div>

            <!-- Experience -->
            <div class="resume-section">
              <h2>Professional Experience</h2>
              <div class="resume-item">
                <div class="item-header">
                  <strong>Software Developer</strong>
                  <span class="date">Sept 2024 - Present</span>
                </div>
                <div class="item-details">BDCI</div>
                <ul>
                  <li>
                    Developed and maintained scalable web applications using modern frameworks
                  </li>
                  <li>Implemented AI-powered solutions and database-driven systems</li>
                  <li>
                    Collaborated with cross-functional teams to deliver production-ready software
                  </li>
                </ul>
              </div>
              <div class="resume-item">
                <div class="item-header">
                  <strong>Web Development Manager</strong>
                  <span class="date">Aug 2023 - Present</span>
                </div>
                <div class="item-details">BDCI (Part-Time)</div>
                <ul>
                  <li>Designed and deployed websites using GoDaddy hosting</li>
                  <li>Increased enrollment by 40% through performance and UX improvements</li>
                  <li>Led web development initiatives and optimized user experience</li>
                </ul>
              </div>
            </div>

            <!-- Projects -->
            <div class="resume-section">
              <h2>Key Projects</h2>
              <div class="resume-item">
                <div class="item-header">
                  <strong>Quiz-Master WebApp</strong>
                  <span class="tech-stack">Python, Flask, SQLite, Bootstrap</span>
                </div>
                <ul>
                  <li>
                    Multi-user quiz platform with real-time scoring and student/teacher portals
                  </li>
                  <li>Implemented secure user authentication and role-based access control</li>
                </ul>
              </div>
              <div class="resume-item">
                <div class="item-header">
                  <strong>Hospital Management System</strong>
                  <span class="tech-stack">Node.js, React, Express, Tailwind CSS</span>
                </div>
                <ul>
                  <li>
                    Complete admin, patient, and doctor portal for scheduling and profile management
                  </li>
                  <li>Integrated appointment booking system with automated notifications</li>
                </ul>
              </div>
              <div class="resume-item">
                <div class="item-header">
                  <strong>AI Chatbot with Gemini API</strong>
                  <span class="tech-stack">Node.js, React, Gemini API</span>
                </div>
                <ul>
                  <li>AI-powered chatbot for real-time conversations using Google's Gemini API</li>
                  <li>Implemented natural language processing for improved user interactions</li>
                </ul>
              </div>
            </div>

            <!-- Skills -->
            <div class="resume-section">
              <h2>Technical Skills</h2>
              <div class="skills-grid">
                <div class="skill-category">
                  <strong>Programming Languages:</strong>
                  <span>Python, JavaScript, Java, C++</span>
                </div>
                <div class="skill-category">
                  <strong>Web Technologies:</strong>
                  <span>React, Vue.js, Flask, Node.js, Express</span>
                </div>
                <div class="skill-category">
                  <strong>AI & Data Science:</strong>
                  <span>TensorFlow, OpenCV, Dialogflow, Computer Vision</span>
                </div>
                <div class="skill-category">
                  <strong>Tools & Technologies:</strong>
                  <span>Git, Linux, Google Cloud, VS Code, PostgreSQL, MongoDB</span>
                </div>
              </div>
            </div>

            <!-- Achievements -->
            <div class="resume-section">
              <h2>Achievements & Certifications</h2>
              <ul class="achievements-list">
                <li>
                  <strong>GSSoC 2024 Contributor</strong> - Contributed to open-source projects
                </li>
                <li>
                  <strong>2nd Prize in TechFest SLIET 2024</strong> - IoT-based voice-controlled RC
                  car project
                </li>
                <li>
                  <strong>Postman Student Expert</strong> - API testing and automation expertise
                </li>
                <li><strong>Academic Excellence</strong> - Maintaining 9.18 CGPA in B.Tech CSE</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ResumeView',
  data() {
    return {
      showLatex: false,
      isCopied: false,
      latexCode: '',
      isLoading: true,
      loadError: null,
    }
  },
  async mounted() {
    await this.loadLatexFile()
  },
  methods: {
    async loadLatexFile() {
      try {
        this.isLoading = true
        this.loadError = null

        // Import the LaTeX file as a text file
        const response = await fetch(new URL('@/assets/resume.latex', import.meta.url))

        if (!response.ok) {
          throw new Error(`Failed to load resume.latex: ${response.status}`)
        }

        this.latexCode = await response.text()
      } catch (error) {
        console.error('Error loading LaTeX file:', error)
        this.loadError = 'Failed to load LaTeX file'
        // Fallback to basic LaTeX template
        this.latexCode = `% LaTeX resume file could not be loaded
% Please ensure resume.latex exists in src/assets/

\\documentclass[letterpaper,11pt]{article}
\\begin{document}
Error loading resume.latex file from assets directory.
\\end{document}`
      } finally {
        this.isLoading = false
      }
    },
    toggleLatex() {
      this.showLatex = !this.showLatex
    },
    async copyLatex() {
      try {
        await navigator.clipboard.writeText(this.latexCode)
        this.isCopied = true
        setTimeout(() => {
          this.isCopied = false
        }, 2000)
      } catch (err) {
        console.error('Failed to copy text: ', err)
      }
    },
    downloadResume() {
      // Create a blob with the LaTeX content
      const blob = new Blob([this.latexCode], { type: 'text/plain' })
      const url = window.URL.createObjectURL(blob)

      // Create a temporary link element and trigger download
      const link = document.createElement('a')
      link.href = url
      link.download = 'resume.tex'
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
      window.URL.revokeObjectURL(url)
    },
  },
}
</script>

<style scoped>
.resume {
  padding-top: 80px;
}

/* Header Section */
.resume-header {
  padding: 4rem 0;

  color: black;
  text-align: center;
}

.resume-header .section-title {
  color: black;
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.resume-header .section-subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  margin-bottom: 2rem;
}

.resume-actions {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* LaTeX Section */
.latex-section {
  padding: 4rem 0;
  background: #f8f9fa;
}

.latex-container {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.latex-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  background: #2c3e50;
  color: black;
}

.latex-header h3 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 600;
}

.copy-btn {
  background: #667eea;
  color: black;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
}

.copy-btn:hover {
  background: #5a6fd8;
  transform: translateY(-2px);
}

.copy-btn.copied {
  background: #27ae60;
}

.copy-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.latex-loading,
.latex-error {
  padding: 3rem 2rem;
  text-align: center;
  background: #f8f9fa;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #e9ecef;
  border-top: 4px solid #667eea;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.latex-error {
  color: #e74c3c;
}

.retry-btn {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  margin-top: 1rem;
}

.retry-btn:hover {
  background: #5a6fd8;
  transform: translateY(-2px);
}

.latex-code {
  display: block;
  padding: 2rem;
  margin: 0;
  background: #f8f9fa;
  color: #2c3e50;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-size: 0.85rem;
  line-height: 1.5;
  overflow-x: auto;
  white-space: pre;
}

/* Resume Preview */
.resume-preview {
  padding: 5rem 0;
  background: white;
}

.preview-container {
  max-width: 900px;
  margin: 0 auto;
}

.resume-document {
  background: white;
  border: 1px solid #e9ecef;
  border-radius: 10px;
  padding: 3rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  font-family: 'Georgia', serif;
  line-height: 1.6;
}

.resume-doc-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 1.5rem;
  border-bottom: 2px solid #2c3e50;
}

.resume-doc-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.contact-info {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
  font-size: 0.95rem;
  color: #5a6c7d;
}

.resume-section {
  margin-bottom: 2.5rem;
}

.resume-section h2 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #2c3e50;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #e9ecef;
}

.resume-item {
  margin-bottom: 1.5rem;
}

.item-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.item-header strong {
  font-size: 1.1rem;
  color: #2c3e50;
}

.date {
  font-style: italic;
  color: #667eea;
  font-weight: 500;
}

.tech-stack {
  font-style: italic;
  color: #667eea;
  font-size: 0.9rem;
}

.item-details {
  color: #5a6c7d;
  margin-bottom: 0.5rem;
  font-style: italic;
}

.resume-item ul {
  margin: 0;
  padding-left: 1.5rem;
}

.resume-item li {
  margin-bottom: 0.3rem;
  color: #5a6c7d;
}

.skills-grid {
  display: grid;
  gap: 1rem;
}

.skill-category {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: baseline;
}

.skill-category strong {
  color: #2c3e50;
  min-width: 150px;
}

.skill-category span {
  color: #5a6c7d;
}

.achievements-list {
  margin: 0;
  padding-left: 1.5rem;
}

.achievements-list li {
  margin-bottom: 0.5rem;
  color: #5a6c7d;
}

/* Button Styles */
.btn-primary {
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  color: #2c3e50;
  padding: 1rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  display: inline-block;
  box-shadow: 0 4px 15px rgba(255, 171, 160, 0.3);
  border: none;
  cursor: pointer;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(255, 171, 160, 0.4);
  color: #2c3e50;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.2);
  color: black;
  padding: 1rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.3s ease;
  display: inline-block;
  border: 2px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
  cursor: pointer;
}

.btn-secondary:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.5);
  color: black;
}

.btn-secondary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* Responsive Design */
@media (max-width: 768px) {
  .resume-actions {
    flex-direction: column;
    align-items: center;
  }

  .btn-primary,
  .btn-secondary {
    width: 100%;
    max-width: 280px;
    text-align: center;
  }

  .latex-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }

  .latex-code {
    font-size: 0.75rem;
    padding: 1.5rem;
  }

  .resume-document {
    padding: 2rem;
  }

  .contact-info {
    flex-direction: column;
    gap: 0.8rem;
  }

  .item-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .skill-category {
    flex-direction: column;
    gap: 0.3rem;
  }

  .skill-category strong {
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .resume-header {
    padding: 3rem 0;
  }

  .resume-header .section-title {
    font-size: 2.2rem;
  }

  .latex-section,
  .resume-preview {
    padding: 3rem 0;
  }

  .resume-document {
    padding: 1.5rem;
  }

  .resume-doc-header h1 {
    font-size: 2rem;
  }

  .contact-info {
    font-size: 0.85rem;
  }
}
</style>
