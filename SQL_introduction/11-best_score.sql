-- Retrieves the 'score' and 'name' columns from the 'second_table'.
-- Only records with a 'score' of 10 or higher are included in the results.
-- The results are ordered by the 'score' column in descending order (highest score first).
-- This command is useful for filtering and ranking entries based on their scores.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
