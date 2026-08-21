-- create credentials
-------------------------------------
-------------------------------------
CREATE DATABASE scoped CREDENTIAL sandhyacreds
WITH
IDENTITY='Managed Identity'


-------------------------------
-- create external data source--
create external data source raw_ext_source
WITH
(
    location='https://datalakesynapsesandhya.dfs.core.windows.net/raw',
    CREDENTIAL=sandhyacreds
)

-------------------------------
-- create external data source abfss--
create external data source raw_ext_source_abfss
WITH
(
    location='abfss://datalakesynapsesandhya.dfs.core.windows.net',
    CREDENTIAL=sandhyacreds
)


-------------




CREATE EXTERNAL file format parquet_format
with(
    FORMAT_TYPE=PARQUET
 
)