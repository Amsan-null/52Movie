import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/movie_detail/:id',
      name: 'movie_detail',
      component: MovieDetailView
    },
    {
      path: '/accounts/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/accounts/login',
      name: 'login',
      component: LoginView
    }

  ]
})

export default router
