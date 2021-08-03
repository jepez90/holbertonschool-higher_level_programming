#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w * h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';
    for (let j = 0; j < this.width; j++) {
      line += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
};
