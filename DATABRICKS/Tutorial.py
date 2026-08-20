# Databricks notebook source
# MAGIC %md
# MAGIC # DATABRICKS

# COMMAND ----------

print("Hello World")

# COMMAND ----------

data=(1,"a",30),(2,"b",40),(3,"c",50)
schema="id int,name string,marks int"
df=spark.createDataFrame(data,schema)

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC # ACCESS DATA

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 5fb8477a-1f09-4530-81df-182af259aec6 applicationid
# MAGIC -- 69155191-f4d0-45e9-8316-64648959bcc3 tenant id
# MAGIC
# MAGIC -- RbP8Q~4MnbUzBkd7G5g~_daGZyJhk~hfExl_DcQY value
# MAGIC -- 98300cda-f30a-4344-9d70-7831f680634f secrate

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.datalakesandhya.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.datalakesandhya.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.datalakesandhya.dfs.core.windows.net", "5fb8477a-1f09-4530-81df-182af259aec6")
spark.conf.set("fs.azure.account.oauth2.client.secret.datalakesandhya.dfs.core.windows.net", "RbP8Q~4MnbUzBkd7G5g~_daGZyJhk~hfExl_DcQY")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.datalakesandhya.dfs.core.windows.net", "https://login.microsoftonline.com/69155191-f4d0-45e9-8316-64648959bcc3/oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATABRICKS UTILITIES

# COMMAND ----------

# MAGIC %md
# MAGIC dbutils.fs()

# COMMAND ----------

# MAGIC %md
# MAGIC ### dbutils.widgets

# COMMAND ----------

dbutils.widgets.text("p_name","sandy")

# COMMAND ----------

var=dbutils.widgets.get("p_name")

# COMMAND ----------

var

# COMMAND ----------

# MAGIC %md
# MAGIC ### dbutils.secrets

# COMMAND ----------

dbutils.secrets.list(scope="sandhyascope")


# COMMAND ----------

dbutils.secrets.get(scope="sandhyascope",key="appsecret")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Reading

# COMMAND ----------

df_sales=spark.read.format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://source@datalakesandhya.dfs.core.windows.net")



# COMMAND ----------

df_sales.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### pyspark trasformations

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1st trans

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

df_sales.withColumn("Item_Type",split(col("Item_Type")," ")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC 2nd trans

# COMMAND ----------

df_sales.withColumn("flag",lit(var)).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3rd trans

# COMMAND ----------

df_sales.withColumn('Item_visibility',col('Item_Visibility').cast(StringType())).display()


# COMMAND ----------

