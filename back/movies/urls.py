from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:movie_pk>/',views.detail,name="detail"),
    # path('comments/', views.comments, name='comments'),
    path('<int:movie_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('<int:movie_pk>/movie_likes/', views.movie_likes, name='movie_likes'),
    path('<int:comment_pk>/comment_likes/', views.comment_likes, name='comment_likes'),
]

# 영화 좋아요, 코멘트 좋아요 구현 필요