<template>
    <div class="search-bar">
        <input
            class="search-input"
            v-model.trim="searchKey"
            :placeholder="placeholder"
            type="text"
        />
        <Button
            v-if="searchKey"
            icon="close-circle-outline"
            size="small"
            color="sidebar"
            @click="clearSearch"
        />
    </div>
</template>

<script setup>
    import { ref, watch } from 'vue'
    import Button from '../generics/Button.vue'

    const props = defineProps({
        placeholder: {
            type: String,
            default: 'Search...',
        },
    })

    const emit = defineEmits(['update:searchKey'])

    const searchKey = ref('')

    watch(searchKey, (value) => {
        emit('update:searchKey', value)
    })

    function clearSearch() {
        searchKey.value = ''
    }
</script>

<style scoped>
    .search-bar {
        display: flex;
        align-items: center;
        background-color: var(--color-sidebar-item-buttons);
        padding: 0.5rem 0.75rem;
        border-radius: 8px;
        gap: 0.5rem;
        min-height: 3rem;
        box-sizing: border-box;
        /* handling the scrollbar space */
        margin-right: 14px;
    }

    .search-input {
        flex: 1;
        background: transparent;
        border: none;
        font-size: 1rem;
        outline: none;
        max-width: calc(100% - 2rem);
        text-overflow: ellipsis;
        white-space: nowrap;
        color: var(--color-text);
    }

    .search-input::placeholder {
        color: var(--color-text);
    }

    .search-bar :deep(.btn) {
        margin-left: -0.25rem;
    }
</style>
