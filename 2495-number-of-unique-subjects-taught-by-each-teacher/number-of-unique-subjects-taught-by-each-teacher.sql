# Write your MySQL query statement below
SELECT t.teacher_id, COUNT(*) AS cnt
FROM (
    SELECT teacher_id, subject_id
    FROM Teacher
    GROUP BY teacher_id, subject_id
) AS t
GROUP BY t.teacher_id;
