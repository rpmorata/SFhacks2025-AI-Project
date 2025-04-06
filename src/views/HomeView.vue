<script setup>
import Button from '../components/Button.vue'
import { onBeforeMount, onBeforeUnmount } from 'vue';

onBeforeMount(() => {
  document.body.className = 'home';
});

onBeforeUnmount(() => {
  if (document.body.className === 'home') {
    document.body.className = '';
  }
});

</script>

<template>
  <div>
      <header class="header">
          <div class="content">
              <div class="text">
                  <h1>Welcome to TopAIcal</h1>
                  <p class="text-description">
                      Your AI-powered companion for skin health, built with people of color in mind.
                      TopAIcal uses advanced artificial intelligence to help detect
                      and understand common skin concerns—providing support,
                      insights, and resources tailored to diverse skin tones.
                  </p>

                  <router-link to="/get-started">
                    <Button buttonText="GET STARTED" />
                  </router-link>
              </div>
              <div class="image-container">
                  <img src="../assets/landing.png" class="image" />
              </div>
          </div>
      </header>
  </div>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: left;
  color: black;
  z-index: 1;
}

.content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
}

.text {
  flex: 1;
  padding-right: 20px;
}

.image-container {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.image {
  max-height: 400px;
}

.btn:hover {
background-color: #b56f12; /* Change color on hover */
}

.btn {
text-decoration: none;
font-weight: bold;
font-size: 1.1rem; /* Increased font size */
padding: 8px 12px;
background-color: #805010; /* Different background color for "GET STARTED" */
color: white; /* White text for contrast */
border-radius: 5px; /* Rounded corners */
}

.text-description {
  margin-bottom: 30px;
}
</style>
