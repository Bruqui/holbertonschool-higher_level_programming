-- Creates a new table named 'force_name' if it does not already exist.
-- This table will store data with two columns: 'id' and 'name'.
-- The 'id' column is an integer and will be used as a unique identifier for each row.
-- The 'name' column is a variable character field with a maximum length of 256 characters.
-- The 'NOT NULL' constraint on 'name' ensures that every row must have a value in this column,
-- which prevents the insertion of records with an empty or null 'name' field.

CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);
