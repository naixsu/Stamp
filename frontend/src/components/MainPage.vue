<template>
    <div class="main-layout">
        <!-- Sidebar Section -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h2 class="sidebar-title">
                    Stamp Cards
                </h2>
                <Button
                    label="Add"
                    icon="plus"
                    size="medium"
                    color="sidebar"
                    @click="handleAdd"
                />
            </div>

            <div class="sidebar-controls">
                <SearchBar
                    placeholder="Search stamp cards"
                    @update:searchKey="searchKey = $event"
                />
            </div>

            <div class="sidebar-list">
                <template v-if="stampCards.length > 0">
                    <StampCardSidebarItem
                        v-for="card in stampCards"
                        :key="card.pk"
                        :card="card"
                        :is-active="card.pk === selectedCard?.pk"
                        @delete="handleDelete"
                        @click="handleCardClick"
                    />
                </template>
                <template v-else>
                    <EmptyState
                        v-if="!isFetching"
                        icon="card-off"
                        size="medium"
                        :primary-text="emptyStateMessage"
                    />
                </template>
            </div>

            <AddStampCardModal
                v-if="showModal"
                :existing-cards="stampCards"
                @submit="handleSubmit"
                @close="handleClose"
            />
        </div>

        <!-- Details Panel -->
        <StampCardDetails
            :card="selectedCard"
            @update-entry="handleEntryUpdate"
            @mark-complete="handleMarkComplete"
        />
    </div>
</template>

<script setup>
    import { ref, onMounted, watch, computed } from 'vue'
    import axios from 'axios'

    // Generics
    import Button from './generics/Button.vue'
    import SearchBar from './generics/SearchBar.vue'
    import EmptyState from './generics/EmptyState.vue'

    // Other components
    import StampCardSidebarItem from './main-stamps/StampCardSidebarItem.vue'
    import AddStampCardModal from './main-stamps/AddStampCardModal.vue'
    import StampCardDetails from './main-stamps/StampCardDetails.vue'

    // Data
    const stampCards = ref([])
    const showModal = ref(false)
    const selectedCard = ref(null)
    const searchKey = ref('')
    const isFetching = ref(false)

    // Watch
    watch(searchKey, (value) => {
        isFetching.value = true;
        fetchCards(value)
    })

    // onMounted
    onMounted(async () => {
        fetchCards();
    })

    // Computed
    const emptyStateMessage = computed(() => {
        return searchKey.value
            ? `No stamp cards found matching "${searchKey.value}."`
            : 'No stamp cards available. Add a new one to get started.';
    })

    // Functions
    function handleAdd() {
        showModal.value = true;
    }

    function handleClose() {
        showModal.value = false;
    }

    function handleCardClick(card) {
        selectedCard.value = card
    }

    function handleUpdateSelectedCard() {
        if (!selectedCard.value) {
            return;
        }

        const updated = stampCards.value.find(card =>
            card.pk === selectedCard.value.pk
        )

        if (updated) {
            selectedCard.value = updated;
        }
    }

    // Async functions
    async function fetchCards(search = '') {
        isFetching.value = true

        try {
            const params = new URLSearchParams()
            if (search) params.append('search', search)

            const { data } = await axios.get(`http://localhost:8000/api/stamp-cards/?${params}`)
            stampCards.value = data
            handleUpdateSelectedCard()
        } catch (error) {
            console.error('Error fetching cards:', error)
        } finally {
            isFetching.value = false
        }
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
            const index = stampCards.value.findIndex(card => card.pk === cardPk)
            await fetchCards();

            // Switch `selectedCard` to an available card
            if (selectedCard.value?.pk === cardPk) {
                if (index > 0) {
                    selectedCard.value = stampCards.value[index - 1]
                } else if (stampCards.value.length > 0) {
                    selectedCard.value = stampCards.value[0]
                } else {
                    selectedCard.value = null
                }
            }
        }
    }

    async function handleEntryUpdate(entry) {
        try {
            const newStatus = !entry.is_active;
            await axios.patch(`http://localhost:8000/api/stamp-entries/${entry.pk}/`, {
                is_active: newStatus,
            });
            await fetchCards();
        } catch (error) {
            console.error(`Failed to update stamp entry ${entry.pk}`, error);
        }
    }

    async function handleMarkComplete(card) {
        try {
            await axios.patch(`http://localhost:8000/api/stamp-cards/${card.pk}/`, {
                is_redeemed: true,
            });
            await fetchCards();
        } catch (error) {
            console.error(`Failed to update card ${card.pk}`, error);
        }
    }
</script>

<style scoped>
    .main-layout {
        display: flex;
        overflow: hidden;
        font-family: sans-serif;
        height: 100%;
    }

    /* Sidebar */
    .sidebar {
        min-width: 280px;
        max-width: 280px;
        background-color: var(--color-sidebar);
        padding: 1rem;
        display: flex;
        flex-direction: column;
        border-top-left-radius: 2rem;
        border-bottom-left-radius: 2rem;
        box-sizing: border-box;
    }

    .sidebar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .sidebar-title {
        font-size: 1.2rem;
        text-align: center;
    }

    .sidebar-controls {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }

    .sidebar-list {
        flex-grow: 1;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        padding-right: 0.5rem;
    }

    .sidebar-list::-webkit-scrollbar {
        width: 6px;
    }

    .sidebar-list::-webkit-scrollbar-track {
        background-color: var(--color-hover);
        border-radius: 3px;
    }

    .sidebar-list::-webkit-scrollbar-thumb {
        background-color: var(--color-text);
        border-radius: 3px;
    }
</style>
