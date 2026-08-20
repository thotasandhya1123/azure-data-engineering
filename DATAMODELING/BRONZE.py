# Databricks notebook source

last_load_date='2000-01-01'

# COMMAND ----------

if spark.catalog.tableExists("datamodeling.bronze.bronze_table"):
    last_load_date = spark.sql("SELECT max(order_date) FROM datamodeling.bronze.bronze_table").collect()[0][0]
else:
    last_load_date = '1000-01-01'

# COMMAND ----------

last_load_date

# COMMAND ----------


spark.sql(f"""
        select * from datamodeling.default.source_data
        where order_date > '{last_load_date}'
""").createOrReplaceTempView("bronze_source")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronze_source

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.bronze.bronze_table
# MAGIC as
# MAGIC select * from bronze_source

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.bronze.bronze_table

# COMMAND ----------

# MAGIC %md
# MAGIC after incremental loadinng

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronze_source