create table LUNCH(
    title varchar2(1000) constraint nn_lunch_title not null,
    type varchar2(1000),
    address varchar2(1000),
    phone varchar2(500),
    link varchar2(1000),
    score varchar2(500)
);

select *
from LUNCH;

DROP TABLE LUNCH CASCADE CONSTRAINTS;

comment on column lunch.title is '상호명';
comment on column lunch.type is '업종';
comment on column lunch.score is '별점';
comment on column lunch.link is '링크';
comment on column lunch.address is '주소';
comment on column lunch.phone is '전화';

commit;



CREATE SEQUENCE SEQ_lunch
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;