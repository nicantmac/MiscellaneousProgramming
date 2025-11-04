-- Create db and use the db to run the sql data
CREATE DATABASE employed_DB;
USE employed_DB;

-- First to create tables utilize the keywords; CREATE TABLE
-- After creating your table, add the columns you want
CREATE TABLE  Employee_TABLE (
    -- created columns, initiated data types and constraints
    -- created employee_id column, of integers, the contraint: Primary key
    Employee_ID INT PRIMARY KEY, 

    -- created firstname column, of text(limited to 30 chars), the contraint: not null
    FirstName VARCHAR(30) NOT NULL,

    -- created lastname column, of text(limited to 30 chars), the contraint: not null
    LastName VARCHAR(30) NOT NULL,

    -- created department column, of text(limited to 35 chars), the contraint: none
    Department VARCHAR(35),

    -- created employee salary column, of decimal with(10-digit limit, 2 integers behind decimal), contraint: if no value input(refer to default)
    Employee_Salary DECIMAL(10, 2) DEFAULT 35000.00,

    -- created hire date column with date data type, format(YYYY-MM-DD) -> "2025-10-20"
    HireDate DATE
);
