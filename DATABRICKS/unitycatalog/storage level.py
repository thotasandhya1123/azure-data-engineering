# Databricks notebook source























# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists managed_catalog.managed_schema;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists managed_catalog.managed_schema.managed_table

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists managed_catalog.managed_schema.managed_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC  insert into managed_catalog.managed_schema.managed_table 
# MAGIC values 
# MAGIC ( 1,"john"),
# MAGIC ( 2,"mary"),
# MAGIC (3,"Mike");

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from managed_catalog.managed_schema.managed_table

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended
# MAGIC managed_catalog.managed_schema.managed_table;

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists ext_catlog
# MAGIC managed location 'abfss://rawdata@databricksunitysandhya1.dfs.core.windows.net/'

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists ext_catlog.ext_schema.ext_table
# MAGIC (
# MAGIC     id int,
# MAGIC     name string
# MAGIC )
# MAGIC using delta
# MAGIC location 'abfss://rawdata@databricksunitysandhya.dfs.core.windows.net/'

# COMMAND ----------

# MAGIC %sql
# MAGIC  insert into ext_catalog.ext_schema.ext_table 
# MAGIC values 
# MAGIC ( 1,"john"),
# MAGIC ( 2,"mary"),
# MAGIC (3,"Mike");

# COMMAND ----------

# MAGIC %md
# MAGIC ## ### VOLUMES

# COMMAND ----------

# MAGIC %sql
# MAGIC Create external volume ext_catlog.ext_schema.ext_volume
# MAGIC location 'abfss://rawdata@databricksunitysandhya.dfs.core.windows.net/data'

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`/Volumes/ext_catlog/ext_schema/ext_volume/DimAirline.csv`

# COMMAND ----------

# MAGIC %md
# MAGIC ## DATA MASKING unity catalog functions

# COMMAND ----------

# MAGIC %sql
# MAGIC create table ext_catlog.ext_schema.employee
# MAGIC (
# MAGIC     id int,
# MAGIC     name string,
# MAGIC     salary int
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into ext_catlog.ext_schema.employee
# MAGIC values
# MAGIC (1,"john",1000),
# MAGIC (2,"mary",2000),
# MAGIC (3,"Mike",3000);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from ext_catlog.ext_schema.employee

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace FUNCTION ext_catlog.ext_schema.maksing(salary STRING) RETURNS STRING
# MAGIC RETURN CASE WHEN is_account_group_member('Admins') THEN salary ELSE '******' END

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE ext_catlog.ext_schema.employee 
# MAGIC ALTER COLUMN salary set mask ext_catlog.ext_schema.maksing

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from ext_catlog.ext_schema.employee