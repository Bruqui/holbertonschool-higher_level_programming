-- Changes the default character set and collation for the database 'hbtn_0c_0'.
-- This command sets the character set to 'utf8mb4', which supports a wider range of Unicode characters,
-- and the collation to 'utf8mb4_unicode_ci', which ensures case-insensitive comparisons.

ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Converts the 'first_table' to use the 'utf8mb4' character set and 'utf8mb4_unicode_ci' collation.
-- This ensures that all existing text data in the table will be stored using the specified character set,
-- allowing for better support for multi-language text and special characters.

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modifies the 'name' column in 'first_table' to explicitly use the 'utf8mb4' character set and 
-- 'utf8mb4_unicode_ci' collation.
-- This ensures that any new data inserted into the 'name' column will be compatible with the 
-- specified character set and collation, allowing for proper handling of Unicode characters.

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL;

