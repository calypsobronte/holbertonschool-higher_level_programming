#!/usr/bin/node

const fs = require('request');

fs(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + response.statusCode);
});
