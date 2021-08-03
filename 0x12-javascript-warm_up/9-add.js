#!/usr/bin/node

let sum = add(process.argv[2], process.argv[3]);
console.log(sum);

function add(a, b) {
  return parseInt(a) + parseInt(b);
}
