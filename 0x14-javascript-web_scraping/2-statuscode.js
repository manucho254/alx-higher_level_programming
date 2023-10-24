#!/usr/bin/node
/*
 * script that display the status code of a GET request.
 *
 *   The first argument is the URL to request (GET)
 *   The status code must be printed like this: code: <status code>
 */

const request = require('request');
const process = require('process');
const args = process.argv;

request(args[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const code = `code: ${resp.statusCode}`;
    console.log(code);
  }
});
