#!/usr/bin/node
const process = require('process');

const num = process.argv[2];
const result = Number.parseInt(num);

if (Number.isInteger(result)) {
  console.log('My number: ' + result);
} else {
  console.log('Not a number');
}
