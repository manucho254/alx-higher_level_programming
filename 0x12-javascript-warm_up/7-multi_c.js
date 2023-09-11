#!/usr/bin/node
const process = require('process');

const num = process.argv[2];
const result = Number.parseInt(num);

if (Number.isInteger(result)) {
  let x = 0;
  while (x < result) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
