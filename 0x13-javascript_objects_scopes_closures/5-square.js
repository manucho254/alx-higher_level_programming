#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Square class, defines a Square.
 */
class Square extends Rectangle {
  /**
   * Square size
   * @param {Number} size
   */

  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
