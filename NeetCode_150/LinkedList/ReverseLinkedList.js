const reverseList = function (head) {
  // head is first ListNode 1
  let prev = null;
  let curr = head;
  let next = null;

  while (curr) {
    // think of curr like Node1: {value: 1, pointer/next: NextNode in this case 2}
    // hold on to value of next for reference then break pointer
    next = curr.next;
    // pointer references previous node
    curr.next = prev;
    // move prev forward
    prev = curr;
    // move curr forward
    curr = next;
  }
  // return new head of list aka first ListNode 5
  return prev;
};

console.log(reverseList([1, 2, 3, 4, 5]));

// 1st while loop
// curr is 1
// next gets set to 2
// curr.next is null
// prev is 1
// curr is 2
