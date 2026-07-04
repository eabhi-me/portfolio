<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-container">
      <!-- Ambient glow line behind nav -->
      <div class="nav-glow"></div>

      <!-- Logo -->
      <div class="nav-logo">
        <RouterLink to="/" class="logo-text">
          <span class="logo-dot"></span>
          Abhishek Yadav
        </RouterLink>
      </div>

      <!-- Desktop Links -->
      <div class="nav-links">
        <RouterLink to="/" exact class="nav-link">Home</RouterLink>
        <RouterLink to="/about" class="nav-link">About</RouterLink>
        <RouterLink to="/projects" class="nav-link">Projects</RouterLink>
        <RouterLink to="/skills" class="nav-link">Skills</RouterLink>
        <RouterLink to="/github" class="nav-link">GitHub</RouterLink>
        <RouterLink to="/contact" class="nav-link">Contact</RouterLink>
      </div>

      <!-- Mobile toggle -->
      <button class="nav-toggle" @click="toggleMenu" aria-label="Toggle menu">
        <span :class="['bar', isMenuOpen && 'open']"></span>
        <span :class="['bar', isMenuOpen && 'open']"></span>
        <span :class="['bar', isMenuOpen && 'open']"></span>
      </button>
    </div>

    <!-- Mobile Dropdown -->
    <transition name="nav-slide">
      <div class="nav-drop" v-show="isMenuOpen">
        <RouterLink to="/" class="drop-link" @click="closeMenu">Home</RouterLink>
        <RouterLink to="/about" class="drop-link" @click="closeMenu">About</RouterLink>
        <RouterLink to="/projects" class="drop-link" @click="closeMenu">Projects</RouterLink>
        <RouterLink to="/skills" class="drop-link" @click="closeMenu">Skills</RouterLink>
        <RouterLink to="/github" class="drop-link" @click="closeMenu">GitHub</RouterLink>
        <RouterLink to="/contact" class="drop-link" @click="closeMenu">Contact</RouterLink>
      </div>
    </transition>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() { return { isScrolled: false, isMenuOpen: false }; },
  mounted() {
    this.onScroll = () => { this.isScrolled = window.scrollY > 40; };
    window.addEventListener('scroll', this.onScroll);
    this.$watch(() => this.$route, () => { this.closeMenu(); });
  },
  beforeUnmount() { window.removeEventListener('scroll', this.onScroll); },
  methods: {
    toggleMenu() { this.isMenuOpen = !this.isMenuOpen; },
    closeMenu() { this.isMenuOpen = false; },
  },
};
</script>

<style scoped>
/* ── CORE NAVBAR ── */
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 1000;
  padding: 1rem 0;
  transition: background 0.4s ease, box-shadow 0.4s ease, padding 0.3s ease;
  background: transparent;
}

/* Glow line + blur when scrolled */
.nav-glow {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(124,58,237,0.5), rgba(6,182,212,0.4), transparent);
  opacity: 0;
  transition: opacity 0.4s;
}

.scrolled {
  background: rgba(10,10,18,0.82);
  backdrop-filter: blur(24px) saturate(140%);
  -webkit-backdrop-filter: blur(24px) saturate(140%);
  box-shadow: 0 8px 40px rgba(0,0,0,0.4), inset 0 -1px 0 rgba(255,255,255,0.04);
  padding: 0.7rem 0;
}
.scrolled .nav-glow { opacity: 1; }

/* ── LOGO ── */
.nav-container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 2.4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.logo-text {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-size: 1.3rem;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
  letter-spacing: -0.01em;
}

.logo-dot {
  display: block;
  width: 12px; height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4d44ad, #7c3aed);
  box-shadow: 0 0 14px rgba(124,58,237,0.55);
  animation: logoBreath 3s ease-in-out infinite;
}

@keyframes logoBreath {
  0%, 100% { box-shadow: 0 0 14px rgba(124,58,237,0.55); transform: scale(1); }
  50%      { box-shadow: 0 0 24px rgba(124,58,237,0.85); transform: scale(1.12); }
}

/* ── DESKTOP LINKS ── */
.nav-links {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.nav-link {
  position: relative;
  padding: 0.5rem 1rem;
  color: var(--text-secondary);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  border-radius: 8px;
  transition: color 0.3s ease, background 0.3s ease;
}

.nav-link:hover { color: var(--text-primary); background: rgba(255,255,255,0.04); }

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 2px; left: 1rem; right: 1rem;
  height: 2px;
  border-radius: 2px;
  background: #7c3aed;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s var(--ease-out);
}

.nav-link:hover::after,
.nav-link.router-link-active::after { transform: scaleX(1); }

.nav-link.router-link-active { color: var(--text-primary); }

/* ── TOGGLE ── */
.nav-toggle { display: none; background: none; border: none; cursor: pointer; z-index: 1100; }
.bar {
  display: block;
  width: 24px; height: 2.5px;
  margin: 5px 0;
  background: var(--text-primary);
  border-radius: 2px;
  transition: all 0.35s cubic-bezier(0.7,0,0.3,1);
}
.bar.open:nth-child(1) { transform: translateY(7.5px) rotate(45deg); }
.bar.open:nth-child(2) { opacity: 0; transform: scaleX(0); }
.bar.open:nth-child(3) { transform: translateY(-7.5px) rotate(-45deg); }

/* ── MOBILE DROP ── */
.nav-drop {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: var(--bg-deep);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.4rem;
  z-index: 999;
  backdrop-filter: blur(20px);
}

.drop-link {
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text-primary);
  text-decoration: none;
  padding: 0.5rem 1.5rem;
  border-radius: 10px;
  transition: background 0.25s, color 0.25s;
}
.drop-link:hover, .drop-link.router-link-active { background: rgba(124,58,237,0.15); color: #a78bfa; }

.nav-slide-enter-active,
.nav-slide-leave-active { transition: all 0.4s var(--ease-out); }
.nav-slide-enter-from,
.nav-slide-leave-to { opacity: 0; transform: translateY(-20px); }

/* ── RESPONSIVE ── */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .nav-toggle { display: block; }
  .nav-container { padding: 0 1.5rem; }
}
</style>