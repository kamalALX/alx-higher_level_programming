-- This script will list all shows in the 'hbtn_0d_tvshows' database. Each record will display the show title and genre ID, sorted in ascending order by both. If a show doesn’t have a genre, it will display NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_show_genres
  RIGHT JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id;
