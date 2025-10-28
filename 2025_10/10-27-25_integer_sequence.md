

#  Integer Sequence
## Prompt

Given a positive integer, return a string with all of the integers from  `1`  up to, and including, the given number, in numerical order.

For example, given  `5`, return  `"12345"`.

## My Thoughts
Really easy. I just had to go the range from 1 to the number inclusive, and add it to the string.

## Solution (Python)
```python
def sequence(n):
	res = ''
	
	for i in  range(1, n+1):
		res += str(i)
	return res
```

