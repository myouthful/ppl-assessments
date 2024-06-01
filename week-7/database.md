**Primary Key:**
A primary key is a field (or combination of fields) in a table that uniquely identifies each row in that table. No two rows can have the same primary key value, and it must not contain `NULL` values. It ensures that each record can be uniquely retrieved and identified.

For example, in a table that stores information about students, the student ID could be used as a primary key because it's unique to each student.

Here's how you might define a primary key in SQL:

```sql
CREATE TABLE Students (
    StudentID INT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ...
    PRIMARY KEY (StudentID)
);
```

**Foreign Key:**
A foreign key is a field (or collection of fields) in one table that uniquely identifies a row of another table or the same table. In other words, a foreign key is defined in a table by referencing the primary key of another table. The purpose of the foreign key is to ensure referential integrity of the data. This means that the value of the foreign key must match one of the values in the table it references or be `NULL`.

For instance, if you have a table of student addresses, the student ID in the addresses table would be a foreign key that references the student ID in the students table.

Here's an example of how a foreign key is defined in SQL:

```sql
CREATE TABLE StudentAddresses (
    AddressID INT NOT NULL,
    StudentID INT,
    Address VARCHAR(100),
    ...
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
```

In this example, `StudentID` in the `StudentAddresses` table is a foreign key that references `StudentID` in the `Students` table.

The primary key and foreign key mechanisms are fundamental in relational database design, allowing for the creation of relationships between tables and ensuring that data remains consistent across the database.
