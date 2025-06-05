<!-- src/components/main-stamps/StampCardDetails.vue -->
<template>
    <div
        class="details-panel"
        v-if="card"
    >
        <h3>Card Details</h3>
        <p><strong>Title:</strong> {{ card.title }}</p>
        <p><strong>Stamps Needed:</strong> {{ card.stamps_needed }}</p>
        <p><strong>Stamps Collected:</strong> {{ card.stamps_collected }}</p>
        <!-- Add more fields here as needed -->
    </div>
</template>

<script setup>
    defineProps({
        card: {
            type: Object,
            required: false,
        },
    });
</script>

<style scoped>
    .details-panel {
        flex: 1;
        padding: 1.5rem;
        background-color: #1f1f2b;
        color: white;
        overflow-y: auto;
    }
</style>
