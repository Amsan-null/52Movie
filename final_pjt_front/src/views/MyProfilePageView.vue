<template>
    <div id="app">
    <h2>{{ user.username }}님의 마이프로필</h2>
    <hr>
    <h2>{{ user.username }}님이 좋아요한 영화</h2>

    <div v-for = "(movie, idx) in my_like_movies" :key="idx">
    <MovieCard :movie="movie" />
    </div>

    <h2>{{ user.username }}님의 코멘트</h2>
    <h2 v-for="(comment, idx) in comments" :key="idx">
      [{{ comment.movie_title }}] -
      {{ comment.content }}</h2>
    </div>
</template>

<script>
import axios from 'axios'
import MovieCard from "@/components/MovieCard"

export default {
  name: "MyProfile",
  data: function () {
    return { 
      like_movies: [],
      comments: [],
      user: '',
    }
  },
  components: {
    MovieCard,
  },
   methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },

     getMyName: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`http://127.0.0.1:8000/accounts/myprofile/`, info, config)
      .then( (res) => {
        this.user = res.data
        this.like_movies = res.data.like_movies

       // 무비pk 부분 고치기
        axios.get(`http://127.0.0.1:8000/movies/${movie_pk}/review/${this.user.id}`, config)
        
        .then( (res) => {
          this.reviews = res.data
          
        
        })
      })

    },
    getMovieDatas: function () {
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then( (res) => {
        for(var i = 0; i < this.like_movies.length; i++){
          this.my_like_movies.push(res.data[this.like_movies[i]-1])
        }

      })
    },
     getComments: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post(`http://127.0.0.1:8000/accounts/myprofile/`, info, config)
      
      .then( (res) => {
        this.user = res.data
        
        axios.get(`http://127.0.0.1:8000/comments/`, config)
        
        .then( (res) => {
          
          this.comments = res.data
          
        
        })
      })
     
   },
  created: function () {
    this.getMyName()
    this.getMovieDatas()
    this.getComments()
   
  },
  
}
}

</script>

<style scoped>

</style>