#!/usr/bin/node
/*
 * script that prints all characters of a Star Wars movie:
 *
 *   The first argument is the Movie ID - example:
 *      3 = “Return of the Jedi”
 *   Display one character name by line
 */

const request = require('request');
const process = require('process');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

function getCharacter (url) {
  request(url, function (err, resp, body) {
    if (err) {
      console.log(err);
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
}

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);

    const characters = data.characters;

    characters.forEach(url => {
      getCharacter(url);
    });
  }
});
