<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation">
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>

<script>

// async function get_JWT_token() {
//   try {
//       const response = await fetch('http://127.0.0.1:8000/api-token-auth/', {
//           method: "POST",
//           headers: {
//               "Content-Type": "application/json"
//           },
//           body: JSON.stringify(userdata)
//       });
//       const data = await response.json();
//       const token = data["token"];
//       console.log(token);
//       return token;
//   } catch (error) {
//       console.log('error');
//   }
// };

// async function call_api() {
//   let api_token = await get_JWT_token();
//   const token = api_token;
//   const called_api = await fetch('http://127.0.0.1:8000/test/api/', {
//           method: "GET",
//           headers: {
//               "Content-Type": "application/json",
//               "Authorization": "JWT " + token
//           }
//       });
//   const api_result = await called_api.json();
//   return api_result;
// };

import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  name: 'Signup',
  setup() {
    const router = useRouter();
    const credentials = ref({
      username: '',
      password: '',
      passwordConfirmation: '',
    });

    const signup = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', credentials.value);
        console.log(response);
        router.push({ name: 'login' });
      } catch (error) {
        console.error(error);
        alert('회원가입에 실패하였습니다.');
      }
    };

    return {
      credentials,
      signup,
    };
  },
};

</script>