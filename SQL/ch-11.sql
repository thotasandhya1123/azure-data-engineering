-- REAL TIME SCENERIO'S
select * from dim_product;
-- SCENARIO 1{FINDING NTH VALUE}
-- manager asks to give top 5th most expensive product freom the store
select * from
(select *,
dense_rank()over(order by unit_price) as ranking
from dim_product) as sub_query
where ranking=5;

-- top 5th category from each product

select * from
(select *,
dense_rank()over(partition by category order by unit_price ) as ranking
from dim_product) as sub_query
where ranking=5;

-- scenerio 2 [ removing duplicates by row_numer ]

select * from customers;
insert into customers
values
(301,'lamba','cc'),
(101,'love','aa');

select *,
row_number()over(partition by id order by id ) as dedup
from customers;
------
select * from 
(select *,
row_number()over(partition by id order by id ) as dedup
from customers) as sub_query
where dedup=1;


-- scenerio 3[lag and lead]
-- lag (preceding ) lead(following value)

create table weather
(
id int,
temp float);

insert into weather
values
(1,'10'),
(2,12),
(3,9),
(4,15),
(5,20),
(6,25),
(7,26);
select * from weather;

-- see the temperature of previous and future day

select *,
  lag(temp,1,0)over(order by id) as prev_day,
    lag(temp,2,0)over(order by id) as prev_2__day,
    lead(temp,1,0)over(order by id) as fut_day
  from weather;


