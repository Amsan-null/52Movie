<template>
    <div>
        <h1>로그인</h1>
        <form @submit.prevent="LogIn">
            <label for="id">아이디: </label>
            <input type="text" id="userid" v-model.trim="userid"><br>
            <label for="id">닉네임: </label>
            <input type="text" id="nickname" v-model.trim="nickname"><br>
            <label for="id">비밀번호: </label>
            <input type="password" id="password" v-model.trim="password"><br>
            <input type="submit" value="가입하기">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '../stores/counter';

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const LogIn = function () {
    const payload = {
      username: username.value,
      password: password.value,
    }
    store.login(payload)
  }
</script>

<style scoped>

</style>