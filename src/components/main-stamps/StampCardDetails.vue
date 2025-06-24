<template>
    <!--
        TODO:
            - Truncate long card titles if ever we dont
                handle max char length on making cards
    -->
    <div
        v-if="props.card"
        class="details-panel"
        :class="{ 'redeemed': isCardRedeemed }"
    >
        <div
            v-if="isCardRedeemed"
            class="redeemed-overlay"
        >
            Redeemed
        </div>
        <div class="details-header">
            <h2>
                {{ props.card.title }}
            </h2>
            <Button
                label="Mark as complete"
                icon="pencil-outline"
                size="medium"
                color="primary"
                :disabled="!isCardComplete || isCardRedeemed"
                @click="handleComplete"
            />
        </div>

        <!-- This is the square wrapper for the stamp entries -->
        <div
            class="stamp-wrapper"
        >
            <div class="stamps">
                <StampEntry
                    v-for="entry in props.card.entries"
                    :key="entry.pk"
                    :disabled="entry.is_active"
                    :entry="entry"
                    @toggle="handleToggle"
                />
            </div>
        </div>
        <div class="notes-wrapper">
            <h3>
                Notes
            </h3>
            <div class="notes">
                {{ entryNotes }}
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

    const entryNotes = computed(() => {
        return props.card.notes || 'No extra info.';
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
        flex-grow: 1;
        background-color: var(--color-details);
        padding: 2rem;
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border-top-right-radius: 2rem;
        border-bottom-right-radius: 2rem;
        position: relative;
    }

    .redeemed-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color:  rgba(27, 45, 72, 0.5);
        color: var(--color-white-text);
        font-size: 1.8rem;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 1;
        pointer-events: none;
        border-top-right-radius: 1rem;
        border-bottom-right-radius: 1rem;
    }

    .details-panel.redeemed {
        cursor: default;
    }

    .details-panel.redeemed * {
        cursor: default !important;
    }

    .details-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
    }

    .stamp-row {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.5rem;
        width: 100%;
        height: 100%;
    }

    .stamp-wrapper {
        background-color: var(--color-wrapper);
        padding: 1rem;
        border-radius: 1rem;
        min-height: 300px; /* Ensures the wrapper has a minimum height */
        box-shadow: 0 2px 10px var(--color-wrapper-shadow);
        position: relative;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .stamps {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 0.25rem; /* This coincides with .stamp-wrapper's min-height */
        width: 100%;
    }

    .notes-wrapper {
        margin-top: 1rem;
        padding: 1rem;
        border-radius: 0.75rem;
        background-color: var(--color-wrapper);
        box-shadow: 0 2px 10px var(--color-wrapper-shadow);
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        min-height: 0;
        min-width: 0;
    }

    .notes-wrapper h3 {
        font-size: 1rem;
        margin-bottom: 0.5rem;
        margin-top: 0px;
    }

    .notes {
        font-size: 0.8rem;
        white-space: pre-wrap;
        word-break: break-word;  
        overflow-y: auto;
        flex-grow: 1;
        min-height: 0;
        min-width: 0;
        max-width: 100%;
        padding-right: 0.5rem;
    }

    .notes::-webkit-scrollbar {
        width: 6px;
    }

    .notes::-webkit-scrollbar-track {
        background-color: var(--color-hover);
        border-radius: 3px;
    }

    .notes::-webkit-scrollbar-thumb {
        background-color: var(--color-text);
        border-radius: 3px;
    }
</style>
