# Databricks notebook source
# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC Create  database sales_scd;

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create table sales_scd.orders( OrderID int , OrderDate date , CustomerID int , CustomerName string, CustomerEmail string,
# MAGIC     ProductID int, ProductName string, ProductCategory string, RegionID int , RegionName string,
# MAGIC     Country string, Quantity int, UnitPrice double, TotalAmount double);
# MAGIC INSERT INTO sales_scd.Orders (
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
# MAGIC select * from sales_scd.orders
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select distinct(productID),
# MAGIC productName,productCategory
# MAGIC  from sales_scd.orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table salesDWH.Dimproducts
# MAGIC (productID int,
# MAGIC  productName string,
# MAGIC  productCategory string)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.Dimproducts

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view sales_scd.view_Dimproduct as
# MAGIC select distinct(productID),
# MAGIC productName,productCategory
# MAGIC from sales_scd.orders

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_scd.view_Dimproduct

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDWH.Dimproducts
# MAGIC select * from sales_scd.view_Dimproduct

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.Dimproducts
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###inserting new records

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO sales_scd.Orders (
# MAGIC     OrderID, OrderDate, CustomerID, CustomerName, CustomerEmail,
# MAGIC     ProductID, ProductName, ProductCategory, RegionID, RegionName,
# MAGIC     Country, Quantity, UnitPrice, TotalAmount
# MAGIC )
# MAGIC VALUES
# MAGIC (1, '2024-02-11', 101, 'Alice Johnson', 'alice@example.com', 201, 'gaming Laptop', 'Electronics', 301, 'North America', 'USA', 2, 800.00, 1600.00),
# MAGIC (2, '2024-02-12', 102, 'Bob Smith', 'bob@example.com', 230, 'Airpods', 'Electronics', 302, 'Europe', 'Germany', 1, 500.00, 500.00)

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace view sales_scd.view_Dimproduct as
# MAGIC select distinct(productID),
# MAGIC productName,productCategory
# MAGIC from sales_scd.orders
# MAGIC where OrderDate > "2024-02-10"

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from sales_scd.view_Dimproduct

# COMMAND ----------

# MAGIC %md
# MAGIC ##
# MAGIC merge scd type-1
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE into salesDWH.Dimproducts AS TRG
# MAGIC USING sales_scd.view_Dimproduct AS SRC
# MAGIC ON trg.productID = src.productID
# MAGIC WHEN MATCHED THEN
# MAGIC UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDWH.Dimproducts