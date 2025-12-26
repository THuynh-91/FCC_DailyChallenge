


# Sum of Divisors
## Prompt

Given a positive integer, return the sum of all its divisors.

-   A divisor is any integer that divides the number evenly (the remainder is  `0`).
-   Only count each divisor once.

For example, given  `6`, return  `12`  because the divisors of  `6`  are  `1`,  `2`,  `3`, and  `6`, and the sum of those is  `12`.

## My Thoughts
This just goes through all the possible divisors of n by iterating through. We use the modulo operator to check if it does equate to 0 and therefore being a divisor then append it to a list. We grab the sum of the list and return it.

## Solution (Python)
```python
def sum_divisors(n):
	div = []

	for i in  range  (1, n+1):
		if n % i == 0:
			div.append(i)
	return  sum(div)

```
