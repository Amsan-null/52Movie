from rest_framework import serializers
from .models import Movie, Comment

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users')

class MovieRandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')


class CommentSerializer(serializers.ModelSerializer):

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields =	('movie', 'user')


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