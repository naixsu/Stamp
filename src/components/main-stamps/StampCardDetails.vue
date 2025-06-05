<template>
    <!--
        TODO:
            - When card is deleted, the details will still show
            - Improve the stamp-grid-wrapper class
    -->
    <div
        class="details-panel"
        v-if="card"
    >
    <h3>{{ card.title }}</h3>
    <div class="actions">
        <Button
            label="Edit"
            icon="pencil-outline"
            size="medium"
            color="secondary"
            @click="handleEdit"
        />
    </div>

    <!-- This is the square wrapper for the stamp entries -->
    <div class="stamp-grid-wrapper">
        <div class="stamp-row">
            <StampEntry
                v-for="entry in card.entries"
                :key="entry.pk"
                :disabled="entry.is_active"
                :entry="entry"
                @toggle="handleToggle"
            />
        </div>
    </div>
</div>

</template>

<script setup>
    import Button from '../generics/Button.vue'
    import StampEntry from './StampEntry.vue'

    defineProps({
        card: {
            type: Object,
            required: false,
        },
    });

    const emit = defineEmits(['update-entry'])

    function handleToggle(entry) {
        emit('update-entry', entry);
    }

    function handleEdit(entry) {
        console.log('handleEdit', entry);
    }
</script>

<style scoped>
    .details-panel {
        flex: 1;
        padding: 1.5rem;
        background-color: #1f1f2b;
        color: white;
        overflow-y: auto;
    }

    .actions {
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
        margin-top: 1rem;
    }

    .stamp-grid-wrapper {
        margin-top: 1rem;
        background-color: #2f2e41;
        padding: 1rem;
        border-radius: 10px;
        aspect-ratio: 1 / 1; /* Keeps the wrapper square */
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .stamp-row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.5rem;
        width: 100%;
        height: 100%;
    }
</style>
