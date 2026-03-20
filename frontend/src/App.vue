<script setup lang="ts">
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="app-wrapper">
    <div class="bg-blur"></div>
    <RouterView />
  </div>
</template>

<style>
:root {
  --bg-color: #09090b;
  --font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

body {
  margin: 0;
  background-color: var(--bg-color);
  color: #fff;
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
}

.app-wrapper {
  position: relative;
  min-height: 100vh;
  overflow-x: hidden;
}

.bg-blur {
  position: fixed;
  top: -10%;
  left: -10%;
  width: 120%;
  height: 120%;
  background: 
    radial-gradient(circle at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
    radial-gradient(circle at 80% 80%, rgba(236, 72, 153, 0.15) 0%, transparent 40%);
  z-index: -1;
  pointer-events: none;
}
</style>
