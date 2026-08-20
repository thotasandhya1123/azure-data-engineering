# Databricks notebook source


# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE deltalake.default.clonetbl
# MAGIC set TBLPROPERTIES(delta.enableChangeDataFeed = true)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.clonetbl

# COMMAND ----------

# MAGIC %md
# MAGIC insert data

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into deltalake.default.clonetbl
# MAGIC values(7,100,"zz",1)

# COMMAND ----------

# MAGIC %md
# MAGIC ### update data

# COMMAND ----------

# MAGIC %sql
# MAGIC update deltalake.default.clonetbl
# MAGIC set name="hi bro" where cust_id=7

# COMMAND ----------

# MAGIC %md
# MAGIC deleted the data

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from deltalake.default.clonetbl where cust_id=3

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history deltalake.default.clonetbl

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table_changes('deltalake.default.clonetbl', 1)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table_changes('deltalake.default.clonetbl', 1,3)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.clonetbl