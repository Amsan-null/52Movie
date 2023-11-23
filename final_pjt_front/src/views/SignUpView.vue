<template>
  <div class="container mt-5 all-text">
    <div class="card p-5 bg-light">
      <h1 class="text-center mb-4">회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="mb-3">
          <label for="username" class="form-label">아이디:</label>
          <input type="text" id="username" v-model="username" class="form-control" required>
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">비밀번호:</label>
          <input type="password" id="password" v-model="password" class="form-control" required>
        </div>
        <div class="mb-4">
          <label for="passwordConfirmation" class="form-label">비밀번호 확인:</label>
          <input type="password" id="passwordConfirmation" v-model="passwordConfirmation" class="form-control" required>
        </div>
        <div class="d-grid">
          <button type="submit" class="btn btn-secondary btn-block">회원가입</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const username = ref(null);
const password = ref(null);
const passwordConfirmation = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password.value,
    password2: passwordConfirmation.value,
  };
  store.signUp(payload);
};
</script>

<style>
.all-text {
  font-family: 'Jua', sans-serif;
}
</style>
