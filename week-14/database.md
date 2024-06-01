
```sql
-- Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DepartmentID INT
);

-- Create the Departments table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(255)
);

-- Create the Salaries table
CREATE TABLE Salaries (
    EmployeeID INT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
);

-- Insert sample data into the Departments table
INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'Human Resources'),
(2, 'Finance'),
(3, 'IT');

-- Insert sample data into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES
(1, 'John', 'Doe', 1),
(2, 'Jane', 'Smith', 2),
(3, 'Jim', 'Beam', NULL), -- Jim does not belong to any department
(4, 'Jill', 'Valentine', 3);

-- Insert sample data into the Salaries table
INSERT INTO Salaries (EmployeeID, Salary) VALUES
(1, 70000.00),
(2, 85000.00),
(3, 55000.00),
(4, 60000.00);

-- Retrieve a list of employees with their corresponding department names
SELECT e.EmployeeID, e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID;

-- Calculate the average salary for each department
SELECT d.DepartmentName, AVG(s.Salary) AS AverageSalary
FROM Departments d
JOIN Employees e ON d.DepartmentID = e.DepartmentID
JOIN Salaries s ON e.EmployeeID = s.EmployeeID
GROUP BY d.DepartmentName;

-- Identify employees who do not belong to any department
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e
WHERE e.DepartmentID IS NULL;
```
