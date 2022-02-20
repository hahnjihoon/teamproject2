
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

COMMENT ON COLUMN HOTPLACE.NO IS '순번';
COMMENT ON COLUMN HOTPLACE.PLACENAME IS '장소명';
COMMENT ON COLUMN HOTPLACE.SCORE IS '평점';
COMMENT ON COLUMN HOTPLACE.REVIEW IS '리뷰수';
COMMENT ON COLUMN HOTPLACE.LINK IS '상세보기링크';
COMMENT ON COLUMN HOTPLACE.ADDR IS '주소';
COMMENT ON COLUMN HOTPLACE.PHONE IS '전화번호';
COMMENT ON COLUMN HOTPLACE.SUBCATEGORY IS '서브카테고리';

CREATE SEQUENCE SEQ_HOTPLACE
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCYCLE
NOCACHE;

COMMIT;

INSERT into HOTPLACE values (SEQ_HOTPLACE.nextval, 'A', 'B', 'C', 'D', 'E', 'F', 'G');