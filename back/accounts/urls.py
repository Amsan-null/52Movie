from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('api-token-auth/', obtain_jwt_token, name='token'),
    path('signup/', views.signup, name='signup'),
    # path('delete/', views.delete, name='delete'),
    # path('update/', views.update, name='update'),
    # path('password/', views.change_password, name='change_password'),
    path('myprofile/', views.my_profile, name='my_profile'),
    path('<int:user_pk>/profile/', views.user_profile, name="user_profile"), # 상대방 프로필
    # path('<username>/follower_list/', views.follower_list, name='follower_list'),
    # path('<username>/following_list/', views.following_list, name='following_list'),
]
