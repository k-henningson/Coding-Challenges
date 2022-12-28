// Create a function with two arguments that will return an array of the first n multiples of x.

// Assume both the given number and the number of times to count will be positive numbers greater than 0.

// Return the results as an array or list

function countBy(num, count) {
  let result = [];
  for (let i = 1; i <= count; i++) {
    result.push(num * i);
  }
  return result;
}
