-- Creates a new user 'user_0d_1' with access restricted to 'localhost' if it doesn't already exist.
-- The 'IDENTIFIED BY' clause sets the user's password to 'user_0d_1_pwd'.
-- This command ensures that the user is created only once, avoiding errors if the user already exists.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges on all databases and tables to 'user_0d_1'@'localhost'.
-- The 'WITH GRANT OPTION' allows 'user_0d_1' to grant these privileges to other users.
-- This command effectively gives the user full administrative rights within the database server.

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Refreshes the in-memory privileges, ensuring all recent changes (like new users or updated permissions)
-- take immediate effect without restarting the server.
-- This command is typically used after modifying user privileges.

FLUSH PRIVILEGES;
