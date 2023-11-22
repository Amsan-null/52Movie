<template>
    <div>
      <h1>코멘트 작성</h1>
      <form @submit.prevent="createComment">
        <div>
          <label for="content">내용:</label>
          <textarea v-model.trim="content" id="content"></textarea>
        </div>
        <input type="submit">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'
  
  const content = ref('')
  const store = useCounterStore()
  const router = useRouter()
  const props = defineProps({
    movieId: Number
});
const createComment = function () {
  store.commentCreate(props.movieId, content.value)
}
  // const createComment = function () {
  //   axios({
  //     method: 'post',
  //     url: `${store.API_URL}/movies/${props.movieId}/comment/`,
  //     data: {
  //       content: content.value
  //     },
  //     headers: {
  //       Authorization: `Token ${store.token}`
  //     }
  //   })
  //   // console.log(content)
  //     .then((res) => {
  //       router.push({ name: 'MovieDetailView' })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }
  
  
  
  </script>
  
  <style>
  
  </style>
  