#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  let arrayNumbers = process.argv.slice(2);
  arrayNumbers = arrayNumbers.sort((a, b) => { return a - b });
  console.log(arrayNumbers.reverse()[1]);
}
