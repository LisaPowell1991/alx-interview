#!/usr/bin/node

// Load request module
const request = require('request');

// Read movieID from 1st command line arg
const movieId = process.argv[2];

// Function to fetch movie data from SWAPI
function fetchMovieData(movieId) {
	// Make an HTTP GET request to SWAPI film endpoint
	const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

	request(url, { json:true }, (error, response, body) => {
		if (error)
			return console.log('Error:', error);

		if (response.statusCode !== 200)
			return console.log('Failed to fetch data:', response.statusCode);

		// Printing each character name
		body.characters.forEach(characterUrl => {
			fetchCharacterName(characterUrl);
		});
	});
}

// Function to fetch character names
function fetchCharacterName(url) {
	request(url, { json: true }, (error, response, body) => {
		if (error) {
			console.log('Error:', error);
			return;
		}
		console.log(body.name);
	});
}

// Call the fetchMovieData function
fetchMovieData(movieId);
