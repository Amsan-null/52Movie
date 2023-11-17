import os
import django
from django.conf import settings

# 프로젝트의 settings 모듈을 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_pjt_back.settings')  # 'your_project_name'을 실제 프로젝트의 이름으로 바꿔주세요.
django.setup()

import requests
from movies.models import Movie, Genre  # 'yourapp'은 실제 Django 앱의 이름으로 바꿔야 합니다.

# API 키
api_key = "d15d5967b6757f765d670d52691a3b4d"

genres = [
    {
        "id": 28,
        "name": "액션"
    },
    {
        "id": 12,
        "name": "모험"
    },
    {
        "id": 16,
        "name": "애니메이션"
    },
    {
        "id": 35,
        "name": "코미디"
    },
    {
        "id": 80,
        "name": "범죄"
    },
    {
        "id": 99,
        "name": "다큐멘터리"
    },
    {
        "id": 18,
        "name": "드라마"
    },
    {
        "id": 10751,
        "name": "가족"
    },
    {
        "id": 14,
        "name": "판타지"
    },
    {
        "id": 36,
        "name": "역사"
    },
    {
        "id": 27,
        "name": "공포"
    },
    {
        "id": 10402,
        "name": "음악"
    },
    {
        "id": 9648,
        "name": "미스터리"
    },
    {
        "id": 10749,
        "name": "로맨스"
    },
    {
        "id": 878,
        "name": "SF"
    },
    {
        "id": 10770,
        "name": "TV 영화"
    },
    {
        "id": 53,
        "name": "스릴러"
    },
    {
        "id": 10752,
        "name": "전쟁"
    },
    {
        "id": 37,
        "name": "서부"
    }
]

# 장르 ID를 장르 이름으로 매핑하는 딕셔너리 생성
genre_dict = {genre['id']: genre['name'] for genre in genres}

# 영화 데이터에서 장르 ID를 장르 이름으로 변환
for i in genre_dict:
    Genre.objects.create(
        genre_id = i,
        name = genre_dict[i]
    )

    print("데이터를 성공적으로 Django DB에 저장했습니다.")
