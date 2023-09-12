#!/usr/bin/node

// Module to reverve a list
exports.esrever = function (list) {
  if (list.length === 0) return list;

  let len = list.length - 1;
  const mid = Number.parseInt(len / 2);
  let x;

  for (x = 0; x <= mid; x++) {
    const tmp = list[len];

    list[len] = list[x];
    list[x] = tmp;
    len -= 1;
  }

  return list;
};
