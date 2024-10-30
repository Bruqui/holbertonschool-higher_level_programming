-- Creates a new table named 'id_not_null' if it does not already exist.
-- This table will store data with two columns: 'id' and 'name'.
-- The 'id' column is an integer with a default value of 1.
-- If no value is provided for 'id' when inserting a new record, it will automatically take the value of 1.
-- The 'name' column is a variable character field with a maximum length of 256 characters.
-- There is no NOT NULL constraint on 'name', meaning it can accept null values.

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
