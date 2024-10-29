-- Creates a new table named 'first_table' if it does not already exist.
-- The 'IF NOT EXISTS' clause prevents errors if the table is already present.
-- The table will have the following columns:
-- - 'id': an integer column to store unique identifiers for each record.
-- - 'name': a variable character column that can store strings with a maximum length of 256 characters.
-- Additional columns can be added here if needed.

CREATE TABLE IF NOT EXISTS first_table (
	id INT,				-- 'id' column to store integer values
	name VARCHAR(256)		-- 'name' column to store string values with a max length of 256
);

-- After execution:
-- If 'first_table' does not exist, it will be created with the specified columns.
-- If it already exists, this command does nothing, avoiding duplicate table errors.
