-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM hbtn_0d_tvshows_rate
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
