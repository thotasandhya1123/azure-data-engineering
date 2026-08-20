CREATE EXTERNAL table revenue_cteas
with(
    location='cetas_revenue',
    DATA_SOURCE=raw_ext_source,
    FILE_FORMAT=parquet_format
)
AS
SELECT * from OPENROWSET
(
    BULK 'revenue',
    DATA_SOURCE ='raw_ext_source',
    FORMAT ='CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW=True
)as query