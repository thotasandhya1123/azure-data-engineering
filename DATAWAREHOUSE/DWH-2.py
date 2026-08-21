# Databricks notebook source
# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC Create or replace database sales_new;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create or replace table sales_new.orders( OrderID int , OrderDate date , CustomerID int , CustomerName string, CustomerEmail string,
# MAGIC     ProductID int, ProductName string, ProductCategory string, RegionID int , RegionName string,
# MAGIC     Country string, Quantity int, UnitPrice double, TotalAmount double);
# MAGIC INSERT INTO sales_new.Orders (
# MAGIC     OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail,
# MAGIC     ProductID, ProductName, ProductCategory, RegionID, RegionName,
# MAGIC     Country, Quantity, UnitPrice, TotalAmount
# MAGIC )
# MAGIC VALUES
# MAGIC (1, '2024-02-01', 101, 'Alice Johnson', 'alice@example.com', 201, 'Laptop', 'Electronics', 301, 'North America', 'USA', 2, 800.00, 1600.00),
# MAGIC (2, '2024-02-02', 102, 'Bob Smith', 'bob@example.com', 202, 'Smartphone', 'Electronics', 302, 'Europe', 'Germany', 1, 500.00, 500.00),
# MAGIC (3, '2024-02-03', 103, 'Charlie Brown', 'charlie@example.com', 203, 'Tablet', 'Electronics', 303, 'Asia', 'India', 3, 300.00, 900.00),
# MAGIC (4, '2024-02-04', 101, 'Alice Johnson', 'alice@example.com', 204, 'Headphones', 'Accessories', 301, 'North America', 'USA', 1, 150.00, 150.00),
# MAGIC (5, '2024-02-05', 104, 'David Lee', 'david@example.com', 205, 'Gaming Console', 'Electronics', 302, 'Europe', 'France', 1, 400.00, 400.00),
# MAGIC (6, '2024-02-06', 102, 'Bob Smith', 'bob@example.com', 206, 'Smartwatch', 'Electronics', 303, 'Asia', 'China', 2, 200.00, 400.00),
# MAGIC (7, '2024-02-07', 105, 'Eve Adams', 'eve@example.com', 201, 'Laptop', 'Electronics', 301, 'North America', 'Canada', 1, 800.00, 800.00),
# MAGIC (8, '2024-02-08', 106, 'Frank Miller', 'frank@example.com', 207, 'Monitor', 'Accessories', 302, 'Europe', 'Italy', 2, 250.00, 500.00),
# MAGIC (9, '2024-02-09', 107, 'Grace White', 'grace@example.com', 208, 'Keyboard', 'Accessories', 303, 'Asia', 'Japan', 3, 100.00, 300.00),
# MAGIC (10, '2024-02-10', 104, 'David Lee', 'david@example.com', 209, 'Mouse', 'Accessories', 302, 'Europe', 'Germany', 2, 50.00, 100.00);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_new.orders

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create schema if not exists orderDWH;

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace  table orderDWH.stg_sales as (select * from sales_new.orders)

# COMMAND ----------

# MAGIC %sql
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC drop view orderDWH.trans_sales_view

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.stg_sales where 
# MAGIC Quantity is not NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop view orderDWH.trans_sales_view

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view  orderDWH.trans_sales_view as
# MAGIC select * from orderDWH.stg_sales where Quantity is not  NULL

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.trans_sales_view

# COMMAND ----------

# MAGIC %md
# MAGIC ###dim customer

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table orderDWH.Dim_customers
# MAGIC (
# MAGIC     customerID int,
# MAGIC     dim_cust_key int,
# MAGIC     CustomerName string,
# MAGIC     CustomerEmail string
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view  orderDWH.Dim_customers_view
# MAGIC  as
# MAGIC Select T.*,row_number()over(order by T.customerID) as dim_cust_key
# MAGIC from(
# MAGIC     select 
# MAGIC Distinct( customerID),
# MAGIC CustomerName,CustomerEmail
# MAGIC from orderDWH.trans_sales_view) as T

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.dim_customers_view

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into orderDWH.Dim_customers
# MAGIC select try_cast(customerID as int),dim_cust_key,CustomerName
# MAGIC ,CustomerEmail from orderDWH.dim_customers_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.Dim_customers
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##dim products

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists orderDWH.Dim_customers

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table orderDWH.dim_products
# MAGIC (
# MAGIC     productID int,
# MAGIC     ProductName string,
# MAGIC     ProductCategory string,
# MAGIC     dim_prod_key int
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC drop view if exists orderDWH.Dim_products_view

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view  orderDWH.Dim_products_view
# MAGIC  as
# MAGIC Select T.*,row_number()over(order by T.productID) as dim_prod_key
# MAGIC from(
# MAGIC     select
# MAGIC Distinct( productID),
# MAGIC productName,ProductCategory
# MAGIC from orderDWH.trans_sales_view) as T

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into orderDWH.Dim_products
# MAGIC select *
# MAGIC from orderDWH.dim_products_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.Dim_products

# COMMAND ----------

# MAGIC %md
# MAGIC ###dim_region

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table orderDWH.dim_region
# MAGIC (
# MAGIC     RegionID int,
# MAGIC     RegionName string,
# MAGIC     Country string,
# MAGIC     dim_region_key int
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view  orderDWH.Dim_region_view
# MAGIC  as
# MAGIC Select T.*,row_number()over(order by T.RegionID) as dim_region_key
# MAGIC from(
# MAGIC     select
# MAGIC Distinct( RegionID),
# MAGIC RegionName,Country
# MAGIC from orderDWH.trans_sales_view) as T

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into orderDWH.Dim_Region
# MAGIC select *
# MAGIC from orderDWH.dim_Region_view;

# COMMAND ----------

# MAGIC %md
# MAGIC ###dim_date

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table orderDWH.dim_date
# MAGIC (
# MAGIC     orderDate Date,
# MAGIC     dim_date_key int
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view  orderDWH.Dim_Date_view
# MAGIC  as
# MAGIC Select T.*,row_number()over(order by T.OrderDate) as dim_date_key
# MAGIC from(
# MAGIC     select
# MAGIC Distinct( OrderDate)
# MAGIC from orderDWH.trans_sales_view) as T

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into orderDWH.Dim_Date
# MAGIC select *
# MAGIC from orderDWH.dim_Date_view;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orderDWH.Dim_Date

# COMMAND ----------



# COMMAND ----------

