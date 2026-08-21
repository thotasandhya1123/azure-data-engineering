-- subqueries
select * from  dim_product;

select avg(unit_price) from dim_product;
-- result 495.790060

-- rcods wwhere unit price is greater then avg price
-- 1
select * from dim_product
where unit_price >= (select avg(unit_price) from dim_product);

-- 2 treat olp as a table.what ever we arite uner from cluase is treated as a table
select 
*
from
(select * from dim_product
where unit_price >= (select avg(unit_price) from dim_product))
as sub_query_tab
where category='clothing'; 







