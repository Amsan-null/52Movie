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

class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'rating' )
        read_only_fields =	('movie', 'user', 'writer')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'rating')
        read_only_fields =	('movie', 'user', 'writer')