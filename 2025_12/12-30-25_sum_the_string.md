


# Sum the String
## Prompt

Given a string containing digits and other characters, return the sum of all numbers in the string.

-   Treat consecutive digits as a single number. For example,  `"13"`  counts as 13, not 1 + 3.
-   Ignore any non-digit characters.

## My Thoughts
We just go through the string. We check if the current character is a digit, we then check if the following character is a digit. If we have consecutive characters as digits we multiply the first one by 10 and then add the next. 

## Solution (Python)
```python
def string_sum(s):
	total = 0
	current = 0

	for ch in s:
		if ch.isdigit():
			current = current * 10 + int(ch)
		else:
			total += current
			current = 0

	return total + current
```
