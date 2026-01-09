



# Circular Prime
## Prompt


Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example,  `197`  is a circular prime because all rotations of its digits:  `197`,  `971`, and  `719`, are prime numbers.

## My Thoughts
This was a relatively simple problem, but could have been more heavily optimized. First there is probably a faster prime checker then the current solution I have provided. Regarding checking for each prime after the rotation, we can immediately eliminate any numbers that have an even number present in the number, as it would eventually be an even number on the last index and furthermore no longer prime.

## Solution (Python)
```python
def is_circular_prime(n):
	# Checks if prime
	def isprime(num):
		if num <= 1:
			return  False

		for i in  range(2, num):
			if num % i == 0:
				return  False
		return  True

	s = str(n)
	rots = []

	# Does the rotations
	for i in  range(len(s)):
		rot = s[i:] + s[:i]
		rots.append(int(rot))

	# Checks prime for each item in rotation
	for r in rots:
		if  not isprime(r):
			return  False

	return  True
```
