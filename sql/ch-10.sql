-- CTE'S (COMMON TABLE EXPRESSIONS)

select 
* 
from 
dim_product
where
 unit_price >= (select avg(unit_price) from dim_product);
 -- treat olp as a temp table
 WITH CTE_table as
 (
 select 
* 
from 
dim_product
where
 unit_price >= (select avg(unit_price) from dim_product)
 )
 select * from cte_table
 where product_name in ('Figure Method','Huge Change');
 
 -- 2) i want to use the result of above so we want another  cte
WITH CTE_table as
 (
 select 
* 
from 
dim_product
where
 unit_price >= (select avg(unit_price) from dim_product)
 ),
 -- we stored the data in one table and gave name as cte_table_2
 cte_table_2 as
 (
 select * from cte_table
 where product_name in ('Figure Method','Huge Change')
 )
 -- from cte_table 2 we are taking the data that we require
 select * from cte_table_2
 where product_name='Figure Method'

