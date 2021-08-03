#!/usr/bin/node

const fs = require('fs');
let str1 = "";
if (process.argv.length === 5) {
  let file1 = process.argv[2];
  let file2 = process.argv[3];
  let fileOut = process.argv[4];

  fs.readFile(file1, function (err, data) {
    fs.writeFile(fileOut, data, (err) => { return; });
  });

  fs.readFile(file2, function (err, data) {
    fs.appendFile(fileOut, data, (err) => { return; });
  });

}
