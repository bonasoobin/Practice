-- 코드를 입력하세요
SELECT animal_id, name, TO_CHar(datetime, 'yyyy-mm-dd')
from animal_ins
order by animal_id;