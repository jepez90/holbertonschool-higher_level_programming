#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const host = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(host, callback);

function callback (err, response, body) {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
}
