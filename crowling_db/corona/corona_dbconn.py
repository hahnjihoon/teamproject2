import oracle_db as oradb
# from crowling import weather_text, now_date, now_time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from collections import OrderedDict # 컬럼 순서를 지정하면서 데이터 프레임을 구성


# oradb.oracle_init();
conn = '';
cursor = '';
query = 'insert into CORONA(DISTRICT, CORONIC, INCREASE) values (:1, :2, :3)';
corona_list = [];


def insert_corona():
    try:
        conn = oradb.connect();
        cursor = conn.cursor();

        web_page2 = urlopen("https://www.seoul.go.kr/coronaV/coronaStatus.do?menu_code=01")  # 코로나 사이트
        html2 = BeautifulSoup(web_page2, "html.parser")  # 코로나 사이트 전체 크롤링

        standard_time = [html2.find(class_="update-date").text]  # 업데이트된 시간
        text = html2.find(class_="tstyle-status mobile mobile-table").text.split()
        current_Co = [text[40], text[46]]  # 마포구, 현재 확진자 수
        compare_Co = [text[52]]  # 어제에 비하여 증가한 확진자 수
        # print(type(standard_time))

        corona_list = [current_Co[0], current_Co[1], compare_Co[0]];
        # cursor.execute(query, corona_list)
        #
        # oradb.commit(conn);
# ------------------------------------oracle db----------------------------------

        # corona_csv = OrderedDict(
        #     [
        #         ('위치',[current_Co[0]]),
        #         ('현재인원',[current_Co[1]]),
        #         ('증가인원',compare_Co)
        #     ]
        # )
        # df=pd.DataFrame.from_dict(corona_csv)

        # df = pd.DataFrame(
        #     [[current_Co[0]],
        #     [current_Co[1]],
        #     [compare_Co[0]]]
        # )
        df = pd.DataFrame(
            {'location' : [current_Co[0]],
            'current': [current_Co[1]],
            'increase': [compare_Co[0]]}
        )

        df.to_csv('./corona.csv', encoding='euc_kr', index = None)

        df2 = pd.read_csv("./corona.csv", encoding='euc_kr')
        print(df2)

        print('코로나 테이블 db 및 csv 저장 완료')

    except Exception as msg:
        oradb.rollback(conn);
        print('오라클 DB 프로젝트2 계정 corona 테이블 기록관련 에러 : ', msg);

    finally:
        cursor.close();
        oradb.close(conn);

insert_corona();
