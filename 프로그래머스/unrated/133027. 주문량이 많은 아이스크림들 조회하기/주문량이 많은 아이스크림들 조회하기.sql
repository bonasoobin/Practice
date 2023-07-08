select flavor
from (select flavor, sum(total_order) total_order
from ((select * from first_half) union all (select * from july))
group by flavor
order by total_order desc)
where rownum <= 3
