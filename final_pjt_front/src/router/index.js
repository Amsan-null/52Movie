import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import MyProfilePageView from '../views/MyProfilePageView.vue'
import RecommendMovies from '@/components/RecommendMovies.vue'
import CommentMovies from '@/components/CommentMovies.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    {
      path: '/movie_detail/:movie_id',
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
      path: '/movies/recommend',
      name: 'recommend',
      component: RecommendMovies,
    },
    {
      path: '/movie_detail/:id/comments',
      name: 'comment',
      component: CommentMovies,
    },
    {
      path: '/movie_detail/:id/like/',
      name: 'like',
      component: CommentMovies,
    }

  ]
})


export default router
