// In this little assignment you are given a string of space separated numbers,
// and have to return the highest and lowest number.

function highAndLow(numbers) {
  let result = [];
  const array = numbers.split(" ");
  let lowest = +array[0];
  let highest = +array[0];
  for (let i = 0; i < array.length; i++) {
    if (array[i] < lowest) {
      lowest = +array[i];
    }
    if (array[i] > highest) {
      highest = +array[i];
    }
  }
  result.push(highest, lowest);
  return result.join(" ");
}
