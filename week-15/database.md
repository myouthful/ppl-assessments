```sql
-- Create the Orders table
CREATE TABLE Orders (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price DECIMAL(10, 2)
);

-- Insert sample data into the Orders table
INSERT INTO Orders (OrderID, ProductID, Quantity, Price) VALUES
(1, 101, 2, 99.99),
(2, 102, 1, 199.99),
(3, 103, 5, 299.99),
(4, 104, 3, 399.99),
(5, 105, 4, 499.99);

-- Calculate the total quantity of products sold
SELECT SUM(Quantity) AS TotalQuantitySold FROM Orders;

-- Find the average price of products
SELECT AVG(Price) AS AveragePrice FROM Orders;

-- Identify the product with the highest price
SELECT ProductID FROM Orders ORDER BY Price DESC LIMIT 1;
```
