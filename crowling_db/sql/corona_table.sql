create table corona(
    district varchar2(30),
    coronic varchar2(30),
    increase varchar2(30)
);

comment on column corona.district is '������';
comment on column corona.coronic is 'Ȯ����';
comment on column corona.increase is '�����ο�';

commit;

DROP TABLE corona CASCADE CONSTRAINTS;