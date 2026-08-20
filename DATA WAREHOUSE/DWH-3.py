# Databricks notebook source
# MAGIC %md
# MAGIC ##FACT TABLE

# COMMAND ----------

# MAGIC %sql
# MAGIC use CATALOG dwh;
# MAGIC use schema data_warehouse;
# MAGIC create table orderDWH.Factsales
# MAGIC (
# MAGIC OrderID int,
# MAGIC Quantity decimal,
# MAGIC UnitPrice decimal,
# MAGIC TotalAmount decimal,
# MAGIC dim_customer_key int,
# MAGIC dim_date_key int,
# MAGIC dim_product_key int,
# MAGIC dim_Region_key int
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC select
# MAGIC F.OrderID,
# MAGIC F.Quantity,
# MAGIC F.UnitPrice,
# MAGIC F.TotalAmount,
# MAGIC DC.dim_cust_key,
# MAGIC DP.dim_prod_key,
# MAGIC DR.dim_region_key,
# MAGIC DD.dim_date_key
# MAGIC from
# MAGIC  orderDWH.trans_sales_view F
# MAGIC Left join
# MAGIC  orderDWH.dim_customers_view DC
# MAGIC  on F.customerID = DC.customerID
# MAGIC  Left join
# MAGIC  orderDWH.Dim_products_view DP
# MAGIC  on F.productID = DP.ProductID
# MAGIC  Left join
# MAGIC  orderDWH.dim_Region_view DR
# MAGIC  on F.Country = DR.Country
# MAGIC  Left join
# MAGIC  orderDWH.dim_date_view DD
# MAGIC  on F.orderDate = DD.orderDate
# MAGIC

# COMMAND ----------

