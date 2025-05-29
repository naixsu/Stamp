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
            :key="card.pk"
            :card="card"
            @delete="handleDelete"
        />

        <AddStampCardModal
            v-model="showModal"
            @submit="handleSubmit"
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
    import AddStampCardModal from './main-stamps/AddStampCardModal.vue'

    // Data
    const stampCards = ref([])
    const showModal = ref(false)

    onMounted(async () => {
        fetchCards();
    })


    /**
     * TODO:
     * - Get base urls and stuff like that so this can be cleaner
     * - Handle these functions in a different file so MainPage.vue is cleaner
     */
    async function fetchCards() {
        const { data } = await axios.get('http://localhost:8000/api/stampcards/')
        stampCards.value = data ;
    }

    function handleAdd() {
        showModal.value = true;
    }

    async function handleSubmit(data) {
        try {
            const response = await axios.post('http://localhost:8000/api/stampcards/', data)
            stampCards.value.push(response.data)
            showModal.value = false
        } catch (error) {
            console.error('Failed to submit new stamp card:', error)
        }
    }

    async function handleDelete(cardPk) {
        try {
            await axios.delete(`http://localhost:8000/api/stampcards/${cardPk}/`)
            fetchCards();
        } catch (error) {
            console.error('Failed to delete stamp card:', error)
        }
    }
</script>

<style scoped>

</style>
