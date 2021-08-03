#!/usr/bin/node

const fs = require('fs');
if (process.argv.length === 5) {
  const file1 = process.argv[2];
  const file2 = process.argv[3];
  const fileOut = process.argv[4];

  fs.readFile(file1, function (err, data) {
    fs.writeFile(fileOut, data, (err) => { if (err) throw err; });
    if (err) throw err;
  });

  fs.readFile(file2, function (err, data) {
    fs.appendFile(fileOut, data, (err) => { if (err) throw err; });
    if (err) throw err;
  });
}
