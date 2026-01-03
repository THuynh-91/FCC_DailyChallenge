



# Nth Fibonacci Number
## Prompt


# Nth Fibonacci Number

Given an integer  `n`, return the  `n`th number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are  `0`,  `1`,  `1`,  `2`,  `3`,  `5`,  `8`,  `13`,  `21`,  `34`.

## My Thoughts
I start the list with the first 2 beginning of the fib order. We then iterate through the number and add the previous 2 numbers in the list as we iterate.

## Solution (Python)
```python
def nth_fibonacci(n):
	lst = [0,  1]

	for i in  range(n+1):
		if i > len(lst):
			lst.append(lst[-2] + lst[-1])

	return lst[-1]
	```
