from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Comment
from accounts.models import User
from django.db.models import Count
import random
from .serializers import MovieRandomSerializer, MovieListSerializer, MovieSerializer, CommentListSerializer, CommentSerializer
from django.http import HttpResponseForbidden
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comments(request, pk):
    
    movie = Movie.objects.get(pk=pk) # movie_pk를 받고 comment_pk는?
    comments = Comment.objects.all()
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return HttpResponseForbidden('로그인이 필요합니다.')
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RandomMoviesView(APIView):
    def get(self, request, format=None):
        count = Movie.objects.aggregate(count=Count('id'))['count']
        random_indices = random.sample(range(1, count+1), 8)
        random_movies = Movie.objects.filter(id__in=random_indices)
        serializer = MovieRandomSerializer(random_movies, many=True)
        return Response(serializer.data)