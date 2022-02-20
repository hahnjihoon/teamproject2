create table weather(
    present varchar2(20),
    temp varchar2(10),
    condition varchar2(10),
    compare varchar2(30),
    ymd varchar2(20),
    current_time varchar2(20)
);

comment on column weather.present is '현재온도';
comment on column weather.temp is '온도';
comment on column weather.condition is '상태';
comment on column weather.compare is '비교';
comment on column weather.ymd is '연월일';
comment on column weather.current_time is '현재시간';

commit;

delete from weather;

DROP TABLE weather CASCADE CONSTRAINTS;


