**Create Database and Table:**
```sql
CREATE DATABASE Library;

USE Library;

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(100),
    PublicationYear INT
);
```

**Populate Table with Sample Data:**
```sql
INSERT INTO Books (BookID, Title, Author, Genre, PublicationYear)
VALUES 
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925),
(2, '1984', 'George Orwell', 'Dystopian', 1949),
(3, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960),
(4, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951),
(5, 'Brave New World', 'Aldous Huxley', 'Dystopian', 1932),
(6, 'The Road', 'Cormac McCarthy', 'Post-apocalyptic', 2006),
(7, 'Educated', 'Tara Westover', 'Memoir', 2018),
(8, 'Becoming', 'Michelle Obama', 'Memoir', 2020),
(9, 'The Silent Patient', 'Alex Michaelides', 'Thriller', 2020),
(10, 'Where the Crawdads Sing', 'Delia Owens', 'Mystery', 2020);
```

**SQL Queries for Tasks:**

1. **Retrieve all columns for books published in the year 2020:**
```sql
SELECT * FROM Books
WHERE PublicationYear = 2020;
```

2. **Find the distinct genres available in the Books table:**
```sql
SELECT DISTINCT Genre FROM Books;
```

3. **Alias the column Author as BookAuthor in a query result:**
```sql
SELECT Title, Author AS BookAuthor, Genre, PublicationYear FROM Books;
```
