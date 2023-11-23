from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework import status
from movies.models import Movie
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import UserMovieListSerializer, ProfileSerializer, UserSerializer, AccountSignUpSerializer, UserProfileSerializer
import random
from rest_framework.authentication import TokenAuthentication

User = get_user_model()

# 회원가입
# 인증 필요 없이 접근 가능한 영역 : 추후 인증 필요
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def signup(request):
    serializer = AccountSignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# def recommend(request, user_pk):
#     Users = get_object_or_404(User, pk=user_pk)
#     serializer = UserMovieListSerializer(Users)
#     like_lst = serializer.data.get('like_movies') # 리스트
#     if like_lst: # 좋아요한 영화가 있는 경우
#         random_list = []
#         for i in range(len(like_lst)):
#             random_list.append(like_lst[i].get('title'))
#         pick_movie = random.choice(random_list)
#     else: # 좋아요한 영화가 없는 경우
#         pick_movie = Movie.objects.values('title').order_by('?').first().get('title')

# @api_view(['POST', 'PUT'])
# def signup(request):
# 	#1-1. Client에서 온 데이터를 받아서
#     password = request.data.get('password')
#     passwordConfirmation = request.data.get('passwordConfirmation')

# 	#1-2. 패스워드 일치 여부 체크
#     if password != passwordConfirmation:
#         return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
# 	#2. UserSerializer를 통해 데이터 직렬화
#     serializer = UserSerializer(data=request.data)
    
# 	#3. validation 작업 진행 -> password도 같이 직렬화 진행
#     if serializer.is_valid(raise_exception=True):
#         user = serializer.save()
#         #4. 비밀번호 해싱 후 
#         user.set_password(request.data.get('password'))
#         user.save()
#     # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 내 프로필 정보 조회 및 수정
# @api_view(['GET', 'PUT'])
# @authentication_classes([TokenAuthentication]) # 인증된 사용자만 권한 허용
# def profile_update(request, username):
#     Users = get_object_or_404(User, username=username)
#     if request.user == User:
#         serializer = ProfileSerializer(instance=Users, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             serializer = ProfileSerializer(Users)
#             return Response(serializer.data)
        
@api_view(['GET'])
@authentication_classes([TokenAuthentication]) # 인증된 사용자만 권한 허용
def my_profile(request, my_pk):
    Users = get_object_or_404(User, pk=my_pk)
    serializer = ProfileSerializer(instance=Users, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        serializer = ProfileSerializer(Users)
        return Response(serializer.data)


# # 상대 프로필 조회
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication]) # 인증된 사용자만 권한 허용
# def user_profile(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = UserProfileSerializer(user)
#     return Response(serializer.data)


# # 사용자가 좋아요/위시리스트/평점을 준 영화 목록 조회
# @api_view(['GET'])
# @authentication_classes([TokenAuthentication]) # 인증된 사용자만 권한 허용
# def user_movie_list(request, user_pk):
#     Users = get_object_or_404(User, pk=user_pk)
#     serializer = UserMovieListSerializer(Users)
#     user_list = {
#         'id' : serializer.data.get('id'),
#         'like_movies_count' : Users.like_movies.count(),
#         'like_movies' : serializer.data.get('like_movies'),
#     }
#     return JsonResponse(user_list)

# @api_view(['POST'])
# def follow(request, username):
#     you = get_object_or_404(get_user_model(), pk=username)
#     me = request.user
#     if me in you.followers.all():
#         you.followers.remove(me)
#         return Response("unfollow", status=status.HTTP_200_OK)
#     else:
#         you.followers.add(me)
#         return Response("follow", status=status.HTTP_200_OK)
    
# @api_view(['POST'])
# def login(request):
#     serializer = UserLoginSerializer(data=request.data)
#     print(serializer)

#     if serializer.is_valid():
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)