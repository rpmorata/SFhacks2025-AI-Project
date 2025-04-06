<template>
  <div v-if="isOpen" class="modal-overlay">
    <div class="modal-content">
      <h2>Your Results</h2>
      <div v-if="photo" class="image-container">
        <img :src="photo" alt="Captured Photo" class="captured-photo" />
      </div>
      <ul class="result-list">
        <ResultItem
          v-for="(result, index) in results"
          :key="index"
          :name="result.name"
          :number="result.number"
        />
      </ul>
      <Button @click="closeModal" buttonText="Close" />
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits, watch, ref } from 'vue';
import ResultItem from './ResultItem.vue';
import Button from './Button.vue';

const props = defineProps({
  isOpen: Boolean,
  photo: String // URL (probably a base64 string like data:image/jpeg;base64,...)
});

const emit = defineEmits(['close']);
const results = ref([]); // Reactive variable to store results

const closeModal = () => {
  emit('close');
};

// Watch for when modal opens
watch(() => props.isOpen, async (newVal) => {
  if (newVal && props.photo) {
    console.log('Modal opened, sending image to backend...');
    await sendImageToBackend(props.photo);
  }
});

// Convert dataURL to Blob
const dataURLtoBlob = (dataURL) => {
  const arr = dataURL.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], { type: mime });
};

// Fetch request
const sendImageToBackend = async (photoDataUrl) => {
  const blob = dataURLtoBlob(photoDataUrl);
  const formData = new FormData();
  formData.append('file', blob, 'image.jpg');

  try {
    const res = await fetch('http://localhost:5000/infer', {
      method: 'POST',
      body: formData
    });

    const data = await res.json();
    console.log('Backend prediction result:', data);
    results.value = data.results; // Assuming the backend returns an array of results
  } catch (err) {
    console.error('Error sending image:', err);
  }
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
