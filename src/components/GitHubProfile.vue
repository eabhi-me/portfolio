<template>
  <div class="github-profile">
    <div class="container">
      <h2 class="section-title">GitHub Profile</h2>
      <p class="section-subtitle">Explore my open source contributions and coding activity</p>

      <!-- GitHub Stats Overview -->
      <div class="github-stats-grid">
        <div class="stat-card">
          <div class="stat-icon">📊</div>
          <div class="stat-content">
            <h3>GitHub Stats</h3>
            <div class="stat-image">
              <img
                :src="`https://github-readme-stats.vercel.app/api?username=${githubUsername}&show_icons=true&theme=${isDarkMode ? 'dark' : 'default'}&hide_border=true&count_private=true`"
                alt="GitHub Stats"
                @error="handleImageError"
              />
            </div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">🔥</div>
          <div class="stat-content">
            <h3>Streak Stats</h3>
            <div class="stat-image">
              <img
                :src="`https://github-readme-streak-stats.herokuapp.com/?user=${githubUsername}&theme=${isDarkMode ? 'dark' : 'default'}&hide_border=true`"
                alt="GitHub Streak"
                @error="handleImageError"
              />
            </div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon">💻</div>
          <div class="stat-content">
            <h3>Top Languages</h3>
            <div class="stat-image">
              <img
                :src="`https://github-readme-stats.vercel.app/api/top-langs/?username=${githubUsername}&layout=compact&theme=${isDarkMode ? 'dark' : 'default'}&hide_border=true`"
                alt="Top Languages"
                @error="handleImageError"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- GitHub Profile README -->
      <div class="github-readme-section">
        <div class="readme-header">
          <h3>📋 Profile README</h3>
          <div class="readme-actions">
            <a
              :href="`https://github.com/${githubUsername}`"
              target="_blank"
              rel="noopener noreferrer"
              class="btn-github"
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                <path
                  d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"
                />
              </svg>
              Visit Profile
            </a>
            <button @click="refreshStats" class="btn-refresh" :disabled="isLoading">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path
                  d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"
                />
              </svg>
              {{ isLoading ? 'Refreshing...' : 'Refresh' }}
            </button>
          </div>
        </div>

        <!-- Loading State -->
        <div v-if="isLoading && !readmeContent" class="readme-loading">
          <div class="loading-spinner"></div>
          <p>Fetching GitHub profile...</p>
        </div>

        <!-- Error State -->
        <div v-else-if="error && !readmeContent" class="readme-error">
          <p>⚠️ {{ error }}</p>
          <button @click="fetchReadme" class="retry-btn">🔄 Retry</button>
        </div>

        <!-- README Content -->
        <div v-else-if="readmeContent" class="readme-content">
          <div class="readme-preview" v-html="readmeHtml"></div>
        </div>

        <!-- Fallback Content -->
        <div v-else class="readme-fallback">
          <div class="fallback-content">
            <h4>👋 Hi there! I'm Abhishek Yadav</h4>
            <p>
              A passionate full-stack developer and AI enthusiast currently pursuing Computer
              Science Engineering. I love building innovative solutions and contributing to
              open-source projects.
            </p>

            <div class="quick-stats">
              <div class="quick-stat">
                <span class="stat-label">🌱 Currently Learning:</span>
                <span class="stat-value">Advanced AI/ML, Cloud Architecture</span>
              </div>
              <div class="quick-stat">
                <span class="stat-label">🔭 Working On:</span>
                <span class="stat-value">Full-stack applications, Computer Vision</span>
              </div>
              <div class="quick-stat">
                <span class="stat-label">💬 Ask me about:</span>
                <span class="stat-value">React, Vue.js, Python, Machine Learning</span>
              </div>
              <div class="quick-stat">
                <span class="stat-label">⚡ Fun fact:</span>
                <span class="stat-value">I love solving complex problems with elegant code!</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- GitHub Activity Graph -->
      <div class="github-activity">
        <h3>📈 Contribution Activity</h3>
        <div class="activity-graph">
          <img
            :src="`https://github-readme-activity-graph.vercel.app/graph?username=${githubUsername}&theme=${isDarkMode ? 'github-dark' : 'github-light'}&hide_border=true&area=true`"
            alt="GitHub Activity Graph"
            @error="handleImageError"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GitHubProfile',
  props: {
    isDarkMode: {
      type: Boolean,
      default: false, // Default to light/white theme
    },
  },
  data() {
    return {
      githubUsername: 'eabhi-me',
      readmeContent: null,
      readmeHtml: '',
      isLoading: false,
      error: null,
      refreshKey: 0,
    }
  },
  mounted() {
    this.fetchReadme()
  },
  watch: {
    isDarkMode() {
      // Force refresh images when theme changes
      this.refreshKey++
    },
  },
  methods: {
    async fetchReadme() {
      this.isLoading = true
      this.error = null

      try {
        // Fetch README from GitHub API
        const response = await fetch(
          `https://api.github.com/repos/${this.githubUsername}/${this.githubUsername}/readme`,
          {
            headers: {
              Accept: 'application/vnd.github.v3+json',
            },
          },
        )

        if (!response.ok) {
          throw new Error('README not found')
        }

        const data = await response.json()
        this.readmeContent = atob(data.content)

        // Convert markdown to HTML (basic conversion)
        this.readmeHtml = this.markdownToHtml(this.readmeContent)
      } catch (err) {
        console.error('Error fetching README:', err)
        this.error = 'Failed to load GitHub profile README'
      } finally {
        this.isLoading = false
      }
    },

    markdownToHtml(markdown) {
      // Basic markdown to HTML conversion
      let html = markdown
        // Headers
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        // Bold
        .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
        // Italic
        .replace(/\*(.*)\*/gim, '<em>$1</em>')
        // Links
        .replace(
          /\[([^\]]*)\]\(([^\)]*)\)/gim,
          '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>',
        )
        // Images
        .replace(
          /!\[([^\]]*)\]\(([^\)]*)\)/gim,
          '<img alt="$1" src="$2" style="max-width: 100%; height: auto;" />',
        )
        // Line breaks
        .replace(/\n/gim, '<br>')
        // Code blocks (simple)
        .replace(/`([^`]*)`/gim, '<code>$1</code>')

      return html
    },

    refreshStats() {
      this.refreshKey++
      this.fetchReadme()
    },

    handleImageError(event) {
      // Hide broken images
      event.target.style.display = 'none'
    },
  },
}
</script>

<style scoped>
.github-profile {
  padding: 8rem 0;
  background: linear-gradient(180deg, white 0%, var(--color-background-soft) 100%);
  position: relative;
}

.github-profile::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, var(--color-primary) 50%, transparent 100%);
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-align: center;
  margin-bottom: 1rem;
}

.section-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: var(--color-text-muted);
  margin-bottom: 4rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.github-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 2.5rem;
  margin-bottom: 5rem;
}

.stat-card {
  background: white;
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  text-align: center;
  border: 1px solid var(--color-border);
  position: relative;
  overflow: hidden;
}

.stat-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  transform: scaleX(0);
  transition: transform 0.4s ease;
}

.stat-card:hover::before {
  transform: scaleX(1);
}

.stat-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-xl);
}

.dark-theme .stat-card {
  background: var(--color-background-soft);
  box-shadow: var(--shadow-lg);
}

.dark-theme .stat-card:hover {
  box-shadow: var(--shadow-xl);
}

.stat-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
  background: linear-gradient(
    135deg,
    var(--color-primary-light) 0%,
    var(--color-background-soft) 100%
  );
  padding: 1rem;
  border-radius: 50%;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
}

.stat-content h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 2rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.stat-content h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 2px;
  background: var(--color-primary);
  border-radius: 1px;
}

.stat-image {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 220px;
  position: relative;
}

.stat-image img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.stat-image:hover img {
  transform: scale(1.02);
}

.github-readme-section {
  background: white;
  border-radius: 24px;
  padding: 3rem;
  margin-bottom: 4rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--color-border);
  position: relative;
  overflow: hidden;
}

.github-readme-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
}

.dark-theme .github-readme-section {
  background: var(--color-background-soft);
  box-shadow: var(--shadow-lg);
}

.readme-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.readme-header h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-heading);
  margin: 0;
}

.readme-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-github {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--color-primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-github:hover {
  background: var(--color-primary-hover);
  transform: translateY(-2px);
}

.btn-refresh {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--color-background-soft);
  color: var(--color-text);
  padding: 0.75rem 1.5rem;
  border-radius: 10px;
  border: 1px solid var(--color-border);
  cursor: pointer;
  font-weight: 500;
  transition: all 0.3s ease;
}

.btn-refresh:hover:not(:disabled) {
  background: var(--color-primary-light);
  border-color: var(--color-primary);
  transform: translateY(-2px);
}

.btn-refresh:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.readme-loading,
.readme-error {
  text-align: center;
  padding: 3rem 2rem;
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 4px solid var(--color-border);
  border-top: 4px solid var(--color-primary);
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

.readme-error {
  color: #e74c3c;
}

.retry-btn {
  background: var(--color-primary);
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 500;
  margin-top: 1rem;
  transition: all 0.3s ease;
}

.retry-btn:hover {
  background: var(--color-primary-hover);
}

.readme-content {
  max-height: 500px;
  overflow-y: auto;
  padding: 1rem;
  background: var(--color-background-soft);
  border-radius: 10px;
  border: 1px solid var(--color-border);
}

.readme-preview {
  line-height: 1.6;
  color: var(--color-text);
}

.readme-preview h1,
.readme-preview h2,
.readme-preview h3 {
  color: var(--color-heading);
  margin: 1rem 0;
}

.readme-preview img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 1rem 0;
}

.readme-preview code {
  background: var(--color-background-mute);
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-family: 'Monaco', 'Menlo', monospace;
  font-size: 0.9rem;
}

.readme-fallback {
  padding: 2rem;
  background: var(--color-background-soft);
  border-radius: 10px;
  border: 1px solid var(--color-border);
}

.fallback-content h4 {
  font-size: 1.3rem;
  color: var(--color-heading);
  margin-bottom: 1rem;
}

.fallback-content p {
  color: var(--color-text-muted);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.quick-stats {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.quick-stat {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.stat-label {
  font-weight: 600;
  color: var(--color-heading);
  min-width: 140px;
}

.stat-value {
  color: var(--color-text-muted);
}

.github-activity {
  background: white;
  border-radius: 24px;
  padding: 3rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--color-border);
  text-align: center;
  position: relative;
  overflow: hidden;
}

.github-activity::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
}

.dark-theme .github-activity {
  background: var(--color-background-soft);
  box-shadow: var(--shadow-lg);
}

.github-activity h3 {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 2.5rem;
  position: relative;
  padding-bottom: 0.5rem;
}

.github-activity h3::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 2px;
  background: var(--color-primary);
  border-radius: 1px;
}

.activity-graph {
  display: flex;
  justify-content: center;
  overflow-x: auto;
  padding: 1rem 0;
}

.activity-graph img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.activity-graph:hover img {
  transform: scale(1.02);
}

/* Responsive Design */
@media (max-width: 768px) {
  .github-stats-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .readme-header {
    flex-direction: column;
    text-align: center;
  }

  .readme-actions {
    justify-content: center;
  }

  .quick-stat {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }

  .stat-label {
    min-width: auto;
  }
}

@media (max-width: 480px) {
  .github-profile {
    padding: 4rem 0;
  }

  .github-readme-section,
  .github-activity {
    padding: 1.5rem;
  }

  .stat-card {
    padding: 1.5rem;
  }
}
</style>
