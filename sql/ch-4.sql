create table orders(
order_id int,
 cust_id int,
price int);

insert into orders
values 
(1,101,1000),
(2,201,1100),
(3,501,1200);

select * from orders;



create table customers (
id int,
cus_Name varchar(100),
email varchar(100));


insert into customers
values 
(101,'love','aa'),
(201,'ansh','bb'),
(301,'lamba','cc');

select * from customers;


-- JOINS
-- inner join
select * from
orders o
inner join
customers c
on o.cust_id=c.id;

-- left join
select * from
orders o
left join
customers c
on o.cust_id=c.id;
-- right join
select * from
orders o
right  join
customers c
on o.cust_id=c.id;


-- full join(not supported)

-- union:
select * from
orders o
 left join
customers c
on o.cust_id=c.id
union
select * from
orders o
right  join
customers c
on o.cust_id=c.id;