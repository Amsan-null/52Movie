<template>
  <h1>52영화!</h1>
  <img src="@/assets/logo.png" alt="logo">
  <header>

<div v-if="store.isLogin">
  <nav>
    <RouterLink :to="{ name: 'main' }">홈</RouterLink> |
    <RouterLink :to="{ name: 'recommend' }">영화추천받기</RouterLink> |
    <a href="/" @click="store.logOut">Logout</a> |
    <RouterLink :to="{ name: 'MyProfile' }">마이프로필</RouterLink>
  </nav>
</div>

<div v-else>
  <nav>
    <RouterLink :to="{ name: 'main' }">홈</RouterLink> |
    <RouterLink :to="{ name: 'login' }">로그인</RouterLink> |
    <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
  </nav>
</div>

  </header>

  <RouterView />

</template>

  <script setup>
  import { useCounterStore } from '@/stores/counter'
  const store = useCounterStore()

  </script>


<style scoped>

</style>
