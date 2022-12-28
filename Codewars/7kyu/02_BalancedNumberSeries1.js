// A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

// If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

// The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.

// The task
// Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly. The passed number will always be positive.

function balancedNum(number) {
  const string = number.toString();
  const array = string.split("");
  let left = 0;
  let right = 0;

  if (array.length === 1 || array.length === 2) {
    return "Balanced";
  }

  if (array.length % 2 === 0) {
    for (let i = 0; i < array.length / 2 - 1; i++) {
      left += Number(array[i]);
    }
    for (let i = array.length - 1; i > array.length / 2; i--) {
      right += Number(array[i]);
    }
    if (left === right) {
      return "Balanced";
    } else {
      return "Not Balanced";
    }
  }

  for (let i = 0; i < Math.floor(array.length / 2); i++) {
    left += Number(array[i]);
  }
  for (let i = array.length - 1; i >= Math.ceil(array.length / 2); i--) {
    right += Number(array[i]);
  }
  if (left === right) {
    return "Balanced";
  } else {
    return "Not Balanced";
  }
}
