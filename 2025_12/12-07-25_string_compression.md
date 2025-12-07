


#  String Compression
## Prompt

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

-   Only consecutive duplicates are compressed.
-   Words are separated by single spaces.

For example, given  `"yes yes yes please"`, return  `"yes(3) please"`.
## My Thoughts
First thing you do is split the string into words. You then iterate through the words and count consecutive duplicates.  Essentially `current` is the word you're counting. `Count` is how many times in a row. `Result` is the list of compressed pieces. Whenever the word changes, append either `word` if count = 1. `word(count)` if count > 1.

## Solution (Python)
```python
def compress_string(s):
	words = s.split()
	result = []

	current = words[0]
	count = 1

	for w in words[1:]:
		if w == current:
			count += 1
		else:
			if count == 1:
				result.append(current)
		else:
			result.append(f"{current}({count})")

		current = w
		count = 1

	if count == 1:
		result.append(current)
	else:
		result.append(f"{current}({count})")
	return  " ".join(result)
```
