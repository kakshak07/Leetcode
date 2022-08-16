# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below


delete p2 from Person p1, Person p2 where (p1.email = p2.email and p1.id<p2.id);

# DELETE p2 
# FROM Person p1, Person p2
# WHERE(
#     p1.email = p2.email AND p2.id > p1.id
# )