-- Creates a new database named 'hbtn_0d_usa' if it does not already exist.
-- This command ensures that the database is available for storing the states table and other data.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the 'hbtn_0d_usa' database for use in subsequent commands.
-- This sets the context to the newly created database, allowing for table creation and data manipulation.

USE hbtn_0d_usa;

-- Creates a new table named 'states' if it does not already exist.
-- This table will store information about states with two columns: 'id' and 'name'.

CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
