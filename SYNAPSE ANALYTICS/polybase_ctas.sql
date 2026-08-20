create external table parquet_table
(
    Dealer_ID vARCHAR(100),
    Model_ID    VARCHAR(100),
    Branch_ID    VARCHAR(100),
    Date_ID    VARCHAR(100),
    Units_Sold    VARCHAR(100),
    Revenue    VARCHAR(100)

)
WITH(
    LOCATION='cetas_revenue/',
    DATA_SOURCE=raw_ext_source_abfss,
    FILE_FORMAT=parquet_format

)



create table poly_table
WITH
(
    DISTRIBUTION=ROUND_ROBIN
)
AS
select * from parquet_table


select * from poly_table




