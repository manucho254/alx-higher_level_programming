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
    super();
    /**
     * @property {Number} width, Square width.
     */
    this.width = size;
    /**
     * @property {Number} height, Square width.
     */
    this.height = size;
  }
}

module.exports = Square;
