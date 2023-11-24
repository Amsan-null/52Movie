from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token # Token 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구
from movies.models import Movie, Comment
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta: 
        model = User
        fields = ('id', 'username', 'password', 'passwordConfirmation',)

class UserMovieListSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path',)
    


    class Meta:
        model = User
        fields = ('id',)

# 내 프로필 조회
class ProfileSerializer(UserDetailsSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
    
    class Meta:
        model = User
        fields = ('id' 'username',)

# 상대방 프로필 조회 
class UserProfileSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        fields = ('id' ,'username', 'profile', )

class AccountSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#     token = serializers.SerializerMethodField()

#     def validate(self, data):
#         username = data.get("username", "")
#         password = data.get("password", "")

#         if username and password:
#             user = authenticate(username=username, password=password)

#             if user:
#                 if not user.is_active:
#                     raise serializers.ValidationError("User is deactivated.")
#             else:
#                 raise serializers.ValidationError("Unable to login with provided credentials.")
#         else:
#             raise serializers.ValidationError("Must include 'username' and 'password'.")

#         data['user'] = user
#         return data

#     def get_token(self, obj):
#         user = obj['user']
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)
#         return token




