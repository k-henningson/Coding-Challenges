// You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

function getMiddle(s) {
  let a = s.split("");
  let result = [];

  if (a.length === 1) {
    return a.join("");
  }

  if (a.length % 2 === 0) {
    const left = a[a.length / 2 - 1];
    const right = a[a.length / 2];
    result.push(left, right);
    return result.join("");
  }

  const middle = a[Math.floor(a.length / 2)];
  result.push(middle);
  return result.join("");
}
