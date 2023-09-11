#!/usr/bin/node
const process = require('process');

const num = process.argv[2];
const result = Number.parseInt(num);

// recursive to culculate factorial
function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (Number.isInteger(result)) {
  console.log(factorial(result));
} else {
  console.log('1');
}
