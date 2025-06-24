<template>
    <div class="stamp-entry">
        <Button
            :icon="disabled ? 'check' : props.icon"
            :disabled="disabled"
            color="primary"
            @click="handleToggle"
        />
    </div>
</template>

<script setup>
    import Button from '../generics/Button.vue'

    const props = defineProps({
        disabled: {
            type: Boolean,
            default: false,
        },

        entry: {
            type: Object,
            required: true,
        },

        icon: {
            type: String,
            required: false,
            default: 'coffee',
        },
    })

    const emit = defineEmits(['toggle'])

    function handleToggle() {
        emit('toggle', props.entry)
    }
</script>

<style scoped>
    .stamp-entry {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .stamp-entry :deep(.btn){
        width: 64px;
        height: 64px;
        border-radius: 50%;
        justify-content: center;
        padding: 0;
        font-size: 1.8rem;
    }
</style>
