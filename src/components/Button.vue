<template>
    <div>
        <button class="btn">{{ buttonText }}</button>
    </div>
</template>

<script>
export default {
    props: {
        buttonText: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.btn {
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem; /* Increased font size */
  padding: 8px 12px; /* Added padding for larger button appearance */
  background-color: #805010; /* Different background color for "GET STARTED" */
  color: white; /* White text for contrast */
  border-radius: 5px; /* Rounded corners */
}

.btn:hover {
    background-color: #b56f12; /* Change color on hover */
    border-color: #b56f12;
}
</style>