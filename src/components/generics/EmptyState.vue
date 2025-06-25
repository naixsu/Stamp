
<template>
    <div class="empty-state">
        <i
            v-if="icon"
            :class="[
                'mdi',
                `mdi-${icon}`,
                sizeClass,
                iconColorClass
            ]"
        />
        <p :class="['text', textSizeClass]">
            {{ primaryText }}
        </p>
    </div>
</template>

<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        icon: String,
        iconColor: {
            type: String,
            default: 'light', // light, dark
        },
        primaryText: {
            type: String,
            default: '',
        },
        size: {
            type: String,
            default: 'medium', // small, medium, large
        },
        textSize: {
            type: String,
            default: 'normal', // small, normal, large
        },
    })

    const sizeClass = computed(() => {
        return {
            small: 'icon-small',
            medium: 'icon-medium',
            large: 'icon-large'
        }[props.size]
    })

    const iconColorClass = computed(() => {
        return {
            light: 'icon-white',
            dark: 'icon-dark',
        }[props.iconColor]
    })

    const textSizeClass = computed(() => {
        return {
            small: 'text-small',
            normal: 'text-normal',
            large: 'text-large'
        }[props.textSize]
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

    /* Sizes */
    .icon-small {
        font-size: 5rem;
    }

    .icon-medium {
        font-size: 10rem;
    }

    .icon-large {
        font-size: 15rem;
    }

    /* Icon Colors */
    .icon-white {
        color: var(--color-white-text)
    }

    .icon-dark {
        color: var(--color-text)
    }

    /* Text */
    .text {
        max-width: 100%;
        overflow: hidden;
        white-space: normal;
        word-wrap: break-word;
    }

    /* Text Size */
    .text-small {
        font-size: 0.75rem;
    }

    .text-normal {
        font-size: 0.9rem;
    }

    .text-large {
        font-size: 1.1rem;
    }
</style>
