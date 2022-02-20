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

comment on column lunch.title is '��ȣ��';
comment on column lunch.type is '����';
comment on column lunch.score is '����';
comment on column lunch.link is '��ũ';
comment on column lunch.address is '�ּ�';
comment on column lunch.phone is '��ȭ';

commit;



CREATE SEQUENCE SEQ_lunch
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;