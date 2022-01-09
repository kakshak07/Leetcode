# Write your MySQL query statement below


select a.name as Employee from Employee a left join Employee b on a.managerId=b.id where a.salary>b.salary

# SELECT a.name Employee FROM Employee a
# LEFT JOIN Employee b
# ON  a.managerId = b.id  
# WHERE a.salary > b.salary