-- Creates a new database named 'hbtn_0d_usa' if it does not already exist.
-- This command ensures that the database is available for storing the cities table and other data.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the 'hbtn_0d_usa' database for use in subsequent commands.
-- This sets the context to the newly created database, allowing for table creation and data manipulation.

USE hbtn_0d_usa;

-- Creates a new table named 'cities' if it does not already exist.
-- This table will store information about cities with three columns: 'id', 'states_id', and 'name'.

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
