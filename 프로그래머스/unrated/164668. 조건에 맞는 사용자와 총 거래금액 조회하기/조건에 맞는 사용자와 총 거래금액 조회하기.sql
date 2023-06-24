select u.user_id, u.nickname, sum(b.price) total_sales
from used_goods_board b, used_goods_user u
where b.status = 'DONE' and b.writer_id = u.user_id 
group by u.user_id, u.nickname
having sum(b.price) >= 700000
order by total_sales;
