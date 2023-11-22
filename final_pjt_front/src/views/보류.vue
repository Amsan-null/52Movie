<template>
    <div>
        <h1>코멘트 작성</h1>
        <input v-model.trim="content" id="content" type="text" placeholder="commentContent" required="required" />
        <button @click="createComment" id="sendMessageButton" type="submit">작성</button>
    </div>
    <ul>
    <li v-for="comment in store.comments">{{ comment.content }}</li>
  </ul>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useCommentStore } from '../stores/counter';
const store = useCommentStore()
const commentElem = ref('')

const props = defineProps({
  movie: {
    type: Object,
  },
});

const fetchComments = async () => {
  try {
    const response = await axios.get(`http://127.0.0.1:8000/movies/${store.movieId}/comments/`);
    console.log(store)
    console.log(store.movieId)
    store.comments = response.data;
    console.log(store.comments)
    console.log(response.data)
  } catch (err) {
    console.error(err);  
  }
};

onMounted(() => {
  fetchComments()
});

const content = ref('');
const createComment = async function () {
  try {
    store.addComment(commentElem.value);
    const token = localStorage.getItem('jwt')
    await axios.post(`http://127.0.0.1:8000/movies/${props.movie.id}/comments/`, {
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

</script>

<style scoped>

</style>