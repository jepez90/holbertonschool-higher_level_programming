#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const host = process.argv[2];
const filePath = process.argv[3];

request(host, callback);

function callback (err, response, body) {
  if (err) console.log(err);
  fs.writeFile(filePath, body, 'utf8', otherErr => otherErr);
}
