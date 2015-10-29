# Write your MySQL query statement below
SELECT Scores.Score, COUNT(Ranking.Score) AS Rank
FROM Scores, (SELECT DISTINCT(Score) FROM Scores ) Ranking
WHERE Scores.Score<=Ranking.Score
ORDER BY Score DESC;
