<script setup>
import { ref } from 'vue'
import Button from '../components/Button.vue'
import ResultItem from '../components/ResultItem.vue'

const fileInput = ref(null)
const imageUrl = ref(null)
const isModalOpen = ref(false) // State to control modal visibility
const errorMessage = ref('') // State to store error messages

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file && file.type === 'image/png') {
    console.log('Valid PNG file selected:', file.name)
    imageUrl.value = URL.createObjectURL(file) // Create a URL for the image
    errorMessage.value = '' // Clear any previous error
  } else {
    console.error('Please select a valid .png file')
    fileInput.value = null // Clear the input
    imageUrl.value = null // Clear the image preview
    errorMessage.value = 'Please select a valid .png file' // Set error message
  }
}

function triggerFileInput() {
  fileInput.value.click() // Programmatically trigger the file input
}

function openModal() {
  if (!imageUrl.value) {
    errorMessage.value = 'Please upload an image before classifying' // Set error message
    return
  }
  isModalOpen.value = true // Open the modal
}

function closeModal() {
  isModalOpen.value = false // Close the modal
  imageUrl.value = null // Clear the image preview
  fileInput.value = null // Reset the file input
  errorMessage.value = '' // Clear any error message
}
</script>

<template>
  <div>
    <input
      ref="fileInput"
      type="file"
      accept=".png"
      @change="handleFileChange"
      style="display: none;"
    />
    <div
      @click="triggerFileInput"
      style="cursor: pointer; text-align: center; border: 2px dashed #ccc; width: 300px; height: 300px; display: flex; align-items: center; justify-content: center; position: relative;"
    >
      <template v-if="imageUrl">
        <img
          :src="imageUrl"
          alt="Uploaded Image"
          class="image-preview"
        />
      </template>
      <template v-else>
        <p>Upload an Image</p>
      </template>
    </div>
    <Button @click="openModal" style="margin-top:20px" buttonText="CLASSIFY" />
    <p v-if="errorMessage" style="color: red; margin-top: 10px;">{{ errorMessage }}</p>

    <!-- Modal -->
    <div
      v-if="isModalOpen"
      class="modal-overlay"
    >
      <div
        style="background: white; padding: 20px; border-radius: 8px; width: 400px; text-align: center;"
      >
        <h2>Your Results</h2>
        <ul class="result-list">
            <ResultItem name="Something1" number="50" />
            <ResultItem name="Something2" number="20" />

        </ul>
        <Button @click="closeModal" buttonText="CLOSE" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.image-preview {
  max-width: 300px;
  max-height: 300px;
  object-fit: contain;
  background-color: white;
}
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
  z-index: 1000; /* Ensure the modal is above other content */
}

.result-list {
  padding: 0px 20px 0px 20px;
}
</style>