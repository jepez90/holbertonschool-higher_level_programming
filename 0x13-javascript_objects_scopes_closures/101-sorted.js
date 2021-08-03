#!/usr/bin/node
const dict = require('./101-data').dict;
const response = {};
for (const key in dict) {
  const value = dict[key];
  if (response[value]) {
    response[value].push(key);
  } else {
    response[value] = [key];
  }
}
console.log(response);
