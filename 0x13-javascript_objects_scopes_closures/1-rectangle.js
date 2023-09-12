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

module.exports = Rectangle;
