----create master key--------------
create master key ENCRYPTION by PASSWORD ='sandhya@11Thota';

---------create credentials-------

create database scoped CREDENTIAL cred_sandy
WITH
IDENTITY='Managed identity'

-------create ext data source------------
---SILVER---
CREATE EXTERNAL data SOURCE source_silver
with(
    LOCATION='https://azprojectdatalake.dfs.core.windows.net/silver',
    CREDENTIAL=cred_sandy
)
---GOLD---
CREATE EXTERNAL data SOURCE source_gold
with(
    LOCATION='https://azprojectdatalake.dfs.core.windows.net/gold',
    CREDENTIAL=cred_sandy
)

------create ext file format for parquet----------
create external file FORMAT parquet_formmat
with(
    FORMAT_TYPE=PARQUET,
    DATA_COMPRESSION='org.apache.hadoop.io.compress.SnappyCodec'
)
------------------create external table extsales-------------
create external table gold.extsales
with(
    LOCATION='extsales',
    DATA_SOURCE=source_gold,
    FILE_FORMAT=parquet_formmat
)AS
select * from gold.sales




