<!-- <template>
    <div>

    </div>
</template>

<script>
import { reactive, toRefs, onMounted } from 'vue'
import axios from 'axios'
import * as jwtDecode from "jwt-decode";


export default {
  name: 'CommunityDetail',
  props: {
    comment_pk: Number,
  },
  setup(props) {
    const data = reactive({
      comment_content: '',
      comments: [Array, Object],
      user: [],
    })

    const getToken = () => {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    }

    const getMyName = () => {
      const config = getToken()
      const hash = localStorage.getItem('jwt')
      const info = jwtDecode(hash);
      axios.post(`http://127.0.0.1:8000/accounts/myProfile/`, info, config)
      .then( (res) => {
        data.user = res.data
      })
      .catch( (err) => {
        console.log(err)
      })
    }

    const getComments = () => {
      const config = getToken()
      const movie_pk = this.$route.params.movie_pk
      axios.get(`http://127.0.0.1:8000/movie_detail/${movie_pk}/comments/`, config)
        .then((res) => {
          data.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }

    const createComment = () => { 
      const config = getToken()
      const commentItem = {
        content: data.comment_content,
      }
      if (commentItem.content) {
          axios.post(`http://127.0.0.1:8000/movie_detail/${this.$route.params.movie_pk}/comments/`, commentItem, config)
          .then( () => {
            getComments()
            data.comment_content = ''
          })
          .catch((err) => {
            console.log(err)
          })
        }
    }

    const deleteComment = (movie, comment) => {
      const config = getToken()
      if(data.user.username === comment.userName){
        axios.delete(`http://127.0.0.1:8000/movie_detail/${movie.id}/comments/${comment.id}/`, config)
          .then((res) => {
            if (res) {
              alert("삭제되었습니다.")
              getComments()
            }
          })
      }
      else{
        alert("본인이 작성한 댓글만 삭제 가능합니다.")
      }
    }

    onMounted(() => {
      getComments()
      getMyName()
    })

    return {
      ...toRefs(data),
      createComment,
      deleteComment,
      getComments,
      getMyName,
      getToken
    }
  }
}

</script>

<style scoped>

</style> -->

<template>
  <li>
    <span>{{ comment.content }}</span>
  </li>
</template>

<script setup>
// import { useCounterStore } from '@/stores/counter'
// import CommentListItemView from './CommentListItemView.vue';

const props = defineProps({
    comment: Object
});


</script>
