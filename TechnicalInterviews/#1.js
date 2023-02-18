// You are analyzing data for Aquaintly, a hot new social network.

// On Aquaintly, connections are always symmetrical.
// If a user Alice is connected to Bob, then Bob is also connected to Alice.

// You are given a sequential log of CONNECT and DISCONNECT
// events of the following form:

// - This event connects users Alice and Bob:
// ["CONNECT", "Alice", "Bob"]
// - This event disconnects the same users:
// ["DISCONNECT", "Bob", "Alice"] (order of users does not matter)

// We want to separate users based on their popularity
// (number of connections). To do this, write a function
// that takes in the event log and a number N and returns
// two collections:
// [Users with less than N connections], [Users with N or
//   more connections]

// grouping(events, 3) => [["Alice", "Charlie", "Pam", "Nicole"], ["Dennis", "Bob", "Edward"]]
// grouping(events, 1) => [[], ["Alice", "Charlie", "Dennis", "Bob", "Pam", "Edward", "Nicole"]]
// grouping(events, 10) => [["Alice", "Charlie", "Dennis", "Bob", "Pam", "Edward", "Nicole"], []]

const events = [
  ["CONNECT", "Alice", "Bob"],
  ["DISCONNECT", "Bob", "Alice"],
  ["CONNECT", "Alice", "Charlie"],
  ["CONNECT", "Dennis", "Bob"],
  ["CONNECT", "Pam", "Dennis"],
  ["DISCONNECT", "Pam", "Dennis"],
  ["CONNECT", "Pam", "Dennis"],
  ["CONNECT", "Edward", "Bob"],
  ["CONNECT", "Dennis", "Charlie"],
  ["CONNECT", "Alice", "Nicole"],
  ["CONNECT", "Pam", "Edward"],
  ["DISCONNECT", "Dennis", "Charlie"],
  ["CONNECT", "Dennis", "Edward"],
  ["CONNECT", "Charlie", "Bob"],
];

const friendsCount = function (events, number) {
  let obj = {};
  let lessThan = [];
  let moreThan = [];
  for (let i = 0; i < events.length; i++) {
    if (events[i][0] === "CONNECT") {
      if (!obj[events[i][1]]) {
        obj[events[i][1]] = 1;
      }
      if (!obj[events[i][2]]) {
        obj[events[i][2]] = 1;
      } else {
        obj[events[i][1]] += 1;
        obj[events[i][2]] += 1;
      }
    }
    if (events[i][0] === "DISCONNECT") {
      if (!obj[events[i][1]] || !obj[events[i][2]]) obj[events[i][1]] -= 1;
      obj[events[i][2]] -= 1;
    }
  }

  for (const person in obj) {
    if (obj[person] >= number) {
      moreThan.push(person);
    }
    if (obj[person] < number) {
      lessThan.push(person);
    }
  }
  return [lessThan, moreThan];
};

console.log(friendsCount(events, 3));
