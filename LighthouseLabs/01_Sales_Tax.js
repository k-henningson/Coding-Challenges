// Given the following data, implement a function calculateSalesTax
// that calculates the total sales and total tax,
// grouped by company.

const calculateSalesTax = function (csd) {
  let result = {};
  for (let i = 0; i < csd.length; i++) {
    if (csd[i].name in result) {
      result[csd[i].name].totalSales += sumSales(csd[i].sales);
      result[csd[i].name].totalTaxes +=
        sumSales(csd[i].sales) * salesTaxRates[csd[i].province];
    } else {
      result[csd[i].name] = {
        totalSales: sumSales(csd[i].sales),
        totalTaxes: sumSales(csd[i].sales) * salesTaxRates[csd[i].province],
      };
    }
  }
  return result;
};

const sumSales = function (arr) {
  let total = 0;
  for (let i = 0; i < arr.length; i++) {
    total += arr[i];
  }
  return total;
};

const salesTaxRates = {
  AB: 0.05,
  BC: 0.12,
  SK: 0.1,
};

const companySalesData = [
  {
    name: "Telus",
    province: "BC",
    sales: [100, 200, 400],
  },
  {
    name: "Bombardier",
    province: "AB",
    sales: [80, 20, 10, 100, 90, 500],
  },
  {
    name: "Telus",
    province: "SK",
    sales: [500, 100],
  },
];

calculateSalesTax(companySalesData);

// Expected Results:
// {
//   Bombardier: {
//       totalSales: 800,
//       totalTaxes: 40
//   },
//   Telus: {
//       totalSales: 1300,
//       totalTaxes: 144
//   }
// }
