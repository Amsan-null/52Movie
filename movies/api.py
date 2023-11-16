import requests
import json

url = "https://api.themoviedb.org/3/movie/now_playing?language=ko-KR&page="

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMTVkNTk2N2I2NzU3Zjc2NWQ2NzBkNTI2OTFhM2I0ZCIsInN1YiI6IjY1NGQ4MzMxMjg2NmZhMTA4YjZjZmZkYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NL5V-pOLqGoGNAONbCgScNTh5AAz1pLDBM5K1uEhbNQ"
}

# 페이지가 1부터 500까지 반복
for page in range(1, 101):
    page_url = f"{url}{page}"
    response = requests.get(page_url, headers=headers)

    if response.status_code == 200:
        # API 응답이 성공적인 경우 데이터를 JSON 파일에 추가
        data = response.json()
        with open('movie.json', mode='a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
            file.write('\n')  # 각각의 JSON 객체를 줄 단위로 구분
        print(f"Page {page} data added to movie.json")
    else:
        print(f"Failed to fetch data for page {page}. Status code: {response.status_code}")
