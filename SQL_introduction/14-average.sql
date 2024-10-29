-- Calculates the average score from the 'score' column in 'second_table'.
-- The AVG function computes the mean value of all the scores present in the table.
-- The result will be labeled as 'average' for clarity in the output.

SELECT AVG(score) AS average
FROM second_table;
