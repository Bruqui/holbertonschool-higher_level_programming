-- Creates a new database named 'hbtn_0d_2' if it does not already exist.
-- This command ensures that a database called 'hbtn_0d_2' is available for storing tables and data.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates a new user 'user_0d_2' with host access limited to 'localhost'.
-- The 'IF NOT EXISTS' clause ensures that the user creation will only occur if the user does not already exist.

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grants the 'SELECT' privilege on all tables within the 'hbtn_0d_2' database to 'user_0d_2' when connecting from 'localhost'.
-- This limited privilege allows 'user_0d_2' to view (read-only access) data within 'hbtn_0d_2', but not to modify it.

GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
