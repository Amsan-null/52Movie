# Generated by Django 3.2 on 2023-11-21 00:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=200)),
                ('genre_ids', models.JSONField(null=True)),
                ('original_language', models.CharField(max_length=200)),
                ('original_title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.CharField(max_length=200)),
                ('release_date', models.DateField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=200)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=100)),
                ('movie', models.ManyToManyField(related_name='movie_genres', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.5), django.core.validators.MaxValueValidator(5.0)])),
                ('like_users', models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
