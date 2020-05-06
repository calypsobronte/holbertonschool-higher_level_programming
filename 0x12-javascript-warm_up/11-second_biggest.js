#!/usr/bin/node
if (process.argv.length === 3 || process.argv.length === 2) {
  console.log(0);
} else {
  const second = process.argv.slice(2).sort(function (a, b) { return a - b; });
  console.log(second[second.length - 2]);
}
