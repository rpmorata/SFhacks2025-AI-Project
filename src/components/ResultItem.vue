<template>
    <li class="result-item">
        <p>{{ name }}</p>
        <p>{{ number }}%</p>
    </li>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            required: true
        },
        number: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.result-item {
    display: flex;
    justify-content: space-between;
}
</style>