# crowling_run.py

import csv
import bs4
import urllib.request
from tkinter import *
from tkinter import ttk
# import numpy as np
import analysis
import oracle_db as oracle

filename = 'news'


def refresh(site, start=0, url=''):
    if site == 'naver' or site == 'all':
        if url == '':
            url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=' + str(start) + '1'
            print(url)
        web_page = urllib.request.urlopen(url)
        result = bs4.BeautifulSoup(web_page, 'html.parser')
        return result

def naver(start=0):
    print('naver crawling...')
    temp = []
    res = refresh('naver', start)

    # 기사 제목 리스트
    titles_urls = res.find(class_='list_news').find_all(class_='bx')
    for j in range(len(titles_urls)):
        temp.append(res.select_one('ul.list_news > li:nth-child(' + str(j+1) + ') > div > div > a').text)
        temp.append(res.select_one('ul.list_news > li:nth-child(' + str(j+1) + ') > div > div > a.news_tit')['href'])
        # all_titles.append(res.select_one('ul.list_news > li:nth-child(' + str(j + 1) + ') > div > div > a').text)
        # all_urls.append(res.select_one('ul.list_news > li:nth-child(' + str(j + 1) + ') > div > div > a.news_tit')['href'])
    # 확인용
    #     onepage_titles.append(res.select_one('ul.list_news > li:nth-child(' + str(j + 1) + ') > div > div > a').text)
    #     onepage_urls.append(res.select_one('ul.list_news > li:nth-child(' + str(j + 1) + ') > div > div > a.news_tit')['href'])
    #     print('{} 페이지 기사 추가된 onepage_titles :'.format(j+1), onepage_titles)
        # print('{} 페이지 url 추가된 onepage_urls :'.format(j + 1), onepage_urls)
    # print('마지막 리턴하는 총기사제목 all_titles : ', all_titles)
    # print('마지막 리턴하는 총기사url all_urls : ', all_urls)
    print('naver crawling Ok')
    def list_chunk(temp, n):
        return [temp[i:i+n] for i in range(0, len(temp), n)]

    temp = list_chunk(temp, 2)
    print(temp)

    f = open(filename + '.csv', "w", encoding="euc_kr", newline="")
    writercsv = csv.writer(f)
    header = ['제목', '링크']
    writercsv.writerow(header)
    for i in temp:
        writercsv.writerow(i)

    return temp


naver()


# def first_news_title():  # 프로그램 첫 실행시 첫 제목 바로 띄워주는 함수
#     url = 'https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&start=1'
#     web_page = urllib.request.urlopen(url)
#     result = bs4.BeautifulSoup(web_page, 'html.parser')
#
#     first_title = result.find(class_='news_tit').text
#     print('제목 : ', first_title)
#     # first_url = result.find(class_='news_tit')['href']
#     # print('url : ', first_url)
#
#     return first_title  # , first_url
