#!/usr/bin/node
/*
 * script that prints all characters of a Star Wars movie:
 *
 *   The first argument is the Movie ID - example:
 *      3 = “Return of the Jedi”
 *   Display one character name by line in the
 *   same order of the list “characters” in the /films/ response
 */

const request = require('request');
const process = require('process');
const args = process.argv;
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;

/*
 * function sends a GET request to a single URL
 * and returns a Promise that resolves
 * with the URL and the response body.
 */
function getCharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      if (err) {
        reject(err);
      } else {
        resolve({ url, body });
      }
    });
  });
}

/*
 * we create an array of Promises, one for each URL,
 * by calling the getCharacter function.
 */
function sendGetRequests (urls) {
  const promises = [];

  for (const url of urls) {
    promises.push(getCharacter(url));
  }

  /* Promise.all to wait for all the requests to complete.
   * This ensures that the responses are in the
   * same order as the URLs in the input array.
  */
  return Promise.all(promises);
}

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    sendGetRequests(characters)
      .then(responses => {
        for (const response of responses) {
          const data = JSON.parse(response.body);
          console.log(data.name);
        }
      }).catch(err => {
        console.log(err);
      });
  }
});
