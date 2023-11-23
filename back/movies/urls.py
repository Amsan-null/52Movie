from django.urls import path
from . import views
from .views import RandomMoviesView


app_name = 'movies'
urlpatterns = [
    path('',views.movies,name="index"),
    path('<int:movie_pk>/',views.movie_detail,name="detail"),
    path('<int:movie_pk>/comment/', views.comment_create_with_movie), # 댓글생성
    path('<int:movie_pk>/comments/', views.comment_list), # 댓글조회
    path('random/', RandomMoviesView.as_view()),
]
