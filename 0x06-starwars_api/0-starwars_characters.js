#!/usr/bin/node

// Load request module
const request = require('request');

// Read movieID from 1st command line arg
const movieId = process.argv[2];

// Function to fetch movie data from SWAPI
function fetchMovieData (movieId) {
  // Make an HTTP GET request to SWAPI film endpoint
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request(url, { json: true }, (error, response, body) => {
    if (error) { return console.log('Error:', error); }

    if (response.statusCode !== 200) { return console.log('Failed to fetch data:', response.statusCode); }

    // Fetch each character name using Promise.all to ensure order
    const characterPromises = body.characters.map(characterUrl => fetchCharacterName(characterUrl));
    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.log('Error fetching character names:', err));
  });
}

// Function to fetch character names
function fetchCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(new Error(error));
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character data: status code ${response.statusCode}`));
      } else {
        resolve(body.name);
      }
    });
  });
}

// Call the fetchMovieData function
fetchMovieData(movieId);
