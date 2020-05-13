#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => list.filter(list_ => list_ === searchElement).length;
