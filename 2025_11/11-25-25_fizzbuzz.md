


# FizzBuzz
## Prompt


Given an integer (`n`), return an array of integers from  `1`  to  `n`  (inclusive), replacing numbers that are multiple of:

-   3 with  `"Fizz"`.
-   5 with  `"Buzz"`.
-   3 and 5 with  `"FizzBuzz"`.

## My Thoughts
Pretty simple, fulfil the categories and update x as we go along. 

## Solution (Python)
```python
def fizz_buzz(n):

	res = []

	for i in  range(1, n + 1):
		x = ''
		if i % 3 == 0:
			x = "Fizz"
		if i % 5 == 0:
			x = "Buzz"
		if i % 3 == 0  and i % 5 == 0:
			x = "FizzBuzz"

	if x:
		res.append(x)
	else:
		res.append(i)

	return res
```
