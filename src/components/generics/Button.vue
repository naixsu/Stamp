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
            small: 'btn-sm',
            medium: 'btn-md',
            large: 'btn-lg'
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
        background: #007bff;
        color: white;
    }

    .btn-primary:hover {
        background: #0056b3;
    }

    .btn-secondary {
        background: #6c757d;
        color: white;
    }

    .btn-secondary:hover {
        background: #5a6268;
    }

    .btn-success {
        background: #28a745;
        color: white;
    }

    .btn-success:hover {
        background: #218838;
    }

    .btn-danger {
        background: #dc3545;
        color: white;
    }

    .btn-danger:hover {
        background: #c82333;
    }

    .btn:disabled {
        background: #FAFAFA;
        color: #6D7679;
        border-color: #E4E7E8;
        cursor: not-allowed;
    }
</style>