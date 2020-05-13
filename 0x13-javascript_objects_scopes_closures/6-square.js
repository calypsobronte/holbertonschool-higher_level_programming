#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
    charPrint (c) {
        super.print(c);
    }
};
