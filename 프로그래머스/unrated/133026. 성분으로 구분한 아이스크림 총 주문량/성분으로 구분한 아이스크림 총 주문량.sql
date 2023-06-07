-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from icecream_info i, first_half f
where i.flavor = f.flavor
group by INGREDIENT_TYPE
order by total_order;