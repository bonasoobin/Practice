SELECT MONTH, CAR_ID, RECORDS FROM (
SELECT MONTH, CAR_ID, COUNT(CAR_ID) OVER (PARTITION BY MONTH, CAR_ID) AS RECORDS,
COUNT(CAR_ID) OVER (PARTITION BY CAR_ID) AS ALL_RECORDS
FROM(
SELECT HISTORY_ID, TO_NUMBER(LTRIM(TO_CHAR(START_DATE,'MM'),'0')) AS MONTH, CAR_ID, 
START_DATE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE START_DATE >= TO_DATE('20220801','YYYY-MM-DD')
))WHERE ALL_RECORDS >= 5 GROUP BY MONTH, CAR_ID, RECORDS
ORDER BY MONTH, CAR_ID DESC;