#!/usr/bin/node

exports.converter = function (base) {
  return (function(number) {
    let b = base;
    return (number.toString(b));
  });
}
