#!/usr/bin/node
const fs = require('request');
fs.get('http://swapi.co/api/films/' + process.argv[2] + '/', function (error, response, body) {
  if (error) throw error;
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
