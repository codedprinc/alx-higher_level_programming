#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
	    let p = '';
	    for (let j = 0; j < this.width; j++) {
        p += 'X';
	    }
	    console.log(p);
    }
  }
}

module.exports = Rectangle;
