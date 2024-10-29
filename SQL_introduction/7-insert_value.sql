-- Inserts a new record with 'id' = 89 and 'name' = 'Best School' into the 'first_table' table.
-- The 'IGNORE' keyword prevents errors if a record with the same 'id' already exists in the table,
-- allowing the insertion to continue without affecting existing data.

INSERT IGNORE INTO first_table (id, name) VALUES (89, 'Best School');
