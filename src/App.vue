<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar,
  },
}
</script>

<template>
  <div id="app">
    <NavBar />
    <RouterView />
  </div>
</template>

<style>
/* ============================================================
   PORT THE PALETTE (core design system)
   ============================================================ */
:root {
  /* Brand */
  --brand-primary: #4d44ad;
  --brand-accent: #7c3aed;
  --brand-secondary: #06b6d4;
  --brand-tertiary: #f59e0b;

  /* Surfaces */
  --bg-deep: #0a0a12;
  --bg-dark: #0f111a;
  --bg-surface: #161827;
  --bg-float: rgba(22,24,39,0.65);

  /* Text */
  --text-primary: #ffffff;
  --text-secondary: #a0a3bd;
  --text-muted: #6b6f8a;

  /* Gradients (key look) */
  --grad-main: linear-gradient(135deg, #4d44ad 0%, #7c3aed 50%, #06b6d4 100%);
  --grad-warm: linear-gradient(135deg, #f59e0b 0%, #ff6b6b 100%);
  --grad-dim: linear-gradient(315deg, rgba(77,68,173,0.15) 0%, rgba(6,182,212,0.05) 100%);

  /* Glow */
  --glow-main:0 0 40px rgba(124,58,237,0.4);
  --glow-accent: 0 0 40px rgba(6,182,212,0.3);

  /* Border & Blur */
  --radius: 16px;
  --radius-small: 8px;
  --border-glow: 1px solid rgba(255,255,255,0.08);
  --blur: blur(24px) saturate(140%);

  /* Motion */
  --ease-out: cubic-bezier(0.16,1,0.3,1);
  --ease-in-out: cubic-bezier(0.87,0,0.13,1);
}

/* ============================================================
   GLOBAL RESET & BASE
   ============================================================ */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: 'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  background: var(--bg-deep);
  color: var(--text-primary);
  line-height: 1.7;
  overflow-x: hidden;
  /* Subtle moving dark noise-glow background */
  animation: bgPulse 15s ease-in-out infinite;
}

#app {
  min-height: 100vh;
  width: 100%;
}

/* Ambient gradient orbs behind content */
#app::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: -1;
  background: radial-gradient(circle at 15% 50%, rgba(77,68,173,0.18), transparent 50%),
              radial-gradient(circle at 85% 80%, rgba(124,58,237,0.10), transparent 50%),
              radial-gradient(circle at 50% 10%, rgba(6,182,212,0.08), transparent 50%);
  pointer-events: none;
}

/* ── cursor glow effect ── */
html {
  cursor: crosshair;
}

/* ============================================================
   ANIMATED BACKGROUND HELPER
   ============================================================ */
@keyframes bgPulse {
  0%, 100% { filter: brightness(1); }
  50%      { filter: brightness(1.08); }
}

/* ============================================================
   UTILITIES
   ============================================================ */
.container {
  max-width: 1300px;
  margin: 0 auto;
  padding: 0 2.4rem;
  width: 100%;
}

.section-title {
  font-size: clamp(2.2rem, 5vw, 3.4rem);
  font-weight: 800;
  text-align: center;
  margin-bottom: 1rem;
  background: var(--grad-main);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.02em;
}

.section-subtitle {
  text-align: center;
  font-size: 1.15rem;
  color: var(--text-secondary);
  margin-bottom: 4rem;
  max-width: 560px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.8;
}

/* ============================================================
   GLASSMORPHISM CARD (base)
   ============================================================ */
.glass {
  background: var(--bg-float);
  backdrop-filter: var(--blur);
  -webkit-backdrop-filter: var(--blur);
  border: var(--border-glow);
  border-radius: var(--radius);
  box-shadow: 0 10px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.06);
  transition: transform 0.4s var(--ease-out), box-shadow 0.4s var(--ease-out), border-color 0.4s ease;
}

.glass:hover {
  border-color: rgba(255,255,255,0.15);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 40px rgba(124,58,237,0.08), inset 0 1px 0 rgba(255,255,255,0.08);
  transform: translateY(-6px);
}

/* ============================================================
   BUTTONS
   ============================================================ */
.btn-primary,
.btn-secondary {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  padding: 1rem 2.4rem;
  border-radius: 50px;
  font-weight: 600;
  font-size: 1.05rem;
  cursor: pointer;
  text-decoration: none;
  border: none;
  overflow: hidden;
  transition: all 0.35s var(--ease-out);
  z-index: 1;
}

/* Main button: solid gradient */
.btn-primary {
  background: var(--grad-main);
  color: #fff;
  box-shadow: 0 6px 28px rgba(124,58,237,0.45), 0 2px 8px rgba(0,0,0,0.3);
}

.btn-primary::after {
  content: '';
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transition: opacity 0.35s ease;
  z-index: -1;
}

.btn-primary:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 10px 36px rgba(124,58,237,0.55), 0 0 20px rgba(124,58,237,0.2);
}

.btn-primary:hover::after {
  opacity: 0.12;
}

.btn-primary:active {
  transform: translateY(-1px) scale(0.97);
}

/* Secondary / ghost button */
.btn-secondary {
  background: rgba(255,255,255,0.06);
  color: var(--text-primary);
  border: 1.5px solid rgba(255,255,255,0.15);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.btn-secondary::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50px;
  background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(6,182,212,0.15));
  opacity: 0;
  transition: opacity 0.35s ease;
  z-index: -1;
}

.btn-secondary:hover {
  border-color: rgba(255,255,255,0.35);
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(124,58,237,0.15);
}

.btn-secondary:hover::before {
  opacity: 1;
}

/* ============================================================
   SECTION CONTRAST (dark card surface)
   ============================================================ */
.surface {
  background: var(--bg-surface);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: var(--radius);
}

/* ============================================================
   MOBILE
   ============================================================ */
@media (max-width: 768px) {
  html { cursor: auto; }
  .container { padding: 0 1.5rem; }
  .section-title  { font-size: clamp(1.8rem, 5vw, 2.5rem); }
  .section-subtitle { font-size: 1rem; margin-bottom: 3rem; padding: 0 1rem; }
}

@media (max-width: 480px) {
  .container { padding: 0 1.2rem; }
  .section-title  { font-size: clamp(1.6rem, 6vw, 2rem); }
  .section-subtitle { font-size: 0.95rem; margin-bottom: 2.5rem; }
}
</style>
