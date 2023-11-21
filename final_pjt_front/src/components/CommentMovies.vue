<template>
    <div>
        <h4>코멘트</h4>
        <form @submit.prevent="createComment">
        <input type="text" v-model="commentElem">
        <input type="submit">
        </form>
    </div>

    <li v-for="comment in comments">{{ comment.user.username }} - {{ comment.content }}</li>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { storeToRefs } from 'pinia';
import { useCommentStore } from '../stores/counter';

// const movieId = route.params.id;
const route = useRoute();
const store = useCommentStore()
const commentElem = ref('')
const comments = ref([]);
store.movieId = route.params.id;

const fetchComments = async () => {
  try {
    const route = useRoute();  // setup 함수 내부에서 호출합니다.
    store.movieId = route.params.id;  // URL의 파라미터에서 영화의 ID를 가져옵니다.
    const response = await axios.get(`http://127.0.0.1:8000/movies/${store.movieId}/comments/`);
    comments.value = response.data;
  } catch (err) {
    console.error(err);  // 에러를 콘솔에 출력합니다.
  }
};

onMounted(fetchComments);

const createComment = async function () {
  try {
    store.addComment(commentElem.value);
    await axios.post(`http://127.0.0.1:8000/movies/${store.movieId}/comments/`, {
      content: commentElem.value,
    }, {headers: {
        Authorization: `Bearer ${store.jwtToken}`,  // JWT 토큰을 헤더에 포함합니다.
      },
  });

    commentElem.value = '';
    await fetchComments();  // 댓글을 생성한 후에 댓글 목록을 다시 불러옵니다.
  } catch (err) {
    console.error(err)
  }
}
</script>

<style scoped>

</style>