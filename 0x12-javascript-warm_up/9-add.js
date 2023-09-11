#!/usr/bin/node
const process = require('process');

const a = process.argv[2];
const b = process.argv[3];
const numA = Number.parseInt(a);
const numB = Number.parseInt(b);

// function to add two integers
function add (a, b) {
  return a + b;
}

console.log(add(numA, numB));
