#!/usr/bin/node

let side = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
} else {
  let line = "";
  for (let j = 0; j < side; j++) {
    line += 'x';
  }
  for (let i = 0; i < side; i++) {
    console.log(line);
  }
}
