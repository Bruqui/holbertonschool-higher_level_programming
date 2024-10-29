-- Creates a new table named 'second_table' if it does not already exist.
-- The table includes three columns:
-- - 'id': an integer column, likely used as a unique identifier for each record.
-- - 'name': a variable character column with a max length of 256, used to store names.
-- - 'score': an integer column, used to store score values associated with each record.

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Inserts multiple records into 'second_table' only if they don’t already exist.
-- The 'IGNORE' keyword prevents insertion errors in case of duplicate 'id' values.
-- Each record includes:
-- - An 'id' value to uniquely identify the entry.
-- - A 'name' for the person or entity.
-- - A 'score' representing some integer value associated with each entry.

INSERT IGNORE INTO second_table (id, name, score) VALUES
	(1, 'John', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);
