<template>
    <div
        class="stamp-card"
        :class="{ active: props.isActive }"
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
        isActive: {
            type: Boolean,
            default: false,
        },
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
        background-color: var(--color-sidebar-item-buttons);
        padding: 0.6rem;
        border-radius: 0.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }

    .stamp-card:hover {
        background-color: var(--color-hover);
    }

    .stamp-card.active {
        background-color: var(--color-active);
    }

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
