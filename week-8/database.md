Here are the SQL statements for each of your questions:

**Question 1: Add a New Customer**
```sql
INSERT INTO Customers (name, city)
VALUES ('Alice Smith', 'New York City');
```
This statement adds a new customer named "Alice Smith" who lives in "New York City" to the "Customers" table.

**Question 2: Correct a Mistake**
```sql
UPDATE Customers
SET city = 'New York City'
WHERE name = 'John Doe' AND city = 'New Yory City';
```
This statement corrects the city name for John Doe from "New Yory City" to "New York City".

**Question 3: Search for Customers in Chicago**
```sql
SELECT * FROM Customers
WHERE city = 'Chicago';
```
This statement retrieves all customers who live in "Chicago".

**Question 4: Delete a Customer**
```sql
DELETE FROM Customers
WHERE customer_id = 1;
```
This statement removes the customer with the `customer_id` of 1 from the "Customers" table. Please note that this action is irreversible, so it should be performed with caution.
