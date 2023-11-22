from django.urls import path
from . import views
from .views import RandomMoviesView


app_name = 'movies'
urlpatterns = [
    path('',views.movies,name="index"),
    path('<int:movie_pk>/',views.movie_detail,name="detail"),
    # path('recommend/', views.recommend),
    path('<int:movie_pk>/comment/', views.comment_create_with_movie), # 댓글생성
    path('<int:movie_pk>/comments/', views.comment_list, name='comments'),

    # path('<int:my_pk>/<movie_pk>/like/', views.movie_like),
    # path('<int:my_pk>/like/', views.my_movie_like),
    # path('<int:my_pk>/like/users/', views.like_movie_users),

    path('<int:movie_pk>/like/', views.movie_like), # 영화 좋아요 등록 및 해제(좋아요 수까지 출력)

    # path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path('<int:pk>/<int:comment_pk>/comments/', views.comment_delete, name='comment_delete'),
    # path('<int:pk>/<int:comment_pk>/comments)
    # path('<int:movie_pk>/like/', views.movie_like, name='like'),
    # path('<int:movie_pk>/like/users/', views.like_movie_users),
    path('random/', RandomMoviesView.as_view()),
]
