import csv
import re
import json
import requests

from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from webdriver_manager.chrome import ChromeDriverManager

# import oracle_db as oradb


def dinnercsv():
    crawling_list = [['dinner', '홍대술집']]
    try:
        driver = wd.Chrome(executable_path='C:/chromedriver.exe')

        main_url = 'https://map.kakao.com/?nil_profile=title&nil_src=local'

        keyword = '홍대술집'
        filename = 'dinner'

        global Rest_list
        Rest_list = []

        driver.get(main_url)

        search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
        search_area.send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)
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

        # store_info() start###################################################
        def store_info():
            time.sleep(0.2)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup)
            cafe_lists = soup.select('.placelist> .PlaceItem')
            # print('내용:',cafe_lists)

            # store_info()
            count = 1
            for cafe in cafe_lists:

                temp = []
                try:
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
                    Rest_list.append(temp)
                    print('상호:', place_name, '\n' '별점:', score, '\n' '리뷰:', review, '\n' '링크:', link, '\n' '주소:',
                          addr, '\n' '위도:', lat, '\n' '경도:', lng, '\n' '전화:', phone, '\n' '업종:', subcategory)

                except Exception as msg:
                    print('에러발생 : ', msg)
                    pass

            # store_info() #end###########################################

            f = open(filename + '.csv', "w", encoding="euc_kr", newline="")
            writercsv = csv.writer(f)
            header = ['Place_name', 'Score', 'review', 'Link', 'Addr', 'Lat', 'Lng', 'Phone', 'Subcategory']
            writercsv.writerow(header)

            for i in Rest_list:
                writercsv.writerow(i)

        page = 1
        page2 = 0

        for i in range(0, 2):

            try:

                page2 += 1

                print(page, "page 이동")

                driver.find_element_by_xpath(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)

                store_info()

                if (page2) % 5 == 0:
                    driver.find_element_by_xpath('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)

                    page2 = 0

                page += 1

            except Exception as e:
                print(e)
                break

    except Exception as msg:
        print('csv생성안됨오류 : ', msg)

    driver.close()  # 크롬 브라우저 닫기
    driver.quit()  # 드라이버 종료
    import sys
    sys.exit()
