-- 코드를 입력하세요
SELECT history_id, car_id, TO_CHAR(start_date,'yyyy-mm-dd') start_date, TO_CHAR(end_date,'yyyy-mm-dd') end_date,(
    CASE
        WHEN to_number(to_char(end_date - start_date + 1)) >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END
    ) AS RENT_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where TO_CHAR(start_date,'yyyy-mm-dd') like '2022-09%'
order by history_id desc;