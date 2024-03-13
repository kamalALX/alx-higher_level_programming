-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM hbtn_0d_tvshows_rate
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
