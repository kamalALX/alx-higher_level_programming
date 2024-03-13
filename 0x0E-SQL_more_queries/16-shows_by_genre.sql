-- Lists all shows and their genres in 'hbtn_0d_tvshows', displaying NULL for shows without a genre, sorted by show title and genre name.
SELECT tv_shows.title, tv_genres.name
  FROM tv_shows
  LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
  ORDER BY tv_shows.title, tv_genres.name;
