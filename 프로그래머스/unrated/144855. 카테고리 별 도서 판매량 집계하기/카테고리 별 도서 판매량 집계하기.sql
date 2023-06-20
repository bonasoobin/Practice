-- 코드를 입력하세요
SELECT b.category, sum(s.sales) total_sales
from book b, book_sales s
where to_char(s.sales_date, 'yyyy-mm') = '2022-01' and b.book_id = s.book_id
group by b.category
order by b.category;
