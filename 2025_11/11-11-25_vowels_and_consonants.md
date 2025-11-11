# Vowels and Consonants
## Prompt

Given a string, return an array with the number of vowels and number of consonants in the string.

-   Vowels consist of  `a`,  `e`,  `i`,  `o`,  `u`  in any case.
-   Consonants consist of all other letters in any case.
-   Ignore any non-letter characters.

For example, given  `"Hello World"`, return  `[3, 7]`.

## My Thoughts
I had fun with this and wanted to use Counter. I probably didn't need to use it. Count the number of each used character and added it to its corresponding category. 

## Solution (Python)
```python
from collections import Counter
import string

alphabet = string.ascii_lowercase

def count(s):
	char_count = Counter(s.lower())
	v = 0
	c = 0
	for i in char_count:
		if i in alphabet:
			if i in  'aeiou':
				v += char_count[i]
				print(i, char_count[i])
		else:
			print(i, char_count[i])
			c += char_count[i]
	return  [v,c]
```

