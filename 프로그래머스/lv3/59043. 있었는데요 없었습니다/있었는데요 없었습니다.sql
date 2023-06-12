-- 코드를 입력하세요
SELECT i.animal_id, i.name
from animal_ins i, animal_outs o
where i.datetime > o.datetime and i.animal_id = o.animal_id
order by i.datetime