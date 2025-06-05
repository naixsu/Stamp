<template>
    <!--
        TODO:
            - When card is deleted, the details will still show
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
                size="small"
                color="secondary"
                @click="handleEdit"
            />
        </div>
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

    .stamp-row {
        display: flex;
        gap: 0.3rem;
        margin-top: 0.5rem;
    }
</style>
