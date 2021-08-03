#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    const b = base;
    return (number.toString(b));
  };
};
