from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model
from rest_framework import status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer, UserLoginSerializer


@api_view(['POST', 'PUT'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    passwordConfirmation = request.data.get('passwordConfirmation')
    print(password, passwordConfirmation)
	#1-2. 패스워드 일치 여부 체크
    if password != passwordConfirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(password)
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def my_profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)

def user_profile(request):
    return

@api_view(['POST'])
def follow(request, username):
    you = get_object_or_404(get_user_model(), pk=username)
    me = request.user
    if me in you.followers.all():
        you.followers.remove(me)
        return Response("unfollow", status=status.HTTP_200_OK)
    else:
        you.followers.add(me)
        return Response("follow", status=status.HTTP_200_OK)
    
@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    print(serializer)

    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)