from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:pk>/delete',views.delete,name="delete"),
    path('<int:pk>/update',views.update,name="update"),
    path('create/',views.create,name="create"),
    path('<int:pk>/',views.detail,name="detail"),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/<int:comment_pk>/comments/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/likes/', views.likes, name='likes'),
    path('<username>/like_list/', views.like_list, name='like_list'),
]
