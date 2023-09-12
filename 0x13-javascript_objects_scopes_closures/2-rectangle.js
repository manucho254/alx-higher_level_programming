#!/usr/bin/node

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
}

module.exports = Rectangle;
