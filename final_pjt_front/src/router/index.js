import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'

import MovieDetailView from '../views/MovieDetailView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import CreateCommentView from '../views/CreateCommentView.vue'
import MyProfilePageView from '../views/MyProfilePageView.vue'
import RecommendMovies from '../views/RecommendMovies.vue'
// import CreateComment from '../views/CreateComment.vue'

// import LoginFormView from '@/views/Accounts/LoginFormView'
// import ProfilePage from '@/views/Profile/ProfilePage'
// import PersonalProfile from '@/views/Profile/PersonalProfile'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainPageView
    },
    // 영화 상세페이지
    {
      path: '/movies/:id',
      name: 'movie_detail',
      component: MovieDetailView
    },
    // 회원가입
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    //로그인
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },

    // 코멘트 생성
    {
      path: '/create',
      name: 'CreateCommentView',
      component: CreateCommentView
    },


    // 내 프로필
    {
      path: '/myProfile',
      name: 'MyProfile',
      component: MyProfilePageView,
    },
    // 상대 프로필
    // {
    //   path: '/profile/:userId',
    //   name: 'PersonalProfile',
    //   component: PersonalProfile
    // },

    {
      path: '/movies/recommend',
      name: 'recommend',
      component: RecommendMovies,
    },

  //   {
  //     path: '/movies/:id/comments',
  //     name: 'comment',
  //     component: CreateComment,
  //   },
  //   {
  //     path: '/movies/:id/:comment_pk',
  //     name: 'CommentDetailView',
  //     component: CommentDetailView,
  //   },
  ]
})

// import { useCounterStore } from '@/stores/counter'

// router.beforeEach((to, from) => {
//   const store = useCounterStore()
//   if (to.name === 'MainPageView' && !store.isLogin) {
//     window.alert('로그인이 필요합니다.')
//     return { name: 'LogInView' }
//   }
//   if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
//     window.alert('이미 로그인 했습니다.')
//     return { name: 'ArticleView' }
//   }
// })


export default router
