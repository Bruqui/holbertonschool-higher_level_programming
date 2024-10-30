-- Selects all columns from the 'cities' table.
-- Filters the results to include only cities that belong to the state named 'California'.
-- The state is identified by its id, which is retrieved from the 'states' table.
-- The results are ordered by the 'id' column in ascending order.

SELECT *
FROM cities
WHERE states_id = (SELECT id FROM states WHERE name = 'California')
