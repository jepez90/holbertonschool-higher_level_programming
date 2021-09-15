#!/usr/bin/node

const request = require('request');
const api = process.argv[2];

request(api, callback);

function callback (err, response, body) {
  const list = {};

  if (err) console.log(err);

  const allTodos = JSON.parse(body);
  allTodos.forEach(todo => {
    if (todo.completed) {
      list[todo.userId] += 1;
      if (isNaN(list[todo.userId])) {
        list[todo.userId] = 1;
      }
    }
  });
  console.log(list);
}
