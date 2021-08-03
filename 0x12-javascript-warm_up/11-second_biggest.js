#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const number = process.argv.slice(2);
  number.sort((a, b) => b - a);
  console.log(number[1]);
}
