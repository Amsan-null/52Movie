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
        fields = ('id', 'title', 'poster_path', 'genre_ids')

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


    class Meta:
        model = Comment
        fields = ('content', )
        read_only_fields = ('write_comment_movie', 'write_comment_user',)

        
# 전체 코멘트 리스트 조회
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# 영화별 코멘트 조회
class MovieCommentSerializer(serializers.ModelSerializer):

    write_movie_comment = CommentSerializer(many=True, read_only=True) # 영화에 작성된 코멘트
    write_comment = CommentSerializer(read_only=True)

    class Meta:
        model = Movie
        # 영화 id, 영화에 작성된 게시글
        fields = '__all__'


