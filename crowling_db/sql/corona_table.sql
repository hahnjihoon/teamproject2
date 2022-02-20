create table corona(
    district varchar2(30),
    coronic varchar2(30),
    increase varchar2(30)
);

comment on column corona.district is '마포구';
comment on column corona.coronic is '확진자';
comment on column corona.increase is '증가인원';

commit;

DROP TABLE corona CASCADE CONSTRAINTS;