-- 코드를 작성해주세요
SELECT COUNT(*) FISH_COUNT, MAX(LENGTH) MAX_LENGTH, FISH_TYPE
FROM (SELECT ID, FISH_TYPE, IFNULL(LENGTH, 10) LENGTH, TIME FROM FISH_INFO) F
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE;