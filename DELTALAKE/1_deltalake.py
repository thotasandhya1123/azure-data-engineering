# Databricks notebook source
# MAGIC %md
# MAGIC #create delta table

# COMMAND ----------

# MAGIC %md
# MAGIC using SQL api

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table deltalake.default.first_table(
# MAGIC     id int unique,
# MAGIC     salary int not null
# MAGIC )

# COMMAND ----------

# MAGIC %md
# MAGIC using delta api

# COMMAND ----------

from delta.tables import DeltaTable, IdentityGenerator

# COMMAND ----------

DeltaTable.createIfNotExists(spark) \
  .tableName("deltalake.default.firstdeltaapi") \
  .addColumn("id", "INT") \
  .addColumn("salary", "INT") \
  .execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC drop  table if exists  deltalake.default.firstdeltaapi

# COMMAND ----------

# MAGIC %md
# MAGIC ###Generated columns

# COMMAND ----------

# MAGIC %md
# MAGIC ####Identity columns

# COMMAND ----------


from pyspark.sql.functions import * 
from pyspark.sql.types import *

# COMMAND ----------

(DeltaTable.create(spark)\
  .tableName("deltalake.default.firstdeltaapi")\
    .addColumn("id_col", dataType=LongType(), generatedAlwaysAs=IdentityGenerator())\
  .addColumn("salary", "INT")\
  .addColumn("name", "STRING")
  .execute())

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.default.firstdeltaapi(salary,name)
# MAGIC values(100,"aa"),
# MAGIC (200,"bb"),
# MAGIC (300,"cc")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.firstdeltaapi

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ####computed columns

# COMMAND ----------

DeltaTable.create(spark)\
  .tableName("deltalake.default.first_1deltaapi")\
  .addColumn("salaryAfterTax", dataType=LongType(), generatedAlwaysAs = "CAST((salary * 0.7) AS BIGINT)")\
   .addColumn("salary", "INT")\
  .addColumn("name", "STRING")\
  .execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.default.first_1deltaapi(salary,name)
# MAGIC values(100,"aa"),
# MAGIC (200,"bb"),
# MAGIC (300,"cc")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.first_1deltaapi

# COMMAND ----------

