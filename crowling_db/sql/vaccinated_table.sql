create table vaccinated(
    name_value varchar2(20),
    first_row varchar2(20),
    second_row varchar2(20),
    third_row varchar2(20)
);

select *
from vaccinated;

commit;

delete from vaccinated;

DROP TABLE vaccinated CASCADE CONSTRAINTS;


