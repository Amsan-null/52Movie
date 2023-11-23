from django.db import models
from django.conf import settings


class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    genre_ids = models.JSONField(null=True)
    original_language = models.CharField(max_length=200)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField(null=True)
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=200)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)


class Genre(models.Model):
    movie = models.ManyToManyField(Movie, related_name='movie_genres')
    genre_id = models.CharField(max_length=15)
    name = models.CharField(max_length=100)


class Comment(models.Model):
    content = models.TextField()
    # 게시글이 달린 영화
    write_comment_movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE, related_name='write_movie_comment', null=True, blank=True)
    # 게시글을 작성한 사용자
    write_comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='write_comment') 
