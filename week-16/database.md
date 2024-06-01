```sql
-- Create EmployeesA table
CREATE TABLE EmployeesA (
    EmployeeID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Salary DECIMAL(10, 2)
);

-- Create EmployeesB table
CREATE TABLE EmployeesB (
    EmployeeID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Salary DECIMAL(10, 2)
);

-- Insert sample data into EmployeesA table
INSERT INTO EmployeesA (EmployeeID, FirstName, LastName, Salary) VALUES
(1, 'John', 'Doe', 50000),
(2, 'Jane', 'Doe', 60000),
(3, 'Jim', 'Beam', 55000);

-- Insert sample data into EmployeesB table
INSERT INTO EmployeesB (EmployeeID, FirstName, LastName, Salary) VALUES
(2, 'Jane', 'Doe', 60000),
(4, 'Jack', 'Daniels', 65000),
(5, 'Jill', 'Valentine', 70000);

-- Use UNION to retrieve a list of unique employees from both tables
SELECT * FROM EmployeesA
UNION
SELECT * FROM EmployeesB;

-- Use INTERSECT to find employees who are common in both tables
-- Note: INTERSECT is not supported in all SQL databases, such as MySQL.
SELECT * FROM EmployeesA
INTERSECT
SELECT * FROM EmployeesB;

-- Use EXCEPT to identify employees present in EmployeesA but not in EmployeesB
-- Note: EXCEPT is not supported in all SQL databases, such as MySQL.
SELECT * FROM EmployeesA
EXCEPT
SELECT * FROM EmployeesB;
```
