#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const userTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (!userTasks[todo.userId]) {
          userTasks[todo.userId] = 0;
        }
        userTasks[todo.userId]++;
      }
    });

    console.log(userTasks);
  }
});
