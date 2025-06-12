<template>
    <!--
        TODO:
            - When card is deleted, the details will still show,
                Add something like a 'No card selected' empty state
            - Improve the stamp-grid-wrapper class
            - Truncate long card titles if ever we dont
                handle max char length on making cards
    -->
    <div
        v-if="props.card"
        class="details-panel"
    >
        <h3>{{ props.card.title }}</h3>
        <div class="actions">
            <Button
                label="Mark as complete"
                icon="pencil-outline"
                size="medium"
                color="success"
                :disabled="!isCardComplete || isCardRedeemed"
                @click="handleComplete"
            />
        </div>

        <!-- This is the square wrapper for the stamp entries -->
        <div
            class="stamp-grid-wrapper"
            :class="{ 'redeemed': isCardRedeemed }"
        >
            <div
                v-if="isCardRedeemed"
                class="redeemed-overlay"
            >
                Redeemed
            </div>
            <div class="stamp-row">
                <StampEntry
                    v-for="entry in props.card.entries"
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
    import { computed } from 'vue'
    import Button from '../generics/Button.vue'
    import StampEntry from './StampEntry.vue'

    const props = defineProps({
        card: {
            type: Object,
            required: false,
        },
    })

    const emit = defineEmits([
        'update-entry',
        'mark-complete',
    ])

    const isCardComplete = computed(() => {
        return props.card.stamps_needed ===
            props.card.stamps_collected;
    })

    const isCardRedeemed = computed(() => {
        return props.card.is_redeemed;
    })

    function handleToggle(entry) {
        emit('update-entry', entry);
    }

    function handleComplete() {
        emit('mark-complete', props.card);
    }
</script>

<style scoped>
    .details-panel {
        flex: 1;
        padding: 1.5rem;
        background-color: var(--color-bg-dark);
        color: var(--color-text);
        overflow: hidden;
        height: 100%;
    }

    .actions {
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
        margin-top: 1rem;
    }

    .stamp-grid-wrapper {
        position: relative;
        margin-top: 1rem;
        background-color: var(--color-bg-medium);
        padding: 1rem;
        border-radius: 10px;
        aspect-ratio: 1 / 1;
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

    .redeemed-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(15, 15, 15, 0.7);
        color: #a7abc4;
        font-size: 1.8rem;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1;
        pointer-events: none;
    }
</style>
