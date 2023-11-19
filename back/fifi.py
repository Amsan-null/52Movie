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

# API 엔드포인트
base_url = "https://api.themoviedb.org/3/movie/popular?language=ko-KR&page="

try:
    # Django 모델에 데이터 저장
    for page in range(1, 601):
        url = f"{base_url}{page}&api_key={api_key}"

        # API로부터 데이터 가져오기
        response = requests.get(url)
        response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴

        # JSON 데이터를 Django 모델에 저장
        data = response.json()
        for movie_data in data['results']:
            Movie.objects.create(
                title=movie_data['title'],
                adult=movie_data['adult'],
                overview=movie_data['overview'],
                poster_path=movie_data['poster_path'],
                release_date=movie_data['release_date'],
                vote_count=movie_data['vote_count'],
                vote_average=movie_data['vote_average'],
                popularity =movie_data['popularity'],
                genre_ids=movie_data['genre_ids']
            )
            # genre_list = []
            # for i in movie_data['genre_ids']:
            #     for j in genres:
            #         if i == j['id']:
            #             genre_list.append(j['name'])
        
        print(f"페이지 {page}의 데이터를 성공적으로 Django DB에 저장했습니다.")

    print("데이터를 성공적으로 Django DB에 저장했습니다.")
except requests.exceptions.HTTPError as errh:
    print(f"HTTP 오류 발생: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"연결 오류 발생: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"시간 초과 오류 발생: {errt}")
except requests.exceptions.RequestException as err:
    print(f"오류 발생: {err}")
