# Write your MySQL query statement below


select name as Customers from Customers left join Orders on Orders.customerID=Customers.id where customerId is null