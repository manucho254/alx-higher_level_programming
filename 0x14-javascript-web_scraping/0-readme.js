#!/usr/bin/node
/*
 * script that reads and prints the content of a file.
 *
 *  The first argument is the file path.
 *  The content of the file must be read in utf-8
 *  If an error occurred during the reading,
 *  print the error object.
 */

const process = require('process');
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
