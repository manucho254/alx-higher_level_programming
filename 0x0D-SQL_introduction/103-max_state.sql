-- script that displays the max temperature of each state (ordered by State name).

SELECT DISTINCT (state) AS state,
MAX(value) max_temp FROM temperatures
WHERE month=7 OR month=8
GROUP BY state ORDER BY state
LIMIT 3;
