-- 코드를 입력하세요
SELECT book_id, DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE
from book
where year(PUBLISHED_DATE) = 2021 and category = '인문'
order by published_date asc;
