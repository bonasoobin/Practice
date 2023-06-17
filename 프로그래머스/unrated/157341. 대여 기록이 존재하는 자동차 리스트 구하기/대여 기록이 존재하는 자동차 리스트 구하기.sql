-- 코드를 입력하세요
SELECT distinct(c.car_id)
from car_rental_company_car c, car_rental_company_rental_history r
where c.car_id = r.car_id and c.car_type = '세단' and to_char(r.start_date,'mm') = 10
order by car_id desc;