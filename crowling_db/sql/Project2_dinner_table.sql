create table DINNER(
    title varchar2(1000) constraint nn_dinner_title not null,
    type varchar2(1000),
    address varchar2(1000),
    phone varchar2(500),
    link varchar2(1000),
    score varchar2(500)
);

select *
from DINNER;

DROP TABLE DINNER CASCADE CONSTRAINTS;

comment on column dinner.title is '상호명';
comment on column dinner.type is '업종';
comment on column dinner.score is '별점';
comment on column dinner.link is '링크';
comment on column dinner.address is '주소';
comment on column dinner.phone is '전화';

commit;





CREATE SEQUENCE SEQ_DINNER
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;

commit;