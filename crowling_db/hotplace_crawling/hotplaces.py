import csv
import re

from selenium import webdriver as wd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import oracle_db as oradb




# oradb.oracle_init()
conn = ''
cursor = ''
query = 'insert into hotplace values (:1, :2, :3, :4, :5, :6)'
link_list = []


def insertnews():
    try:
        conn = oradb.connect()
        cursor = conn.cursor()

        driver = wd.Chrome(executable_path='C:/Users/chromedriver.exe')

        main_url = 'https://map.kakao.com/?nil_profile=title&nil_src=local'

        keyword = '서교동'
        filename = 'hotplace'

        global Rest_list
        Rest_list = []

        driver.get(main_url)

        search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')
        search_area.send_keys(keyword)
        driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)
        time.sleep(0.2)

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
            for cafe in soup:

                temp = []
                try:
                    global cafe_name
                    global cafe_type
                    global score
                    global link
                    global addr
                    global phone
                    cafe_name = cafe.select('.head_item > .tit_name> .link_name')[0].text
                    cafe_type = cafe.select('.head_item > .subcategory')[0].text
                    score = cafe.select('.rating> .score > .num')[0].text
                    link = cafe.select('.contact > .moreview')[0]['href']
                    addr = cafe.select('.addr > p')[0].text
                    phone = cafe.select('.info_item > .clickArea > .phone')[0].text


                    if '-' in addr:
                        pass
                    else:
                        temp.append(cafe_name)
                        temp.append(cafe_type)
                        temp.append(addr)
                        temp.append(phone)
                        temp.append(link)
                        temp.append(score)
                        Rest_list.append(temp)

                    #print('상호:', cafe_name, '\n' '업종:', cafe_type, '\n' '별점:', score, '\n' '링크:', link, '\n' '주소:',
                      #    addr, '전화:', phone)
                    link_list =  (cafe_name, cafe_type, addr, phone, link, score)
                    print(link_list)
                    cursor.execute(query, link_list)





                    # print(link_list)

                except Exception as msg:
                    print('에러발생 : ', msg)
                    pass

            # store_info() #end###########################################
            oradb.commit(conn)
            print('저장완료')

            f = open(filename + '.csv', "w", encoding="euc_kr", newline="")
            writercsv = csv.writer(f)
            header = ['상호명', '업종', '도로명주소', '전화번호', '링크', '별점']
            writercsv.writerow(header)

            for i in Rest_list:
                writercsv.writerow(i)

        page = 1
        page2 = 0

        for i in range(0, 15):

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
        oradb.rollback(conn)
        print('오라클 DB 과제용 계정 hotplace 테이블 기록관련 에러 : ', msg)

    finally:
        cursor.close()
        oradb.close(conn)



