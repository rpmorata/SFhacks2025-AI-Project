<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const imageUrl = ref(null)
const isModalOpen = ref(false) // State to control modal visibility

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file && file.type === 'image/png') {
    console.log('Valid PNG file selected:', file.name)
    imageUrl.value = URL.createObjectURL(file) // Create a URL for the image
  } else {
    console.error('Please select a valid .png file')
    fileInput.value = null // Clear the input
    imageUrl.value = null // Clear the image preview
  }
}

function triggerFileInput() {
  fileInput.value.click() // Programmatically trigger the file input
}

function openModal() {
  isModalOpen.value = true // Open the modal
}

function closeModal() {
  isModalOpen.value = false // Close the modal
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
          style="max-width: 300px; max-height: 300px; object-fit: contain; background-color: white;"
        />
      </template>
      <template v-else>
        <p>Upload an Image</p>
      </template>
    </div>
    <button @click="openModal" style="margin-top: 20px;">
      Clasify
    </button>

    <!-- Modal -->
    <div
      v-if="isModalOpen"
      style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); display: flex; align-items: center; justify-content: center;"
    >
      <div
        style="background: white; padding: 20px; border-radius: 8px; width: 400px; text-align: center;"
      >
        <h2>Modal Title</h2>
        <p>Modal content goes here.</p>
        <button @click="closeModal" style="margin-top: 20px;">
          Close
        </button>
      </div>
    </div>
  </div>
</template>
