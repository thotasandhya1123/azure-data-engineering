# Databricks notebook source
# MAGIC %md
# MAGIC ###SILVER LAYER SCRIPT

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *


# COMMAND ----------

# MAGIC %md
# MAGIC ##DATA ACCESS USING APPLICATION

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.azprojectdatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.azprojectdatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.azprojectdatalake.dfs.core.windows.net", "f5264f02-c25d-4724-ba34-faa9d0ad8bfe")
spark.conf.set("fs.azure.account.oauth2.client.secret.azprojectdatalake.dfs.core.windows.net","ZSh8Q~9mUR3uBTlvhkDIa3l9pQDDhJanL79E3ad~")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.azprojectdatalake.dfs.core.windows.net", 
               "https://login.microsoftonline.com/69155191-f4d0-45e9-8316-64648959bcc3/oauth2/token")


# COMMAND ----------

# MAGIC %md
# MAGIC ## READ DATA

# COMMAND ----------

df_cal=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Calendar")

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cust=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Customers")

# COMMAND ----------

df_prod_cat=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")

# COMMAND ----------

df_prods=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Products")

# COMMAND ----------

df_ret=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Returns")

# COMMAND ----------

df_sales15=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Sales_2015")

# COMMAND ----------

df_terr=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Territories")

# COMMAND ----------

df_prod_sub=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/Product_Subcategories")

# COMMAND ----------

df_sales=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Sales*")

# COMMAND ----------

df_sales16=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Sales_2016")

# COMMAND ----------

df_sales17=spark.read.format('csv')\
    .option("header",True)\
    .option("inferSchema",True)\
    .load("abfss://bronze@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Sales_2017")

# COMMAND ----------

# MAGIC %md
# MAGIC ###TRANSFORMATIONS

# COMMAND ----------

# MAGIC %md
# MAGIC ###calender

# COMMAND ----------

df_cal=df_cal.withColumn('month',month(col('Date')))\
        .withColumn('year',dayofmonth(col('Date')))

# COMMAND ----------

df_cal.display()

# COMMAND ----------

# MAGIC %md
# MAGIC write transformed data to silver layer

# COMMAND ----------

df_cal.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Calendar")\
    .save()

   

# COMMAND ----------

# MAGIC %md
# MAGIC # customers

# COMMAND ----------

df_cust.display()

# COMMAND ----------

df_cust.withColumn("fullname",concat(col('prefix'),lit(''),col('firstname'),lit(' '),col('lastname'))).display()

# COMMAND ----------

df_cust=df_cust.withColumn("fullname",concat_ws(' ',col("Prefix"),col("FirstName"),col("LastName")))
df_cust.display()

# COMMAND ----------

df_cust.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Customers")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ## prod_categerioes

# COMMAND ----------

df_prod_cat.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Product_Categories")\
    .save()


# COMMAND ----------

# MAGIC %md
# MAGIC # sub categerioes

# COMMAND ----------

df_prod_sub.display()

# COMMAND ----------

df_prod_sub.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/Product_Subcategories")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### # products

# COMMAND ----------

df_prods.display()

# COMMAND ----------

df_prods=df_prods.withColumn("ProductSKU",split(col('ProductSKU'),'-')[0])\
                .withColumn("ProductName",split(col('ProductName'),' ')[0])
               

# COMMAND ----------

df_prods.display()

# COMMAND ----------

df_prods.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_Products")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC returns

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_return")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ## TERRITORIES

# COMMAND ----------

df_terr.display()

# COMMAND ----------

df_terr.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_territories")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales=df_sales.withColumn('StockDate',to_timestamp("StockDate"))

# COMMAND ----------

df_sales=df_sales.withColumn('OrderNumber',regexp_replace(col("OrderNumber"),'S','T'))

# COMMAND ----------

df_sales=df_sales.withColumn('Multiply',col("OrderlineItem")*col("OrderQuantity"))

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('parquet')\
    .mode('append')\
    .option("path","abfss://silver@azprojectdatalake.dfs.core.windows.net/AdventureWorks_sales")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sales Analysis

# COMMAND ----------

df_sales.groupby("OrderDate").agg(count("OrderNumber").alias("total_orders")).display()


# COMMAND ----------

df_prod_cat.display()


# COMMAND ----------

df_terr.display()