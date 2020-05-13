#!/usr/bin/node
const fs = require('request');

fs('https://swapi-api.hbtn.io/api/films/' + process.argv.slice(2)[0], function (error, body) {
  if (JSON.parse(body.body).title !== undefined) {
    console.log(JSON.parse(body.body).title);
    return;
  }
  console.log(error);
});
