import csv
import json
import re
import os
import requests
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
# from model import DBHelper




def run():
    crawling_list = [['bicycle_place', '서교동 자전거 대여소'], ['cafe_place', '서교동 카페'], ['cinema_place', '서교동 영화관'],
                     ['shopping_place', '서교동 의류'], ['stay_place', '서교동 숙박'], ['subway_place', '서교동 지하철'],
                     ['tour_place', '서교동 관광']]
    for key in crawling_list:
        driver = wd.Chrome(ChromeDriverManager().install())
        options = wd.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        place_csv = []
        filename = key[0]
        main_url = 'https://map.kakao.com/?nil_profile=title&nil_src=local'

        keyword = key[1]

        #크롤링 자료 저장 리스트
        place_list = []

        driver.get(main_url)

        search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]') #검색창
        search_area.send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER) #검색실행
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER) #장소클릭
        time.sleep(0.2)

        def getLatLng(addr):
            url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
            headers = {"Authorization": "KakaoAK 6feae8abc9f2e17422685f5465accd16"}
            result = json.loads(str(requests.get(url, headers=headers).text))
            match_first = result['documents'][0]['address']
            lat = float(match_first['y'])
            lng = float(match_first['x'])
            result = [lat, lng]
            return result

        #store_info() start###################################################
        # db = DBHelper()
        def store_info():
            time.sleep(0.2)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            cafe_lists = soup.select('.placelist> .PlaceItem')

            count = 1
            for cafe in cafe_lists:

                temp = []
                place_name = cafe.select('.head_item > .tit_name> .link_name')[0].text
                try:
                    score = cafe.select('.rating> .score > .num')[0].text
                except:
                    score = 0
                try:
                    review = cafe.select('.rating > .review')[0].text
                    review = review[3: len(review)]
                    review = int(re.sub(",", "", review))
                except:
                    review = 0
                link = cafe.select('.contact > .moreview')[0]['href']
                global addr, lat, lng
                addr = cafe.select('.addr > p')[0].text

                phone = cafe.select('.info_item > .clickArea > .phone')[0].text
                try:
                    subcategory = cafe.select('.head_item > .subcategory')[0].text
                except:
                    subcategory = ''
                try:
                    latlng = getLatLng(addr)
                    lat = str(latlng[0])
                    lng = str(latlng[1])
                except Exception as e:
                    print(e)
                temp.append(place_name)
                temp.append(score)
                temp.append(review)
                temp.append(link)
                temp.append(addr)
                temp.append(lat)
                temp.append(lng)
                temp.append(phone)
                temp.append(subcategory)
                place_csv.append(temp)
                place_list = [place_name, score, review, link, addr, lat, lng, phone, subcategory]
                print(place_list)
                BASE_PATH = os.path.dirname(os.path.abspath(__file__))
                data_path = os.path.dirname(BASE_PATH)
                data_path = data_path + '/data'
                f = open(data_path+'/' + filename + '.csv', "w", encoding="utf-8-sig", newline="")
                writercsv = csv.writer(f)
                header = ['Place_name', 'Score', 'review', 'Link', 'Addr', 'Lat', 'Lng', 'Phone', 'Subcategory']
                writercsv.writerow(header)

                for i in place_csv:
                    writercsv.writerow(i)


                # db.db_insertCrawlingData(place_list)






        #store_info() end###########################################

        page = 1 #실제페이지
        page2 = 0 # 5페이지 이후 다음을 누르면 0으로 초기화 되는 용도

        for i in range(0, 5): #34페이지까지 반복 크롤링

            try:

                page2 += 1

                print(page, "page 이동")

                driver.find_element_by_xpath(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER) # 페이지 클릭 page2가 바뀌면서(.format과 같은기능) 실행됨

                store_info() # store_info()함수 실행시켜서 크롤링

                if (page2)%5 ==0: # 5페이지 크롤링 된 후 page2를 0으로 초기화해서 다음 섹션의 0~5 선택 반복
                    driver.find_element_by_xpath('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER) # 페이지 다음으로 넘기기 버튼 클릭

                    page2 = 0


                page += 1

            except Exception as e:
                print(e)
                break

    driver.close()  # 크롬 브라우저 닫기
    driver.quit()  # 드라이버 종료
    import sys
    sys.exit()





if __name__ == "__main__":
    #run(filename, keyword):
    run()




