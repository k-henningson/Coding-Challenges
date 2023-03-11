function calculateAmount(prices) {
  if (prices.length === 0) {
    return 0;
  }
  let min = prices[0];
  let totalCost = prices[0];

  for (let i = 1; i < prices.length; i++) {
    if (prices[i] - min > 0) {
      totalCost += prices[i] - min;
    } else {
      min = prices[i];
    }
  }
  return totalCost;
}
