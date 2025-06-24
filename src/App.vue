<template>
    <MainPage />
    <!-- <TestTwo /> -->
</template>


<script setup>
    import MainPage from './components/MainPage.vue';
    // import TestTwo from './components/TestTwo.vue';

</script>


<style>
    html, body, #app {
        height: 100%;
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
