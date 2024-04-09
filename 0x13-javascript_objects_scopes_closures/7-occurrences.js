#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurence = 0;
  list.map(myFunction);
  function myFunction (value) {
    if (value === searchElement) {
      occurence += 1;
    }
  }
  return occurence;
};
