#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOccurences = 0;

  if (list.length === 0) {
    return numOccurences;
  }

  list.forEach(item => {
    if (item === searchElement) numOccurences += 1;
  });

  return numOccurences;
};
