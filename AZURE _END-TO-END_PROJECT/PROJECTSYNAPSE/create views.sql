----------------CREATING VIEWS-------------------
--------CALENDER VIEW---------------
CREATE view gold.calender
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_Calendar',
    FORMAT='PARQUET'
)as query1

select * from gold.calender

--------CUSTOMRS VIEWS------------------
CREATE view gold.customers
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_Customers',
    FORMAT='PARQUET'
)as query1

select * from gold.customers



-----------product_catageroes views-------------
CREATE view gold.Product_Categories
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_Product_Categories',
    FORMAT='PARQUET'
)as query1

select * from gold.Product_Categories


-----------------------products view----------

CREATE view gold.Products
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_Products',
    FORMAT='PARQUET'
)as query1

select * from gold.Products



-------------returns view---------------
CREATE view gold.Retur
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_return',
    FORMAT='PARQUET'
)as query1

select * from gold.Retur


------------sales view-----------------------
CREATE view gold.sales
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_sales',
    FORMAT='PARQUET'
)as query1

select * from gold.sales


---------------territories views------------
CREATE view gold.territories
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/AdventureWorks_territories',
    FORMAT='PARQUET'
)as query1

select * from gold.territories


----------------Product_Subcategories views-----------------
CREATE view gold.prod_sub
AS
SELECT * from OPENROWSET(
    BULK 'https://azprojectdatalake.dfs.core.windows.net/silver/Product_Subcategories',
    FORMAT='PARQUET'
)as query1

select * from gold.prod_sub
