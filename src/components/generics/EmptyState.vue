
<template>
    <div class="empty-state">
        <i
            v-if="icon"
            :class="[
                'mdi',
                `mdi-${icon}`,
                sizeClass
            ]"
        />
        <p>{{ primaryText }}</p>
    </div>
</template>

<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        icon: String,
        primaryText: {
            type: String,
            default: '',
        },
        size: {
            type: String,
            default: 'medium', // small, medium, large
        },
    })

    const sizeClass = computed(() => {
        return {
            small: 'icon-small',
            medium: 'icon-medium',
            large: 'icon-large'
        }[props.size]
    })
</script>

<style scoped>
    .empty-state {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        flex-grow: 1;
        padding: 2rem;
        font-size: 0.9rem;
        color: var(--color-text);
        opacity: 0.75;
    }

    .mdi {
        /* color: var(--color-white-text);; */
    }

    /* Sizes */
    .icon-small {
        font-size: 5rem;
    }

    .icon-medium {
        font-size: 7rem;
    }

    .icon-large {
        font-size: 10rem;
    }
</style>
