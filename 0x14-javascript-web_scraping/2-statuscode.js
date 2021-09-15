#!/usr/bin/node

const request = require('request');
const host = process.argv[2];

request
  .get(host)
  .on('response', response => {
    console.log('code: ' + response.statusCode);
  });
