
```sql
-- Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Salary DECIMAL(10, 2),
    BonusPercentage INT
);

-- Insert sample data into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, Salary, BonusPercentage) VALUES
(1, 'John', 'Doe', 70000.00, 10),
(2, 'Jane', 'Smith', 85000.00, 15),
(3, 'Jim', 'Beam', 55000.00, 8),
(4, 'Jill', 'Valentine', 60000.00, 12);

-- Add a new column named TotalCompensation
ALTER TABLE Employees
ADD TotalCompensation DECIMAL(10, 2);

-- Update TotalCompensation for each employee
UPDATE Employees
SET TotalCompensation = Salary + (Salary * BonusPercentage / 100);

-- Query to identify employees with a Total Compensation greater than $80,000
SELECT * FROM Employees
WHERE TotalCompensation > 80000;

-- Update the FirstName of employees with a Total Compensation less than $60,000
UPDATE Employees
SET FirstName = 'LowCompensation'
WHERE TotalCompensation < 60000;
```
