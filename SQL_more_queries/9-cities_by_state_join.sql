-- Selects the 'id' and 'name' columns from the 'cities' table.
-- Also selects the 'name' column from the 'states' table to display the state name associated with each city.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;
