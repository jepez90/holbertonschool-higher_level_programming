#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf8', callback);

function callback (err, data) {
  err
    ? console.log(err)
    : console.log(data);
}
