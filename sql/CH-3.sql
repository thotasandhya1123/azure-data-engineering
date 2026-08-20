-- First select

select * from dim_customer;
-- LIMIT
select 
customer_id ,email
from 
dim_customer
limit 10;

-- WHERE [CONDITION]
-- 1
SELECT * FROM dim_customer
where (gender='f') ;

-- 2 (and/or)
SELECT * FROM 
dim_customer
where
  (gender='f') and ((country='France') or (join_date > '2022-01-01'));

-- Like
-- 1
SELECT * FROM 
dim_customer
where First_name LIke 'T%';
-- 2
SELECT * FROM 
dim_customer
where First_name LIke 'T%y';
-- 3
SELECT * FROM 
dim_customer
where First_name LIke 'T__f%y';

-- sorting
SELECT * FROM dim_product
order by launch_date asc;
-- 2 top 3 expensive products
SELECT * FROM dim_product
order by unit_price desc
limit 3;

-- Alias a nw name for the column
select 
product_id id,
product_name as 'product name',
category 
from dim_product;

-- group by (avg price for each categeory)
select * from dim_product;
-- 1
select 
category,
avg(unit_price) avg_price,
sum(unit_price)
from dim_product
group by category;

-- 2(categeory whose avg is greater than 500)
-- where clause can't be used beacuse ,where ia applicable only for those coluns availablein in table
-- so we will use having 
select 
category,
avg(unit_price) avg_price,
sum(unit_price)
from dim_product
group by category
having avg_price >500;


