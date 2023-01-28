// There's a "3 for 2" (or "2+1" if you like) offer on mangoes.
// For a given quantity and price (per mango),
// calculate the total cost of the mangoes.

export function mango(quantity: number, price: number): number {
  let freeMango = 0;
  for (let i = quantity; i > 2; i -= 3) {
    freeMango++;
  }
  return price * (quantity - freeMango);
}
