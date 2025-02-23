WITH RECURSIVE T AS (
    SELECT 0 AS HOUR    
    UNION ALL
    SELECT HOUR + 1 FROM T WHERE HOUR < 23)

SELECT T.HOUR, COUNT(A.ANIMAL_ID) COUNT
FROM T LEFT JOIN (SELECT ANIMAL_ID, HOUR(DATETIME) HOUR FROM ANIMAL_OUTS) A
ON T.HOUR = A.HOUR
GROUP BY T.HOUR
ORDER BY T.HOUR;
