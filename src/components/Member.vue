<template>
    <li class="list-item">
        <strong>{{ name }}</strong>
        <img :src="imgSrc" class="image-pp" />
    </li>
</template>

<script>
export default {
    props: {
        name: {
            type: String,
            required: true
        },
        imgSrc: {
            type: String,
            required: true
        }
    }
};
</script>

<style scoped>
.list-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}
.image-pp {
    width: 100px;
    height: 100px;
    border-radius: 50%; /* Makes the image circular */
    margin-left: auto;
    margin-right: auto;
}
</style>