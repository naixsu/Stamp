<template>
    <!--
        TODO:
            - Make filled one look better?
    -->
    <Button
        :icon="disabled ? 'check' : 'square'"
        :disabled="disabled"
        size="small"
        @click="handleToggle"
    />
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
    })

    const emit = defineEmits(['toggle'])

    function handleToggle() {
        emit('toggle', props.entry)
    }
</script>

<style scoped>
    .stamp {
        font-size: 1.2rem;
        opacity: 0.3;
        transition: opacity 0.2s;
    }
</style>
