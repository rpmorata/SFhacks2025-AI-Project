<template>
    <div v-if="isOpen" class="modal-overlay">
      <div class="modal-content">
        <h2>Your Results</h2>
        <div v-if="photo" class="image-container">
          <img :src="photo" alt="Captured Photo" class="captured-photo" />
        </div>
        <ul class="result-list">
          <ResultItem name="Something1" number="50" />
          <ResultItem name="Something2" number="20" />
        </ul>
        <Button @click="closeModal" buttonText="Close" />
      </div>
    </div>
  </template>

  <script setup>
  import { defineProps, defineEmits } from 'vue';
  import ResultItem from './ResultItem.vue';
  import Button from './Button.vue';

  const props = defineProps({
    isOpen: Boolean, // Control modal visibility
    photo: String // The captured photo URL to be displayed
  });

  const emit = defineEmits(['close']); // Emit close event

  const closeModal = () => {
    emit('close'); // Close the modal
  };
  </script>

  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }

  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 400px;
    text-align: center;
  }

  .image-container {
    margin-bottom: 20px;
  }

  .captured-photo {
    max-width: 100%;
    max-height: 300px;
    object-fit: contain;
  }

  .result-list {
    padding: 0px 20px 0px 20px;
  }
  </style>
