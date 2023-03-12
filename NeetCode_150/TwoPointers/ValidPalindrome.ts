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

function isPalindrome2(str: string): boolean {
  const regex = /[^A-Za-z0-9]/g;
  const newStr = str.toLowerCase().replace(regex, "");
  let left = 0;
  let right = newStr.length - 1;

  let lChar: string;
  let rChar: string;

  while (left < right) {
    lChar = newStr[left];
    rChar = newStr[right];

    if (lChar === rChar) {
      left++;
      right--;
    } else {
      return false;
    }
  }
  return true;
}
