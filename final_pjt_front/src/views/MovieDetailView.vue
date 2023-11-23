<template>
    <div class="movie-details">
      <div class="left-column">
        <img :src="'https://www.themoviedb.org/t/p/w500/' + movie?.poster_path" alt="poster" class="rounded-image"/>
      </div>
      <div class="right-column">
          <h1>{{ movie?.title }}</h1>
          <h5>★ {{ formatVoteAverage(movie?.vote_average) }}</h5>
          <div class="genre">
        <div v-for="genreId in movie?.genre_ids"> # {{ getGenreName(genreId) }} </div></div>

        <div class="movieinfo">
        <h5>{{ movie?.release_date }} 개봉</h5>
        <h5>{{ movie?.overview }}</h5>
        </div>
  
    </div>
</div>
<CreateCommentView :movie="movie" @commentCreated="handleCommentCreated"/>
  </template>

<script>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import CreateCommentView from './CreateCommentView.vue';
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
        ];
        const getToken = () => {
            const token = localStorage.getItem("jwt");
            return { headers: { Authorization: `Bearer ${token}` } };
        };
        
        onMounted(async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/movies/${movieId}/`, getToken());
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
        
        const handleCommentCreated = (newComment) => {
        // movie.value.write_movie_comment가 배열인지 확인
        if (!Array.isArray(movie.value.write_movie_comment)) {
            movie.value.write_movie_comment = [];
        }

        // 코멘트 객체 생성
        const comment = {
            content: newComment,
        };

        // 코멘트 객체를 배열에 추가
        movie.value.write_movie_comment.push(comment);
        };
        
        return { handleCommentCreated, movie, genres, formatVoteAverage, getGenreName, getToken };
    },
    components: { CreateCommentView,}
};
</script>


<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
.movie-details {
  display: flex;
  justify-content: space-between;
  padding-top: 20px;
  font-family: 'Jua', sans-serif;
}

.left-column {
  flex: 1;
  margin-right: 20px;
  border-radius: 15px; 
  overflow: hidden; 
}

.left-column img {
  max-width: 100%;
  height: auto;
  border-radius: 15px; 
}

.right-column {
  flex: 2;
  background-color: #f0f0f0; 
  border-radius: 15px; 
  padding: 20px; 
  margin-bottom: 10px;
}


.rounded-image {
  border-radius: 15px; 
}

.genre {
  font-size: 17px;
  display: flex;
  flex-direction: row;
  gap: 10px;
  margin-bottom: 15px;
}

.movieinfo > * {
    margin-bottom: 15px;
    letter-spacing: 1px;

}
</style>