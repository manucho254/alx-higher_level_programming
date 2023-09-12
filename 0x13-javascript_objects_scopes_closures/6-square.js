#!/usr/bin/node

const parentSquare = require('./5-square');
const process = require('process');

/**
 * Square class, defines a Square.
 */
class Square extends parentSquare {
  /**
   * print rectangle using character c
   */
  charPrint (c) {
    let symbol = c;
    let x, y;

    if (c === undefined) {
      symbol = 'X';
    }

    for (x = 0; x < this.height; x++) {
      for (y = 0; y < this.width; y++) {
        if (y === this.width - 1) {
          console.log(symbol);
        } else {
          process.stdout.write(symbol);
        }
      }
    }
  }
}

module.exports = Square;
