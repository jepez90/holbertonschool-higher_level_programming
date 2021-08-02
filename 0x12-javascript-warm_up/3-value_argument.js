#!/usr/bin/node

let argument = process.argv[2];
if (argument) {
  console.log(argument);
} else {
  console.log("No argument");
}
