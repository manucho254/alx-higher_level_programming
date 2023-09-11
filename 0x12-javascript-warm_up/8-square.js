#!/usr/bin/node
const process = require('process');

const num = process.argv[2];
const result = Number.parseInt(num);

// function that print result times
function printX () {
  for (let y = 0; y < result; y++) {
    if (y === result - 1) {
      console.log('x');
    } else {
      process.stdout.write('x');
    }
  }
}

if (Number.isInteger(result)) {
  for (let x = 0; x < result; x++) {
    printX();
  }
} else {
  console.log('Missing size');
}
