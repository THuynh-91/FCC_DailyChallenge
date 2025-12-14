


# Capitalize It
## Prompt


Given a string title, return a new string formatted in title case using the following rules:

-   Capitalize the first letter of each word.
-   Make all other letters in each word lowercase.
-   Words are always separated by a single space.

## My Thoughts
This was relatively easy. Split the string via white space. From that we iterate putting everything in lower case, and capitalizing the first letter then add to our result. 

## Solution (Python)
```python
def title_case(title):
	lst = title.split()
	res = ''

	for i in lst:
		res += i.lower().capitalize()
		res += ' '
	return res.strip()

```
