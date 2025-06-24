<template>
    <div class="app">
        <aside class="sidebar">
            <h2>Stamp Cards</h2>
            <ul>
                <li v-for="card in cards" :key="card.id" :class="{ active: card.id === selectedCard.id }"
                    @click="selectCard(card)">
                    {{ card.name }}
                </li>
            </ul>
        </aside>

        <main class="details" v-if="selectedCard">
            <!-- <h1>Loyalty Stamp Card</h1> -->
            <h2>{{ selectedCard.name }}</h2>
            <p>{{ selectedCard.stamps.length }} Stamps Collected</p>

            <div class="stamp-grid">
                <div v-for="(filled, index) in selectedCard.stamps" :key="index" :class="['stamp', { filled }]" />
            </div>

            <p><strong>Reward</strong><br />{{ selectedCard.reward }}</p>
            <p><strong>Valid Thru</strong><br />{{ selectedCard.validThru }}</p>
        </main>
    </div>
</template>

<script setup>
    import { ref } from 'vue';

    const cards = ref([
        {
            id: 1,
            name: 'Coffee Shop',
            stamps: [true, true, true, true, true, true, true, true, false, false],
            reward: 'Free Coffee',
            validThru: '12/31/2024',
        },
        {
            id: 2,
            name: 'Bakery',
            stamps: [true, true, false, false, false, false, false, false, false, false],
            reward: 'Free Bread',
            validThru: '01/31/2025',
        },
        // Add more cards as needed
    ]);

    const selectedCard = ref(cards.value[0]);
    const selectCard = (card) => (selectedCard.value = card);
</script>

<style scoped>
    .app {
        display: flex;
        height: 100vh;
        font-family: sans-serif;
        /* color: #2c3e50; */
    }

    .sidebar {
        width: 250px;
        /* background: #d6e7f8; */
        background-color: var(--color-sidebar);
        padding: 20px;
        overflow-y: auto;
    }

    .sidebar h2 {
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }

    .sidebar ul {
        list-style: none;
        padding: 0;
    }

    .sidebar li {
        padding: 10px;
        margin-bottom: 5px;
        border-radius: 5px;
        cursor: pointer;
        background-color: var(--color-sidebar-item-buttons);
    }

    .sidebar li.active {
        /* background: #a5c6e7; */
        background-color: var(--color-active);
        font-weight: bold;
    }

    .details {
        flex: 1;
        padding: 40px;
        background-color: var(--color-details);
    }

    .details h1 {
        font-size: 1.5rem;
    }

    .stamp-grid {
        display: grid;
        grid-template-columns: repeat(5, 40px);
        gap: 10px;
        margin: 20px 0;
        background-color: var(--color-wrapper);
    }

    .stamp {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid var(--color-icon);
    }

    .stamp.filled {
        background-color: var(--color-icon);
        border-color: var(--color-icon-border);
    }
</style>