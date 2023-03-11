function maxTickets(tickets) {
  if (tickets.length === 0) {
    return 0;
  }

  const sorted = tickets.sort((a, b) => a - b);

  let currentLength = 1;
  let longestLength = 1;

  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] - sorted[i - 1] <= 1) {
      currentLength += 1;
      longestLength = Math.max(currentLength, longestLength);
    } else {
      currentLength = 1;
    }
  }
  return longestLength;
}
