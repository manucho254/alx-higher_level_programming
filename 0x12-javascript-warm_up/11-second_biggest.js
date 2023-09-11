#!/usr/bin/node
const process = require('process');

if (process.argv.length < 4) {
  console.log('0');
  process.exit();
}

const numArr = [];
const args = process.argv;
const length = args.length;

for (let x = 2; x < length; x++) {
  const num = Number.parseInt(args[x]);

  if (Number.isInteger(num)) {
    numArr.push(num);
  }
}

// function that find the largest in integer in an array.
function findMax (arr) {
  let max = 0;

  numArr.forEach(item => {
    if (item > max) {
      max = item;
    }
  });

  return max;
}

const maxVal = findMax(numArr);

numArr.splice(numArr.indexOf(maxVal), 1); // remove max value from array
console.log(findMax(numArr)); // print new max value
