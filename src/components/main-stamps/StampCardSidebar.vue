<template>
    <!--
        TODO:
            - Truncate long card titles
            - Add a search bar
    -->
    <div
        class="stamp-card"
        @click="handleClick"
    >
        <div class="header">
            <h3 class="title">
                {{ card.title }}
            </h3>
            <div class="actions">
                <Button
                    label="Delete"
                    icon="trash-can-outline"
                    size="small"
                    color="danger"
                    @click.stop="handleDelete"
                />
            </div>
        </div>
        <p class="stamps">{{ formatStampText }}</p>
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
        padding: 1rem;
        border-radius: 8px;
        background: #2a2b30;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        cursor: pointer;
        transition: background 0.2s;
    }

    .stamp-card:hover {
        background: #35363b;
    }

    .title {
        font-size: 1.1rem;
        font-weight: bold;
    }

    .stamps {
        color: #ccc;
        margin-top: 0.5rem;
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
</style>
