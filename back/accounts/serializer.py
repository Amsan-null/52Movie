from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token # Token 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구
from movies.models import Movie, Comment
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
    # write_only는 시리얼라이징은 하지만 응답에는 포함시키지 않는다는 의미
    # 비밀번호를 응답에 표현한다면 보안상의 유출이 되는 것이기 떄문

    password = serializers.CharField(write_only=True)

    class Meta: 
        model = User
        fields = ('username', 'password', 'passwordConfirmation',)
        read_only_fields = ('reviews', 'like_movies')


class UserProfileSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    like_movies = serializers.SerializerMethodField()
    like_comments = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'followings', 'followers', 'like_movies', 'like_comments']

    def get_followers(self, obj):
        return UserSerializer(obj.followers.all(), many=True).data
    
    def get_followings(self, obj):
        return UserSerializer(obj.followings.all(), many=True).data

    def get_like_movies(self, obj):
        return MovieSerializer(obj.like_movies.all(), many=True).data

    def get_like_comments(self, obj):
        return CommentSerializer(obj.like_comments.all(), many=True).data


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Unable to login with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data

    def get_token(self, obj):
        user = obj['user']
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token




