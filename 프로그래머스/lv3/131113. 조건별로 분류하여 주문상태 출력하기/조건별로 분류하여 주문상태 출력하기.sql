-- 코드를 입력하세요
SELECT order_id, 
       product_id, 
       TO_CHAR(OUT_DATE,'YYYY-MM-DD') OUT_DATE, 
       case when to_char(out_date,'yyyymmdd') <= 20220501 then '출고완료' 
            when to_char(out_date,'yyyymmdd') > 20220501 then '출고대기' 
       else '출고미정'
       end as 출고여부
from food_order
order by order_id;

