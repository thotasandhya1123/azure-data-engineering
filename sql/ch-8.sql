-- window function

select * from dim_product;
-- avg (where data is squeezed)
select 
avg(unit_price)
from dim_product;

-- get the sum for each ad every row
-- running sum



-- 2
select *,
sum(unit_price)over(order by launch_date )
from dim_product;

-- 3 frames
select *,
sum(unit_price)over(order by launch_date rows between unbounded preceding and current row ),
sum(unit_price)over(order by launch_date rows between unbounded preceding and unbounded following)

from dim_product;

-- ranking
-- 1)
select 
unit_price,
row_number()over(order by unit_price) as row_num,
rank()over(order by unit_price) as 'rank',
dense_rank()over(order by unit_price) as dens_num
from dim_product;

-- 2 partitioning
select 
category,
unit_price,
row_number()over(partition by category order by unit_price) as row_num,
rank()over(partition by category order by unit_price) as 'rank',
dense_rank()over(partition by category order by unit_price) as dens_num
from dim_product

