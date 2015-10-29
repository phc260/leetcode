# Write your MySQL query statement below
SELECT c.Name FROM Customers c LEFT JOIN Orders o ON c.Id=o.CustomerId WHERE o.Id IS NULL;
