<template>
    <div class="main-layout">
        <!-- Sidebar Section -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h2>Active Stamp Cards</h2>
                <Button
                    label="Add"
                    icon="plus"
                    size="small"
                    color="primary"
                    @click="handleAdd"
                />
            </div>

            <div class="stamp-cards-list">
                <StampCardSidebar
                    v-for="card in stampCards"
                    :key="card.pk"
                    :card="card"
                    @delete="handleDelete"
                    @update-entry="handleEntryUpdate"
                    @click="handleCardClick"
                />
            </div>

            <AddStampCardModal
                v-if="showModal"
                @submit="handleSubmit"
                @close="handleClose"
            />
        </div>

        <!-- Details Panel -->
        <StampCardDetails
            :card="selectedCard"
        />
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue'
    import axios from 'axios'

    // Generics
    import Button from './generics/Button.vue'

    // Other components
    import StampCardSidebar from './main-stamps/StampCardSidebar.vue'
    import AddStampCardModal from './main-stamps/AddStampCardModal.vue'
    import StampCardDetails from './main-stamps/StampCardDetails.vue'

    // Data
    const stampCards = ref([])
    const showModal = ref(false)
    const selectedCard = ref(null)

    onMounted(async () => {
        fetchCards();
    })

    async function fetchCards() {
        const { data } = await axios.get('http://localhost:8000/api/stamp-cards/')
        stampCards.value = data;
    }

    function handleAdd() {
        showModal.value = true;
    }

    function handleClose() {
        showModal.value = false;
    }

    async function handleSubmit(data) {
        try {
            const response = await axios.post('http://localhost:8000/api/stamp-cards/', data);
            stampCards.value.push(response.data);
            showModal.value = false;
        } catch (error) {
            console.error('Failed to submit new stamp card:', error);
        }
    }

    async function handleDelete(cardPk) {
        try {
            await axios.patch(`http://localhost:8000/api/stamp-cards/${cardPk}/`, {
                is_removed: true,
            });
        } catch (error) {
            console.error(`Failed to delete stamp card ${cardPk}`, error);
        } finally {
            fetchCards();
        }
    }

    async function handleEntryUpdate(entry) {
        try {
            const newStatus = !entry.is_active;

            await axios.patch(`http://localhost:8000/api/stamp-entries/${entry.pk}/`, {
                is_active: newStatus,
            });
        } catch (error) {
            console.error(`Failed to update stamp entry ${entry.pk}`, error);
        } finally {
            fetchCards();
        }
    }

    function handleCardClick(card) {
        selectedCard.value = card
    }
</script>

<style scoped>
    .main-layout {
        display: flex;
        height: 100vh;
        overflow: hidden;
    }

    .sidebar {
        width: 300px;
        background-color: #2f2e41;
        color: white;
        padding: 1rem;
        box-sizing: border-box;
        overflow-y: auto;
    }

    .sidebar-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .stamp-cards-list {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
</style>
