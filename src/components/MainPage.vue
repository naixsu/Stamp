<template>
    <div>
        <h2>Active Stamp Cards</h2>
        <ul>
            <li v-for="card in stampCards" :key="card.id">
                {{ card.title }} - {{ card.stamps_needed }} stamps needed
            </li>
        </ul>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    const stampCards = ref([])

    onMounted(async () => {
        const { data } = await axios.get('http://localhost:8000/api/active-stampcards/')
        stampCards.value = data
    })
</script>


<style scoped>

</style>
