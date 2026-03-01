-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME
from item_info i
join item_tree t on i.ITEM_ID = t.ITEM_ID
where parent_item_id is NULL
order by ITEM_ID asc;