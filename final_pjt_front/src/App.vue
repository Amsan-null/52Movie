<template>
  <div class="container p-3 all-text">
    <header>

      <nav class="navbar navbar-expand-lg navbar-dark fixed-top bg-secondary">
        
        
        <div v-if="store.isLogin" class="collapse navbar-collapse justify-content-end">
          <ul class="navbar-nav">
            <router-link class="navbar-brand" :to="{ name: 'main' }">Home</router-link>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'recommend' }">Recommned</router-link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/" @click="store.logOut">Logout</a>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'MyProfile' }">Mypage</router-link>
            </li>
          </ul>
        </div>

        <div v-else class="collapse navbar-collapse justify-content-end">
          <ul class="navbar-nav">
            <router-link class="navbar-brand" :to="{ name: 'main' }">Home</router-link>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }">Sign up</router-link>
            </li>
          </ul>
        </div>

      </nav>

    </header>

    <router-view />

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
</script>

<style>
/* body {
  background-color: rgb(43, 43, 43);
} */


h1 {
  font-size: 2.5rem;
  text-align: left;
}


h1.my-4 {
  margin-top: 40px; 
}


img {
  display: block;
}


header {
  padding: 20px 0;
}

.navbar .nav-link {
  color: white;
}


.navbar .nav-link:hover {
  color: rgb(255, 218, 7); 
}

.navbar-nav .nav-item {
  margin-right: 10px;
}

.all-text {
  font-family: 'Jua', sans-serif;
}

</style>
