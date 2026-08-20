# Databricks notebook source
data=[(1,100,'aa',1),(2,200,'bb',1),(3,300,'cc',1)]
df=spark.createDataFrame(data,['cust_id','income','name','tip'])
df.write.format("delta")\
    .mode("append")\
    .save("/Volumes/deltalake/default/deltalakevol/schemalevel/")
display(df)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Enable column mapping first
# MAGIC ALTER TABLE delta.`/Volumes/deltalake/default/deltalakevol/schemalevel/`
# MAGIC SET TBLPROPERTIES (
# MAGIC     'delta.minReaderVersion' = '2',
# MAGIC     'delta.minWriterVersion' = '5',
# MAGIC     'delta.columnMapping.mode' = 'name');

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Now rename the column
# MAGIC ALTER TABLE delta.`/Volumes/deltalake/default/deltalakevol/schemalevel/`
# MAGIC RENAME COLUMN name to customer_name;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/deltalake/default/deltalakevol/schemalevel`

# COMMAND ----------

df=spark.read.format("json")\
    .load("/Volumes/deltalake/default/deltalakevol/schemalevel/_delta_log/00000000000000000002.json")
df.display()