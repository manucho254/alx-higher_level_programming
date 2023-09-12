#!/usr/bin/node

const process = require('process');

/**
 * Rectangle class that defines a rectangle
 */
class Rectangle {
  /**
   * Rectangle size
   * @param {Number} w
   * @param {Number} h
   */
  constructor (w, h) {
    // only intilaize if heigt and width is greater than 0
    if ((w > 0 && h > 0)) {
      /**
       * @property {Number} width, rectangle width.
       */
      this.width = w;
      /**
       * @property {Number} height, rectangle height.
       */
      this.height = h;
    }
  }

  /**
   * print a rectangle using X
   */
  print () {
    let x, y;

    for (x = 0; x < this.height; x++) {
      for (y = 0; y < this.width; y++) {
        if (y === this.width - 1) {
          console.log('X');
        } else {
          process.stdout.write('X');
        }
      }
    }
  }
}

module.exports = Rectangle;
