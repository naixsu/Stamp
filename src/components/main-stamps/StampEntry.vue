<template>
    <!--
        TODO:
            - Do the filled one
            - Disable(?) the filled one
            - Add `disabled` to `Button.vue`
    -->
    <Button
        :class="{ filled }"
        icon="square"
        size="small"
        @click="handleToggle"
    />
</template>

<script setup>
    import Button from '../generics/Button.vue'

    const props = defineProps({
        filled: {
            type: Boolean,
            default: false,
        },

        entryPk: {
            type: Number,
            required: true,
        },
    })

    const emit = defineEmits(['toggle'])

    function handleToggle() {
        emit('toggle', props.entryPk)
    }

</script>

<style scoped>
    .stamp {
        font-size: 1.2rem;
        opacity: 0.3;
        transition: opacity 0.2s;
    }

    .stamp.filled {
        opacity: 1;
    }
</style>
