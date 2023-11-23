<template>
    <div>
        <h5>당신을 위한 장르별 인기영화추천</h5>
        <h1>이런 영화들은 어때요?</h1>
    </div>

<div v-if="horror && horror.length">
    <h2>공포</h2>
      <div class="movie-container">
        <div v-for="(movie,index) in horror" :key="index">
          <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
          </router-link>
          <p>{{ movie.title }}</p>
        </div>
      </div>
    </div>

    
    <div v-if="romance && romance.length">
      <h2>로맨스</h2>
      <div class="movie-container">
        <div v-for="(movie,index) in romance" :key="index">
          <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
        </router-link>
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
  
  <div v-if="action && action.length">
    <h2>액션</h2>
    <div class="movie-container">
      <div v-for="(movie,index) in action" :key="index">
          <router-link :to="`/movies/${movie.movie_id}`">
            <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
          </router-link>
          <p>{{ movie.title }}</p>
        </div>
      </div>
    </div>

    <div v-if="comedy && comedy.length">
      <h2>코미디</h2>
      <div class="movie-container">
        <div v-for="(movie,index) in comedy" :key="index">
          <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
        </router-link>
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
  
  <div v-if="music && music.length">
    <h2>음악</h2>
    <div class="movie-container">
      <div v-for="(movie,index) in music" :key="index">
        <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
        </router-link>
        <p>{{ movie.title }}</p>
      </div>
    </div>
  </div>
  
  <div v-if="thriller && thriller.length">
    <h2>스릴러</h2>
    <div class="movie-container">
        <div v-for="(movie,index) in thriller" :key="index">
          <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
          </router-link>
          <p>{{ movie.title }}</p>
        </div>
      </div>
  </div>

  <div v-if="SF && SF.length">
    <h2>SF</h2>
    <div class="movie-container">
      <div v-for="(movie,index) in SF" :key="index">
        <router-link :to="`/movies/${movie.movie_id}`">
          <img :src="'https://www.themoviedb.org/t/p/w200/' + movie.poster_path" alt="poster"/>
        </router-link>
          <p>{{ movie.title }}</p>
        </div>
      </div>
    </div>


</template>

<script>
import { onMounted, ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const horror = ref([]);
    const action = ref([]);
    const comedy = ref([]);
    const fantasy = ref([]);
    const romance = ref([]);
    const music = ref([]);
    const SF = ref([]);
    const thriller = ref([]);

    const allMovies = ref([])
    const getToken = () => {
            const token = localStorage.getItem("jwt");
            return { headers: { Authorization: `Bearer ${token}` } };
        };
    onMounted(async () => {
      try {

        const response = await axios.get(`http://127.0.0.1:8000/movies/random/`, getToken());
        const allMovies = response.data;
        
        for (const movie of allMovies) {

            if (movie.genre_ids.includes(27)) {
              horror.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(28)) {
              action.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(35)) {
              comedy.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(14)) {
              fantasy.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(10402)) {
              music.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(10749)) {
              romance.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(878)) {
              SF.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }

            if (movie.genre_ids.includes(53)) {
              thriller.value.push({ 
                title: movie.title,
                movie_id: movie.id,
              poster_path: movie.poster_path
            
            });
            }


        }
      } catch (error) {
        console.error('Failed to fetch movies:', error.message);
      }
    });
    return { horror,action, comedy, fantasy, romance, music, SF, thriller}
  }
  
};


</script>

<style scoped>
.movie-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
</style>