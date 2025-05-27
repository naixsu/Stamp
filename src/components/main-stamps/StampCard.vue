<template>
    <div class="stamp-card">
        <h3 class="title">{{ card.title }}</h3>
        <p class="stamps">
            {{ card.stamps_needed }} {{ formatStampText }} needed
        </p>
    </div>
</template>

<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        card: {
            type: Object,
            required: true,
            validator: (value) =>
                'title' in value && 'stamps_needed' in value,
        },
    })

    const formatStampText = computed(() => {
        return props.card.stamps_needed === 1 ? 'stamp' : 'stamps'
    })
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
</style>