// You will be given an array and a limit value. You must check that all values in
// the array are below or equal to the limit value. If they are, return true. Else, return false.

// You can assume all values in the array are numbers.

export function smallEnough(arr: number[], limit: number): boolean {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] <= limit) {
      continue;
    } else {
      return false;
    }
  }
  return true;
}
