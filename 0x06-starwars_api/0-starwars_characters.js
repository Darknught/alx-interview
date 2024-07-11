#!/usr/bin/node
// Starwars API

const request = require('request');

// Function to fetch movie details
function fetchMovie (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, (err, res, body) => {
    if (err) {
      return console.error('Error:', err);
    }

    const movieTitle = body.title;
    const characters = body.characters;

    console.log(`Characters in "${movieTitle}":`);
    fetchCharacters(characters);
  });
}

// Function to fetch character names
function fetchCharacters (characterUrls) {
  characterUrls.forEach(url => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        return console.error('Error:', err);
      }

      console.log(body.name);
    });
  });
}

// Get the movie ID from command-line arguments
const args = process.argv.slice(2);
const movieId = args[0];

if (movieId) {
  fetchMovie(movieId);
} else {
  console.log('Please provide a Movie ID as a command-line argument.');
}
