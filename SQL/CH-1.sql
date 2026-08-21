create table sales_new
(
id int,
store_name varchar(200)
);

insert into sales_new
values (1,"aa"),
(2,"bb")
;



-- ALTER COMMAND
ALTER TABLE SALES_NEW
ADD COLUMN STORE_LOCATION VARCHAR(200);
RENAME COLUMN STORE_LOCATION TO STORE_CITY;
Select * from store_new;