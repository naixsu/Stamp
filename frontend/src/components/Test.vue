<template>
    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2 class="sidebar-title">Active Stamp Cards</h2>
                <button class="add-btn">+ Add</button>
            </div>

            <div class="sidebar-controls">
                <input type="text" placeholder="Search..." class="search-bar" />
            </div>

            <div class="sidebar-list">
                <div v-for="card in dummyCards" :key="card.id" class="sidebar-item">
                    <div class="item-info">
                        <div class="item-title">{{ card.title }}</div>
                        <div class="item-progress">{{ card.stamped }} / {{ card.total }}</div>
                    </div>
                    <button class="delete-btn">🗑</button>
                </div>
            </div>
        </aside>

        <!-- Details Section -->
        <section class="details">
            <div class="details-header">
                <h2>{{ selectedCard.title }}</h2>
                <button class="complete-btn">Mark as Complete</button>
            </div>

            <div class="stamp-wrapper">
                <div class="stamps">
                    <div v-for="(stamp, index) in selectedCard.total" :key="index" class="stamp">
                        ⭐
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>

<script setup>
    const dummyCards = [
        { id: 1, title: 'Test', stamped: 3, total: 10 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
        { id: 2, title: 'Test2', stamped: 5, total: 8 },
    ];

    const selectedCard = dummyCards[0];
</script>

<style scoped>
    .app-container {
        display: flex;
        overflow: hidden;
        font-family: sans-serif;
        height: 100%;
    }

    /* Sidebar */
    .sidebar {
        width: 280px;
        background-color: var(--color-bg-medium);
        padding: 1rem;
        display: flex;
        flex-direction: column;
        border-top-left-radius: 1rem;
        border-bottom-left-radius: 1rem;
        box-sizing: border-box;
    }

    .sidebar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }

    .sidebar-title {
        color: var(--color-highlight);
        font-size: 1.2rem;
    }

    .sidebar-controls {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }

    .search-bar {
        padding: 0.5rem;
        border: none;
        border-radius: 0.5rem;
        background-color: var(--color-primary);
        color: var(--color-text);
    }

    .add-btn {
        padding: 0.4rem 0.8rem;
        border: none;
        border-radius: 0.5rem;
        background-color: var(--color-accent);
        color: var(--color-text);
        cursor: pointer;
        font-size: 0.9rem;
        white-space: nowrap;
    }

    /* Thin scrollbar for WebKit browsers */
    .sidebar-list::-webkit-scrollbar {
        width: 6px;
    }

    .sidebar-list::-webkit-scrollbar-track {
        background: transparent;
    }

    .sidebar-list::-webkit-scrollbar-thumb {
        background-color: var(--color-highlight);
        border-radius: 3px;
    }

    .sidebar-list {
        flex-grow: 1;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
    }

    .sidebar-item {
        background-color: var(--color-primary);
        padding: 0.5rem;
        border-radius: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: var(--color-text);
        cursor: pointer;
    }

    .item-info {
        display: flex;
        flex-direction: column;
    }

    .item-title {
        font-weight: bold;
    }

    .item-progress {
        font-size: 0.85rem;
        opacity: 0.8;
    }

    .delete-btn {
        background: none;
        border: none;
        color: var(--color-highlight);
        font-size: 1rem;
        cursor: pointer;
    }

    /* Details Section */
    .details {
        flex-grow: 1;
        background-color: var(--color-disabled);
        padding: 2rem;
        color: var(--color-text);
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border-top-right-radius: 1rem;
        border-bottom-right-radius: 1rem;
    }

    .details-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }

    .complete-btn {
        background-color: var(--color-highlight);
        color: var(--color-disabled);
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        cursor: pointer;
        white-space: nowrap;
    }

    .stamp-wrapper {
        background-color: var(--color-bg-medium);
        padding: 1rem;
        border-radius: 1rem;
        height: 100%;
    }

    .stamps {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 1rem;
    }

    .stamp {
        width: 50px;
        height: 50px;
        background-color: var(--color-accent);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        color: var(--color-text);
        font-size: 1.5rem;
        transition: transform 0.2s ease;
        margin: 0 auto;
    }

    .stamp:hover {
        transform: scale(1.1);
        background-color: var(--color-highlight);
        color: var(--color-disabled);
    }
</style>
