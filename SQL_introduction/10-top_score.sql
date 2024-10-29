-- Retrieves the 'score' and 'name' columns from the 'second_table'.
-- The results are ordered by the 'score' column in descending order (highest score first).
-- This command is useful for ranking the entries in 'second_table' based on their scores.

SELECT score, name FROM second_table ORDER BY score DESC;
