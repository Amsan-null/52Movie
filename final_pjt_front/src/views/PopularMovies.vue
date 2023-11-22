<template>
  <div class="movie-list">
    <h1>인기 영화들</h1>
    <div class="movie-container">
      <div v-for="movie in movies" :key="movie.id" class="movie-item">
        <router-link :to="`/movies/${movie.id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
        </router-link>
        <h3>{{ movie.title }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import axios from 'axios';

export default defineComponent({
  components: {
    RouterLink,
  },
  setup() {
    const movies = ref([]);

    onMounted(async () => {
      const response = await axios.get('http://127.0.0.1:8000/movies/random/');
      movies.value = response.data;
    });

    return { movies };
  },
});
</script>

<style scoped>
.movie-list {
  margin: 20px;
}

.movie-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.movie-item {
  width: 200px;
  text-align: center;
}
</style>
