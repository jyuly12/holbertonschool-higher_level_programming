#!/usr/bin/node

const Base = require('./5-square');

class Square extends Base {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
