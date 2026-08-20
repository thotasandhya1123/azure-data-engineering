# Databricks notebook source
# MAGIC %md
# MAGIC ###schema enforcement

# COMMAND ----------

data=[(1,100,'aa',1),(2,200,'bb',1),(3,300,'cc',1)]
df=spark.createDataFrame(data,['id','salary','name','se'])
display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalake/default/deltalakevol/demosink/")

# COMMAND ----------

# MAGIC %md
# MAGIC # SCHEMA EVOLUTION

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("mergeSchema",True)\
    .save("/Volumes/deltalake/default/deltalakevol/demosink/")

# COMMAND ----------

# MAGIC %md
# MAGIC #READ DELTA DATA

# COMMAND ----------

# MAGIC %md
# MAGIC ####table

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from deltalake.default.firstdeltaapi

# COMMAND ----------

# MAGIC %md
# MAGIC # DATA LAKE 

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from delta .`/Volumes/deltalake/default/deltalakevol/demosink/`

# COMMAND ----------

# MAGIC %md
# MAGIC ## ### schema overwrite

# COMMAND ----------

data=[(1,100,'aa',1),(2,200,'bb',1),(3,300,'cc',1)]
df=spark.createDataFrame(data,['cust_id','income','name','tip'])
display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("mergeSchema",True)\
    .save("/Volumes/deltalake/default/deltalakevol/demosink/")

display(df)