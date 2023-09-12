#!/usr/bin/node

/**
 * script that concats 2 files.
 * - The first argument is the file path of the first source file
 * - The second argument is the file path of the second source file
 * - The third argument is the file path of the destination
 */

const process = require('process');
const fs = require('fs');

// array of commandline arguments
const args = process.argv;

fs.readFile(args[2], (err, data) => {
  if (err) throw err;
  fs.writeFile(args[4], data.toString(), (err) => {
    if (err) throw err;
  });
});

fs.readFile(args[3], (err, data) => {
  if (err) throw err;
  fs.appendFile(args[4], data.toString(), (err) => {
    if (err) throw err;
  });
});
