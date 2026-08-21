# Databricks notebook source
# MAGIC %md
# MAGIC ###Incremental data loading

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC Create database sales

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC drop table if exists sales.Orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create table orders( OrderID int , OrderDate date , CustomerID int , CustomerName string, CustomerEmail string,
# MAGIC     ProductID int, ProductName string, ProductCategory string, RegionID int , RegionName string,
# MAGIC     Country string, Quantity int, UnitPrice double, TotalAmount double);
# MAGIC INSERT INTO Orders (
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
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales.Orders

# COMMAND ----------

# MAGIC %md
# MAGIC ###data warehousing

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC drop database if exists salesDWH;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create database SalesDWH

# COMMAND ----------

# MAGIC %md
# MAGIC ###staging

# COMMAND ----------

# MAGIC %md
# MAGIC #initial load

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create table salesDWH.stg_sales as (select * from sales.orders)

# COMMAND ----------

# MAGIC %sql
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC #TRANSFORMATION

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.stg_sales

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.stg_sales where RegionID =302
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create view salesDWH.trans_sales_view as
# MAGIC select * from salesDWH.stg_sales where RegionID =302

# COMMAND ----------

# MAGIC %md
# MAGIC ###core layer

# COMMAND ----------

# MAGIC %sql
# MAGIC create table salesDWH.core_sales as
# MAGIC select * from salesDWH.trans_sales_view
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##dwh core layer display

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.core_sales;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##records has been added

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sales.Orders (
# MAGIC     OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail,
# MAGIC     ProductID, ProductName, ProductCategory, RegionID, RegionName,
# MAGIC     Country, Quantity, UnitPrice, TotalAmount
# MAGIC )
# MAGIC VALUES
# MAGIC (11, '2024-02-11', 108, 'Hannah Green', 'hannah@example.com', 210, 'Wireless Earbuds', 'Accessories', 302, 'Europe', 'Spain', 12, 120.00, 240.00),
# MAGIC (12, '2024-02-12', 109, 'Ian Black', 'ian@example.com', 201, 'Laptop', 'Electronics', 303, 'Asia', 'India', 1, 800.00, 800.00),
# MAGIC (13, '2024-02-13', 105, 'Eve Adams', 'eve@example.com', 202, 'Smartphone', 'Electronics', 301, 'North America', 'Canada', 1, 500.00, 500.00),
# MAGIC (14, '2024-02-14', 110, 'Jack Wilson', 'jack@example.com', 211, 'External Hard Drive', 'Accessories', 302, 'Europe', 'UK', 2, 150.00, 300.00),
# MAGIC (15, '2024-02-15', 101, 'Alice Johnson', 'alice@example.com', 203, 'Tablet', 'Electronics', 301, 'North America', 'USA', 1, 300.00, 300.00);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales.orders

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ##staging

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace  table salesDWH.stg_sales as (select * from sales.orders where OrderDate > '2024-02-10')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.stg_sales

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.trans_sales_view

# COMMAND ----------

# MAGIC %md
# MAGIC #core layer

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table salesDWH.core_sales( OrderID int , OrderDate date , CustomerID int , CustomerName string, CustomerEmail string,
# MAGIC     ProductID int, ProductName string, ProductCategory string, RegionID int , RegionName string,
# MAGIC     Country string, Quantity int, UnitPrice double, TotalAmount double);

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDWH.core_sales 
# MAGIC select * from salesDWH.trans_sales_view;