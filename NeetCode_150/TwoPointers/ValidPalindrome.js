// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.

const isPalindrome = function (s) {
  const regexPattern = /[^A-Za-z0-9]/g;
  const newStr = s.toLowerCase().replace(regexPattern, "");
  let reversedStr = "";
  for (let i = newStr.length - 1; i >= 0; i--) {
    reversedStr += newStr[i];
  }
  if (newStr === reversedStr) {
    return true;
  }
  return false;
};
