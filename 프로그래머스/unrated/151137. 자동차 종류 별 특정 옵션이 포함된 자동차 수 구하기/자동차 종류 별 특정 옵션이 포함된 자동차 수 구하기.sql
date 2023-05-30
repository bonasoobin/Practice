-- 코드를 입력하세요
SELECT car_type, COUNT(OPTIONS) cars
FROM CAR_RENTAL_COMPANY_CAR where options like '%통풍시트%' or options like '%열선시트%' or options like '%가죽시트%'
GROUP BY CAR_TYPE
order by car_type;