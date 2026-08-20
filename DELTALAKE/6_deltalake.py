# Databricks notebook source
# MAGIC %md
# MAGIC # TABLE UTILITY COMMANDS

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail deltalake.default.first_table

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended deltalake.default.first_table

# COMMAND ----------

# MAGIC %md
# MAGIC ## versioning

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY delta.`/Volumes/deltalake/default/deltalakevol/dmlsink/`

# COMMAND ----------

# MAGIC %md
# MAGIC ## TIME TRAVELLING

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta. `/Volumes/deltalake/default/deltalakevol/dmlsink/`

# COMMAND ----------

# MAGIC %sql
# MAGIC restore delta.`/Volumes/deltalake/default/deltalakevol/dmlsink/` 
# MAGIC     TO VERSION AS OF 3

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta. `/Volumes/deltalake/default/deltalakevol/dmlsink/`

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta. `/Volumes/deltalake/default/deltalakevol/dmlsink/`
# MAGIC version as  of 5

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta. `/Volumes/deltalake/default/deltalakevol/dmlsink/`
# MAGIC timestamp as of '2026-08-02T05:30:20.000+00:00'

# COMMAND ----------

# MAGIC %md
# MAGIC ### #table properties

# COMMAND ----------

# MAGIC %sql
# MAGIC -- NORMAL TABLE
# MAGIC SHOW TBLPROPERTIES deltalake.default.first_table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- DELTA TABLE
# MAGIC SHOW TBLPROPERTIES delta.`/Volumes/deltalake/default/deltalakevol/dmlsink`

# COMMAND ----------

# MAGIC %md
# MAGIC ### VACCUME COMMAND 

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum delta .`/Volumes/deltalake/default/deltalakevol/dmlsink`

# COMMAND ----------

# MAGIC %md
# MAGIC ### CLONE

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table deltalake.default.clonetbl
# MAGIC clone delta . `/Volumes/deltalake/default/deltalakevol/dmlsink/` version as of 3
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.clonetbl

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table deltalake.default.clonetblshallow
# MAGIC shallow clone deltalake.default.first_table
# MAGIC     
# MAGIC