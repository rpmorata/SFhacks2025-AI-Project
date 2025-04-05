<script setup>
import { ref } from 'vue'

const fileInput = ref(null)
const imageUrl = ref(null)

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
    <button @click="() => { console.log('Clicked!') }">
      Clasify
    </button>
  </div>
</template>
