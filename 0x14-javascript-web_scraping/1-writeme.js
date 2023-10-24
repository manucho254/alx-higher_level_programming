#!/usr/bin/node
/*
 * script that writes a string to a file.
 *
 *   The first argument is the file path
 *   The second argument is the string to write
 *   The content of the file must be written in utf-8
 *   If an error occurred during while writing,
 *   print the error object
 *
 */

const process = require('process');
const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
