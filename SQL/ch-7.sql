-- conditionals

select * from dim_product;
select  *,
case
when unit_price <=100 then 'affordable'
when unit_price <=200 then 'normal'
else 'expensive'
end as price_cat
from dim_product;

-- 2) add price only for clothing cat

select  *,
case
when unit_price <=100 and category then 'affordable'
when unit_price <=200 and category then 'normal'
when unit_price >=200 and category then 'expensive'
else concat('not for',category)
end as price_cat
from dim_product
