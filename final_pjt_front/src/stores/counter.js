import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const comments = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${pk}/comment/`,
      data: {
        content
      }
    })
    .then(res => detailMovie.write_movie_comment.push(res.data))
    .catch(err => console.log(err))
  }

  const detailMovie = ref([])
  const getDetailMovie = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${pk}`
    })
    .then(res => detailMovie.value = res.data)
    .catch(err => console.log(err))
  }

  const getComments = function () {
    axios({
      method: 'get',
      url: `${API_URL}/movies/${movie_id}/comments`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { commentCreate, getDetailMovie, detailMovie, comments, API_URL, getComments, signUp, logIn, token, isLogin, logOut }
}, { persist: true })

