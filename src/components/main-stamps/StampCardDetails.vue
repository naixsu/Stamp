<template>
    <!--
        TODO:
            - Truncate long card titles if ever we dont
                handle max char length on making cards
            - Ignore cursors if redeemed
    -->
    <div
        v-if="props.card"
        class="details-panel"
    >
        <div class="details-header">
            <h2>
                {{ props.card.title }}
            </h2>
            <!-- TODO: .complete-btn -->
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
            class="stamp-wrapper"
            :class="{ 'redeemed': isCardRedeemed }"
        >
            <div
                v-if="isCardRedeemed"
                class="redeemed-overlay"
            >
                Redeemed
            </div>
            <div class="stamps">
                <StampEntry
                    class="stamp"
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
        flex-grow: 1;
        /* background-color: var(--color-details); */
        /* background-color: var(--color-primary-one); */
        background-color: var(--color-accent-two);
        /* background-color: var(--color-bg-medium-one); */
        padding: 2rem;
        color: var(--color-text);
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        border-top-right-radius: 1rem;
        border-bottom-right-radius: 1rem;
        position: relative;
    }

    .details-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
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
        color: var(--color-text);
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

    .stamp-wrapper {
        /* background-color: var(--color-bg-medium); */
        background-color: var(--color-primary-two);
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
