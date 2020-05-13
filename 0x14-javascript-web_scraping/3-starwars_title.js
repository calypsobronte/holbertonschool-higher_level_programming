#!/usr/bin/node

const request = require('request');
const api_file = 'https://swapi-api.hbtn.io/api/films/';

request(api_file + process.argv[2], (error, response, body) => {
  if (error === null) {
    const resp = JSON.parse(body);
    console.log(resp.title);
  }
  if (error) {
    console.log(error);
  }
});
