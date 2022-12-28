// Your job is to figure out the index of which vowel is missing from a given string:

// A has an index of 0,
// E has an index of 1,
// I has an index of 2,
// O has an index of 3,
// U has an index of 4.
// Notes: There is no need for string validation and every sentence given will contain all vowels but one.
// Also, you won't need to worry about capitals.

function absentVowel(x) {
  const array = x.split("");
  if (!array.includes("a")) {
    return 0;
  }
  if (!array.includes("e")) {
    return 1;
  }
  if (!array.includes("i")) {
    return 2;
  }
  if (!array.includes("o")) {
    return 3;
  } else {
    return 4;
  }
}
