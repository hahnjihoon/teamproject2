from django.shortcuts import render
from django.http import HttpResponse
import json
import random
import pandas as pd
import os
from apscheduler.jobstores.base import JobLookupError
from apscheduler.schedulers.background import BackgroundScheduler
import time
from hello import hotplace
from django.shortcuts import render

import requests
# Create your views here.


def home(request):
    return render(request,'home.html')

def food(request):
    return render(request,'food.html');

# def traffic(request):
#     return render(request,'traffic.html');

def covid(request):
    return render(request,'covid.html');

def getdata_news(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'
    news = pd.read_csv(data_path+'/news.csv', encoding='euc-kr')
    news_list = news.values.tolist()

    news_titles = [];
    for i in range(0, len(news_list)):
        news_titles.append(news_list[i][0])

    news_link = [];
    for i in range(0, len(news_list)):
        news_link.append(news_list[i][1])

    news_data = [];
    for i in range(1, len(news_link)):
        news_data.append({
            'title': news_titles[i],
            'link': news_link[i]
        });
    return HttpResponse(json.dumps(news_data), content_type='application/json');

def getdata_covid(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'
    corona = pd.read_csv(data_path+'/corona.csv', encoding='euc-kr')
    corona_list = corona.values.tolist()

    corona_contents = [];
    corona_contents.append({
        'confirmed': corona_list[0][1],
        'add': corona_list[0][2]
    });

    return HttpResponse(json.dumps(corona_contents), content_type='application/json');

def getdata_vaccinated(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'
    vaccinated = pd.read_csv(data_path+'/vaccinated.csv',   encoding='euc-kr')
    vaccinated_list = vaccinated.values.tolist()

    vaccinated_contents = [];
    vaccinated_contents.append({
        'first': vaccinated_list[1][1],
        'second': vaccinated_list[1][2],
        'third': vaccinated_list[1][3],

        'first_con': vaccinated_list[2][1],
        'second_con': vaccinated_list[2][2],
        'third_con': vaccinated_list[2][3],

        'first_per': vaccinated_list[3][1],
        'second_per': vaccinated_list[3][2],
        'third_per': vaccinated_list[3][3],
    });

    return HttpResponse(json.dumps(vaccinated_contents), content_type='application/json');



def lunch1(request):
    context = {};
    context['center'] = 'lunch1.html';
    context['center2'] = 'lunch2.html';
    return render(request,'food.html',context);
def dinner1(request):
    context = {};
    context['center'] = 'dinner1.html';
    context['center2'] = 'dinner2.html';
    return render(request,'food.html',context);

def location(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'
    loc = request.GET['loc'];
    data = {};
    if loc == 'st':

        df = pd.read_csv(data_path+'/dinner.csv', encoding='euc_kr')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55161692365908;
        data['lng'] = 126.92297178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;

    elif loc == 'lu':
        df = pd.read_csv(data_path+'/lunch.csv', encoding='euc_kr')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55151692365908;
        data['lng'] = 126.92297178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    return HttpResponse(json.dumps(data), content_type='application/json');

def traffic(request):
    return render(request,'hotplace_layout.html');

def stay(request):
    context = {};
    context['center'] = 'stay.html';
    return render(request,'hotplace_layout.html',context);

def cafe(request):
    context = {};
    context['center'] = 'cafe.html';
    return render(request,'hotplace_layout.html',context);

def bicycle(request):
    context = {};
    context['center'] = 'bicycle.html';
    return render(request,'hotplace_layout.html',context);

def cinema(request):
    context = {};
    context['center'] = 'cinema.html';
    return render(request,'hotplace_layout.html',context);

def shopping(request):
    context = {};
    context['center'] = 'shopping.html';
    return render(request,'hotplace_layout.html',context);

def subway(request):
    context = {};
    context['center'] = 'subway.html';
    return render(request,'hotplace_layout.html',context);

def tour(request):
    context = {};
    context['center'] = 'tour.html';
    return render(request,'hotplace_layout.html',context);

def hotplace_location(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'

    loc = request.GET['loc'];
    data = {};
    if loc == 'c':
        df = pd.read_csv(data_path + '/cafe_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h6>{}</h6>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 'ci':
        df = pd.read_csv(data_path+'/cinema_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 'sh':
        df = pd.read_csv(data_path+'/shopping_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 'st':
        df = pd.read_csv(data_path+'/stay_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 'sb':
        df = pd.read_csv(data_path+'/subway_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 't':
        df = pd.read_csv(data_path+'/tour_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    elif loc == 'b':
        df = pd.read_csv(data_path+'/bicycle_place.csv', encoding='utf-8')
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        lat = list(df['Lat'].values)
        lng = list(df['Lng'].values)
        data['lat'] = 37.55041692365908;
        data['lng'] = 126.91037178013711;
        info_json = []
        for i in range(len(name)):
            info_dict = {'content': '<h4>{}</h4>'.format(name[i]), 'target': link[i], 'lat':lat[i], 'lng':lng[i]}
            info_json.append(info_dict)
        data['positions'] = info_json;
    return HttpResponse(json.dumps(data), content_type='application/json');

def ranking(request):
    BASE_PATH = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(BASE_PATH)
    data_path = data_path + '/data'

    sect = request.GET['sect'];
    data = {};
    if sect == 'c':
        df = pd.read_csv(data_path+'/cafe_place.csv', encoding='utf-8')
        df = df.sort_values(by=['Score', 'review'] ,ascending=False)
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        score = list(df['Score'].values)
        review = list(df['review'].values)

        info_json = []
        for i in range(10):
            info_dict = {'name': name[i], 'review': str(review[i]), 'score': str(score[i])}
            info_json.append(info_dict)
        data = info_json;
    elif sect == 'ci':
        df = pd.read_csv(data_path+'/cinema_place.csv', encoding='utf-8')
        df = df.sort_values(by=['Score', 'review'], ascending=False)
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        score = list(df['Score'].values)
        review = list(df['review'].values)

        info_json = []
        for i in range(10):
            info_dict = {'name': name[i], 'review': str(review[i]), 'score': str(score[i])}
            info_json.append(info_dict)
        data = info_json;
    elif sect == 'sh':
        df = pd.read_csv(data_path+'/shopping_place.csv', encoding='utf-8')
        df = df.sort_values(by=['Score', 'review'], ascending=False)
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        score = list(df['Score'].values)
        review = list(df['review'].values)

        info_json = []
        for i in range(10):
            info_dict = {'name': name[i], 'review': str(review[i]), 'score': str(score[i])}
            info_json.append(info_dict)
        data = info_json;
    elif sect == 'st':
        df = pd.read_csv(data_path+'/stay_place.csv', encoding='utf-8')
        df = df.sort_values(by=['Score', 'review'], ascending=False)
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        score = list(df['Score'].values)
        review = list(df['review'].values)

        info_json = []
        for i in range(10):
            info_dict = {'name': name[i], 'review': str(review[i]), 'score': str(score[i])}
            info_json.append(info_dict)
        data = info_json;
    elif sect == 't':
        df = pd.read_csv(data_path+'/tour_place.csv', encoding='utf-8')
        df = df.sort_values(by=['Score', 'review'], ascending=False)
        # Place_name,Score,review,Link,Addr,Phone,Subcategory
        name = list(df['Place_name'].values)
        link = list(df['Link'].values)
        score = list(df['Score'].values)
        review = list(df['review'].values)

        info_json = []
        for i in range(10):
            info_dict = {'name': name[i], 'review': str(review[i]), 'score': str(score[i])}
            info_json.append(info_dict)
        data = info_json;

    return HttpResponse(json.dumps(data), content_type='application/json');



# batch 프로그램 시작 #######
class Scheduler:
    def __init__(self):
        self.sched = BackgroundScheduler()
        self.sched.start()
        self.job_id = ''

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        self.sched.shutdown()

    def kill_scheduler(self, job_id):
        try:
            self.sched.remove_job(job_id)
        except JobLookupError as err:
            print("fail to stop Scheduler: {err}".format(err=err))
            return

    # csv 생성하도록 하는 함수
    def make_place_list(self, type, job_id):
        print("%s Scheduler process_id[%s] : %d" % (type, job_id, time.localtime().tm_sec))
        hotplace.run() # hotplace.py 에서 run() 함수 실행

    def scheduler(self, type, job_id):
        print("{type} Scheduler Start".format(type=type))
        if type == 'interval':
            self.sched.add_job(self.make_place_list, type, seconds=300, id=job_id, args=(type, job_id)) #시간설정
        elif type == 'cron':
            self.sched.add_job(self.make_place_list, type, day_of_week='mon-fri',
                                                 hour='0-23', second='*/2',
                                                 id=job_id, args=(type, job_id))

def batch_start(request):
    scheduler = Scheduler()
    scheduler.scheduler('interval', "1")  # interval : 무한대로 돌라는 매개변수, "1" : job_id로 동작 함수 구분
    return HttpResponse('batchstart');

# batch 종료 프로그램 (아직 정상작동 안되는중)
def batch_stop(request):
    scheduler = Scheduler()
    scheduler.shutdown()
    print('batch stop')
    return HttpResponse('batchstop');
#### 배치프로그램 끝 ###############################3

