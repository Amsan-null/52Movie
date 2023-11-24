from django.urls import path
from . import views


app_name = 'accounts'
# urlpatterns = [
    # path('api-token-auth/', obtain_jwt_token, name='token'),
#     # path('delete/', views.delete, name='delete'),
#     # path('update/', views.update, name='update'),
#     # path('password/', views.change_password, name='change_password'),
#     path('my_profile/', views.my_profile, name='my_profile'),
#     path('<int:user_pk>/profile/', views.user_profile, name="user_profile"), # 상대방 프로필
#     # path('<username>/follow/', views.follow, name='follow'),

# ]

urlpatterns = [
    # path('delete/', views.user_delete), # 회원탈퇴
    # path('logout/', views.logout, name='logout'),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('<int:my_pk>/myprofile/', views.my_profile ), # 내 정보(프로필)
]