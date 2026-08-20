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



-------------
--open row set
-----------------
SELECT * from OPENROWSET
(
    BULK 'revenue',
    DATA_SOURCE ='raw_ext_source',
    FORMAT ='CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW=True
)as query




CREATE EXTERNAL file format parquet_format
with(
    FORMAT_TYPE=PARQUET,
 
)
