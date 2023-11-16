from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200)
    genres_id = models.ManyToManyField(Genre, related_name='movie_genres')
    original_language = models.CharField(max_length=200)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=200)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    writer = models.CharField(max_length=200)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
