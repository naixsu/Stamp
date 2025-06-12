<template>
    <div class="main-layout">
        <!-- Sidebar Section -->
        <!-- TODO
            - Style the scrollbar
        -->
        <div class="sidebar">
            <div class="sidebar-header">
                <h2>Active Stamp Cards</h2>
                <Button
                    label="Add"
                    icon="plus"
                    size="medium"
                    color="primary"
                    @click="handleAdd"
                />
            </div>

            <div class="sidebar-scroll-wrapper">
                <SearchBar
                    placeholder="Search stamp cards"
                    @update:searchKey="searchKey = $event"
                />

                <div class="stamp-cards-list">
                    <StampCardSidebar
                        v-for="card in stampCards"
                        :key="card.pk"
                        :card="card"
                        @delete="handleDelete"
                        @click="handleCardClick"
                    />
                </div>
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
            v-if="selectedCard"
            :card="selectedCard"
            @update-entry="handleEntryUpdate"
            @mark-complete="handleMarkComplete"
        />
    </div>
</template>

<script setup>
    import { ref, onMounted, watch } from 'vue'
    import axios from 'axios'
    import debounce from 'debounce'

    // Generics
    import Button from './generics/Button.vue'
    import SearchBar from './generics/SearchBar.vue'

    // Other components
    import StampCardSidebar from './main-stamps/StampCardSidebar.vue'
    import AddStampCardModal from './main-stamps/AddStampCardModal.vue'
    import StampCardDetails from './main-stamps/StampCardDetails.vue'

    // Data
    const stampCards = ref([])
    const showModal = ref(false)
    const selectedCard = ref(null)
    const searchKey = ref('')

    // Debounced
    const debouncedFetchCards = debounce((value) => {
        fetchCards(value)
    }, 300)

    // Watch
    watch(searchKey, (value) => {
        debouncedFetchCards(value);
    })

    // onMounted
    onMounted(async () => {
        fetchCards();
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
        const params = new URLSearchParams()
        if (search) {
            params.append('search', search)
        }

        const { data } = await axios.get(`http://localhost:8000/api/stamp-cards/?${params}`)
        stampCards.value = data

        handleUpdateSelectedCard()
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
        height: 100%;
        overflow: hidden;
    }

    .sidebar {
        display: flex;
        flex-direction: column;
        width: 300px;
        background-color: var(--color-bg-dark);
        color: var(--color-text);
        padding: 1rem;
        box-sizing: border-box;
        overflow: hidden;
    }

    .sidebar-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }

    .stamp-cards-list {
        flex: 1;
        overflow-y: auto;
        padding-right: 4px;
        display: flex;
        flex-direction: column;
        gap: 1rem;
        box-sizing: border-box;
        padding-bottom: 2rem;
        scrollbar-gutter: stable;
    }

    .sidebar-scroll-wrapper {
        overflow-y: auto;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
</style>
