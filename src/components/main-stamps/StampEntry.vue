<template>
    <!--
        TODO:
            - Make filled one look better?
    -->
    <div class="stamp-entry">
        <Button
            :icon="disabled ? 'check' : 'square'"
            :disabled="disabled"
            size="large"
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
    })

    const emit = defineEmits(['toggle'])

    function handleToggle() {
        emit('toggle', props.entry)
    }
</script>

<style scoped>
    .stamp-entry {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;  /* horizontally center */
        align-items: flex-start;  /* align top vertically */
    }
</style>
