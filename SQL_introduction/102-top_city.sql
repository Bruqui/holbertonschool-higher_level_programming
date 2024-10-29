-- Retrieves the 'city' and the average temperature ('value') from the 'temperatures' table.
-- This query filters the data to include only records where the 'month' is July (7) or August (8).
-- The AVG function calculates the mean temperature for each city during these months.
-- The results are grouped by the 'city' column, allowing for aggregation of temperature data per city.
-- The output is ordered by the average temperature (labeled as 'avg_temp') in descending order,
-- so cities with the highest average temperatures for the specified months appear first.
-- The 'LIMIT 3' clause restricts the output to the top three cities with the highest average temperatures.

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
