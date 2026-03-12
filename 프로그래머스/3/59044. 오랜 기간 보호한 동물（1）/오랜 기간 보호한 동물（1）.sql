-- 코드를 입력하세요
select i.NAME, i.DATETIME
from animal_ins i
left join animal_outs o on i.animal_id = o.animal_id
where o.DATETIME is NULL
order by i.DATETIME asc
limit 3;
