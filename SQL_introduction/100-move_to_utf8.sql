-- Alters the character set and collation of the database 'hbtn_0c_0'.
-- This sets the character set to 'utf8mb4', which supports a wider range of characters (including emojis).
-- The collation 'utf8mb4_unicode_ci' allows for case-insensitive comparisons based on Unicode standards.
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Selects the database 'hbtn_0c_0' for use in subsequent commands.
-- This command ensures that the following commands operate on the correct database context.
USE hbtn_0c_0;

-- Alters the 'first_table' to convert its character set and collation to match the database settings.
-- This ensures that all textual data in 'first_table' will support the same character set and collation,
-- allowing for consistent data handling and compatibility with various characters.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

