-- 코드를 입력하세요
SELECT *
FROM (select * from food_product order by price desc)
WHERE rownum=1;