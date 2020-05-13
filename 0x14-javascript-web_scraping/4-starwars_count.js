#!/usr/bin/node
const fs = require('request');
let aux = 0;

fs(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  for (const wars of JSON.parse(body).results) {
    aux += wars.characters.filter(each => each.search('/18/') > 0).length;
  }
  console.log(aux);
});
