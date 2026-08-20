# Databricks notebook source
# MAGIC %run ./Tutorial

# COMMAND ----------

# MAGIC %md
# MAGIC # DELTA LAKE

# COMMAND ----------

df_sales.write.format("delta")\
    .mode("append")\
    .save('abfss://destination@datalakesandhya.dfs.core.windows.net/sales')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Managed Vs External Delta Tables
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Managed Table**

# COMMAND ----------

# MAGIC %md
# MAGIC **DATABASE**

# COMMAND ----------

# MAGIC %sql
# MAGIC create database salesDB;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table salesDB.mantble(
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     marks int   
# MAGIC )
# MAGIC using delta

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDB.mantble
# MAGIC values
# MAGIC (1,"aa",30),
# MAGIC (2,"bb",40),
# MAGIC (3,"cc",50),
# MAGIC (4,"dd",60)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.mantble

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table salesDB.mantble

# COMMAND ----------

# MAGIC %md
# MAGIC External **table**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace TABLE salesDB.ext_1table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     marks int
# MAGIC )
# MAGIC using delta
# MAGIC LOCATION 'abfss://destination@datalakesandhya.dfs.core.windows.net/salesDB/ext_1table'
# MAGIC     
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDB.ext_1table
# MAGIC values
# MAGIC (1,"aa",30),
# MAGIC (2,"bb",40),
# MAGIC (3,"cc",50),
# MAGIC (4,"dd",60)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

dbutils.fs.ls('abfss://destination@datalakesandhya.dfs.core.windows.net/')

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC ## Delta table functionalities

# COMMAND ----------

# MAGIC %md
# MAGIC ### insert

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace TABLE salesDB.ext_1table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     marks int
# MAGIC )
# MAGIC using delta
# MAGIC LOCATION 'abfss://destination@datalakesandhya.dfs.core.windows.net/salesDB/ext_1table'

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDB.ext_1table
# MAGIC values
# MAGIC (1,"aa",30),
# MAGIC (2,"bb",40),
# MAGIC (3,"cc",50),
# MAGIC (4,"dd",60)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into salesDB.ext_1table
# MAGIC values
# MAGIC (5,"aa",30),
# MAGIC (6,"bb",40),
# MAGIC (7,"cc",50),
# MAGIC (8,"dd",60)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC ### delete

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from salesDB.ext_1table
# MAGIC where id=8

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC TIME TRAVEL

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table salesDB.ext_1table to version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC ### VACCUME
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC ### vacuum retain 0 hours

# COMMAND ----------

# MAGIC %sql
# MAGIC VACUUM salesDB.ext_1table reatin 0 hours

# COMMAND ----------

# MAGIC %md
# MAGIC ## DELTA TABLEOPTIMIZATION

# COMMAND ----------

# MAGIC %md
# MAGIC ### OPTIMIZE

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

# MAGIC %sql
# MAGIC optimize salesDB.ext_1table
# MAGIC     
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Z ORDER BY

# COMMAND ----------

# MAGIC %sql
# MAGIC optimize salesDB.ext_1table zorder by (id)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from salesDB.ext_1table

# COMMAND ----------

# MAGIC %md
# MAGIC ### AUTO LOADER

# COMMAND ----------

# MAGIC %md
# MAGIC ### streamind data frame

# COMMAND ----------

df=spark.readStream.format("cloudFiles")\
    .option("cloudFiles.format", "parquet")\
    .option("cloudFiles.schemaLocation","abfss://aldestination@datalakesandhya.dfs.core.windows.net/checkpoint")\
    .load("abfss://alsource@datalakesandhya.dfs.core.windows.net")

# COMMAND ----------

k=dbutils.secrets.get(scope="sandhyascope", key="appsecret")
print(len(k))

# COMMAND ----------

dbutils.secrets.get(scope="sandhyascope", key="appsecret")

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.datalakesandhya.dfs.core.windows.net",
    dbutils.secrets.get(scope="sandhyascope", key="appsecret")
)

# COMMAND ----------

df.writeStream.format("delta")\
    .option("checkpointLocation", "abfss://aldestination@datalakesandhya.dfs.core.windows.net/checkpoint")\
    .trigger(processingTime="5 seconds")\
    .start("abfss://aldestination@datalakesandhya.dfs.core.windows.net/data")

# COMMAND ----------

