// Given a valid (IPv4) IP address, return a defanged
// version of that IP address.

// A defanged IP address replaces every period "." with "[.]".

// Input: address = "1.1.1.1"
// Output: "1[.]1[.]1[.]1"

const defangIPaddr = function (address) {
  let result = "";
  for (let i = 0; i < address.length; i++) {
    if (address[i] === ".") {
      result += "[.]";
    } else {
      result += address[i];
    }
  }
  return result;
};
