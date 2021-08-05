#!/usr/bin/node

const list = require('./100-data.js').list;
const newmap = list.map((item, index) => item * index);

console.log(list);
console.log(newmap);
