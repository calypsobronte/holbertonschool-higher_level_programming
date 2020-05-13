#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (error, response) => {
  if (error) {
    return console.log(error);
  }
  process.stdout.write(response);
});
