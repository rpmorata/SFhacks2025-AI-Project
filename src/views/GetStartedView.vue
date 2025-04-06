<script setup>
import LargerButton from '../components/LargerButton.vue';
</script>

<template>
  <h1>GET STARTED RIGTH NOW!</h1>
  <div class="container">
    <router-link to="/upload">
      <LargerButton buttonText="UPLOAD IMAGE" />
    </router-link>
    <router-link to="/camera">
      <LargerButton buttonText="START CAMERA" />
    </router-link>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 5rem;
}
</style>