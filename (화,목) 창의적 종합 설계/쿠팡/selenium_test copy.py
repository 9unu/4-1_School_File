from bs4 import BeautifulSoup
import requests
import time
import random
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import io
from PIL import Image
from paddleocr import PaddleOCR
import shutil
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)
random_sec=random.uniform(1,3)
ocr=PaddleOCR(lang="korean")

options=Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
"""앞에서 구한 제품 링크를 통해 제품 상세 페이지에 들어감"""


url="https://www.coupang.com/vp/products/7694670793?itemId=20585529461&vendorItemId=81208415049&sourceType=srp_product_ads&clickEventId=6a0bc460-e6b1-11ee-bbc9-6ea917fac501&korePlacement=15&koreSubPlacement=1&isAddedCart="
driver.get(url)
time.sleep(random_sec)
# 밑으로 스크롤
for i in range(0,10000,10):
    driver.execute_script(f"window.scrollTo(0,{i})")
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
response=requests.get(url, headers=headers) 
html=response.text
soup = BeautifulSoup(html, "html.parser")
brand=soup.select_one(".prod-brand-name").text.strip() #빈 공간 제거
title=soup.select_one(".prod-buy-header__title").text.strip()
print(f"브랜드: {brand}, 제품명:{title}")
detail = driver.find_element(By.ID, "productDetail")
    # images = detail.find_elements(By.TAG_NAME, "img") # product-detail 안에 들어있는 이미지를 전부 긁어옴
    # # 이미지 URL 추출
    # image_urls = [image.get_attribute("src") for image in images]

    # # 이미지 URL 출력
    # for url in image_urls:
    #     print(url)
    
"""
    문제점 : 이미지 사이에 text박스가 끼워져있는 경우가 있음
    -> product-detail 안에 있는 모든 요소를 긁어오고 순서대로 저장해야함
"""
"""
<div>product detail 안에 있는 'subType-TEXT', 'subType-IMAGE' 클래스를 순서대로 가져옴 (O)
-> sequence라는 딕셔너리에 1...n까지 텍스트면 문자열, 이미지면 이미지 링크를 순서대로 삽입 (O)
-> 이미지의 index image_index=[]를 만들어 놓기 (O)
-> sequence 딕셔너리에서 key가 이미지 인덱스인 요소를 찾기 -> 이미지 저장-> OCR을 적용해서 텍스트랑 바운딩 박스 위치로 값을 바꿔주기 -> 이미지는 삭제  
=> sequence 딕셔너리에는 텍스트, 이미지에서 뽑아낸 텍스트가 순서대로 저장된다.
"""    
# detail안에 있는 모든 html 태그 + 내용을 긁어옴
soup_detail = BeautifulSoup(detail.get_attribute('innerHTML'), 'html.parser')
print(soup_detail)
sequence = {}
image_index=[]
# subType-TEXT와 subType-IMAGE 클래스가 있는 모든 div 요소 찾기
for i, div in enumerate(soup_detail.find_all(class_=['subType-TEXT', 'subType-IMAGE'])):
    if(div.find('img')):
        img_tag=div.find('img')
        if img_tag and 'src' in img_tag.attrs:
            if img_tag['src'].startswith("http"):
                sequence[i]=img_tag['src']
            else:
                sequence[i]= "https:"+img_tag['src']
            image_index.append(i)
    else:
        sequence[i]=div.text.strip()

# 결과 출력
print(sequence)
# 이미지 임시 저장할 폴더
folder_name = 'image_and_text'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for index in image_index:
    response = requests.get(sequence[index])
    if response.status_code == 200:
        _, ext = os.path.splitext(sequence[i])
        filename = f"{index}{ext}"
        with open(os.path.join(folder_name, filename), 'wb') as f:
            f.write(response.content)
    else:
        break   #이미지 다운 안되면 오류 -> 디버깅 필요

image_list = os.listdir(folder_name)
# 파일명을 숫자 기준으로 정렬
image_list = sorted(image_list, key=lambda x: int(''.join(filter(str.isdigit, x))))
# print(image_list)
for index, image in zip(image_index, image_list):
    image_path=os.path.join(folder_name,image)
    result=ocr.ocr(image_path, cls=False)
    sequence[index]=result[0]

# 임시로 만들었던 폴더 제거
if os.path.exists(folder_name):
    for file_name in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file_name)
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    os.rmdir(folder_name)

print(sequence.items())