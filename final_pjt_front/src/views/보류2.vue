<template>

  <div>
    <h4>코멘트</h4>
    <form @submit.prevent="createComment">
      <input type="text" v-model="commentElem">
      <input type="submit">
    </form>

    <ul>
      <li v-for="comment in store.comments">

        {{ comment.content }}
        <!-- <button @click="updateComment(comment.id)">수정</button>
        <button @click="deleteComment(comment.id)">삭제</button> -->
      </li>
    </ul>
  </div>

    
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCommentStore } from '../stores/counter';

const route = useRoute();
const store = useCommentStore()
const commentElem = ref('')
store.movieId = route.params.id;

const fetchComments = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/movies/${store.movieId}/comments/`);
    store.comments = response.data;
  } catch (err) {
    console.error(err);  
  }
};
onMounted(() => {
  fetchComments()
});

const createComment = async function () {
  try {
    store.addComment(commentElem.value);
    const token = localStorage.getItem('jwt')
    await axios.post(`http://127.0.0.1:8000/movies/${store.movieId}/comments/`, {
      content: commentElem.value,
    }, {headers: {

        Authorization: `Bearer ${token}`,  // JWT 토큰을 헤더에 포함합니다.
      },
    });

    commentElem.value = '';
    await fetchComments();  // 댓글을 생성한 후에 댓글 목록을 다시 불러옵니다.
  } catch (err) {
    console.error(err)
  }
}

// const deleteComment = async function (commentId) {
//   try {
//     const token = localStorage.getItem('jwt') // 로컬 스토리지에서 토큰을 가져옵니다.
//     await axios.delete(`http://127.0.0.1:8000/movies/${store.movieId}/comments/${commentId}/`, {
//       headers: {
//         Authorization: `Bearer ${token}`,  // JWT 토큰을 헤더에 포함합니다.
//       },
//     });
//     await fetchComments();  // 댓글을 삭제한 후에 댓글 목록을 다시 불러옵니다.
//   } catch (err) {
//     console.error(err)
//   }
// }

// const updateComment = async function (commentId) {
//   try {
//     const token = localStorage.getItem('jwt') // 로컬 스토리지에서 토큰을 가져옵니다.
//     const newContent = prompt('새로운 댓글 내용을 입력하세요.');
//     if (newContent) {
//       await axios.put(`http://127.0.0.1:8000/movies/${store.movieId}/comments/${commentId}/`, {
//         content: newContent,
//       }, {
//         headers: {
//           Authorization: `Bearer ${token}`,  // JWT 토큰을 헤더에 포함합니다.
//         },
//       });
//       await fetchComments();  // 댓글을 수정한 후에 댓글 목록을 다시 불러옵니다.
//     }
//   } catch (err) {
//     console.error(err)
//   }
// }
</script>

<style scoped>

</style>