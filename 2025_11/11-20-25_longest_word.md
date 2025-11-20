


# Longest Word
## Prompt

Given a sentence string, return the longest word in the sentence.

-   Words are separated by a single space.
-   Only letters (`a-z`, case-insensitive) count toward the word's length.
-   If there are multiple words with the same length, return the first one that appears.
-   Return the word as it appears in the given string, with punctuation removed.

## My Thoughts
I just had to remove the symbols and keep the spacing then just returned the max lenth word in the list.

## Solution (Python)
```python
def longest_word(sentence):
	res = ""

	for i in sentence:
		if i.isalpha()  or i == " ":
		res += i
		
	res = res.split()
	return  max(res, key = len)
```
