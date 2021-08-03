#!/usr/bin/node

if (process.argv.length <= 3){
  console.log('0');
} else {
  let arrayNumbers  = process.argv.slice(2)
  arrayNumbers  = arrayNumbers.map(function(val){return parseInt(val)});+
  arrayNumbers.sort().reverse();
  console.log(arrayNumbers[1]);
}
