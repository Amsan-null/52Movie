<template>
  <h1>52영화!</h1>
  <header>

<div v-if="isLogin">
  <h2>로그인시보이는화면</h2>
  <nav>
    <RouterLink :to="{ name: 'main' }">홈</RouterLink> |
    <RouterLink :to="{ name: 'recommend' }">영화추천받기</RouterLink> |
    <RouterLink @click.native="logout" to="/">로그아웃</RouterLink> |
    <RouterLink :to="{ name: 'MyProfile' }">마이프로필</RouterLink>
  </nav>
</div>

<div v-else>
  <h2>비로그인시보이는화면</h2>
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
  import { ref, onMounted, watch } from "vue";
  import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useLoginStore } from "./stores/counter";
import { storeToRefs } from "pinia";


const loginStore = useLoginStore()
// const { isLogin } = loginStore
const { isLogin } = storeToRefs(loginStore)

// const isLogin = ref(false);
  const router = useRouter();

  const logout = function() {
    isLogin.value = false;
    localStorage.removeItem('jwt');
    router.push({ name: 'Login' });
}

const checkJwt = () => {
  const jwtToken = localStorage.getItem('jwt');
      if (jwtToken) {
          router.push({ name: 'main' });
      }
}

  onMounted(() => {
    checkJwt()
  });

  watch(isLogin, (newVal) => {
  if (newVal) {
    router.push({ name: 'main' });
  }
});

  </script>


<style scoped>

</style>
