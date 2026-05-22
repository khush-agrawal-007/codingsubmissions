#   SOLVE USING WINDOWS FUNCTION ( VERY EASY )

-- select person_name from WINOW FUNC 
-- WHERE
-- ORDER BY turn
-- LIMIT 

with runningmen as(
    select 
        person_name,
        turn,
        sum(weight) over(order by turn) as tot_wt
        from queue
)

select person_name from runningmen where tot_wt <=1000 order by tot_wt desc 
limit 1;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna