<template>
    <MainPage />
</template>


<script setup>
    import MainPage from './components/MainPage.vue';
</script>


<style>
    html, body, #app {
        height: 100%;
        overflow: hidden;
        margin: 0;
        box-sizing: border-box;
    }

    *, *::before, *::after {
        box-sizing: inherit;
    }

    #app {
        padding: 1rem;
    }

</style>
