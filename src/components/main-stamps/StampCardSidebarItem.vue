<template>
    <div
        class="stamp-card"
        @click="handleClick"
    >
        <div class="stamp-card-info">
            <div class="stamp-card-title">
                {{ card.title }}
            </div>
            <div class="stamp-card-progress">
                {{ formatStampText }}
            </div>
        </div>

        <Button
            label="Delete"
            icon="trash-can-outline"
            size="small"
            color="danger"
            @click.stop="handleDelete"
        />
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import Button from '../generics/Button.vue'

    const props = defineProps({
        card: Object,
    })

    const emit = defineEmits(['delete', 'click'])

    const formatStampText = computed(() => {
        const total = props.card.stamps_needed
        const remaining = total- props.card.stamps_collected;
        const suffix = total === 1 ? 'stamp' : 'stamps';
        return remaining > 0 ? `${remaining}/${total} ${suffix} needed` : 'All stamps collected';
    })

    function handleDelete() {
        emit('delete', props.card.pk)
    }

    function handleClick() {
        emit('click', props.card)
    }
</script>

<style scoped>
    .stamp-card {
        background-color: var(--color-primary);
        padding: 0.6rem;
        border-radius: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: var(--color-text);
        cursor: pointer;
        transition: background-color 0.2s ease;
    }

    .stamp-card:hover {
        background-color: var(--color-highlight);
    }

    /* TODO: Figure this transform hover out maybe */
    /* .stamp-card {
        background-color: var(--color-primary);
        padding: 0.5rem;
        border-radius: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: var(--color-text);
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        position: relative;
        z-index: 1;
    }

    .stamp-card:hover {
        transform: scale(1.1);
        z-index: 10;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    } */

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .stamp-card-info {
        display: flex;
        flex-direction: column;
    }

    .stamp-card-title {
        font-weight: bold;
    }

    .stamp-card-progress {
        font-size: 0.85rem;
        opacity: 0.8;
    }
</style>
