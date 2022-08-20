# Write your MySQL query statement below


SELECT
    w1.id AS 'Id'
FROM
    weather w1
        JOIN
    weather w ON DATEDIFF(w1.recordDate, w.recordDate) = 1
        AND w1.Temperature > w.Temperature
;