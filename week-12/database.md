```sql
-- Create the Sales table
CREATE TABLE Sales (
    ProductID INT,
    Category VARCHAR(255),
    QuantitySold INT,
    Revenue DECIMAL(10, 2)
);

-- Insert sample data into the Sales table
INSERT INTO Sales (ProductID, Category, QuantitySold, Revenue) VALUES
(1, 'Electronics', 10, 1200.00),
(2, 'Electronics', 15, 1800.00),
(3, 'Clothing', 20, 500.00),
(4, 'Clothing', 10, 250.00),
(5, 'Furniture', 5, 1500.00),
(6, 'Furniture', 2, 600.00);

-- Calculate the total quantity sold and revenue for each product category
SELECT Category, SUM(QuantitySold) AS TotalQuantitySold, SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY Category;

-- Find the average revenue per unit sold for each product category
SELECT Category, AVG(Revenue / QuantitySold) AS AverageRevenuePerUnit
FROM Sales
GROUP BY Category;

-- Identify the product categories with the highest total revenue
SELECT Category, SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY Category
ORDER BY TotalRevenue DESC
LIMIT 1;
```
