-- 코드를 입력하세요
SELECT to_number(to_char(datetime, 'hh24')) hour, count(to_char(datetime, 'hh24')) count
from animal_outs
where to_char(datetime, 'hh24') between 9 and 19
group by to_char(datetime, 'hh24')
order by to_char(datetime, 'hh24');
