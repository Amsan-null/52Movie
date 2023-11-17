import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `http://localhost:5173/accounts/login/`,
      data: {
        userid, password
      }
    })
    .then(res => {
      consol.log("로그인 완료")
    })
    .catch(err => consol.log(err))
    
  }

  const signup = function (payload) {
    const { username, nickname, password } = payload

    axios({
      method: 'post',
      url: `http://localhost:5173/accounts/signup/`,
      data: {
        userid, nickname, password
      }
    })
    .then(res => {
      consol.log("회원가입 완료")
    })
    .catch(err => consol.log(err))
  }

  return { }
})
