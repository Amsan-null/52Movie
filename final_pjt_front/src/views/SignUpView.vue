<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
    <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="passwordConfirmation">
    </div>
    <input type="submit" value="회원가입">
  </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)
const passwordConfirmation = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password.value,
    password2: passwordConfirmation.value
  }
  store.signUp(payload)
}

</script>