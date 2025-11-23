


# Character Count
## Prompt


Given a sentence string, return an array with a count of each character in alphabetical order.

-   Treat upper and lowercase letters as the same letter when counting.
-   Ignore numbers, spaces, punctuation, etc.
-   Return the count and letter in the format  `"letter count"`. For instance,  `"a 3"`.
-   All returned letters should be lowercase.
-   Do not return a count of letters that are not in the given string.

## My Thoughts
Essentially you just create a new string with only alphabet characters. From that we use the Counter to grab the count of each character, then format it into the result array and have it sorted.

## Solution (Python)
```python
from collections import Counter
import string

alphabet = string.ascii_lowercase

def count_characters(sentence):
	updated = ''
	res = []

	for i in sentence.lower():
		if i in alphabet:
			updated += i

	count = Counter(updated)
	for _ in count:
		res.append(f"{_} {count[_]}")
	return  sorted(res)
```
