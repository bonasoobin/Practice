-- 코드를 입력하세요
SELECT *
FROM (SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME)
WHERE ROWNUM = 1;