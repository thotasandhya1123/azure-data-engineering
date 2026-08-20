create EXTERNAL file format csv_format
with(
    FORMAT_TYPE=DELIMITEDTEXT,
    format_options(
        field_terminator=''
    )
)


create external table revenue_ext_table
(
    Dealer_ID vARCHAR(100),
    Model_ID    VARCHAR(100),
    Branch_ID    VARCHAR(100),
    Date_ID    VARCHAR(100),
    Units_Sold    VARCHAR(100),
    Revenue    VARCHAR(100)


)
WITH(
    LOCATION='revenue',
    DATA_SOURCE=raw_ext_source,
    file_FORMAT =csv_format,
   
)
select * from revenue_ext_table