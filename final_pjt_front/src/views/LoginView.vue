<template>
  <div class="container mt-5 all-text">
    <div class="card p-5 bg-light">
      <h1 class="text-center mb-4">LOGIN</h1>
      <form @submit.prevent="logIn">
        <div class="mb-3">
          <label for="username" class="form-label">ID:</label>
          <input type="text" v-model.trim="username" class="form-control" id="username" required>
        </div>
        <div class="mb-4">
          <label for="password" class="form-label">PASSWORD:</label>
          <input type="password" v-model.trim="password" class="form-control" id="password" required>
        </div>
        <div class="d-grid">
          <button type="submit" class="btn btn-secondary">LOGIN</button>
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

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style>
.all-text {
  font-family: 'Jua', sans-serif;
}
</style>
