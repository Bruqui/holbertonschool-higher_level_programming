-- Creates a new user 'user_0d_1' with host access limited to 'localhost'.
-- The 'IF NOT EXISTS' clause ensures that no error is thrown if the user already exists.
-- The user is assigned a password ('user_0d_1_pwd') for authentication.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases and tables to 'user_0d_1' when connecting from 'localhost'.
-- The 'ALL PRIVILEGES' keyword allows the user full access, including the ability to SELECT, INSERT, 
-- UPDATE, DELETE, CREATE, DROP, and more across the entire MySQL server.
-- This is typically used for administrative users.

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
