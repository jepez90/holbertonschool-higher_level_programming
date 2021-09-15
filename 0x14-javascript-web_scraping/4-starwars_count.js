#!/usr/bin/node

const request = require('request');
const host = process.argv[2];
const characterMatch = 'https://swapi-api.hbtn.io/api/people/18/';

request(host, callback);

function callback (err, response, body) {
  const allContent = JSON.parse(body);
  let counter = 0;

  if (err) console.log(err);

  allContent.results.forEach(movie => {
    const foundList = movie.characters.filter(char => char === characterMatch);
    if (foundList.length !== 0) {
      counter++;
    }
  });
  console.log(counter);
}
