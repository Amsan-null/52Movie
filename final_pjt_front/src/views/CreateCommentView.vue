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
    <div v-if="movie && movie.write_movie_comment">
      <div v-for="comment in movie.write_movie_comment" :key="comment.id">
        <li>
        <span>{{ comment.content }}</span>
      </li>

    </div>
  </div>
  <div v-else>아직 코멘트가 없어요</div>


  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue'
  import axios from 'axios'
  import { useCounterStore } from '@/stores/counter'
  import { useRouter } from 'vue-router'

  const emits = defineEmits(['commentCreated'])
  const content = ref('')
  const store = useCounterStore()
  const router = useRouter()
  const props = defineProps({
    movie: {
      type: Object,
    },
  });
  const createComment = async function () {
  await store.commentCreate(props.movie.id, content.value);
  emits('commentCreated', content.value);
};
  
  </script>
  
  <style>
  
  </style>
  