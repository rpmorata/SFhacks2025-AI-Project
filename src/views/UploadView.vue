<script setup>
import { ref } from 'vue'
import Button from '../components/Button.vue'
import Modal from '../components/Modal.vue'

const fileInput = ref(null)
const imageUrl = ref(null)
const isModalOpen = ref(false) // State to control modal visibility
const errorMessage = ref('Please upload an image before classifying') // State to store error messages

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file && file.type === 'image/png') {
    imageUrl.value = URL.createObjectURL(file) // Create a URL for the image
    document.getElementById('error').className = 'no-show'
  } else {
    fileInput.value = null // Clear the input
    imageUrl.value = null // Clear the image preview
  }
}

function triggerFileInput() {
  fileInput.value.click() // Programmatically trigger the file input
}

function openModal() {
  if (!imageUrl.value) {
    document.getElementById('error').className = 'show'
    return
  }
  isModalOpen.value = true // Open the modal
}

function closeModal() {
  isModalOpen.value = false // Close the modal
  imageUrl.value = null // Clear the image preview
  fileInput.value = null // Reset the file input
  document.getElementById('error').className = 'no-show'
}
</script>

<template>
  <div style="margin-top: 100px">
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
      <p id="error" class="no-show">{{ errorMessage }}</p>

      <!-- Modal Component -->
      <Modal
        :isOpen="isModalOpen"
        :photo="imageUrl"
        @close="closeModal"
      />
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

.no-show {
  margin-top: 10px;
  visibility: hidden
}

.show {
  color: red;
  margin-top: 10px;
}
</style>
