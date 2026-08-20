# Databricks notebook source
df=spark.read.table("deltalake.default.clonetbl")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta")\
        .mode("append")\
        .save("/Volumes/deltalake/default/deltalakevol/OPTIMIZATION/")

# COMMAND ----------

# MAGIC %md
# MAGIC ### optimize

# COMMAND ----------

# MAGIC %sql
# MAGIC optimize delta.`/Volumes/deltalake/default/deltalakevol/OPTIMIZATION/`

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history delta. `/Volumes/deltalake/default/deltalakevol/OPTIMIZATION`

# COMMAND ----------

# MAGIC %md
# MAGIC ### zorder

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`/Volumes/deltalake/default/deltalakevol/OPTIMIZATION/`
# MAGIC WHERE cust_id = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC OPTIMIZE delta .`/Volumes/deltalake/default/deltalakevol/OPTIMIZATION/`
# MAGIC ZORDER BY (cust_id)

# COMMAND ----------

# MAGIC %md
# MAGIC liquid cluster

# COMMAND ----------

# MAGIC %sql
# MAGIC ALTER TABLE deltalake.default.clonetbl
# MAGIC CLUSTER BY AUTO