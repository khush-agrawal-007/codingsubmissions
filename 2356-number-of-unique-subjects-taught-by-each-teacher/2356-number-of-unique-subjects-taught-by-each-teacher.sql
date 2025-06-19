SELECT teacher_id ,count(distinct subject_id) as cnt from Teacher
Group BY teacher_id 