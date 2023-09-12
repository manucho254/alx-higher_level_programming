#!/usr/bin/node

// script that imports an array and computes a new array.
const list = require('./100-data').list;

const newArr = list.map((item, index) => {
  const newVal = item * index;
  return newVal;
});

console.log(list);
console.log(newArr);
