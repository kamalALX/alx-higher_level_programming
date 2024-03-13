-- This script lists all the cities of California in the 'hbtn_0d_usa' database
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities, states WHERE states.name = 'California' AND cities.state_id = states.id ORDER BY cities.id ASC;
