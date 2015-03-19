## cc (Part 4)

Finally, `cc` will require three different base cases:

1. If `amount` is exactly zero, count that as one way to make change.

2. If `amount` is less than zero, count that as zero ways to make change.

3. If `kinds-of-coins` is zero, count that as zero ways to make change.

The complete algorithm is given on the next page. Convince yourself that it
works.

