from django.urls import path
from . import views
from .views import RandomMoviesView


app_name = 'movies'
urlpatterns = [
    path('',views.movies,name="index"),
    path('<int:movie_pk>/',views.detail,name="detail"),
    path('recommend/', views.recommend),

    path('<int:my_pk>/<movie_pk>/like/', views.movie_like),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),

    path('<int:movie_pk>/comments/', views.comments, name='comments'),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path('<int:pk>/<int:comment_pk>/comments/', views.comment_delete, name='comment_delete'),
    # path('<int:pk>/<int:comment_pk>/comments)
    # path('<int:movie_pk>/like/', views.movie_like, name='like'),
    # path('<int:movie_pk>/like/users/', views.like_movie_users),
    path('random/', RandomMoviesView.as_view()),
]

# 영화 좋아요, 코멘트 좋아요 구현 필요