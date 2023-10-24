#!/usr/bin/node
/*
 * script that prints the title of a Star Wars
 * movie where the episode number matches a given integer.
 *    The first argument is the movie ID
 */

const request = require('request');
const process = require('process');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);

    console.log(data.title);
  }
});
