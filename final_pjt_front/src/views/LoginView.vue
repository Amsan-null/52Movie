<template>
    <div>
        <h1>로그인</h1>
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="credentials.username"><br>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="credentials.password" @keypress.enter="login(credentials)"><br>
        <button @click="login(credentials)">로그인</button>
    </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useLoginStore } from '../stores/counter';

export default {
  name: 'Login',
  setup(props, { emit }) {
    const router = useRouter();
    const credentials = ref({
      username: '',
      password: '',
    });
    const { doLogin } = useLoginStore()
    const login = async () => {
      try {
        const res = await axios.post(`http://127.0.0.1:8000/accounts/api-token-auth/`, credentials.value);
        localStorage.setItem('jwt', res.data.token);
        emit('login');
        doLogin() // Store -> login -> True
        router.push({ name: 'main' });
      } catch (err) {
        console.error(err);
        alert('존재하지 않는 회원입니다.');
      }
    };

    return {
      credentials,
      login,
    }
  },
};

</script>

<style scoped>

</style>