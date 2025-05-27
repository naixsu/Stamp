<template>
    <div>
        <h2>Active Stamp Cards</h2>

        <Button
            label="Add"
            icon="plus"
            size="small"
            color="primary"
            @click="handleAdd"
        />

            <StampCard
                v-for="card in stampCards"
                :key="card.id"
                :card="card"
            />
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    // Generics
    import Button from './generics/Button.vue'

    // Other components
    import StampCard from './main-stamps/StampCard.vue'

    const stampCards = ref([])

    onMounted(async () => {
        const { data } = await axios.get('http://localhost:8000/api/active-stampcards/')
        stampCards.value = data
    })

    function handleAdd() {
        console.log('handleAdd');
    }

</script>


<style scoped>

</style>
