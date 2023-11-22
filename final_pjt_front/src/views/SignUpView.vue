<template>
  <div>
    <h1>Signup</h1>
    <form @submit.prevent="signUp">
    <div>
      <label for="username">아이디: </label>
      <input type="text" id="username" v-model="username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="passwordConfirmation">
    </div>
    <input type="submit" value="회원가입">
  </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router';
// import axios from 'axios';
// import { storeToRefs } from 'pinia';

const router = useRouter()
const store = useCounterStore()
const username = ref(null)
const password = ref(null)
const passwordConfirmation = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password.value,
    password2: passwordConfirmation.value
  }
  store.signUp(payload)
}
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




// export default {
//   name: 'Signup',
//   setup() {
//     const router = useRouter();
//     const credentials = ref({
//       username: '',
//       password: '',
//       passwordConfirmation: '',
//     });

//     const signup = async () => {
//       try {
//         const response = await axios.post('http://127.0.0.1:8000/accounts/signup/', credentials.value);
//         console.log(response);
//         router.push({ name: 'login' });
//       } catch (error) {
//         console.error(error);
//         alert('회원가입에 실패하였습니다.');
//       }
//     };

//     return {
//       credentials,
//       signup,
//     };
//   },
// };

</script>