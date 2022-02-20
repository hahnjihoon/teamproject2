import oracle_db as oradb
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from collections import OrderedDict # 컬럼 순서를 지정하면서 데이터 프레임을 구성

# oradb.oracle_init();
conn = '';
cursor = '';
query = "insert into vaccinated values (:1, :2, :3, :4)";


def insert_vaccinated():
    try:
        conn = oradb.connect();
        cursor = conn.cursor();

        web_page3 = urlopen("https://www.mapo.go.kr/site/main/home")  # 마포구청 사이트
        html3 = BeautifulSoup(web_page3, "html.parser")  # 마포구 코로나 사이트 전체 크롤링

        text_a = html3.select(".font1")
        text_b = html3.select(".font2")
        title = text_a[1].text  # 코로나19백신 예방접종현황
        update_time = text_b[1].text  # 연월일, 요일, 시간

        text_c = html3.select("div.tableT2 > table > thead")
        head = text_c[0].text.strip('\n')
        head_text = head.split()  # 회차, 마포구민, 접종자, 접종률(%)

        text_d = html3.select("div.tableT2 > table > tbody")
        body = text_d[0].text.strip('\n')
        body_text = body.split('\n')  # 1차접종 ~ 3차 접종 끝까지

        row_1st = [head_text[0], head_text[1], head_text[2], head_text[3]]  # 회차, 마포구민, 접종자, 접종률(%)
        row_2nd = [body_text[0], body_text[1], body_text[2], body_text[3]]  # 1차접종, 구민수, 접종자수, 접종률
        row_3rd = [body_text[6], body_text[7], body_text[8], body_text[9]]  # 2차접종, 구민수, 접종자수, 접종률
        row_4th = [body_text[12], body_text[13], body_text[14], body_text[15]]  # 3차접종, 구민수, 접종자수, 접종률

        # cursor.execute(query, row_1st);
        # cursor.execute(query, row_2nd);
        # cursor.execute(query, row_3rd);
        # cursor.execute(query, row_4th);
        #
        # oradb.commit(conn);

        # ------------------------------------oracle db----------------------------------

        # vaccinated_csv = OrderedDict(
        #     [
        #         ('구분', [row_1st[0], row_1st[1], row_1st[2], row_1st[3]]),
        #         ('첫째줄', [row_2nd[0], row_2nd[1], row_2nd[2], row_2nd[3]]),
        #         ('둘째줄', [row_3rd[0], row_3rd[1], row_3rd[2], row_3rd[3]]),
        #         ('셋째줄', [row_4th[0], row_4th[1], row_4th[2], row_4th[3]])
        #     ]
        # )
        # df = pd.DataFrame.from_dict(vaccinated_csv)
        df = pd.DataFrame(
            {'kind':[head_text[0], head_text[1], head_text[2], head_text[3]],
            'first':[body_text[0], body_text[1], body_text[2], body_text[3]],
            'second':[body_text[6], body_text[7], body_text[8], body_text[9]],
            'third':[body_text[12], body_text[13], body_text[14], body_text[15]]}
        )

        df.to_csv('./vaccinated.csv', encoding='euc_kr', index=False)

        df2 = pd.read_csv("./vaccinated.csv", encoding='euc_kr')
        print(df2)

        print('백신 테이블 db 및 csv 저장 완료')

    except Exception as msg:
        oradb.rollback(conn);
        print('오라클 DB 프로젝트2 계정 weather 테이블 기록관련 에러 : ', msg);

    finally:
        cursor.close();
        oradb.close(conn);

insert_vaccinated();









