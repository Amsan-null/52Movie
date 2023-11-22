from rest_framework import serializers
from .models import Movie, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)

class MovieRandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')

# 단일 코멘트 조회, 수정, 삭제
class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', )

    write_comment_movie = MovieSerializer(read_only=True) # 게시글이 달린 영화
    write_comment_user = UserSerializer(read_only=True) # 게시글 작성자


    class Meta:
        model = Comment
        fields = ('id', 'write_review_user', 'content', )

# 영화별 코멘트 조회
class MovieCommentSerializer(serializers.ModelSerializer):

    userName = serializers.SerializerMethodField()
  
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'

    write_movie_comment = CommentSerializer(many=True) # 영화에 작성된 코멘트


    class Meta:
        model = Movie
        # 영화 id, 영화에 작성된 게시글
        fields = ('id', 'write_movie_review')


# 영화 좋아요 등록 및 해제
class MovieLikeSerialzer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    # 좋아요한 사용자
    like_movie_users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        # 영화 id, 좋아요를 한 사용자 목록, 좋아요 수
        fields = ('id','like_movie_users', )

# class CommentLikeSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#     likes = serializers.StringRelatedField(many=True)
#     likes_count = serializers.SerializerMethodField()

#     def get_user(self, obj):
#         return obj.user.username

#     def get_like_count(self, obj):
#         return obj.likes.count()

#     class Meta:
#         model = Movie
#         fields = ("id", "user", "likes_count", 'likes')