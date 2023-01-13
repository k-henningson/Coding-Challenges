// The main idea is to count all the occurring characters in a string.
// If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

// What if the string is empty? Then the result should be empty object literal, {}.

function count(string) {
  let result = {};
  const array = string.split("");
  for (let i = 0; i < array.length; i++) {
    if (!result[array[i]]) {
      result[array[i]] = 1;
    } else {
      result[array[i]] += 1;
    }
  }
  return result;
}
