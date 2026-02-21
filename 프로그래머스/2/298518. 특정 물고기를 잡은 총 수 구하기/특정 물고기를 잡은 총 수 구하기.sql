-- 코드를 작성해주세요
select count(*) as FISH_COUNT
from fish_info i
join fish_name_info n on i.fish_type = n.fish_type
where N.FISH_NAME='BASS' OR N.FISH_NAME='SNAPPER'