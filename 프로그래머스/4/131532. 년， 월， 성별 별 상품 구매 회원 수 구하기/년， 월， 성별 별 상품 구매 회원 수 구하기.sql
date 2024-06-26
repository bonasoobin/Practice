-- 코드를 입력하세요
SELECT DISTINCT YEAR(O.SALES_DATE) YEAR, MONTH(O.SALES_DATE) MONTH, U.GENDER, COUNT(DISTINCT O.USER_ID) USERS
FROM USER_INFO U, ONLINE_SALE O
WHERE U.USER_ID = O.USER_ID AND U.GENDER IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3