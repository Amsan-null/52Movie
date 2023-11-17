
<template>
  <h1>52영화!</h1>
  <header>

<div v-if="!isLogin">
  <nav>
    <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
    <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>
  </nav>
</div>
<v-else>
  <nav>
    <RouterLink :to="{ name: 'logout' }">로그아웃</RouterLink>
    <RouterLink :to="{ name: 'mypage' }">마이페이지</RouterLink>
  </nav>
</v-else>
  </header>

  <RouterView />
</template>

  <script setup>
  import { computed } from "@vue/reactivity";
  import { ref, onMounted } from "vue";
  import { RouterLink, RouterView } from 'vue-router'

  const app = createApp({
    setup() {
      const isLogin = ref(false)
    }
  })
  </script>


<style scoped>

</style>
