<template>
    <!--
        TODO:
        - Add EmptyState
    -->
    <div class="search-bar">
        <input
            v-model.trim="searchKey"
            :placeholder="placeholder"
            type="text"
            class="search-input"
        />
        <Button
            v-if="searchKey"
            icon="close-circle-outline"
            size="small"
            color="secondary"
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
        background-color: var(--color-accent-two);
        padding: 0.5rem 0.75rem;
        border-radius: 8px;
        gap: 0.5rem;
        min-height: 3rem;
        box-sizing: border-box;
        /* handling the scrollbar space */
        /* margin-right: 21px; */
    }

    .search-input {
        flex: 1;
        background: transparent;
        border: none;
        font-size: 1rem;
        outline: none;
        color: var(--color-text);
        max-width: calc(100% - 2rem);
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .search-input::placeholder {
        color: var(--color-text-two);
        /* opacity: 0.6; */
    }
</style>
