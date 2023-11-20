from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('api-token-auth/', obtain_jwt_token, name='token'),
    path('signup/', views.signup, name='signup'),
    # path('delete/', views.delete, name='delete'),
    # path('update/', views.update, name='update'),
    # path('password/', views.change_password, name='change_password'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('<int:user_pk>/profile/', views.user_profile, name="user_profile"), # 상대방 프로필
    path('<username>/follow/', views.follow, name='follow'),
    path('api/token/', ObtainJSONWebToken.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', RefreshJSONWebToken.as_view(), name='token_refresh'),
]
