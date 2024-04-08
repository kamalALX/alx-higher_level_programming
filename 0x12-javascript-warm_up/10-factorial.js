#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  } else if (a <= 1) {
    return (1);
  }

  return (factorial(a - 1) * a);
}

const arg = parseInt(process.argv[2]);

console.log(factorial(arg));
