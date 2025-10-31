

#  Nth Prime
## Prompt


A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are  `2`,  `3`,  `5`,  `7`, and  `11`.

Given a positive integer  `n`, return the  `n`th prime number. For example, given  `5`  return the 5th prime number:  `11`.

## My Thoughts
I first had `isPrime` that checked if a number was prime or not. I then had a while loop that would keep track on what nth term prime we had. If the count was a prime I would iterate the nth term by 1 until we got to the desired nth term.

## Solution (Python)
```python
def nth_prime(n):
	track = 0
	count = 0
	res = 0

	while track < n+1:
		if isPrime(count):
			track += 1
			res = count
			count += 1
	return res

def isPrime(num):
	if num < 2:
		return  False
	if num == 2:
		return  True

	for i in  range(3, num):
		if num % i == 0:
			return  False
	return  True
```

