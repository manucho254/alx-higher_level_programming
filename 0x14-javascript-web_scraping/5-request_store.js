#!/usr/bin/node
/*
 * script that gets the contents of a webpage and stores it in a file.
 *
 *  The first argument is the URL to request
 *  The second argument the file path to store the body response
 *  The file must be UTF-8 encoded
 */

const request = require('request');
const process = require('process');
const fs = require('fs');
const args = process.argv;

request(args[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    // create and add response data to file
    fs.writeFile(args[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
