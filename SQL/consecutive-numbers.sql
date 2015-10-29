# Write your MySQL query statement below
SELECT DISTINCT(a.Num) FROM Logs a, Logs b, Logs c WHERE a.Num=b.Num AND b.Num=c.Num AND a.Id=b.Id-1 AND b.Id=c.Id-1;