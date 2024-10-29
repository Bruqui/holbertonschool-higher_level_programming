-- Retrieves the 'city' and the average temperature ('value') from the 'temperatures' table.
-- The AVG function calculates the mean temperature for each city.
-- The results are grouped by the 'city' column, allowing aggregation of temperature data per city.
-- The output is ordered by the average temperature (labeled as 'avg_temp') in descending order,
-- so cities with the highest average temperatures appear first.

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
