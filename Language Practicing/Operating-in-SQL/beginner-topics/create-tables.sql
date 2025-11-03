-- Create db and use the db to run the sql data
CREATE DATABASE employed_DB;
USE employed_DB;

-- First to create tables utilize the keywords; CREATE TABLE
-- After creating your table, add the columns you want
CREATE TABLE  Employee_TABLE (
    Employee_ID INT PRIMARY KEY,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Department VARCHAR(35),
    Employee_Salary DECIMAL(10, 2) DEFAULT 35000.00,
    HireDate DATE
);
