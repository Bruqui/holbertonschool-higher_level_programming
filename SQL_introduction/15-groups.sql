-- Retrieves the 'score' and the count of occurrences for each unique score 
-- from the 'second_table'.
-- The COUNT(*) function counts how many times each score appears in the table.
-- The results are grouped by the 'score' column, allowing for aggregation of scores.
-- The output is ordered by the count of occurrences (labeled as 'number') in descending order,
-- so the most common scores appear first.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
