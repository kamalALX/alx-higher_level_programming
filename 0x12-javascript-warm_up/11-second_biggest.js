#!/usr/bin/node

const arr = process.argv.slice(2).map(Number);

if (arr.length === 0 || arr.length === 1) {
  console.log('0');
} else {
  let max = arr[0];
  let secondMax = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > max) {
      secondMax = max;
      max = arr[i];
    } else if (arr[i] < max && arr[i] > secondMax) {
      secondMax = arr[i];
    }
  }
  console.log(secondMax);
}
