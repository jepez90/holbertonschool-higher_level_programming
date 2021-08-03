#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if ((w * h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    let line = '';
    for (let j = 0; j < this.width; j++) {
      line += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate() {
    const oldWidth = this.width;
    this.width = this.height;
    this.height = oldWidth;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
};
