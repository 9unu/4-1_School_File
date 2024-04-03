from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd
import numpy as np
import os
# 영상 정보 긁어오는 함수 (Yotube_info_extraction.py에 정의되어있음)
from Yotube_info_extraction import video_info_extract

DEVEOPER_KEY="AIzaSyAXP8Jy2OXmdO6yLeQlKbTjiaeyi77uSOc"
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
youtube=build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVEOPER_KEY)


watched=pd.read_json(r"C:\Users\KHU\Desktop\4학년 1학기\웹파이썬 조교\p1.json", encoding='utf-8')

# titleUrl에 있는 영상 id 추출
watched['video_id']=watched['titleUrl'].str.replace(r'https://www\.youtube\.com/watch\?v=', '')
YouTube_video = watched[watched['header'] == 'YouTube']
YouTube_video.reset_index(drop=True, inplace=True)
YouTube_music=watched[watched['header'] == 'YouTube Music']
YouTube_music.reset_index(drop=True, inplace=True)
"""
시청기록 데이터프레임 생성
"""
"""
api 사용제한으로 한번에 모두 크롤링하는 것은 불가능할 수 있음
-> 다음날 다시 실행시키면 기존에 있던 csv파일에 더해서 추가로 크롤링되도록 구현
-> 오류나지 않고 끝날때까지 돌아가면 전부 크롤링된 것!
"""

print("크롤링 시작")
# 이전에 저장된 데이터 불러오기
prev_df_path = "/시청기록.csv"
if os.path.exists(prev_df_path):
    prev_df = pd.read_csv(prev_df_path)
    start_index = len(prev_df)  # 이전 데이터의 길이를 시작 인덱스로 설정
# 이전에 저장된 데이터가 없으면 (처음 실행시키는 거면) 새롭게 데이터프레임 생성
else:
    prev_df = pd.DataFrame()
    start_index = 0

total_df = prev_df

k = 10
# 무한루프 
while True:
    detail_df = video_info_extract(youtube, watched, start_index, start_index + k)  # watched : 음악 + 영상 전체 기록, Youtube_video : 영상 기록만, Youtube_music : 노래 기록만
    
    # 더이상 크롤링할 영상 (데이터프레임)이 없으면 무한루프 종료
    if detail_df.empty:
        break

    total_df = pd.concat([total_df, detail_df], ignore_index=True)
    
    start_index += k

total_df.to_csv('시청기록.csv', index=False)



