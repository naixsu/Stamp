<template>
    <h1>Testing</h1>
    <body>
        {{ testMessage }}
    </body>
    <p>{{ message }}</p>
</template>

<script setup>
    import { ref, onMounted } from 'vue'

    const props = defineProps(['testMessage'])
    const message = ref('Loading...')

    onMounted(async () => {
        const res = await fetch('http://127.0.0.1:8000/api/hello/')
        const data = await res.json()
        message.value = data.message
    })
</script>

<style scoped>

</style>
