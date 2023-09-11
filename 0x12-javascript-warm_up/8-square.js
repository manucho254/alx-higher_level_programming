#!/usr/bin/node
const process = require('process');

const num = process.argv[2];
const result = Number.parseInt(num);
let x, y, word;

if (Number.isInteger(result)) {
  for (x = 0; x < result; x++) {
    word = '';
    for (y = 0; y < result; y++) {
      word += 'X';
    }
    console.log(word);
  }
} else {
  console.log('Missing size');
}
