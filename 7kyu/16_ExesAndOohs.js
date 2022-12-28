// Check to see if a string has the same amount of 'x's and 'o's.
// The method must return a boolean and be case insensitive.
// The string can contain any char.

function XO(str) {
  const x = str.match(/x/gi);
  const o = str.match(/o/gi);

  if (!x && !o) {
    return true;
  }
  if (!x || !o) {
    return false;
  }
  return x.length === o.length;
}
