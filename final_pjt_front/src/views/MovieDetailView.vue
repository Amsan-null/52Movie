<template>
  <div>
    <img :src="'https://www.themoviedb.org/t/p/w500/' + movie?.poster_path" alt="poster"/>
    <h1>{{ movie?.title }}</h1>

    <!-- <button v-if="movie?.is_liked" @click="like">좋아요 취소</button>
    <button v-else @click="like">좋아요</button> -->
    <div>
        <span>
          <div v-if="is_liked">
            <button
            @click="likeMovie"
            >
            좋아요 취소
            </button>
          </div>
          <div v-else>
            <button
            @click="likeMovie">좋아요</button>
          </div>
        </span>
      </div>


    <h5 v-for = "genreId in movie?.genre_ids"> # {{ getGenreName(genreId) }} </h5>
    <h5>평점 : {{ formatVoteAverage(movie?.vote_average) }}</h5>
    <h5>개봉 일자 : {{ movie?.release_date }}</h5>
    <h5>{{ movie?.overview }}</h5>
    <CommentMovies/>
  </div>

</template>

<script>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import CommentMovies from '../components/CommentMovies.vue';
import { useUserStore } from '../stores/counter';

export default {
    setup() {
        const movie = ref(null);
        const route = useRoute();
        const movieId = route.params.id;
        const formatVoteAverage = (voteAverage) => {
            // 평점은 소수점 첫째자리까지 반올림
            if (voteAverage !== null) {
                return Math.round(voteAverage * 10) / 10;
            }
            else {
                return null;
            }
        };
        const getGenreName = (genreId) => {
            const genre = genres.find((g) => g.id === genreId);
            return genre ? genre.name : "";
        };

        // 장르 정의 
        const genres = [
            {
                "id": 28,
                "name": "액션"
            },
            {
                "id": 12,
                "name": "모험"
            },
            {
                "id": 16,
                "name": "애니메이션"
            },
            {
                "id": 35,
                "name": "코미디"
            },
            {
                "id": 80,
                "name": "범죄"
            },
            {
                "id": 99,
                "name": "다큐멘터리"
            },
            {
                "id": 18,
                "name": "드라마"
            },
            {
                "id": 10751,
                "name": "가족"
            },
            {
                "id": 14,
                "name": "판타지"
            },
            {
                "id": 36,
                "name": "역사"
            },
            {
                "id": 27,
                "name": "공포"
            },
            {
                "id": 10402,
                "name": "음악"
            },
            {
                "id": 9648,
                "name": "미스터리"
            },
            {
                "id": 10749,
                "name": "로맨스"
            },
            {
                "id": 878,
                "name": "SF"
            },
            {
                "id": 10770,
                "name": "TV 영화"
            },
            {
                "id": 53,
                "name": "스릴러"
            },
            {
                "id": 10752,
                "name": "전쟁"
            },
            {
                "id": 37,
                "name": "서부"
            }
        ]
    
    const getToken = () => {
      const token = localStorage.getItem('jwt');
      return { headers: { Authorization: `Bearer ${token}` } };
    };

    const like = async () => {

    const token = localStorage.getItem('jwt');
      if (!token) {
        alert('로그인이 필요한 기능입니다.');
        return;
      }

      try {
        // 서버에 좋아요 요청을 보냅니다.
        const response = await axios.post(`http://127.0.0.1:8000/movies/${movieId}/like/`, {}, {
          headers: {
            Authorization: `Bearer ${token}`,  // JWT 토큰을 헤더에 포함합니다.
          },
        });

        // 성공적으로 좋아요를 했다면, 좋아요 상태를 업데이트합니다.
        if (response.data === 'like') {
          movie.value.is_liked = true;
        } else {
          movie.value.is_liked = false;
        }
      } catch (err) {
        console.error(err);
      }
    };


        onMounted(async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/movies/${movieId}/`,getToken());
                if (!response.data) {
                    throw new Error("영화 정보를 찾을 수 없습니다.");
                }
                movie.value = response.data;
                movie.value.is_liked = response.data.likes ? response.data.likes.includes(userId) : false;
            }
            catch (error) {
                console.error("영화 정보를 가져오는 중 에러 발생:", error.message);
            }
        });
        return { movie, genres, like, formatVoteAverage, getGenreName, getToken };
    },
    components: { CommentMovies }
};
</script>


<style scoped>

</style>
