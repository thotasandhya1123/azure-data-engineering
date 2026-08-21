# Databricks notebook source
df=spark.read.format('csv')\
    .option('inferschema',True)\
        .option('header',True)\
            .load('/Volumes/workspace/stream/csv/BigMart_Sales.csv')


# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC #window functions

# COMMAND ----------

# MAGIC %md
# MAGIC #row_number()

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
df.withColumn("row_num",row_number().over(Window.orderBy('Item_Identifier'))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #rank()

# COMMAND ----------

from pyspark.sql.functions import rank
df.withColumn("row_num",rank().over(Window.orderBy(col('Item_Identifier').desc()))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #dense_rank()

# COMMAND ----------

from pyspark.sql.functions import dense_rank,col
df.withColumn("den_rk",dense_rank().over(Window.orderBy('Item_Identifier'))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #cumulative sum

# COMMAND ----------

from pyspark.sql.functions import sum
df.withColumn('cumsum',sum(col('Item_MRP')).over(Window.orderBy(col('Item_Type')))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #frame clause

# COMMAND ----------


df.withColumn('cumsum',sum(col('Item_MRP')).over(Window.orderBy(col('Item_Type')).rowsBetween(Window.unboundedPreceding,Window.currentRow))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #over all sum

# COMMAND ----------

df.withColumn('tolsum',sum(col('Item_MRP')).over(Window.orderBy(col('Item_Type')).rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing))).display()




# COMMAND ----------

# MAGIC %md
# MAGIC #user defined function

# COMMAND ----------

# MAGIC %md
# MAGIC #step1

# COMMAND ----------

def my_func(x):
    return x*x

# COMMAND ----------

# MAGIC %md
# MAGIC #step2

# COMMAND ----------

my_udf=udf(my_func)

# COMMAND ----------

df.withColumn("square",my_udf("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC DATA WRITING

# COMMAND ----------

# MAGIC %md
# MAGIC #csv

# COMMAND ----------

df.write.format("csv")\
    .save("/Volumes/workspace/stream/csv/data.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC #append

# COMMAND ----------

df.write.format("csv")\
    .mode("append")\
    .save("/Volumes/workspace/stream/csv/data.csv")

# COMMAND ----------

df.write.format("csv")\
    .mode("append")\
    .option("path","/Volumes/workspace/stream/csv/data.csv")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #over write

# COMMAND ----------

df.write.format("csv")\
    .mode("overwrite")\
    .option("path","/Volumes/workspace/stream/csv/data.csv")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #error

# COMMAND ----------

df.write.format("csv")\
    .mode("error")\
    .option("path","/Volumes/workspace/stream/csv/data.csv")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ###ignore

# COMMAND ----------

df.write.format("csv")\
    .mode("ignore")\
    .option("path","/Volumes/workspace/stream/csv/data.csv")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #parquet

# COMMAND ----------

df.write.format("parquet")\
    .mode("overwrite")\
    .option("path","/Volumes/workspace/stream/csv/data.csv")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #table

# COMMAND ----------

df.write.format("Delta")\
    .mode("overwrite")\
    .saveAsTable("my_table")

# COMMAND ----------

# MAGIC %md
# MAGIC #spark sql

# COMMAND ----------

# MAGIC %md
# MAGIC #createtempview

# COMMAND ----------

df.createTempView('my_view')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_view

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from my_view where Item_Fat_Content = "Regular"

# COMMAND ----------

df_sql=spark.sql('select * from my_view where Item_Fat_Content = "Regular"')


# COMMAND ----------

display(df_sql)