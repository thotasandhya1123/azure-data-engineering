# Databricks notebook source
# MAGIC %md
# MAGIC ##scd type 1

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.default.scdtype1_source(
# MAGIC     prod_id int,
# MAGIC     prod_name string,
# MAGIC     prod_car string,
# MAGIC     processDate date
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into datamodeling.default.scdtype1_source
# MAGIC  values (1, 'prod1','cat1',current_date()),
# MAGIC         (2, 'prod2','cat2',current_date()),
# MAGIC         (3, 'prod3','cat3',current_date())

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.default.scdtype1_source

# COMMAND ----------

# MAGIC %md
# MAGIC ##target table

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.scdtype1_table(
# MAGIC     prod_id int,
# MAGIC     prod_name string,
# MAGIC     prod_car string,
# MAGIC     processDate date
# MAGIC )

# COMMAND ----------

spark.sql("select * from datamodeling.default.scdtype1_source").createOrReplaceTempView("sr")

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.gold.scdtype1_table as tr
# MAGIC using datamodeling.default.scdtype1_source as sr
# MAGIC on
# MAGIC     tr.prod_id = sr.prod_id
# MAGIC when matched and sr.processDate >= tr.processDate then update set *
# MAGIC when not matched then insert *
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.scdtype1_table

# COMMAND ----------

# MAGIC %md
# MAGIC ###change in dimesnsion table

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into datamodeling.default.scdtype1_source
# MAGIC  values 
# MAGIC         (3, 'prod3','new categeory',current_date())

# COMMAND ----------

# MAGIC %sql
# MAGIC update datamodeling.default.scdtype1_source set prod_car = 'new categeory' where prod_id = 3

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace table datamodeling.gold.scdtype1_table(
# MAGIC     prod_id int,
# MAGIC     prod_name string,
# MAGIC     prod_car string,
# MAGIC     processDate date
# MAGIC )

# COMMAND ----------

spark.sql("select * from datamodeling.default.scdtype1_source").createOrReplaceTempView("sr")

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.gold.scdtype1_table as tr
# MAGIC using datamodeling.default.scdtype1_source as sr
# MAGIC on
# MAGIC     tr.prod_id = sr.prod_id
# MAGIC when matched and sr.processDate >= tr.processDate then update set *
# MAGIC when not matched then insert *

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from datamodeling.gold.scdtype1_table