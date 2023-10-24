#!/usr/bin/node
/*
 * script that prints the number of movies where
 * the character “Wedge Antilles” is present.
 *
 *   The first argument is the API URL of the
 *     Star wars API: https://swapi-api.alx-tools.com/api/films/
 *   Wedge Antilles is character ID 18 - your script
 *     must use this ID for filtering the result of the API
 */

const request = require('request');
const process = require('process');
const args = process.argv;

function checkCharacter (data) {
  let count = 0;

  for (const val in data) {
    const characters = data[val].characters;
    for (const idx in characters) {
      let character = characters[idx];

      character = character.split('/');
      const characterId = Number.parseInt(character[5]);

      if (characterId === 18) {
        count += 1;
      }
    }
  }

  return count;
}

request(args[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;

    console.log(checkCharacter(results));
  }
});
