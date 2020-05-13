#!/usr/bin/node
const fs = require('fs');

fs(process.argv[2], { json: true }, (error, response, body) => {
  if (error) { console.log(error); } else {
    const aux = {};
    for (const wars of body) {
      if (wars.completed) {
        if (aux[wars.userId]) {
          aux[wars.userId] += 1;
        } else {
          aux[wars.userId] = 1;
        }
      }
    }
    console.log(aux);
  }
});
