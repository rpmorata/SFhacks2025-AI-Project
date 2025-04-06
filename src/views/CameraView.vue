<template>
    <div style="margin-top: 100px">
        <h1>Camera Input</h1>
        <!-- Conditionally display the video feed or the captured photo -->
        <div v-if="!capturedPhoto">
            <video ref="videoElement" width="320" height="240" autoplay class="flipped"></video>
        </div>
        <div v-else>
            <img :src="capturedPhoto" width="320" height="240" alt="Captured Photo" class="flipped"/>
        </div>
        <!-- Buttons to control the camera -->
        <div style="margin-top: 20px; display: flex; justify-content: space-between;">
            <Button v-if="!capturedPhoto" @click="startCamera" buttonText="Start Camera" />
            <Button v-if="!capturedPhoto" @click="stopCamera" buttonText="Stop Camera" />
        </div>
        <Button v-if="!capturedPhoto" @click="capturePhoto" buttonText="Capture Photo" class="btn-mrg"/>
        <div>
        <Button v-if="capturedPhoto" @click="resetCamera" buttonText="Reset Camera" />
        </div>
        <Button v-if="capturedPhoto" @click="resetCamera" buttonText="Classify" class="btn-mrg"/>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import Button from '../components/Button.vue';

// Refs for video element and captured photo
const videoElement = ref(null);
const capturedPhoto = ref(null);
let mediaStream = null;

// Function to start camera
const startCamera = async () => {
    try {
        mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.value.srcObject = mediaStream;
    } catch (err) {
        console.error('Error accessing camera: ', err);
    }
};

// Function to stop camera
const stopCamera = () => {
    if (mediaStream) {
        mediaStream.getTracks().forEach(track => track.stop());
        videoElement.value.srcObject = null;
    }
};

// Function to capture photo
const capturePhoto = () => {
    if (videoElement.value) {
        const canvas = document.createElement('canvas');
        canvas.width = videoElement.value.videoWidth;
        canvas.height = videoElement.value.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(videoElement.value, 0, 0, canvas.width, canvas.height);
        capturedPhoto.value = canvas.toDataURL('image/png');
        stopCamera();
    }
};

// Function to reset the camera view
const resetCamera = () => {
    capturedPhoto.value = null;
};
</script>

<style scoped>
video {
    border: 1px solid #ccc;
    margin-bottom: 20px;
}
button {
    margin: 5px;
}
img {
    border: 1px solid #ccc;
    margin-bottom: 20px;
    max-width: 100%;
}
.btn-mrg {
    margin-top: 20px;
}
.flipped {
    transform: scaleX(-1); /* Flip the video feed horizontally */
}
</style>
