#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error', error);
  }

  const moviesWithWedge = body.results.filter(movie =>
    movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );

  console.log(`${moviesWithWedge.length}`);
});
