-- This script lists all cities in the 'hbtn_0d_usa' database
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id;
