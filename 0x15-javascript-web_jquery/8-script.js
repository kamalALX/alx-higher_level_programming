#!/usr/bin/node
/* golabl $ */
$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json' , function (response) {
    const movies = response.results;
    movies.forEach(function(movie) {
      $('<li></li>').text(movie.title).appendTo('ul#list_movies')
	  });
	});
});
