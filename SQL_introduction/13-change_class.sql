-- Deletes records from 'second_table' where the 'score' is less than or equal to 5.
-- This command will remove any entries that do not meet the specified score criteria.
-- It is useful for cleaning up data by removing low-scoring records.

DELETE FROM second_table
WHERE score <= 5;
