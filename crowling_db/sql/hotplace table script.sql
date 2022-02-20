
CREATE TABLE HOTPLACE(
    title varchar2(1000) constraint nn_hotplace_title not null,
    type varchar2(1000),
    address varchar2(1000),
    phone varchar2(500),
    link varchar2(1000),
    score varchar2(500)
);

select *
from hotplace;

DROP TABLE hotplace CASCADE CONSTRAINTS;
COMMIT;

COMMENT ON COLUMN HOTPLACE.NO IS '����';
COMMENT ON COLUMN HOTPLACE.PLACENAME IS '��Ҹ�';
COMMENT ON COLUMN HOTPLACE.SCORE IS '����';
COMMENT ON COLUMN HOTPLACE.REVIEW IS '�����';
COMMENT ON COLUMN HOTPLACE.LINK IS '�󼼺��⸵ũ';
COMMENT ON COLUMN HOTPLACE.ADDR IS '�ּ�';
COMMENT ON COLUMN HOTPLACE.PHONE IS '��ȭ��ȣ';
COMMENT ON COLUMN HOTPLACE.SUBCATEGORY IS '����ī�װ���';

CREATE SEQUENCE SEQ_HOTPLACE
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;

COMMIT;

INSERT into HOTPLACE values (SEQ_HOTPLACE.nextval, 'A', 'B', 'C', 'D', 'E', 'F', 'G');