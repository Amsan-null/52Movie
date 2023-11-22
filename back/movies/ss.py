from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Comment
from accounts.models import User
from .serializers import MovieLikeSerializer, MovieListSerializer, MovieSerializer, CommentListSerializer, CommentSerializer, MovieLikeSerializer, CommentLikeSerializer, MovieRandomSerializer
from django.db.models import Count
import random
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# @permission_classes([IsAuthenticated])
@api_view(['GET']) # 전체 영화 조회
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET']) 
def detail(request, movie_pk): # 각 영화 조회
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])  
def comment_create_read(request, movie_pk): # 각 코멘트 조회, 생성

    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        print(serializer)
        # if request.user.is_authenticated:
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
        # return HttpResponseForbidden('로그인이 필요합니다.')


@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def movie_like(request, movie_pk): # 영화 좋아요
    movie = get_object_or_404(Movie, pk=movie_pk)

    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)

    serializer = MovieLikeSerializer(movie)

    like_movie_register = {
        'id' : serializer.data.get('id'),
        'like_users_count' : movie.like_users.count(),
        'like_users' : serializer.data.get('like_users'),
    }
    return Response(like_movie_register)

@api_view(['GET', 'POST'])
def comment_likes(request, comment_pk): # 코멘트 좋아요
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentLikeSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':

        if request.user in comment.like_users.all():
            comment.like_users.remove(request.user)
            return Response("unlike", status=status.HTTP_200_OK)
        else:
            comment.like_users.add(request.user)
            return Response("like", status=status.HTTP_200_OK)

class RandomMoviesView(APIView):
    def get(self, request, format=None):
        count = Movie.objects.aggregate(count=Count('id'))['count']
        random_indices = random.sample(range(1, count+1), 8)
        random_movies = Movie.objects.filter(id__in=random_indices)
        serializer = MovieRandomSerializer(random_movies, many=True)
        return Response(serializer.data)
