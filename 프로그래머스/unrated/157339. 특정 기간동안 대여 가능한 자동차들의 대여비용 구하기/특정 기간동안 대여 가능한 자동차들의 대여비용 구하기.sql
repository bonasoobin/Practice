SELECT * FROM 
(SELECT 
      A.CAR_ID   
    , A.CAR_TYPE
    , A.DAILY_FEE*30*((100-B.DISCOUNT_RATE)/100) AS FEE
FROM   CAR_RENTAL_COMPANY_CAR A
     , CAR_RENTAL_COMPANY_DISCOUNT_PLAN B
WHERE A.CAR_TYPE = B.CAR_TYPE
AND A.CAR_ID NOT IN
(
SELECT DISTINCT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE (TO_CHAR(START_DATE,'YYYYMM') <= '202211') AND
    (TO_CHAR(END_DATE,'YYYYMM') >= '202211')
)
AND B.DURATION_TYPE LIKE '%30%')
    WHERE CAR_TYPE IN ('세단', 'SUV')
    AND FEE >= 500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC;