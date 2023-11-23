<template>
  <div class="my-3">
    <h1 class="all_text">Comment</h1>
    <form @submit.prevent="createComment" class="comment-form">
      <div class="mb-3">
        <label for="content" class="form-label all_text">내용:</label>
        <textarea v-model.trim="content" class="form-control" id="content"></textarea>
      </div>
      <button type="submit" class="mt-1 btn btn-secondary float-end all_text">Submit</button>
    </form>
  </div>
  
  <div v-if="movie && movie.write_movie_comment" class="comment-list">
    <div v-if="movie.write_movie_comment.length > 0">
      <div v-for="comment in movie.write_movie_comment" :key="comment.id" class="comment-item">
        <li>
          <span class="all_text">{{ comment.content }}</span>
        </li>
      </div>
    </div>
    <div v-else class="all_text">
      첫 코멘트를 남겨보세요!
    </div>
  </div>
</template>



<script setup>
import { ref, defineProps, defineEmits } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const emits = defineEmits(['commentCreated']);
const content = ref('');
const store = useCounterStore();
const router = useRouter();
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

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Jua&display=swap");
.comment-form {
  margin-bottom: 20px;
}

.all_text {
  font-family: 'Jua', sans-serif;
}
.comment-list {
  margin-top: 80px;
  background-color: #f0f0f0; 
  border-radius: 10px; 
  padding: 10px; 
}

.comment-item {
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 8px;
  background-color: #fff; 
}

.comment-item li {
  list-style: none;
  margin: 0;
  padding: 0;
}

.comment-item span {
  display: block;
}
</style>

