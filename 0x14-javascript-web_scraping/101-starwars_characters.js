#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

axios.get(url)
  .then(response => {
    const characters = response.data.characters;

    const characterRequests = characters.map(characterUrl => {
      return axios.get(characterUrl).then(characterResponse => characterResponse.data.name);
    });

    return Promise.all(characterRequests);
  })
  .then(characterNames => {
    characterNames.forEach(name => console.log(name));
  })
  .catch(error => {
    console.error(error);
  });
