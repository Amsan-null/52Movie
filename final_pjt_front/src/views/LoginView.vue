<template>
    <div>
        <h1>로그인</h1>
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="credentials.username"><br>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="credentials.password" @keypress.enter="login(credentials)">><br>
        <button @click="login(credentials)">로그인</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login: function () {
      axios.post(`http://127.0.0.1:8000/accounts/api-token-auth/`, this.credentials)
      .then((res) => {
        // console.log(res.data.token)
        // localstorage에 jwt 토큰 저장
        localStorage.setItem('jwt', res.data.token)
        // App 컴포넌트한테 로그인 됐습니다를 알려야 함.
        this.$emit('login') // 데이터는 안 담아서 보내도됨 (이벤트(신호)만 알리면 됨)
        this.$router.push({ name: 'Home' })
      })
      .catch((err) => {
        console.log(err)
        alert('회원정보가 존재하지 않습니다! 회원가입 해주세요.')
      })
    },
}
}
</script>

<style scoped>

</style>