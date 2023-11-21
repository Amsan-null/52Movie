import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLoginStore = defineStore('login', () => {
  const isLogin = ref(false)
  const doLogin = () => {
    isLogin.value = true
  }
  return { isLogin, doLogin }
}, { persist: true })

export const useCommentStore = defineStore('comment', () => {
  const comments = ref([]);

  const addComment = function (commentElem) {
    comments.value.push({
      content: commentElem
    });
  }

  return { addComment, comments }; }, {persist: true})
