from django.urls import path
from . import views


app_name = 'accounts1'
# urlpatterns = [
#     path('api-token-auth/', obtain_jwt_token, name='token'),
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
    path('<int:user_pk>/list/', views.user_movie_list), # 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회각 목록과 그 수를 출력)
    path('<int:user_pk>/profile/', views.user_profile),# 상대방 프로필 조회
    path('<int:user_pk>/recommend/', views.recommend), # 사용자가 좋아요를 한 영화리스트에서 해당 영화와 유사한 영화를 출력
]