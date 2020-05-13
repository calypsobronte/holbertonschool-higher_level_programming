#!/usr/bin/node
let aux = 0;
exports.logMe = (item) => {
  console.log(aux + ': ' + item);
  aux++;
};
