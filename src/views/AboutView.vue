<script setup>
import Member from '../components/Member.vue'
</script>

<template>
    <div style="margin-top: 100px">
    <h1>ABOUT US</h1>
    <div>
        <div class="section">
            <div class="text">
                <h2>OUR MISSION</h2>
                <p>
                    At TopAIcal, our mission is to empower people of color with accessible, inclusive,
                    and trustworthy AI tools for skin health. We aim to close the gap in dermatological
                    care by creating technology that understands and respects diverse skin tones and conditions,
                     helping users feel seen, supported, and confident in their skin.
                </p>
            </div>
            <img src="../assets/phone.png" class="image" />
        </div>
        <div class="section">
            <img src="../assets/brainstorm.png" class="image" />
            <div class="text">
                <h2>OUR STORY</h2>
                <p>
                    TopAIcal was born from a simple realization: traditional
                    skincare tools and diagnostics often overlook the needs of people with
                    darker skin tones. Our team—made up of technologists, healthcare advocates,
                    and creatives—came together to build something better. We combined our passion
                    for AI with a commitment to equity in health tech, creating an
                    intelligent tool that reflects the beauty and diversity of all skin.
                </p>
            </div>
        </div>
        <div>
            <h2>OUR TEAM</h2>
            <p>
                Get to know the passionate minds behind TopAIcal—creators, technologists,
                and advocates dedicated to building AI that truly sees everyone.
            </p>
            <ul class="list">
                <Member name="Ronin Morata" imgSrc="/src/assets/ronin.png" />
                <Member name="Samanta Chang" imgSrc="/src/assets/samanta.png" />
                <Member name="Christopher Lee" imgSrc="/src/assets/christopher.png" />
            </ul>
        </div>
    </div>
</div>
</template>

<style scoped>
.list {
    display: flex;
    list-style: none;
    padding: 0;
    gap: 50px;
    justify-content: center;
}

.section {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.text {
    flex: 1;
    margin-right: 20px;
    margin-left: 20px;
}

.image {
    max-height: 300px;
    margin: 20px 50px 20px 50px;
}

</style>