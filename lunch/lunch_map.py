import requests
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap
# filename = input('파일 이름 : ')

#import dinner
from lunch import lunch_csv

def lunchmap():
    lunch_csv.lunchcsv()

    ApiKey = "A330DF4B-35F7-3E5C-BB85-0395C1B2B412"

    # df = pd.read_csv(filename + '.csv', encoding='utf-8')
    df = pd.read_csv('../dinner.csv', encoding='euc-kr')

    df.head()

    lat = []
    lng =[]
    address = list(df['도로명주소'].values)

    for add in address:
        r = requests.get('http://api.vworld.kr/req/address?service=address&request=GetCoord&version=2.0&crs=EPSG:4326'
                         '&key=%s&address=%s&refine=true&simple=false&format=json&type=road'% (ApiKey, add))
        add_dict = r.json()

        if add_dict['response']['status'] == 'OK':
            lng.append(add_dict['response']['result']['point']['x'])
            lat.append(add_dict['response']['result']['point']['y'])
        else:
            lng.append(None)
            lat.append(None)
    print(add_dict)
    print(lng)

    df['경도'] = lng = [float (i) for i in lng]
    df['위도'] = lat = [float (i) for i in lat]

    df['업종분류_1'] = df['업종'].apply(lambda x : x.split(' - ')[0])
    # df['업종분류_2'] = df['업종'].apply(lambda x : x.split(' - ')[1])

    shop_type = list(df['업종분류_1'].unique())
    type_sort = df['업종분류_1'].value_counts()
    type_list = list(type_sort.index)
    type_list = type_list[:18]

    color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'cadetblue', 'darkpurple', 'black',
                  'pink', 'lightblue', 'lightgreen']

    def show_marker_map(df):
        map = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=15)
        for n in df.index:
            shop_name = df.loc[n, '상호명'] + '  :  '+ df.loc[n, '도로명주소'] + '     / (' +str(df.loc[n, '별점'])+ '점)'
            print(shop_name)

            if df['업종분류_1'][n] in type_list:
                icon_color = color_list[type_list.index(df['업종분류_1'][n])]
            else:
                icon_color = color_list[len(color_list)-1]

            folium.Marker([df.loc[n, '위도'], df.loc[n, '경도']],
                          #popup="<a href=>shop_name</a>",
                          popup="<a href=" + df.loc[n, '링크'] + ">go_to_link</a>",
                          tooltip = shop_name,
                          icon = folium.Icon(color = icon_color)).add_to(map)
            # https://place.map.kakao.com/733953859
            # popup = folium.Popup('<a href=" [URL GOES HERE] "target="_blank"> [text for link goes here]' </a>')
    # folium.Marker([lat,long],popup= ('<a href=\"file:///C:/Users/.../test_doc%23**existing_bookmark**\">test_word</a>',
        #                               icon=folium.Icon(color='darkred')).add_to(m)

        return map

    map = show_marker_map(df)

    html_file = 'dinner_map.html'
    map.save(html_file)
