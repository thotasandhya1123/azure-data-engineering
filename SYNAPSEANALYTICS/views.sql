----------------------------
--VIEWS------------------------
-----------------
create view revenue_view
AS
SELECT * from OPENROWSET
(
    BULK 'revenue',
    DATA_SOURCE ='raw_ext_source',
    FORMAT ='CSV',
    PARSER_VERSION = '2.0',
    HEADER_ROW=True
)as query

select * from revenue_view