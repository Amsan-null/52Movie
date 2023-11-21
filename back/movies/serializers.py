from rest_framework import serializers
from .models import Movie, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('poster_path', 'adult', 'title', 'overview', 'genre_ids', 'release_date', 'vote_average', 'vote_count')
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('poster_path', 'adult', 'title', 'overview', 'genre_ids', 'release_date', 'vote_average', 'vote_count')

class MovieRandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content' )
        read_only_fields =	('movie', 'user')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields =	('movie', 'user', 'like_users',)

class MovieLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_like_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Movie
        fields = ("id", "user", "likes_count", 'likes')

class CommentLikeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True)
    likes_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_like_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Movie
        fields = ("id", "user", "likes_count", 'likes')