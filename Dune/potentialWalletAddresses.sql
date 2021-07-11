


with loans as (
select borrower,count(usd_value) as loant_count, sum(usd_value) as loan_value from lending."borrow" 
group by borrower
order by loan_value desc
)
select *,sum(loan_value) over (order by loan_value asc)
from loans