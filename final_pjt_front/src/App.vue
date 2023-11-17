<template>
  <h1>52영화!</h1>
  <header>

<div v-if="!isLogin">
  <h2>비로그인시보이는화면</h2>
  <nav>
    <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
    <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
  </nav>
</div>
<div v-else>
  <h2>로그인시보이는화면</h2>
  <nav>
    <!-- <RouterLink :to="{ name: 'logout' }">로그아웃</RouterLink> -->
    <RouterLink :to="{ name: 'mypage' }">마이페이지</RouterLink>
  </nav>
</div>
  </header>

  <RouterView />
</template>

  <script setup>
  import { ref, onMounted } from "vue";
  import { RouterLink, RouterView } from 'vue-router'

  const isLogin = ref(false);

  </script>


<style scoped>

</style>
