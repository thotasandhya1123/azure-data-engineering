# SQL NOTES – PART 2 (Joins, Subqueries & Advanced Topics)

These notes continue from your existing "SQL Notes by Nidhi Kushwaha" and use the same **CUSTOMERS** and **ORDERS** tables for consistency.

**CUSTOMERS Table**

| ID | NAME     | AGE | ADDRESS   | SALARY   |
|----|----------|-----|-----------|----------|
| 1  | Ramesh   | 32  | Ahmedabad | 2000.00  |
| 2  | Khilan   | 25  | Delhi     | 1500.00  |
| 3  | Kaushik  | 23  | Kota      | 2000.00  |
| 4  | Chaitali | 25  | Mumbai    | 6500.00  |
| 5  | Hardik   | 27  | Bhopal    | 8500.00  |
| 6  | Muffy    | 24  | Indore    | 10000.00 |

**ORDERS Table**

| OID | DATE       | CUSTOMER_ID | AMOUNT  |
|-----|------------|-------------|---------|
| 100 | 2009-10-08 | 3           | 3000.00 |
| 101 | 2009-10-08 | 3           | 1500.00 |
| 102 | 2009-11-20 | 2           | 1560.00 |
| 103 | 2008-05-20 | 4           | 2060.00 |

---

## JOINS

- A **JOIN** is used to combine rows from two or more tables based on a related column between them.
- Joins are essential whenever data is split across multiple normalized tables (e.g., CUSTOMERS and ORDERS).

### 1. INNER JOIN
- Returns only the rows that have matching values in **both** tables.
- Most commonly used join.

**Syntax-**
```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

**Example-** Get customer name with their order amount.
```sql
SELECT C.NAME, O.AMOUNT
FROM CUSTOMERS C
INNER JOIN ORDERS O
ON C.ID = O.CUSTOMER_ID;
```

| NAME     | AMOUNT  |
|----------|---------|
| Kaushik  | 3000.00 |
| Kaushik  | 1500.00 |
| Khilan   | 1560.00 |
| Chaitali | 2060.00 |

Note: Ramesh, Hardik, and Muffy don't appear because they have no matching order — INNER JOIN only returns matched rows.

---

### 2. LEFT JOIN (LEFT OUTER JOIN)
- Returns **all rows from the left table**, and matching rows from the right table.
- If there is no match, NULL is returned for right table columns.

**Syntax-**
```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

**Example-**
```sql
SELECT C.NAME, O.AMOUNT
FROM CUSTOMERS C
LEFT JOIN ORDERS O
ON C.ID = O.CUSTOMER_ID;
```

| NAME     | AMOUNT  |
|----------|---------|
| Ramesh   | NULL    |
| Khilan   | 1560.00 |
| Kaushik  | 3000.00 |
| Kaushik  | 1500.00 |
| Chaitali | 2060.00 |
| Hardik   | NULL    |
| Muffy    | NULL    |

---

### 3. RIGHT JOIN (RIGHT OUTER JOIN)
- Returns **all rows from the right table**, and matching rows from the left table.
- If there is no match, NULL is returned for left table columns.

**Syntax-**
```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

**Example-**
```sql
SELECT C.NAME, O.AMOUNT
FROM CUSTOMERS C
RIGHT JOIN ORDERS O
ON C.ID = O.CUSTOMER_ID;
```

| NAME     | AMOUNT  |
|----------|---------|
| Kaushik  | 3000.00 |
| Kaushik  | 1500.00 |
| Khilan   | 1560.00 |
| Chaitali | 2060.00 |

(Result looks similar to INNER JOIN here since every order has a valid customer.)

---

### 4. FULL OUTER JOIN
- Returns all rows when there is a match in **either** the left or right table.
- Unmatched rows from both sides are filled with NULL.

**Syntax-**
```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

**Example-**
```sql
SELECT C.NAME, O.AMOUNT
FROM CUSTOMERS C
FULL OUTER JOIN ORDERS O
ON C.ID = O.CUSTOMER_ID;
```
Returns every customer (even with no orders) AND every order (even with no matching customer, if any existed).

Note: MySQL does not support FULL OUTER JOIN directly — it is usually simulated using `LEFT JOIN UNION RIGHT JOIN`.

---

### 5. CROSS JOIN
- Returns the **Cartesian product** of two tables — every row of table1 combined with every row of table2.
- No ON condition is used.
- Result size = (rows in table1) × (rows in table2).

**Syntax-**
```sql
SELECT columns
FROM table1
CROSS JOIN table2;
```

**Example-**
```sql
SELECT C.NAME, O.OID
FROM CUSTOMERS C
CROSS JOIN ORDERS O;
```
This would return 6 customers × 4 orders = 24 rows.

---

### 6. SELF JOIN
- A table is joined with **itself**.
- Useful for comparing rows within the same table (e.g., employees and their managers).
- Requires table aliases since the same table is referenced twice.

**Syntax-**
```sql
SELECT A.column, B.column
FROM table A, table B
WHERE condition;
```

**Example-** Find pairs of customers who live in the same address.
```sql
SELECT A.NAME AS Customer1, B.NAME AS Customer2, A.ADDRESS
FROM CUSTOMERS A
INNER JOIN CUSTOMERS B
ON A.ADDRESS = B.ADDRESS AND A.ID <> B.ID;
```

---

## SUBQUERIES

- A **subquery** (or inner query/nested query) is a query written inside another SQL query.
- The inner query runs first, and its result is used by the outer query.
- Subqueries can be used with SELECT, INSERT, UPDATE, or DELETE statements.

### 1. Single-Row Subquery
- Returns only **one row** as the result.
- Can be used with operators like `=`, `>`, `<`.

**Example-** Find customers with salary greater than Ramesh's salary.
```sql
SELECT NAME, SALARY
FROM CUSTOMERS
WHERE SALARY > (SELECT SALARY FROM CUSTOMERS WHERE NAME = 'Ramesh');
```

### 2. Multi-Row Subquery
- Returns **multiple rows**.
- Used with operators like `IN`, `ANY`, `ALL`.

**Example-** Find customers who have placed an order.
```sql
SELECT NAME
FROM CUSTOMERS
WHERE ID IN (SELECT CUSTOMER_ID FROM ORDERS);
```

### 3. Correlated Subquery
- The inner query depends on the outer query — it runs **once for each row** processed by the outer query.
- Generally slower than a normal subquery since it re-executes repeatedly.

**Example-** Find customers whose salary is above the average salary of customers from the same address.
```sql
SELECT NAME, ADDRESS, SALARY
FROM CUSTOMERS C1
WHERE SALARY > (
    SELECT AVG(SALARY)
    FROM CUSTOMERS C2
    WHERE C2.ADDRESS = C1.ADDRESS
);
```

### 4. EXISTS / NOT EXISTS
- `EXISTS` checks whether a subquery returns **any rows** — returns TRUE/FALSE instead of actual data.
- Often more efficient than IN for large datasets.

**Syntax-**
```sql
SELECT columns
FROM table_name
WHERE EXISTS (subquery);
```

**Example-** Find customers who have at least one order.
```sql
SELECT NAME
FROM CUSTOMERS C
WHERE EXISTS (
    SELECT 1 FROM ORDERS O WHERE O.CUSTOMER_ID = C.ID
);
```

**Example-** Find customers who have NOT placed any order.
```sql
SELECT NAME
FROM CUSTOMERS C
WHERE NOT EXISTS (
    SELECT 1 FROM ORDERS O WHERE O.CUSTOMER_ID = C.ID
);
```

---

## CTE (Common Table Expression)

- A **CTE** is a temporary named result set defined using the `WITH` keyword.
- Makes complex queries more readable by breaking them into logical steps.
- Exists only for the duration of the query.

**Syntax-**
```sql
WITH cte_name AS (
    SELECT columns
    FROM table_name
    WHERE condition
)
SELECT * FROM cte_name;
```

**Example-** Get customers with salary above 2000 using a CTE.
```sql
WITH HighEarners AS (
    SELECT NAME, SALARY
    FROM CUSTOMERS
    WHERE SALARY > 2000
)
SELECT * FROM HighEarners
ORDER BY SALARY DESC;
```

### Recursive CTE
- A CTE that references itself — used for hierarchical or sequential data (e.g., org charts, number sequences).

**Syntax-**
```sql
WITH cte_name AS (
    -- Anchor member
    SELECT ...
    UNION ALL
    -- Recursive member
    SELECT ...
    FROM cte_name
    WHERE condition
)
SELECT * FROM cte_name;
```

**Example-** Generate numbers from 1 to 5.
```sql
WITH Numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM Numbers WHERE n < 5
)
SELECT * FROM Numbers;
```

---

## AGGREGATE FUNCTIONS

- Aggregate functions perform a calculation on a set of values and return a **single value**.
- Commonly used with GROUP BY.

| Function  | Description                  |
|-----------|-------------------------------|
| COUNT()   | Counts number of rows         |
| SUM()     | Adds up numeric values        |
| AVG()     | Returns the average value     |
| MAX()     | Returns the highest value     |
| MIN()     | Returns the lowest value      |

**Example-**
```sql
SELECT COUNT(*) AS TotalCustomers,
       SUM(SALARY) AS TotalSalary,
       AVG(SALARY) AS AvgSalary,
       MAX(SALARY) AS MaxSalary,
       MIN(SALARY) AS MinSalary
FROM CUSTOMERS;
```

Note: Aggregate functions ignore NULL values (except COUNT(*), which counts all rows regardless of NULLs).

---

## CASE Statement

- The `CASE` statement adds if-then-else logic to a query.
- Goes through conditions and returns a value when the first condition is met.

**Syntax-**
```sql
SELECT column,
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE result3
END AS alias_name
FROM table_name;
```

**Example-** Categorize customers by salary range.
```sql
SELECT NAME, SALARY,
CASE
    WHEN SALARY >= 8000 THEN 'High'
    WHEN SALARY >= 3000 THEN 'Medium'
    ELSE 'Low'
END AS SalaryCategory
FROM CUSTOMERS;
```

---

## STRING FUNCTIONS

| Function                  | Description                              | Example                              |
|----------------------------|-------------------------------------------|----------------------------------------|
| LEN(str)                  | Returns length of string                  | `SELECT LEN('Ramesh')` → 6            |
| UPPER(str)                | Converts to uppercase                     | `SELECT UPPER('ramesh')` → RAMESH     |
| LOWER(str)                | Converts to lowercase                     | `SELECT LOWER('RAMESH')` → ramesh     |
| SUBSTRING(str, start, len)| Extracts part of a string                 | `SELECT SUBSTRING('Ramesh',1,3)` → Ram|
| CONCAT(str1, str2, ...)   | Joins two or more strings                 | `SELECT CONCAT(NAME,' - ',ADDRESS)`   |
| TRIM(str)                 | Removes leading/trailing spaces           | `SELECT TRIM('  Ramesh  ')`           |
| REPLACE(str, old, new)    | Replaces part of a string                 | `SELECT REPLACE('Ramesh','a','o')`    |

**Example-**
```sql
SELECT NAME, UPPER(NAME) AS UPPER_NAME, LEN(NAME) AS NameLength
FROM CUSTOMERS;
```

---

## DATE FUNCTIONS

| Function                          | Description                          |
|------------------------------------|----------------------------------------|
| GETDATE()                         | Returns current date and time          |
| DATEPART(part, date)              | Extracts a part of a date (year, month)|
| DATEADD(part, number, date)       | Adds an interval to a date             |
| DATEDIFF(part, date1, date2)      | Returns difference between two dates   |
| YEAR(date) / MONTH(date) / DAY(date) | Extracts year, month, or day         |

**Example-**
```sql
SELECT OID, DATE, DATEDIFF(DAY, DATE, GETDATE()) AS DaysSinceOrder
FROM ORDERS;
```

---

## TRANSACTIONS (TCL)

- A **transaction** is a group of SQL statements executed as a single unit of work — either all succeed, or none do.
- Ensures data consistency (follows ACID properties: Atomicity, Consistency, Isolation, Durability).

### COMMIT
- Permanently saves all changes made during the current transaction.

### ROLLBACK
- Undoes changes made during the current transaction (reverts to the last COMMIT or SAVEPOINT).

### SAVEPOINT
- Sets a point within a transaction to which you can later roll back, without rolling back the entire transaction.

**Syntax & Example-**
```sql
BEGIN TRANSACTION;

UPDATE CUSTOMERS SET SALARY = SALARY + 500 WHERE ID = 1;
SAVEPOINT BeforeSecondUpdate;

UPDATE CUSTOMERS SET SALARY = SALARY - 1000 WHERE ID = 2;
-- realize this was a mistake
ROLLBACK TO BeforeSecondUpdate;

COMMIT;
```
Here, the first update is kept, but the second update is undone, and the transaction is then permanently committed.

---

## VIEWS

- A **view** is a virtual table based on the result of a SQL query.
- It does not store data itself (in a normal view) — it pulls data live from the underlying tables.
- Used to simplify complex queries, restrict access to specific columns/rows, and improve readability.

**Syntax-**
```sql
CREATE VIEW view_name AS
SELECT columns
FROM table_name
WHERE condition;
```

**Example-**
```sql
CREATE VIEW HighSalaryCustomers AS
SELECT NAME, ADDRESS, SALARY
FROM CUSTOMERS
WHERE SALARY > 5000;
```

To use the view:
```sql
SELECT * FROM HighSalaryCustomers;
```

**Dropping a View-**
```sql
DROP VIEW HighSalaryCustomers;
```

---

## STORED PROCEDURES

- A **stored procedure** is a precompiled collection of SQL statements stored under a name and executed as a unit.
- Improves performance (precompiled) and reusability, and helps centralize business logic.

**Syntax-**
```sql
CREATE PROCEDURE procedure_name
    @param1 datatype,
    @param2 datatype
AS
BEGIN
    SQL statements;
END;
```

**Example-** Procedure to get customers above a given salary.
```sql
CREATE PROCEDURE GetCustomersBySalary
    @MinSalary DECIMAL(18,2)
AS
BEGIN
    SELECT NAME, SALARY
    FROM CUSTOMERS
    WHERE SALARY >= @MinSalary;
END;
```

**Executing the procedure-**
```sql
EXEC GetCustomersBySalary @MinSalary = 5000;
```

**Dropping a Procedure-**
```sql
DROP PROCEDURE GetCustomersBySalary;
```

---

## USER-DEFINED FUNCTIONS (UDF)

- A function that returns a single value (scalar) or a table, and can be reused inside queries.

**Example-** Scalar function to calculate annual salary.
```sql
CREATE FUNCTION GetAnnualSalary (@MonthlySalary DECIMAL(18,2))
RETURNS DECIMAL(18,2)
AS
BEGIN
    RETURN @MonthlySalary * 12;
END;
```

**Using the function-**
```sql
SELECT NAME, dbo.GetAnnualSalary(SALARY) AS AnnualSalary
FROM CUSTOMERS;
```

---

## INDEXES

- An **index** is a database object that speeds up data retrieval on a table, at the cost of slower writes (INSERT/UPDATE/DELETE) and extra storage.
- Works like a book's index — helps the database find rows without scanning the whole table.

### Types-
- **Clustered Index:** Determines the physical order of data in the table. A table can have only ONE clustered index (usually the primary key).
- **Non-Clustered Index:** A separate structure that points back to the data. A table can have MULTIPLE non-clustered indexes.

**Syntax-**
```sql
CREATE INDEX index_name
ON table_name (column_name);
```

**Example-**
```sql
CREATE INDEX idx_customer_name
ON CUSTOMERS (NAME);
```

**Dropping an Index-**
```sql
DROP INDEX idx_customer_name ON CUSTOMERS;
```

---

## WINDOW FUNCTIONS

- Window functions perform calculations across a set of rows **related to the current row**, without collapsing the rows like GROUP BY does.
- Used with the `OVER()` clause.

### 1. ROW_NUMBER()
- Assigns a unique sequential number to each row within a partition.

```sql
SELECT NAME, SALARY,
ROW_NUMBER() OVER (ORDER BY SALARY DESC) AS RowNum
FROM CUSTOMERS;
```

### 2. RANK()
- Assigns a rank to each row; **skips** numbers after a tie.

```sql
SELECT NAME, SALARY,
RANK() OVER (ORDER BY SALARY DESC) AS SalaryRank
FROM CUSTOMERS;
```

### 3. DENSE_RANK()
- Same as RANK(), but does **not skip** numbers after a tie.

```sql
SELECT NAME, SALARY,
DENSE_RANK() OVER (ORDER BY SALARY DESC) AS SalaryDenseRank
FROM CUSTOMERS;
```

### 4. PARTITION BY
- Divides the result set into partitions (groups) before applying the window function — similar to GROUP BY, but rows aren't collapsed.

```sql
SELECT NAME, ADDRESS, SALARY,
RANK() OVER (PARTITION BY ADDRESS ORDER BY SALARY DESC) AS RankInCity
FROM CUSTOMERS;
```

### 5. LAG() and LEAD()
- `LAG()` accesses data from a **previous** row.
- `LEAD()` accesses data from the **next** row.
- Useful for comparing a row to the row before/after it (e.g., month-over-month change).

```sql
SELECT NAME, SALARY,
LAG(SALARY) OVER (ORDER BY SALARY) AS PreviousSalary,
LEAD(SALARY) OVER (ORDER BY SALARY) AS NextSalary
FROM CUSTOMERS;
```

---

## QUICK SUMMARY TABLE

| Topic              | Key Use                                      |
|---------------------|-----------------------------------------------|
| JOINS               | Combine data from multiple tables             |
| Subqueries          | Query nested inside another query             |
| CTE                 | Readable, reusable temporary result sets      |
| Aggregate Functions | Summarize data (COUNT, SUM, AVG, etc.)        |
| CASE                | Conditional logic inside a query              |
| String/Date Functions | Manipulate text and date/time values        |
| Transactions        | Ensure all-or-nothing execution of changes    |
| Views               | Save a reusable virtual query/table           |
| Stored Procedures   | Reusable, precompiled SQL logic               |
| Indexes             | Speed up data retrieval                       |
| Window Functions    | Row-level calculations without collapsing rows|
