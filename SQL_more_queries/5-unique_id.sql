-- Creates the table 'unique_id' if it does not already exist.
-- The 'id' column is an integer with a default value of 1 and must be unique.
-- The 'name' column is a variable character field with a maximum length of 256 characters.

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
