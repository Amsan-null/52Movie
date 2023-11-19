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
    <RouterLink @click.native="logout" to="#">로그아웃</RouterLink>
    <RouterLink :to="{ name: 'MyProfile' }">마이프로필</RouterLink>
  </nav>
</div>
  </header>

  <RouterView />
</template>

  <script setup>
  import { ref, onMounted } from "vue";
  import { RouterLink, RouterView } from 'vue-router'

  const isLogin = ref(false);

  const logout = function() {
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
  }

  // const created =  function () {
  //   const token = localStorage.getItem('jwt')
  //   if (token) {
  //     this.isLogin = true
  //   }
  // }





  </script>


<style scoped>

</style>
