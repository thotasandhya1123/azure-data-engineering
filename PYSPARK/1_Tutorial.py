# Databricks notebook source
# MAGIC %md
# MAGIC ###DATA READING JSON

# COMMAND ----------

df_json=spark.read.format('json').option('inferschema',True)\
                                 .option('header',True)\
                                 .option('Multiline',False)\
                                 .load('/Volumes/workspace/stream/json')
                        

# COMMAND ----------

display(df_json)


# COMMAND ----------

# MAGIC %md
# MAGIC ###DATA READING

# COMMAND ----------

df=spark.read.format('csv')\
    .option('inferschema',True)\
        .option('header',True)\
            .load('/Volumes/workspace/stream/csv/BigMart_Sales.csv')


# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###DDL SCHEMA

# COMMAND ----------

df.printSchema()

# COMMAND ----------

my_ddl_schema='''
                Item_Identifier STRING,
                    Item_Weight STRING,
                    Item_Fat_Content STRING, 
                    Item_Visibility DOUBLE,
                    Item_Type STRING,
                    Item_MRP DOUBLE,
                    Outlet_Identifier STRING,
                    Outlet_Establishment_Year INT,
                    Outlet_Size STRING,
                    Outlet_Location_Type STRING, 
                    Outlet_Type STRING,
                    Item_Outlet_Sales DOUBLE
 '''

# COMMAND ----------

df=spark.read.format('csv')\
    .schema(my_ddl_schema)\
    .option('header',True)\
    .load('/Volumes/workspace/stream/csv/BigMart_Sales.csv')

# COMMAND ----------

df.display()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### struct type schema

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

my_strct_schema = StructType([ 
                              StructField('Item_Identifier',StringType(),True),
                             StructField('Item_Weight',StringType(),True),
                             StructField('Item_Fat_Content',StringType(),True),
                              StructField('Item_Visibility',StringType(),True), 
                              StructField('Item_MRP',StringType(),True), 
                              StructField('Outlet_Identifier',StringType(),True), 
                              StructField('Outlet_Establishment_Year',StringType(),True), 
                              StructField('Outlet_Size',StringType(),True), 
                              StructField('Outlet_Location_Type',StringType(),True),
                            StructField('Outlet_Type',StringType(),True),
                             StructField('Item_Outlet_Sales',StringType(),True)

])

# COMMAND ----------

df=spark.read.format('csv')\
    .schema(my_strct_schema)\
    .option('header',True)\
    .load('/Volumes/workspace/stream/csv/BigMart_Sales.csv')

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### select
# MAGIC

# COMMAND ----------

df.display()

# COMMAND ----------

df_select=df.select("Item_Identifier","Item_Weight").display()

# COMMAND ----------

from pyspark.sql.functions import col
df.select(col("Item_Identifier"),col("Item_Weight")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###alias

# COMMAND ----------

df.select(col("Item_Identifier").alias ("Item_ID")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###FILTER/WHERE

# COMMAND ----------

# MAGIC %md
# MAGIC ### SCENERIO 1PULL THE DATA FRAME AND RECORDS WHERE FAT CINTENT IS REGULAR 
# MAGIC

# COMMAND ----------

df.filter(col("Item_Fat_Content")== "Regular").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 2 fetch data where item_type is soft drinks and item weight is less than 5.92
# MAGIC

# COMMAND ----------

df.filter( (col("Item_Type") == 'Soft Drinks') &
            ((col("Item_Weight")) <= 5.92) ).display()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 3 .Fetch the data with tiet in(tier 1 or tier 2)and outlet size is null

# COMMAND ----------

from pyspark.sql.functions import col
df.filter(
    (col("Outlet_Size").isNull()) &(col("Outlet_Location_Type").isin("Tier 1","Tier 2"))).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### WITH COLUMN RENAMED

# COMMAND ----------

df.withColumnRenamed("Item_Weight","Item_WT").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### withColumn

# COMMAND ----------

# MAGIC %md
# MAGIC ### scenerio-1

# COMMAND ----------

from pyspark.sql.functions import lit
df=df.withColumn('flag',lit('new')).display()


# COMMAND ----------

df.display()

# COMMAND ----------

df.withColumn('multiply',col('Item_Visibility')*col('Item_MRP')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio -2

# COMMAND ----------

from pyspark.sql.functions import regexp_replace
df.withColumn("Item_Fat_Content",regexp_replace(col("Item_Fat_Content"),"Regular","Reg"))\
   .withColumn("Item_Fat_Content",regexp_replace(col("Item_Fat_Content"),"Low Fat","LF")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###type casting
# MAGIC

# COMMAND ----------

 from pyspark.sql.types import StringType 
 df=df.withColumn("Item_Weight",col('Item_Weight').cast(StringType())).display()


# COMMAND ----------

# MAGIC %md
# MAGIC sort/order by

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 1
# MAGIC

# COMMAND ----------

df.sort(col("Item_weight").desc()).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 2
# MAGIC

# COMMAND ----------

df.sort(col("Item_Visibility").asc()).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerios 3

# COMMAND ----------

df.sort(["Item_Weight","Item_Visibility"],ascending=[0,0]).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #scenerio 4

# COMMAND ----------

df.sort(["Item_Weight","Item_Visibility"],ascending=[0,1]).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###limit

# COMMAND ----------

df.limit(5).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###DROP

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 1

# COMMAND ----------

df.drop("Item_Visibility").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 2 drop multiple colums

# COMMAND ----------

df.drop("Item_Visibility","Item_MRP").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###drop duplicates

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 1

# COMMAND ----------

df.drop_duplicates().display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 2

# COMMAND ----------

df.drop_duplicates( subset=["Item_Type"]).display()

# COMMAND ----------

df.distinct().display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###union

# COMMAND ----------

# MAGIC %md
# MAGIC ###preparing dataframe

# COMMAND ----------

data1 = [('1','kad'),
        ('2','sid')]
schema1 = 'id STRING, name STRING' 

df1 = spark.createDataFrame(data1,schema1)

data2 = [('3','rahul'),
        ('4','jas')]
schema2 = 'id STRING, name STRING' 

df2 = spark.createDataFrame(data2,schema2)
display(df1)
display(df2)


# COMMAND ----------

df1. union( df2).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###union by name

# COMMAND ----------

data1 = [('kad','1'),
        ('sid','2')]
schema1 = 'name STRING,id STRING ' 

df1 = spark.createDataFrame(data1,schema1)

data2 = [('3','rahul'),
        ('4','jas')]
schema2 = 'id STRING, name STRING' 

df2 = spark.createDataFrame(data2,schema2)
display(df1)
display(df2)


# COMMAND ----------

df1.unionByName(df2).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###string functions
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###Initcap()

# COMMAND ----------

from pyspark.sql.functions import initcap
df.select(initcap("Item_Type")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###upper

# COMMAND ----------

from pyspark.sql.functions import upper
df.select(upper("Item_Type")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###lower

# COMMAND ----------

from pyspark.sql.functions import lower
df.select(lower("Item_Type").alias("lower") ).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###date functions

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC current_date

# COMMAND ----------

from pyspark.sql.functions import current_date
df=df.withColumn("cur_date", current_date())
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Date_Add()
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import date_add
df=df.withColumn("1_week_later",date_add("cur_date",7))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###date_sub()

# COMMAND ----------

from pyspark.sql.functions import date_sub
df=df.withColumn("week_ago",date_sub("cur_date",7))
df.display()


# COMMAND ----------

df=df.withColumn("1_week_before",date_add("cur_date",-7))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###datediff

# COMMAND ----------

from pyspark.sql.functions import datediff,col
df=df.withColumn("datediff",datediff("week_ago","cur_date"))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###dateformat
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import date_format
df=df.withColumn("week_ago",date_format("week_ago","dd-MM-yyyy"))
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Handling null 
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ###dropping nulls

# COMMAND ----------

df.dropna("all").display()

# COMMAND ----------

df.dropna("any").display()

# COMMAND ----------

df.dropna(subset=["Item_Weight"]).display()


# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###filling nulls

# COMMAND ----------


df.fillna("NotAvailable").display()

# COMMAND ----------

df.fillna("Notavailable",subset=["Outlet_Size"]).display()


# COMMAND ----------

# MAGIC %md
# MAGIC ###split and indexing

# COMMAND ----------

# MAGIC %md
# MAGIC ###split

# COMMAND ----------

from pyspark.sql.functions import split
df.withColumn("Outlet_Type",split("Outlet_Type"," ")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###index

# COMMAND ----------

df.withColumn("Outlet_Type",split("Outlet_Type"," ")[1]).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###explod

# COMMAND ----------

df_exp=df.withColumn("Outlet_Type",split("Outlet_Type"," "))
df_exp.display()

# COMMAND ----------

from pyspark.sql.functions import explode
df_exp.withColumn("Outlet_Type",explode("Outlet_Type")).display()

# COMMAND ----------

df_exp.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Array contains

# COMMAND ----------

from pyspark.sql.functions import array_contains
df_exp.withColumn("TYPE1_FLAG",array_contains("Outlet_Type","Type1")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###groupby

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio 1

# COMMAND ----------

from pyspark.sql.functions import sum
df.groupBy("Item_Type").agg(sum("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio -2

# COMMAND ----------

from pyspark.sql.functions import avg
df.groupBy("Item_Type").agg(avg("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenerio-3
# MAGIC

# COMMAND ----------

df.groupBy("Item_Type","Outlet_Size").agg(sum("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###scenrio-4

# COMMAND ----------

df.groupBy("Item_Type","Outlet_Size").agg(sum("Item_MRP"),
avg("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #Collect_list

# COMMAND ----------

data=[("user1","book1"),
("user1","book2"),
("user2","book2"),
("user3","book1"),
("user2","book4")]
schema ="user string,book string"
df_book=spark.createDataFrame(data,schema)
df_book.display()
from pyspark.sql.functions import collect_list


# COMMAND ----------

df_book.groupBy('user').agg(collect_list('book')).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #pivot

# COMMAND ----------

df.select ("Item_Type","Outlet_Size","Item_MRP").display() 

# COMMAND ----------

from pyspark.sql.functions import avg
df.groupBy("Item_Type").pivot("Outlet_Size").agg(avg("Item_MRP")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC #when-otherwise

# COMMAND ----------

# MAGIC %md
# MAGIC #scenero 1

# COMMAND ----------

from pyspark.sql.functions import when
df=df.withColumn('veg_flag',when(col("Item_Type")=='Meat','Non-veg').otherwise('veg') )
display(df)

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #scenerio 2

# COMMAND ----------

from pyspark.sql.functions import lower
df.withColumn('veg_exp_flag',when((col('veg_flag')=='veg') & (col('Item_MRP')<100),'Veg_Inexpensive')\
                            .when((col('veg_flag')=='veg') & (col('Item_MRP')>100),'Veg_Expensive')\
                            .otherwise('Non_Veg')).display()


# COMMAND ----------

# MAGIC %md
# MAGIC #joins

# COMMAND ----------

dataj1 = [('1','gaur','d01'),
          ('2','kit','d02'),
          ('3','sam','d03'),
          ('4','tim','d03'),
          ('5','aman','d05'),
          ('6','nad','d06')] 

schemaj1 = 'emp_id STRING, emp_name STRING, dept_id STRING' 

df1 = spark.createDataFrame(dataj1,schemaj1)

dataj2 = [('d01','HR'),
          ('d02','Marketing'),
          ('d03','Accounts'),
          ('d04','IT'),
          ('d05','Finance')]

schemaj2 = 'dept_id STRING, department STRING'

df2 = spark.createDataFrame(dataj2,schemaj2)

# COMMAND ----------

display(df1)
display(df2)

# COMMAND ----------

# MAGIC %md
# MAGIC #innerjoins

# COMMAND ----------

df1.join(df2,df1["dept_id"]==df2["dept_id"],"inner").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #left join

# COMMAND ----------


df1.join(df2,df1["dept_id"]==df2["dept_id"],"left").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #right join

# COMMAND ----------

df1.join(df2,df1["dept_id"]==df2["dept_id"],"right").display()

# COMMAND ----------

# MAGIC %md
# MAGIC #anti join

# COMMAND ----------

df1.join(df2,df1["dept_id"]==df2["dept_id"],"anti").display()