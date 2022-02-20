import requests as rq
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime
import requests

now = datetime.now()
now_date = now.strftime("%Y-%m-%d") # 날짜 객체에 속하는 strftime() 메서드로 읽기 가능한 문자열로 변환.
now_time = now.strftime("%p %H:%M") # %p 는 am, pm 표시

# print(now_date)   # 연,월,일
# print(now_time)   # 시간

web_page1 = urlopen("https://weather.naver.com/today/09440120")  # 날씨 사이트
web_page2 = urlopen("https://www.seoul.go.kr/coronaV/coronaStatus.do?menu_code=01")  # 코로나 사이트

html1 = BeautifulSoup(web_page1, "html.parser") # 날씨 사이트 전체 크롤링
html2 = BeautifulSoup(web_page2, "html.parser") # 코로나 사이트 전체 크롤링

# 날씨 ------------------------------------------------------------------------
weather = html1.find(class_="weather_now")
weather_img = weather.find(class_="summary_img")
text1 = weather.find(class_="current").text
text2 = weather.find(class_="summary").text  # 맑음, 어제보다 ?도 높,낮아요

a1 = text1[0:5]  #'현재온도'
b1 = text1[5:8]  #온도
a2 = text2[1:3] # 맑음
b2 = text2[4:18] # 어제보다 ?도 높,낮아요    수정해야함.
weather_text = [a1, b1, a2, b2] # 날씨 text 모음.

# print(weather_text)
# -------------------------------------------------------------------------------

# 코로나 --------------------------------------------------------------------------
standard_time = [html2.find(class_="update-date").text]   # 업데이트된 시간
text = html2.find(class_="tstyle-status mobile mobile-table").text.split()
current_Co = [text[40], text[46]]   # 마포구, 현재 확진자 수
compare_Co = [text[52]] # 어제에 비하여 증가한 확진자 수
# print(type(standard_time))

# ---------------------------------------------------------------------------------
# print(weather_text)
print(current_Co)
print(compare_Co[0])
