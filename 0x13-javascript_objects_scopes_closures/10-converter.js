#!/usr/bin/node

// convert a number to specified base uisng closures
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
