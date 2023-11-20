import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import MyProfilePageView from '../views/MyProfilePageView.vue'
import RecommendMovies from '@/components/RecommendMovies.vue'


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
    },
    {
      path: '/accounts/myProfile',
      name: 'MyProfile',
      component: MyProfilePageView,
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendMovies,
    },


  ]
})


export default router
