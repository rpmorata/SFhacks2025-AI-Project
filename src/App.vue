<script setup>
import Button from './components/Button.vue'
</script>

<template>
  <header class="header">
    <router-link to="/" class="logo-link">
      <img src="/topaical.svg" alt="Logo" class="logo" />
      <h1>TopAIcal</h1>
    </router-link>
    <nav class="nav-links">
      <router-link to="/" class="nav-item">HOME</router-link>
      <router-link to="/about" class="nav-item">ABOUT US</router-link>
      <router-link to="/get-started" >
        <Button buttonText="GET STARTED" />
      </router-link>
    </nav>
  </header>

  <router-view />
</template>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #ffffff;
  padding: 10px;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between; /* Space between logo and nav links */
  align-items: center;
}

.logo-link {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo {
  height: 60px;
  margin-right: 10px;
}

h1 {
  margin: 10px;
  color: black;
}

.nav-links {
  display: flex;
  gap: 25px; /* Increased space between nav items */
  margin-right: 30px;
}

.nav-item {
  text-decoration: none;
  color: black;
  font-weight: bold;
  font-size: 1.1rem; /* Increased font size */
  padding: 8px 12px; /* Added padding for larger button appearance */
}

.nav-item:hover {
  color: #b56f12; /* Change color on hover */
}

</style>
