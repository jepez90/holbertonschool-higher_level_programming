#!/usr/bin/node
const dict = require('./101-data').dict;
let response = {};
for (key in dict) {
  let value = dict[key];
  if (response[value]) {
    response[value].push(key);
  } else {
    response[value] = [key];
  }
}
console.log(response);
