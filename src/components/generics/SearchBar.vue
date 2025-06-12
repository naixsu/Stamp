<template>
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
        background-color: var(--color-bg-medium);
        padding: 0.5rem 0.75rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        gap: 0.5rem;
        min-height: 3rem;
        box-sizing: border-box;

         /* handling the scrollbar space */
        margin-right: 18px;
    }

    .search-input {
        flex: 1;
        background: transparent;
        border: none;
        color: white;
        font-size: 1rem;
        outline: none;
    }
</style>
