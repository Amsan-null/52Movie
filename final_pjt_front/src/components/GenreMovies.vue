<template>
    <div>
        <h1>장르별 추천</h1>
        <h2>{{ genres.name }}</h2>
    <img :src="movieImage" alt="poster_path" >
    </div>
</template>

<script setup>
import MovieDetailView from './MovieDetailView.vue';

const props = defineProps(['movie']);

const movieImage = computed(() => {
  return `https://image.tmdb.org/t/p/w500/${props.movie.poster_path}`;
});
</script>

<style scoped>

</style>