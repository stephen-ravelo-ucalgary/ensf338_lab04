## Exercise 7

### Question 1

$\sum_{i=0}^{n - 1} n - i = {n(n+1)\over2}$

Thus, the time complexity is $O(n^2)$.

This is because after each loop it will have to travel one less element each time:

$n + (n - 1) + ... + 1$

By Gauss ${{(n + 1) + (n - 1 + 2) + ... (1 + n)}\over2}$.

Which further simplifies to ${n(n+1)\over2}$.

And finally $O({n(n+1)\over2}) = O(n^2)$

### Question 2

To optimize, we can instead iterate through the list starting from the head and do a head insertion each time instead, which should result in a time complexity of $O(n)$.