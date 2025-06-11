<template>
    <button
        :class="['btn', sizeClass, colorClass]"
        :disabled="disabled"
    >
        <i
            v-if="icon"
            :class="`mdi mdi-${icon}`"
        />
        <span v-if="label">{{ label }}</span>
        <slot />
    </button>
</template>

<script setup>
    import { computed } from 'vue'

    const props = defineProps({
        label: String,
        icon: String,
        size: {
            type: String,
            default: 'medium', // small, medium, large
        },
        color: {
            type: String,
            default: 'primary', // primary, secondary, success, danger
        },
        disabled: {
            type: Boolean,
            default: false,
        }
    })

    const sizeClass = computed(() => {
        return {
            small: 'btn-small',
            medium: 'btn-medium',
            large: 'btn-large'
        }[props.size]
    })

    const colorClass = computed(() => {
        return {
            primary: 'btn-primary',
            secondary: 'btn-secondary',
            success: 'btn-success',
            danger: 'btn-danger',
        }[props.color]
    })
</script>

<style scoped>
    .btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        border: none;
        transition: background 0.2s ease;
    }

    .btn i {
        font-size: 1.2em;
    }

    /* Sizes */
    .btn-small {
        padding: 0.25rem 0.5rem;
        font-size: 0.8rem;
    }

    .btn-medium {
        font-size: 1rem;
    }

    .btn-large {
        padding: 0.75rem 1.5rem;
        font-size: 1.2rem;
    }

    /* Colors */
    .btn-primary {
        background: var(--color-primary);
        color: white;
    }

    .btn-primary:hover {
        background: var(--color-accent);
    }

    .btn-secondary {
        background: var(--color-bg-medium);
        color: white;
    }

    .btn-secondary:hover {
        background: var(--color-primary);
    }

    .btn-success {
        background: var(--color-highlight);
        color: black;
    }

    .btn-success:hover {
        background: var(--color-accent);
    }

    .btn-danger {
        background: #ED2B42;
        color: white;
    }

    .btn-danger:hover {
        background: #c82333;
    }

    .btn:disabled {
        background: var(--color-disabled);
        color: white;
        border-color: #E4E7E8;
        cursor: not-allowed;
    }
</style>
