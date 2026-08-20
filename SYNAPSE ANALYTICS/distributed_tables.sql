-- round robhin
-----------------------------------
-----------------------------------
create table round_table
(
    id int,
    name varchar(300),
    salary int
)
WITH
(
    DISTRIBUTION= ROUND_ROBIN
)
INSERT into round_table
VALUES
(1,'aa',1000)


select * from round_table




-----------------------
-- replicated tables
----------------
CREATE schema gold


create table gold.dim_prod
(
    dim_key_id int,
    dim_prod_id int,
    prod_name VARCHAR(200)
)
WITH(
    DISTRIBUTION=REPLICATE
)

-------------------
-- HASH distribution------------
-------------------------------
create table gold.fact_table
(
    dim_key_prod int,
    revenue int,
    cost int
)
WITH(
    DISTRIBUTION=HASH(dim_key_prod)
)







