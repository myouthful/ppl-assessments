**Create Table:**
```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Grade CHAR(1)
);
```

**Populate Table with Sample Data:**
```sql
INSERT INTO Students (StudentID, FirstName, LastName, Age, Grade) VALUES
(1, 'John', 'Doe', 24, 'C'),
(2, 'Jane', 'Smith', 28, 'A'),
(3, 'Emily', 'Jones', 22, 'B'),
(4, 'Chris', 'Brown', 26, 'A'),
(5, 'Mike', 'Davis', 27, 'B');
```

**SQL Queries:**

1. **Retrieve all students who are older than 25 years:**
```sql
SELECT * FROM Students
WHERE Age > 25;
```

2. **Find students with a grade of 'A' or 'B':**
```sql
SELECT * FROM Students
WHERE Grade IN ('A', 'B');
```

3. **Display the distinct age values of students:**
```sql
SELECT DISTINCT Age FROM Students;
```
