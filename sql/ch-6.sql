-- Transformations

-- numeric transformations
select * from dim_product;
-- sale with 10 % dicount

SELECT 
unit_price * 0.90 as discount_price,
unit_price + 10 as taxe_price,
unit_price / 10 as fract_price,
round (unit_price,1) as rounded_price
from dim_product;


-- DATE TRANSFORMATIONS (VERY IMP FOR DE )

SELECT * FROM DIM_DATE;
-- 1) fetrch current date
select 
date, 
now() as 'current_timestamp',
utc_date(),
utc_time(),
utc_timestamp()
From
dim_date;


-- 2)
select
 date,
 year(date),
 month(date),
 day(date),
 dayname(date),
 weekday(date),
 date(utc_timestamp()),
 adddate(date,2),
 subdate(date,2),
 datediff(date(utc_timestamp()),date) as total_day,
 cast('2026-07-03' as datetime )
 from dim_date; 
-- 3)
select 
date,
date_format(date,"%W %M %e %y")
from dim_date;

-- TYPR CASTING
Select * from dim_customer;

select
 customer_key,
cast(customer_key as char(100))
from 
dim_customer;


-- string functions
select * from dim_customer;

select
 concat(first_name,' ',last_name) as full_name,
 concat_ws(' ',first_name,last_name,country),
length(country) as country_size,
upper(first_name),
lower(city),
substring(email,1,4),
replace(email,'@','%'),
right(country,3),
left(country,3),
reverse(country),
repeat(first_name,2)
from dim_customer