#!/usr/bin/node
/*
 * Script that computes the number of tasks completed by user id.
 *
 *   The first argument is the API URL:
 *        https://jsonplaceholder.typicode.com/todos
 *   Only print users with completed task
 */

const request = require('request');
const process = require('process');
const args = process.argv;

request(args[2], function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const dict = {};

    for (const val of Object.values(data)) {
      if (val.completed === true) {
        const keys = Object.keys(dict);
        const userId = val.userId.toString();

        if (keys.includes(userId)) {
          dict[val.userId] += 1;
        } else {
          dict[val.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
