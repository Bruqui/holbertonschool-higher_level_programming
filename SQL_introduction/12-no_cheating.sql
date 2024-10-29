-- Updates the 'score' column for the record in 'second_table' where the 'name' is 'Bob'.
-- This command sets the 'score' value to 10 for the specified record.
-- If there are multiple records with the name 'Bob', only the first one encountered will be updated.
-- This command is useful for modifying existing data in the table.

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
