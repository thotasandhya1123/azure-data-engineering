# Databricks notebook source
# MAGIC %sql
# MAGIC Select * from datamodeling.bronze.bronze_table

# COMMAND ----------

# MAGIC %md
# MAGIC ##upserrt

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * ,
# MAGIC upper(customer_name)as customer_name_upper,
# MAGIC date(current_timestamp())as process_data
# MAGIC from datamodeling.bronze.bronze_table

# COMMAND ----------

# MAGIC %md
# MAGIC ##create source table

# COMMAND ----------

spark.sql("""Select * ,
upper(customer_name)as customer_name_upper,
date(current_timestamp())as process_data
from datamodeling.bronze.bronze_table""").createOrReplaceTempView("silver_source")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver_source

# COMMAND ----------

# MAGIC %md
# MAGIC ###_merge using pyspark

# COMMAND ----------

if spark.catalog.tableExists('datamodeling.silver.silver_table'):
    src=spark.sql(""" select * from silver_source""")


else:
    spark.sql("""
                CREATE TABLE IF NOT EXISTS datamodeling.silver.silver_table
                AS 
                SELECT * FROM silver_source""")

# COMMAND ----------

# MAGIC %md
# MAGIC ##merge using sql

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS datamodeling.silver.silver_table
# MAGIC                 AS 
# MAGIC                 SELECT * FROM silver_source

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO  datamodeling.silver.silver_table  t
# MAGIC USING silver_source s
# MAGIC ON t.order_id = s.order_id
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.silver.silver_table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- extra
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###incremental data to source 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- data added
# MAGIC INSERT INTO datamodeling.default.source_data VALUES 
# MAGIC (1004, '2024-07-02', 4, 'David Lee', 'david@abc.com', 504, 'Samsung S23', 'Electronics', 1, 899.99, 'Credit Card', 'USA', '2024-07-02'),
# MAGIC (1005, '2024-07-02', 1, 'Alice Johnson', 'alice@gmail.com', 503, 'Nike Shoes', 'Footwear', 2, 129.99, 'Credit Card', 'USA', '2024-07-02');

# COMMAND ----------

if spark.catalog.tableExists("datamodeling.bronze.bronze_table"):
    last_load_date=spark.sql("select max(order_date) from datamodeling.bronze.bronze_table").collect()[0][0]
else:
    last_load_date='1000-01-01'

# COMMAND ----------

last_load_date