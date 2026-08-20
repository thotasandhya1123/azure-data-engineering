# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE or replace TABLE deltalake.default.unitbl(
# MAGIC     id  int,
# MAGIC     name string
# MAGIC
# MAGIC )
# MAGIC USING DELTA TBLPROPERTIES(
# MAGIC   'delta.enableIcebergCompatV2' = 'true',
# MAGIC   'delta.universalFormat.enabledFormats' = 'iceberg');
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO deltalake.default.unitbl
# MAGIC values(1,'aa'),(2,'bb')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.unitbl