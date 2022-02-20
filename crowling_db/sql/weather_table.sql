create table weather(
    present varchar2(20),
    temp varchar2(10),
    condition varchar2(10),
    compare varchar2(30),
    ymd varchar2(20),
    current_time varchar2(20)
);

comment on column weather.present is '����µ�';
comment on column weather.temp is '�µ�';
comment on column weather.condition is '����';
comment on column weather.compare is '��';
comment on column weather.ymd is '������';
comment on column weather.current_time is '����ð�';

commit;

delete from weather;

DROP TABLE weather CASCADE CONSTRAINTS;


