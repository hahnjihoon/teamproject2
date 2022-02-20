import oracle_db as oradb
from crowling import weather_text, now_date, now_time


oradb.oracle_init();
conn = '';
cursor = '';
query = 'insert into WEATHER(present, temp, condition, compare, ymd, current_time) values (:1, :2, :3, :4, :5, :6)';
weather_list = [];


def insert_weather():
    try:
        conn = oradb.connect();
        cursor = conn.cursor();

        weather_list = [weather_text[0], weather_text[1], weather_text[2], weather_text[3], now_date, now_time];
        cursor.execute(query, weather_list)

    except Exception as msg:
        oradb.rollback(conn);
        print('오라클 DB 프로젝트2 계정 weather 테이블 기록관련 에러 : ', msg);

    finally:
        cursor.close();
        oradb.close(conn);

insert_weather();
