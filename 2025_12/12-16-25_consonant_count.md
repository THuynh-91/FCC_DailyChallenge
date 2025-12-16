


# Consonant Count
## Prompt

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

-   Consonants are all alphabetic characters except  `"a"`,  `"e"`,  `"i"`,  `"o"`, and  `"u"`  in any case.
-   Ignore digits, punctuation, spaces, and other non-letter characters when counting.

## My Thoughts
I just had to follow the requirements which were to iterate through the string. Count how many consonants there were and compared to the expected.

## Solution (Python)
```python
def has_consonant_count(text, target):
	res = 0
	vowel = ['a',  'e',  'i',  'o',  'u']

	for i in text:
		if i.isalpha()  and i not  in vowel:
			res += 1

	return res == target

  

```
