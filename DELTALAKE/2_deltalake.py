# Databricks notebook source
# MAGIC %md
# MAGIC # **DELTA LOG**

# COMMAND ----------

data=[(1,100,'aa'),(2,200,'bb'),(3,300,'cc')]
df=spark.createDataFrame(data,['id','salary','name'])
display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalake/default/deltalakevol/demosink/")

# COMMAND ----------

df=spark.read.format("json")\
    .load("/Volumes/deltalake/default/deltalakevol/demosink/_delta_log/00000000000000000000.json")
display(df)