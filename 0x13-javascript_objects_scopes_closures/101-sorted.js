#!/usr/bin/node

const dict = require('./101-data').dict;

const newdict = {};
for (const key of Object.keys(dict)) {
  if (!(dict[key] in newdict)) {
    newdict[dict[key]] = [key];
  } else {
    newdict[dict[key]].push(key);
  }
}
console.log(newdict);
