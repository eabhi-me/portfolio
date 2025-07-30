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
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  overflow-x: hidden;
}

#app {
  font-family:
    'Inter',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background: #ffffff;
  width: 100%;
  min-height: 100vh;
}

body {
  line-height: 1.6;
  scroll-behavior: smooth;
}

/* Global styles for modern design */
.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
  width: 100%;
}

/* Full width sections */
.full-width {
  width: 100vw;
  margin-left: calc(50% - 50vw);
  margin-right: calc(50% - 50vw);
}

.btn-primary {
  background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
  color: #2c3e50;
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: inline-block;
  font-size: 1.05rem;
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
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  text-decoration: none;
  display: inline-block;
  font-size: 1.05rem;
  backdrop-filter: blur(10px);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.5);
  transform: translateY(-3px);
  color: white;
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

@media (max-width: 768px) {
  .container {
    padding: 0 1.5rem;
  }

  .section-title {
    font-size: clamp(1.8rem, 5vw, 2.5rem);
  }

  .section-subtitle {
    font-size: 1.1rem;
    margin-bottom: 3rem;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 0 1rem;
  }

  .section-title {
    font-size: clamp(1.6rem, 6vw, 2rem);
  }

  .section-subtitle {
    font-size: 1rem;
    margin-bottom: 2.5rem;
  }
}
</style>
