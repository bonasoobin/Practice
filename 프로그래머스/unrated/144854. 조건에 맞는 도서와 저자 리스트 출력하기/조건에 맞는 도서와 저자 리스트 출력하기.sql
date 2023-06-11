-- 코드를 입력하세요
SELECT book.book_id, author.author_name, to_char(book.published_date,'yyyy-mm-dd')
from book, author
where book.author_id = author.author_id and book.category = '경제'
order by published_date;