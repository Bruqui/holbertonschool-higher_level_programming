-- Retrieves the 'state' and the maximum temperature ('value') from the 'temperatures' table.
-- The MAX function identifies the highest temperature recorded for each state.
-- The results are grouped by the 'state' column, allowing for aggregation of temperature data per state.
-- The output is ordered by the 'state' name in descending order,
-- so states will appear from Z to A.
-- The 'LIMIT 3' clause restricts the output to the top three states based on the alphabetical order of their names.

SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state DESC
LIMIT 3
