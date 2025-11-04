USE employed_DB;

-- view everything
SELECT * FROM Employee_TABLE;

-- choose specific columns
SELECT FirstName, LastName, Department FROM Employee_TABLE;

-- filter by condition
SELECT * 
FROM Employee_TABLE
WHERE Department = 'Engineering';

-- filter by range
SELECT *
FROM Employee_TABLE
WHERE Employee_Salary BETWEEN 60000 AND 90000;

-- pattern match with LIKE
SELECT *
FROM Employee_TABLE
WHERE LastName LIKE 'N%';   -- starts with N

-- combine filters
SELECT *
FROM Employee_TABLE
WHERE Department = 'Engineering'
  AND Employee_Salary > 80000;

-- order results
SELECT *
FROM Employee_TABLE
ORDER BY Employee_Salary DESC;

-- distinct values
SELECT DISTINCT Department FROM Employee_TABLE;

-- null checks
SELECT *
FROM Employee_TABLE
WHERE Department IS NULL;
