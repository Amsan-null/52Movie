<template>
  <div class="movie-list">
    <h1 class="section-title">Popular Movies</h1>
    <div class="movie-container">
      <div v-for="movie in movies" :key="movie.id" class="movie-item">
        <router-link :to="`/movies/${movie.id}`" class="movie-link">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster" class="movie-poster"/>
        </router-link>
        <h3 class="movie-title">{{ movie.title }}</h3>
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
  font-family: 'Jua', sans-serif;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 20px;
  background-color: #e4e4e4; 
  border-radius: 10px; 
  padding: 10px; 
  display: inline-block; 
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

.movie-link {
  text-decoration: none;
  color: inherit;
}

.movie-poster {
  width: 100%;
  border-radius: 10px; 
  overflow: hidden; 
}

.movie-title {
  margin-top: 10px;
  font-size: 1.2rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
