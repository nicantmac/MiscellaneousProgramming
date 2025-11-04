-- Use your DB
CREATE DATABASE employed_DB;
USE employed_DB;

-- ---------- INSERT ----------
-- Add a few employees (note: Employee_ID is NOT auto_increment in your table)
INSERT INTO Employee_TABLE
  (Employee_ID, FirstName, LastName, Department, Employee_Salary, HireDate)
VALUES
  (201, 'Alice', 'Brown',   'Engineering', 90000.00, '2021-02-14'),
  (202, 'Brian', 'Cruz',    'HR',          62000.00, '2022-08-01'),
  (203, 'Clara', 'Nguyen',  'Sales',       71000.00, '2020-11-11'),
  (204, 'Derek', 'Stone',   'Engineering', 88000.00, '2023-03-10'),
  (205, 'Eve',   'Park',    NULL,          35000.00, '2024-06-05');  -- falls back to your default if omitted

-- Quick check
SELECT * FROM Employee_TABLE ORDER BY Employee_ID;

-- ---------- UPDATE ----------
-- 1) Give Engineering a 5% raise
UPDATE Employee_TABLE
SET Employee_Salary = Employee_Salary * 1.05
WHERE Department = 'Engineering';

-- 2) Move Eve into Sales and set a new salary
UPDATE Employee_TABLE
SET Department = 'Sales', Employee_Salary = 56000.00
WHERE Employee_ID = 205;

-- Check the changes
SELECT Employee_ID, FirstName, Department, Employee_Salary
FROM Employee_TABLE
ORDER BY Employee_ID;

-- ---------- DELETE ----------
-- Remove any HR employees (careful: WHERE is required!)
DELETE FROM Employee_TABLE
WHERE Department = 'HR';

-- Confirm deletion
SELECT Employee_ID, FirstName, Department
FROM Employee_TABLE
ORDER BY Employee_ID;
