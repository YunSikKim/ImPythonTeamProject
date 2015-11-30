drop table if exists pharmacy;
create table pharmacy(
p_name string not null,
p_tel string not null,
p_address string primary key,
p_lat string not null,
p_lon string not null,
p_weekdayopen string,
p_weekdaynightopen string,
p_saturdayopen string,
p_sundayopen string,
p_isanimal string not null
);