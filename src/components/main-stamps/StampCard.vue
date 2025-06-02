<template>
    <div class="stamp-card">
        <div class="actions">
            <Button
                label="Edit"
                icon="pencil-outline"
                size="small"
                color="secondary"
                @click="handleEdit"
            />
            <Button
                label="Delete"
                icon="trash-can-outline"
                size="small"
                color="danger"
                @click="handleDelete"
            />
        </div>
        <h3 class="title">{{ card.title }}</h3>
        <p class="stamps">
            {{ formatStampText }}
        </p>

        <div class="stamp-row">
            <StampEntry
                v-for="entry in card.entries"
                :key="entry.pk"
                :disabled="entry.is_active"
                :entry="entry"
                @toggle="handleToggle"
            />
        </div>

        Debug
        <p>
            {{ card }}
        </p>
    </div>
</template>

<script setup>
    import { computed } from 'vue'
    import Button from '../generics/Button.vue'
    import StampEntry from './StampEntry.vue'

    const props = defineProps({
        card: {
            type: Object,
            required: true,
            validator: (value) =>
                'title' in value && 'stamps_needed' in value,
        },
    })

    const emit = defineEmits([
        'delete',
        'update-entry',
    ])

    const formatStampText = computed(() => {
        const prefix = props.card.stamps_needed - props.card.stamps_collected;
        const suffix = props.card.stamps_needed === 1 ? 'stamp' : 'stamps'

        return prefix > 0 ?
            `${prefix} ${suffix} needed` :
            'All stamps collected';
    })

    function handleDelete() {
        emit('delete', props.card.pk)
    }

    function handleEdit() {

    }

    function handleToggle(entry) {
        emit('update-entry', entry)
    }

</script>

<style scoped>
    .stamp-card {
        padding: 1rem;
        border-radius: 8px;
        background: #2a2b30;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }

    .title {
        font-size: 1.1rem;
        font-weight: bold;
        margin-bottom: 0.25rem;
    }

    .stamps {
        color: #555;
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