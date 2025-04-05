

<template>
  <router-link to="/">
    <header class="header">
      <img src="/topaical.svg" alt="Logo" class="logo" />
      <h1>TopAIcal</h1>
    </header>
  </router-link>


  <router-view />

</template>
<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #f0f0f0;
  padding: 10px;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: center; /* Centers content horizontally */
  align-items: center; /* Centers content vertically */
}

.logo {
  height: 60px;
  margin-right: 10px;
}

h1 {
  margin: 10px; /* Reduce margin */
  color: black; /* Set text color to black */
}
</style>
