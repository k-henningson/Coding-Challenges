// Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

function doubleChar(str) {
  let newStr = [];
  let split = str.split("");
  for (let i = 0; i < split.length; i++) {
    newStr.push(split[i]);
    newStr.push(split[i]);
  }
  return newStr.join("");
}

function doubleChar2(str) {
  return str
    .split("")
    .map((letter) => letter + letter)
    .join("");
}
