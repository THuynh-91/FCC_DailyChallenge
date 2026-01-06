



# vOwElcAsE
## Prompt

Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

-   Vowels are  `"a"`,  `"e"`,  `"i"`,  `"o"`, and  `"u"`  in any case.
-   Non-alphabetical characters should remain unchanged.

## My Thoughts
I was originally going to have a set to map out the vowels, but to make the code a bit shorter, I decided to iterate through the list and check if the current value of the index is a vowel. If it was return the capital version, and append, then return the lowercase version for everything else.

## Solution (Python)
```python
def vowel_case(s):
	vowel = 'aeiou'
	res = ''
	
	for i in s:
		if i.lower()  in vowel:
			res += i.upper()
		else:
			res += i.lower()

	return res
```
