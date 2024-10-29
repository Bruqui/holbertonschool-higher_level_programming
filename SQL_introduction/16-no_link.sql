-- Retrieves the 'score' and 'name' columns from the 'second_table'.
-- Only records where 'name' is not null and not an empty string are included in the results.
-- This command ensures that only valid names are considered in the output.
-- The results are ordered by the 'score' column in descending order (highest score first).

SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
