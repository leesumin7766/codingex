-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from member_profile
where gender = 'w' and DATE_OF_BIRTH LIKE '%03%' and TLNO is not null
order by MEMBER_ID asc;