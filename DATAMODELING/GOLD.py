# Databricks notebook source
# MAGIC %sql
# MAGIC select * from datamodeling.silver.silver_table

# COMMAND ----------

# MAGIC %md
# MAGIC ##DIM CUSTOMERS

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.dim_customer
# MAGIC as
# MAGIC with rem_dup
# MAGIC (
# MAGIC     select
# MAGIC  distinct(customer_id),
# MAGIC  customer_email,
# MAGIC  customer_name,
# MAGIC  customer_name_upper
# MAGIC from datamodeling.silver.silver_table
# MAGIC )
# MAGIC select *, row_number() over( order by customer_id) as dim_cust_key from rem_dup

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM  datamodeling.gold.dim_customer
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###dim products

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.dim_product
# MAGIC as
# MAGIC with rem_dup
# MAGIC (
# MAGIC     select
# MAGIC  distinct(product_id),
# MAGIC  product_name,
# MAGIC  product_category
# MAGIC from datamodeling.silver.silver_table
# MAGIC )
# MAGIC select *, row_number() over( order by product_id) as dim_prod_key from rem_dup

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM  datamodeling.gold.dim_product

# COMMAND ----------

# MAGIC %md
# MAGIC ###DIM PAYMENT

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.dim_payment
# MAGIC as
# MAGIC with rem_dup(
# MAGIC select distinct(payment_type) from datamodeling.silver.silver_table
# MAGIC )
# MAGIC select *,row_number() over (order by payment_type) as dim_payment_key from rem_dup

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.dim_payment

# COMMAND ----------

# MAGIC %md
# MAGIC ##dim region

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.dim_region
# MAGIC as
# MAGIC with rem_dup
# MAGIC (
# MAGIC select
# MAGIC  distinct(country) from datamodeling.silver.silver_table
# MAGIC )
# MAGIC select *,row_number()over (order by country) as dim_country_key from rem_dup

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.dim_country

# COMMAND ----------

# MAGIC %md
# MAGIC ###DIM SALES

# COMMAND ----------

spark.sql("select * from datamodeling.silver.silver_table").columns

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.dim_sales
# MAGIC as
# MAGIC select
# MAGIC row_number()over (order by order_id)as dim_sales_key,
# MAGIC  order_id,
# MAGIC  order_date,
# MAGIC  customer_id,
# MAGIC  customer_name,
# MAGIC customer_email,
# MAGIC  product_id,
# MAGIC  product_name,
# MAGIC  product_category,
# MAGIC  payment_type,
# MAGIC  country,
# MAGIC  last_updated,
# MAGIC  customer_name_upper,
# MAGIC process_data from datamodeling.silver.silver_table

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.dim_sales

# COMMAND ----------

# MAGIC %md
# MAGIC ###fact table

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.FACT_SALES
# MAGIC as 
# MAGIC select
# MAGIC F.quantity ,
# MAGIC F.unit_price,
# MAGIC c.dim_cust_key,
# MAGIC p.dim_prod_key,
# MAGIC py.dim_payment_key,
# MAGIC R.dim_country_key,
# MAGIC s.dim_sales_key
# MAGIC from datamodeling.silver.silver_table as F
# MAGIC Left join
# MAGIC datamodeling.gold.dim_customer as c
# MAGIC on c.customer_id=F.customer_id
# MAGIC
# MAGIC Left join
# MAGIC datamodeling.gold.dim_product as p
# MAGIC on p.product_id=F.product_id
# MAGIC
# MAGIC Left join
# MAGIC datamodeling.gold.dim_payment as py
# MAGIC on py.payment_type=F.payment_type
# MAGIC
# MAGIC Left join
# MAGIC datamodeling.gold.dim_country as R
# MAGIC on R.country=F.country
# MAGIC
# MAGIC Left join 
# MAGIC datamodeling.gold.dim_sales as s
# MAGIC on s.order_id=F.order_id
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.FACT_SALES