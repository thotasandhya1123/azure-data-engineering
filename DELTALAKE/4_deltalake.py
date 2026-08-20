# Databricks notebook source
# MAGIC %md
# MAGIC #DML
# MAGIC

# COMMAND ----------

data=[(1,100,'aa',1),(2,200,'bb',1),(3,300,'cc',1)]
df=spark.createDataFrame(data,['cust_id','income','name','tip'])
df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalake/default/deltalakevol/dmlsink/")

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #data added

# COMMAND ----------

data=[(4,100,'aa',1),(5,200,'bb',1),(6,300,'cc',1)]
df=spark.createDataFrame(data,['cust_id','income','name','tip'])
df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalake/default/deltalakevol/dmlsink/")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalake/default/deltalakevol/dmlsink`

# COMMAND ----------

# MAGIC %md
# MAGIC #update

# COMMAND ----------

# MAGIC %sql
# MAGIC update delta.`/Volumes/deltalake/default/deltalakevol/dmlsink` 
# MAGIC set income = '1000' where cust_id =5

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalake/default/deltalakevol/dmlsink`

# COMMAND ----------

# MAGIC %md
# MAGIC # UPSERT

# COMMAND ----------

data=[(1,100,'XYZ',1),(7,200,'bb',1),(8,300,'cc',1)]
df=spark.createDataFrame(data,['cust_id','income','name','tip'])


display(df)

# COMMAND ----------


from delta.tables import DeltaTable


# COMMAND ----------

dlt_obj=DeltaTable.forPath(spark,"/Volumes/deltalake/default/deltalakevol/dmlsink")
dlt_obj.alias("trg").merge(df.alias("src"),
                            "trg.cust_id = src.cust_id")\
.whenMatchedUpdateAll()\
.whenNotMatchedInsertAll()\
.execute()

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalake/default/deltalakevol/dmlsink/`