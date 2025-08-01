<template>
  <div class="github-page">
    <!-- Header Section -->
    <section class="github-header">
      <div class="container">
        <h1 class="section-title">
          {{ githubData.user?.name || 'GitHub Profile' }}
        </h1>
        <p class="section-subtitle">
          {{
            githubData.user?.bio ||
            'Explore my open source contributions, repositories, and coding activity'
          }}
        </p>

        <div class="profile-links">
          <a
            :href="`https://github.com/${githubUsername}`"
            target="_blank"
            rel="noopener noreferrer"
            class="btn-primary"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M12 0C5.374 0 0 5.373 0 12 0 17.302 3.438 21.8 8.207 23.387c.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.30.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"
              />
            </svg>
            Visit My GitHub
          </a>
          <button @click="refreshAll" class="btn-secondary" :disabled="isRefreshing">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <path
                d="M17.65 6.35C16.2 4.9 14.21 4 12 4c-4.42 0-7.99 3.58-7.99 8s3.57 8 7.99 8c3.73 0 6.84-2.55 7.73-6h-2.08c-.82 2.33-3.04 4-5.65 4-3.31 0-6-2.69-6-6s2.69-6 6-6c1.66 0 3.14.69 4.22 1.78L13 11h7V4l-2.35 2.35z"
              />
            </svg>
            {{ isRefreshing ? 'Refreshing...' : 'Refresh Data' }}
          </button>
        </div>
      </div>
    </section>

    <!-- GitHub Stats Section -->
    <section class="extended-stats">
      <div class="container">
        <h2 class="section-title">GitHub Statistics</h2>

        <div class="extended-stats-grid">
          <!-- GitHub Stats -->
          <div class="stat-widget">
            <h3>� GitHub Statistics</h3>
            <div class="widget-content" v-if="!loading">
              <div class="stats-grid">
                <div class="stat-item">
                  <div class="stat-number">{{ githubData.stats.totalRepos }}</div>
                  <div class="stat-label">Public Repos</div>
                </div>
                <div class="stat-item">
                  <div class="stat-number">{{ githubData.stats.totalStars }}</div>
                  <div class="stat-label">Total Stars</div>
                </div>
                <div class="stat-item">
                  <div class="stat-number">{{ githubData.stats.totalForks }}</div>
                  <div class="stat-label">Total Forks</div>
                </div>
                <div class="stat-item">
                  <div class="stat-number">{{ githubData.stats.followers }}</div>
                  <div class="stat-label">Followers</div>
                </div>
              </div>
            </div>
            <div v-else class="loading-state">
              <div class="spinner"></div>
              <p>Loading GitHub stats...</p>
            </div>
          </div>

          <!-- Profile Info -->
          <div class="stat-widget">
            <h3>👤 Profile Information</h3>
            <div class="widget-content" v-if="!loading && githubData.user">
              <div class="profile-info">
                <img
                  :src="githubData.user.avatar_url"
                  :alt="githubData.user.name"
                  class="profile-avatar"
                />
                <div class="profile-details">
                  <h4>{{ githubData.user.name || githubData.user.login }}</h4>
                  <p class="profile-bio">{{ githubData.user.bio || 'No bio available' }}</p>
                  <div class="profile-meta">
                    <span v-if="githubData.user.location">📍 {{ githubData.user.location }}</span>
                    <span v-if="githubData.user.company">🏢 {{ githubData.user.company }}</span>
                  </div>
                </div>
              </div>
            </div>
            <div v-else class="loading-state">
              <div class="spinner"></div>
              <p>Loading profile info...</p>
            </div>
          </div>

          <!-- Top Repositories -->
          <div class="stat-widget">
            <h3>🏆 Top Repositories</h3>
            <div class="widget-content" v-if="!loading">
              <div class="repos-list">
                <div v-for="repo in githubData.repos.slice(0, 5)" :key="repo.id" class="repo-item">
                  <div class="repo-info">
                    <h5 class="repo-name">{{ repo.name }}</h5>
                    <p class="repo-description">{{ repo.description || 'No description' }}</p>
                    <div class="repo-stats">
                      <span v-if="repo.language" class="language">{{ repo.language }}</span>
                      <span class="stars">⭐ {{ repo.stargazers_count }}</span>
                      <span class="forks">🍴 {{ repo.forks_count }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-else class="loading-state">
              <div class="spinner"></div>
              <p>Loading repositories...</p>
            </div>
          </div>

          <!-- Recent Activity -->
          <div class="stat-widget full-width">
            <h3>📋 Recent Activity</h3>
            <div v-if="!loading" class="activity-list">
              <div
                class="activity-item"
                v-for="(event, index) in githubData.events.slice(0, 8)"
                :key="index"
              >
                <div class="activity-icon">{{ getEventIcon(event) }}</div>
                <div class="activity-content">
                  <p class="activity-text">{{ getEventDescription(event) }}</p>
                  <span class="activity-date">{{ formatDate(event.created_at) }}</span>
                </div>
              </div>
            </div>
            <div v-else class="loading-state">
              <div class="spinner"></div>
              <p>Loading recent activity...</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'GitHubView',
  data() {
    return {
      isDarkMode: false, // Default to light/white theme
      isRefreshing: false,
      hideWakatimeStats: false,
      githubData: {
        user: null,
        repos: [],
        events: [],
        stats: {
          totalStars: 0,
          totalForks: 0,
          totalRepos: 0,
          followers: 0,
          following: 0,
        },
      },
      loading: true,
      error: null,
      githubUsername: 'eabhi-me',
    }
  },
  mounted() {
    this.detectTheme()
    this.fetchGitHubData()
    // Listen for theme changes
    const observer = new MutationObserver(() => {
      this.detectTheme()
    })
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    })
  },
  methods: {
    detectTheme() {
      this.isDarkMode = document.documentElement.classList.contains('dark-theme')
    },

    async fetchGitHubData() {
      this.loading = true
      this.error = null

      try {
        // Fetch user data
        const userResponse = await fetch(`https://api.github.com/users/${this.githubUsername}`)
        if (!userResponse.ok) throw new Error('Failed to fetch user data')
        this.githubData.user = await userResponse.json()

        // Fetch repositories
        const reposResponse = await fetch(
          `https://api.github.com/users/${this.githubUsername}/repos?sort=updated&per_page=10`,
        )
        if (!reposResponse.ok) throw new Error('Failed to fetch repositories')
        this.githubData.repos = await reposResponse.json()

        // Fetch recent events
        const eventsResponse = await fetch(
          `https://api.github.com/users/${this.githubUsername}/events?per_page=10`,
        )
        if (!eventsResponse.ok) throw new Error('Failed to fetch events')
        this.githubData.events = await eventsResponse.json()

        // Calculate stats
        this.calculateStats()
      } catch (error) {
        console.error('Error fetching GitHub data:', error)
        this.error = error.message
      } finally {
        this.loading = false
      }
    },

    calculateStats() {
      if (this.githubData.repos.length > 0) {
        this.githubData.stats.totalStars = this.githubData.repos.reduce(
          (sum, repo) => sum + repo.stargazers_count,
          0,
        )
        this.githubData.stats.totalForks = this.githubData.repos.reduce(
          (sum, repo) => sum + repo.forks_count,
          0,
        )
        this.githubData.stats.totalRepos = this.githubData.user?.public_repos || 0
        this.githubData.stats.followers = this.githubData.user?.followers || 0
        this.githubData.stats.following = this.githubData.user?.following || 0
      }
    },

    formatDate(dateString) {
      const date = new Date(dateString)
      const now = new Date()
      const diffTime = Math.abs(now - date)
      const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

      if (diffDays === 1) return '1 day ago'
      if (diffDays < 7) return `${diffDays} days ago`
      if (diffDays < 30) return `${Math.ceil(diffDays / 7)} weeks ago`
      return `${Math.ceil(diffDays / 30)} months ago`
    },

    getEventIcon(event) {
      switch (event.type) {
        case 'PushEvent':
          return '🚀'
        case 'CreateEvent':
          return '🆕'
        case 'IssuesEvent':
          return '🐛'
        case 'PullRequestEvent':
          return '🔄'
        case 'WatchEvent':
          return '⭐'
        case 'ForkEvent':
          return '🍴'
        default:
          return '📝'
      }
    },

    getEventDescription(event) {
      switch (event.type) {
        case 'PushEvent':
          const commits = event.payload.commits?.length || 1
          return `Pushed ${commits} commit${commits > 1 ? 's' : ''} to ${event.repo.name}`
        case 'CreateEvent':
          return `Created ${event.payload.ref_type} in ${event.repo.name}`
        case 'IssuesEvent':
          return `${event.payload.action} issue in ${event.repo.name}`
        case 'PullRequestEvent':
          return `${event.payload.action} pull request in ${event.repo.name}`
        case 'WatchEvent':
          return `Starred ${event.repo.name}`
        case 'ForkEvent':
          return `Forked ${event.repo.name}`
        default:
          return `Activity in ${event.repo.name}`
      }
    },

    async refreshAll() {
      this.isRefreshing = true
      await this.fetchGitHubData()
      setTimeout(() => {
        this.isRefreshing = false
      }, 1000)
    },

    hideWakatime() {
      this.hideWakatimeStats = true
    },
  },
}
</script>

<style scoped>
.github-page {
  padding-top: 80px;
}

/* Header Section */
.github-header {
  padding: 5rem 0;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  position: relative;
  overflow: hidden;
}

.github-header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 1000'%3E%3Cpolygon fill='%23f1f5f9' points='0,1000 1000,0 1000,1000'/%3E%3C/svg%3E");
  opacity: 0.1;
}

.github-header .container {
  position: relative;
  z-index: 1;
}

.section-title {
  font-size: 3.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1rem;
}

.section-subtitle {
  font-size: 1.25rem;
  color: var(--color-text-muted);
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.profile-links {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.btn-primary,
.btn-secondary {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem 2.5rem;
  border-radius: 60px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
  color: white;
  box-shadow: var(--shadow-lg);
}

.btn-primary::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.6s;
}

.btn-primary:hover::before {
  left: 100%;
}

.btn-primary:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-xl);
}

.btn-secondary {
  background: white;
  color: var(--color-text);
  border: 2px solid var(--color-border);
  box-shadow: var(--shadow-md);
}

.btn-secondary:hover:not(:disabled) {
  transform: translateY(-4px);
  background: var(--color-primary-light);
  border-color: var(--color-primary);
  box-shadow: var(--shadow-lg);
}

.btn-secondary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* Extended Stats Section */
.extended-stats {
  padding: 8rem 0;
  background: linear-gradient(
    180deg,
    var(--color-background) 0%,
    var(--color-background-soft) 100%
  );
  position: relative;
}

.extended-stats::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent 0%, var(--color-primary) 50%, transparent 100%);
}

.extended-stats .section-title {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  text-align: center;
}

.extended-stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
  gap: 2.5rem;
  margin-top: 4rem;
}

.stat-widget {
  background: white;
  border-radius: 24px;
  padding: 2.5rem;
  box-shadow: var(--shadow-lg);
  border: 1px solid var(--color-border);
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.stat-widget::before {
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

.stat-widget:hover::before {
  transform: scaleX(1);
}

.stat-widget:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-xl);
}

.dark-theme .stat-widget {
  background: var(--color-background-soft);
  box-shadow: var(--shadow-lg);
}

.dark-theme .stat-widget:hover {
  box-shadow: var(--shadow-xl);
}

.stat-widget.full-width {
  grid-column: 1 / -1;
}

.stat-widget h3 {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
  padding-bottom: 0.5rem;
}

.stat-widget h3::after {
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

.widget-content {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 160px;
  position: relative;
}

.widget-content img {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  transition: transform 0.3s ease;
}

.widget-content:hover img {
  transform: scale(1.02);
}

/* Loading State */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 2rem;
  color: var(--color-text-muted);
}

.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--color-border);
  border-top: 3px solid var(--color-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  width: 100%;
}

.stat-item {
  text-align: center;
  padding: 1rem;
  background: var(--color-background-mute);
  border-radius: 12px;
  border: 1px solid var(--color-border);
  transition: all 0.3s ease;
}

.stat-item:hover {
  background: var(--color-primary-light);
  border-color: var(--color-primary);
  transform: translateY(-2px);
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-primary);
  line-height: 1;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  font-weight: 500;
}

/* Profile Info */
.profile-info {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  width: 100%;
}

.profile-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 3px solid var(--color-border);
  transition: all 0.3s ease;
}

.profile-avatar:hover {
  border-color: var(--color-primary);
  transform: scale(1.05);
}

.profile-details {
  flex: 1;
}

.profile-details h4 {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--color-heading);
  margin-bottom: 0.5rem;
}

.profile-bio {
  color: var(--color-text-muted);
  font-size: 0.95rem;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.profile-meta {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.profile-meta span {
  font-size: 0.9rem;
  color: var(--color-text-muted);
}

/* Repositories List */
.repos-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
}

.repo-item {
  padding: 1rem;
  background: var(--color-background-mute);
  border-radius: 12px;
  border: 1px solid var(--color-border);
  transition: all 0.3s ease;
}

.repo-item:hover {
  background: var(--color-primary-light);
  border-color: var(--color-primary);
  transform: translateX(4px);
}

.repo-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--color-heading);
  margin-bottom: 0.5rem;
}

.repo-description {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  line-height: 1.4;
  margin-bottom: 0.75rem;
}

.repo-stats {
  display: flex;
  gap: 1rem;
  align-items: center;
  flex-wrap: wrap;
}

.language {
  padding: 0.25rem 0.75rem;
  background: var(--color-primary);
  color: white;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

.stars,
.forks {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  font-weight: 500;
}

/* Activity List */
.activity-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: 1.5rem;
  background: var(--color-background-mute);
  border-radius: 16px;
  border: 1px solid var(--color-border);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.activity-item::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: var(--color-primary);
  transform: scaleY(0);
  transition: transform 0.3s ease;
}

.activity-item:hover::before {
  transform: scaleY(1);
}

.activity-item:hover {
  background: white;
  border-color: var(--color-primary);
  transform: translateX(8px);
  box-shadow: var(--shadow-md);
}

.activity-icon {
  font-size: 1.8rem;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(
    135deg,
    var(--color-primary-light) 0%,
    var(--color-background-soft) 100%
  );
  border-radius: 50%;
  border: 2px solid var(--color-border);
  transition: all 0.3s ease;
}

.activity-item:hover .activity-icon {
  background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
  border-color: var(--color-primary);
  transform: scale(1.1);
}

.activity-content {
  flex: 1;
}

.activity-text {
  font-weight: 500;
  color: var(--color-text);
  margin-bottom: 0.5rem;
  font-size: 1rem;
  line-height: 1.5;
}

.activity-date {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  font-weight: 400;
}

/* Responsive Design */
@media (max-width: 768px) {
  .github-header {
    padding: 4rem 0;
  }

  .section-title {
    font-size: 2.5rem;
  }

  .section-subtitle {
    font-size: 1.1rem;
  }

  .extended-stats {
    padding: 6rem 0;
  }

  .extended-stats-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .profile-links {
    flex-direction: column;
    align-items: center;
  }

  .btn-primary,
  .btn-secondary {
    width: 100%;
    max-width: 300px;
    justify-content: center;
    padding: 1rem 2rem;
  }

  .stat-widget {
    padding: 2rem;
  }

  .activity-item {
    flex-direction: column;
    text-align: center;
    gap: 1rem;
    padding: 1.5rem;
  }

  .activity-item:hover {
    transform: translateY(-4px);
  }

  .profile-info {
    flex-direction: column;
    text-align: center;
  }

  .stats-grid {
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }

  .profile-meta {
    align-items: center;
  }
}

@media (max-width: 480px) {
  .github-header {
    padding: 3rem 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .extended-stats {
    padding: 4rem 0;
  }

  .stat-widget {
    padding: 1.5rem;
    border-radius: 16px;
  }

  .stat-widget h3 {
    font-size: 1.2rem;
  }

  .extended-stats-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .profile-avatar {
    width: 60px;
    height: 60px;
  }

  .repo-stats {
    justify-content: center;
  }
}
</style>
