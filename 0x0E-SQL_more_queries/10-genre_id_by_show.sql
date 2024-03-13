-- This script will list all shows in the 'hbtn_0d_tvshows' database that have at least one genre linked. Each record will display the show title and genre ID, sorted in ascending order by both.
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_show_genres
  INNER JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id;
