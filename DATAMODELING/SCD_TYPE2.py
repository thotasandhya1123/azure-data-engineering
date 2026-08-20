# Databricks notebook source
# MAGIC %md
# MAGIC ###SCD_TYPE2

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace TABLE datamodeling.default.scdtyp2_source
# MAGIC (
# MAGIC   prod_id INT,
# MAGIC   prod_name STRING,
# MAGIC   prod_cat STRING,
# MAGIC   processDate DATE
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO datamodeling.default.scdtyp2_source
# MAGIC VALUES
# MAGIC (1,'prod1','cat1',CURRENT_DATE()),
# MAGIC (2,'prod2','cat2',CURRENT_DATE()),
# MAGIC (3,'prod3','cat3',CURRENT_DATE())

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.default.scdtyp2_source

# COMMAND ----------

# MAGIC %md
# MAGIC ###target table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE or replace TABLE datamodeling.gold.scdtype2_table
# MAGIC (
# MAGIC   prod_id INT,
# MAGIC   prod_name STRING,
# MAGIC   prod_cat STRING,
# MAGIC   processDate DATE,
# MAGIC   start_date DATE,
# MAGIC   end_date DATE,
# MAGIC   is_current STRING
# MAGIC )

# COMMAND ----------

# MAGIC %md
# MAGIC ##sourrce_table

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *,
# MAGIC         current_timestamp as start_date,
# MAGIC         CAST('3000-01-01' AS TIMESTAMP) as end_date,
# MAGIC         'Y' as is_current
# MAGIC FROM datamodeling.default.scdtyp2_source

# COMMAND ----------

spark.sql("""SELECT *,
        current_timestamp as start_date,
        CAST('3000-01-01' AS TIMESTAMP) as end_date,
        'Y' as is_current
FROM datamodeling.default.scdtyp2_source""").createOrReplaceTempView("src")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM src

# COMMAND ----------

# MAGIC %md
# MAGIC MERGE-1 : This command will check if we have any data in the target table that is updated in the source, and will mark it as expired.

# COMMAND ----------

# MAGIC %sql
# MAGIC merge into datamodeling.gold.scdtype2_table as tr
# MAGIC using  src
# MAGIC on tr.prod_id=src.prod_id
# MAGIC and tr.is_current='Y'
# MAGIC -- When We have New Data With Updates
# MAGIC when matched and 
# MAGIC src.prod_cat != tr.prod_cat or
# MAGIC src.prod_name != tr.prod_name or
# MAGIC src.processDate != tr.processDate
# MAGIC  then update set 
# MAGIC  tr.end_date = current_timestamp,
# MAGIC   tr.is_current = 'N'

# COMMAND ----------

# MAGIC %md
# MAGIC MERGE-2 : This command will bring all the non-expired commands bcz we have filter of "is_current = 'Y'". So, this will not bring the updated records as well bcz previous MERGE command marked it as expired. So all the new records [including updated] will be inserted in this MERGE.

# COMMAND ----------

# MAGIC %sql
# MAGIC merge into datamodeling.gold.scdtype2_table as tr
# MAGIC using  src
# MAGIC on tr.prod_id=src.prod_id
# MAGIC and tr.is_current='Y'
# MAGIC when not matched then insert
# MAGIC (prod_id,prod_name,prod_cat,processDate,start_date,end_date,is_current)
# MAGIC values
# MAGIC (src.prod_id,src.prod_name,src.prod_cat,src.processDate,src.start_date,src.end_date,src.is_current)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.scdtype2_table

# COMMAND ----------

# MAGIC %sql
# MAGIC update datamodeling.gold.scdtype2_table
# MAGIC set prod_cat="new_category"
# MAGIC where prod_id=3

# COMMAND ----------

spark.sql("""SELECT *,
        current_timestamp as start_date,
        CAST('3000-01-01' AS TIMESTAMP) as end_date,
        'Y' as is_current
FROM datamodeling.default.scdtyp2_source""").createOrReplaceTempView("src")

# COMMAND ----------

# MAGIC %sql
# MAGIC merge into datamodeling.gold.scdtype2_table as tr
# MAGIC using  src
# MAGIC on tr.prod_id=src.prod_id
# MAGIC and tr.is_current='Y'
# MAGIC -- When We have New Data With Updates
# MAGIC when matched and 
# MAGIC src.prod_cat != tr.prod_cat or
# MAGIC src.prod_name != tr.prod_name or
# MAGIC src.processDate != tr.processDate
# MAGIC  then update set 
# MAGIC  tr.end_date = current_timestamp,
# MAGIC   tr.is_current = 'N'

# COMMAND ----------

# MAGIC %sql
# MAGIC merge into datamodeling.gold.scdtype2_table as tr
# MAGIC using  src
# MAGIC on tr.prod_id=src.prod_id
# MAGIC and tr.is_current='Y'
# MAGIC when not matched then insert
# MAGIC (prod_id,prod_name,prod_cat,processDate,start_date,end_date,is_current)
# MAGIC values
# MAGIC (src.prod_id,src.prod_name,src.prod_cat,src.processDate,src.start_date,src.end_date,src.is_current)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.scdtype2_table