#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const host = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(host, callback);

function callback (err, response, body) {
  const movie = JSON.parse(body);

  if (err) console.log(err);

  movie.characters.forEach(showChars);
}

function showChars (charURL) {
  request(charURL, (err, response, body) => {
    if (err) console.log(err);

    console.log(JSON.parse(body).name);
  });
}
