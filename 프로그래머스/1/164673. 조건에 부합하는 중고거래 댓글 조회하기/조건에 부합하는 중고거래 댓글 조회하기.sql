-- 코드를 입력하세요
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, date_format(r.created_date, '%Y-%m-%d') as CREATED_DATE
from used_goods_board b
join used_goods_reply r on b.board_id = r.board_id
WHERE b.CREATED_DATE >= '2022-10-01'
  AND b.CREATED_DATE <  '2022-11-01'
order by r.created_date asc, b.title asc;