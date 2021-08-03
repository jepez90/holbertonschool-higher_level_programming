#!/usr/bin/node

let number = parseInt(process.argv[2]);
console.log(factorial(number));

function factorial(number) {
  if (isNaN(number) | number === 1) {
    return (1);
  }
  return (number * factorial(number - 1));
}
