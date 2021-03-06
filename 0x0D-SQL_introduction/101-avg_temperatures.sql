-- Displays the average temperature (Fahrenheit) by city ordered by temperature.
SELECT city, AVG(value) avg_temp FROM temperatures
GROUP BY city ORDER BY AVG(value) DESC
