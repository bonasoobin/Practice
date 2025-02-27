-- 코드를 작성해주세요
WITH S AS (
SELECT ID, NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC) SIZE
FROM ECOLI_DATA)

SELECT ID, CASE WHEN SIZE = 1 THEN 'CRITICAL'
                WHEN SIZE = 2 THEN 'HIGH'
                WHEN SIZE = 3 THEN 'MEDIUM'
                ELSE 'LOW' END COLONY_NAME
FROM S
ORDER BY ID;