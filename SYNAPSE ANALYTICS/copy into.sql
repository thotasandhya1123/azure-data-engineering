CREATE table copy_into_table
(
    Dealer_ID vARCHAR(100),
    Model_ID    VARCHAR(100),
    Branch_ID    VARCHAR(100),
    Date_ID    VARCHAR(100),
    Units_Sold    BIGINT,
    Revenue  BIGINT
)
WITH
(
    DISTRIBUTION=ROUND_ROBIN
)

-------------
--LOADING DATA----------
----------------------
COPY into copy_into_table
(
    Dealer_ID 1,
    Model_ID  2,
    Branch_ID 3,
    Date_ID  4,
    Units_Sold 5,
    Revenue 6
)
from 'https://datalakesynapsesandhya.dfs.core.windows.net/raw/cetas_revenue'
with
(
    FILE_TYPE='parquet',
    CREDENTIAL=(IDENTITY='managed identity')
)


select * from copy_into_table


