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

comment on column dinner.title is '��ȣ��';
comment on column dinner.type is '����';
comment on column dinner.score is '����';
comment on column dinner.link is '��ũ';
comment on column dinner.address is '�ּ�';
comment on column dinner.phone is '��ȭ';

commit;





CREATE SEQUENCE SEQ_DINNER
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;

commit;