from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/',views.detail,name="detail"),
    path('<int:pk>/comments/', views.comment_index, name='comment_index'),
    # path('<int:pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path('<int:pk>/<int:comment_pk>/comments/', views.comment_delete, name='comment_delete'),
    # path('<int:pk>/<int:comment_pk>/comments)
    # path('<int:movie_pk>/likes/', views.likes, name='likes'),
    # path('<username>/like_list/', views.like_list, name='like_list'),
]
