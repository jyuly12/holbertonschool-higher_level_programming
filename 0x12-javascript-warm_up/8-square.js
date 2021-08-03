#!/usr/bin/node

const number = Number(process.argv[2]);
if (!number) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let square = '';
    for (let j = 0; j < number; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
