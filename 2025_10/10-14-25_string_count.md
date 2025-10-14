

#  String Count
## Prompt



Given two strings, determine how many times the second string appears in the first.

-   The pattern string can overlap in the first string. For example,  `"aaa"`  contains  `"aa"`  twice. The first two  `a`'s and the second two.

## My Thoughts
This was pretty simple. I just checked the length of the pattern and the string and checked how many times it appeared in the loop.

## Solution (Python)
```python
def count(s, pattern):
	total = 0
	i = 0
	while i <= len(s) - len(pattern):
		if s[i:i+len(pattern)] == pattern:
			total += 1
		i += 1 
	return total
```

