-- This script will list all shows in the 'hbtn_0d_tvshows' database that do not have a genre linked. Each record will display the show title and genre ID (which will be NULL for these shows), sorted in ascending order by both.
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_show_genres
  RIGHT JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_show_genres.show_id IS NULL
  ORDER BY tv_shows.title, tv_show_genres.genre_id;
