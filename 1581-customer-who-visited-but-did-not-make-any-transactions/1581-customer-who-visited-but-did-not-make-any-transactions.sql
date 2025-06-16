/* Write your T-SQL query statement below */
select distinct Customer_id ,count(v.customer_id)  as count_no_trans from Visits as v
left join Transactions as T 
on v.visit_id=T.visit_id
where t.visit_id is null
group by customer_id