from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie, Comment
from django.db.models import Count
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
import jwt
import random
from django.conf import settings
from .serializers import MovieCommentSerializer, MovieSerializer, CommentSerializer, MovieRandomSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import TokenAuthentication

User = get_user_model()

@api_view(['GET'])
def movies(request):
    movie_list = get_list_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(movie)
    return Response(serializer.data)

class RandomMoviesView(APIView):
    def get(self, request, format=None):
        count = Movie.objects.aggregate(count=Count('id'))['count']
        random_indices = random.sample(range(1, count+1), 24)
        random_movies = Movie.objects.filter(id__in=random_indices)
        serializer = MovieRandomSerializer(random_movies, many=True)
        return Response(serializer.data)


# 전체 코멘트 조회 및 코멘트 생성
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST'])
# def comments(request, movie_pk):
#     if request.method == 'POST':
#         movie = get_object_or_404(Movie, pk=movie_pk)
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=request.user, movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         movie = get_object_or_404(Movie, pk=movie_pk)
#         comments = movie.comment_set.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def comment_list(request):
    # 코멘트 전체 조회
    def comment_list():
        comments = get_list_or_404(Comment)
        serializer = MovieCommentSerializer(comments, many=True)
        return Response(serializer.data)
    if request.method == 'GET':
        return comment_list()
    
@authentication_classes([TokenAuthentication])
@api_view(['DELETE'])
def comment_delete(request, movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = movie.write_movie_comment.get(pk=comment_pk)
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 영화를 선택한 코멘트 생성, 전체 코멘트 조회
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
def comment_create_with_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        comments = get_list_or_404(Comment, write_comment_movie=movie)
        serializer = MovieCommentSerializer(comments, many=True)
        # serializer = MovieCommentSerializer(data=request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(write_comment_user = request.user, write_comment_movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

# @api_view(['DELETE'])
# def comment_detail(request, movie_pk, comment_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     comment = movie.comment_set.get(pk=comment_pk)
#     if request.method == 'DELETE':
#         comment.delete()
#         return Response({'pk': comment_pk})


# @api_view(['POST'])
# def recommend(request):
#     me_like = request.data.get('me_like')

#     # 좋아요 기반추천
#     my_user_like_movies = []
#     user_like_movies = []

#     like_movies = request.data.get('like_movies')
#     for like_movie in like_movies:
#         movie = get_object_or_404(Movie, pk=like_movie)
#         if not movie in my_user_like_movies:
#             my_user_like_movies.append(movie)
    
#     user_like_serialize = MovieSerializer(user_like_movies, many=True)
#     return Response([user_like_serialize.data])


# 영화 좋아요 등록 & 해제
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    # 해제
    if movie.like_movie_users.filter(pk=user.pk).exists():
        movie.like_movie_users.remove(user)
    # 등록
    else:
        movie.like_movie_users.add(user)
  
    serializer = MovieLikeSerialzer(movie)
    
    like_movie_register = {
        'id' : serializer.data.get('id'),
        'like_movie_users' : serializer.data.get('like_movie_users'),
    }
    return JsonResponse(like_movie_register)

# @api_view(['POST'])
# def like_movie_users(request, my_pk):
#   users = []
#   movies = request.data.get('movies')

#   for movie in movies:
#     movie = get_object_or_404(Movie, pk=movie)
#     serializer = MovieSerializer(movie)

#     for user in serializer.data.get('like_users'):
#       if user not in users:
#         users.append(user)
    
#   return Response(users)

