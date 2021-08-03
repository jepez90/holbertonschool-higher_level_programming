#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(element => {
    if (searchElement === element) {
      counter++;
    }
  });
  return (counter);
};
