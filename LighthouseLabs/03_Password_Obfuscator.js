// Our program should define a function named obfuscate.
// This function should take a string as an argument and obfuscate it by applying the following rules:

// Every "a" in the string should be replaced with a "4".
// Every "e" in the string should be replaced with a "3".
// Every "o" (oh) in the string should be replaced with a "0" (zero).
// Every "l" (el) in the string should be replaced with a "1" (one).
// Do not use any built-in functions like String.prototype.replace that
// do all the work of scanning through the string for you. => but I did anyways for practice :) 

const obfuscate1 = function (str) {
  return str
    .split("")
    .map((i) => {
      if (i === "a") return "4";
      if (i === "e") return "3";
      if (i === "o") return "0";
      if (i === "l") return "1";
      return i;
    })
    .join("");
};

const obfuscate2 = function (str) {
  return str
    .replaceAll(/a/gi, "4")
    .replaceAll(/e/gi, "3")
    .replaceAll(/o/gi, "0")
    .replaceAll(/l/gi, "1");
};

obfuscate1("password");
obfuscate2("abracadabra");
obfuscate2("audaciously");
