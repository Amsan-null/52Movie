<template>
  <div>
    <img :src="'https://www.themoviedb.org/t/p/w500/' + movie?.poster_path" alt="poster"/>
    <h1>{{ movie?.title }}</h1>
    <!-- <h5>장르: <div v-for = "genre in movie.genre_ids"> {{ genre.name }}</div> -->
    <!-- </h5> -->
    <h5>평점 : {{ formatVoteAverage(movie?.vote_average) }}</h5>
    <h5>개봉 일자 : {{ movie?.release_date }}</h5>
    <h5>{{ movie?.overview }}</h5>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

export default {
  setup() {
    const movie = ref(null);
    const route = useRoute();
    const movieId = route.params.id; 

    const formatVoteAverage = (voteAverage) =>  {
      // 평점은 소수점 첫째자리까지 반올림
      if (voteAverage !== null) {
        return Math.round(voteAverage * 10) / 10;
      } else {
        return null;
      }
    }

    // 장르 정의 


    // genre_ids라는 배열을 받아서 하나씩 name으로 출력?

  //   function getGenreNamesByIds(genre_ids) {
  // // genre_ids에 해당하는 name을 찾아 배열로 만듦
  // const genreNames = genre_ids.map(genre_id => {
  //   const foundGenre = movies_genre.find(genre => genre.genre_id === genre_id);
  //   return foundGenre ? foundGenre.name : ''; // 일치하는 genre가 없으면 빈 문자열 반환
  // });

  // // 배열을 ','로 join하여 문자열로 합침
  // const result = genreNames.join(', ');

  // return result;

  onMounted(async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/movies/${movieId}/`);
        if (!response.data) {
          throw new Error('영화 정보를 찾을 수 없습니다.');
        }

        movie.value = response.data;
      } catch (error) {
        console.error('영화 정보를 가져오는 중 에러 발생:', error.message);
      }
    });

    return { movie, formatVoteAverage };
  },
};
</script>


<style scoped>

</style>
