


# Camel to Snake
## Prompt


Given a string in camel case, return the snake case version of the string using the following rules:

-   The input string will contain only letters (`A-Z`  and  `a-z`) and will always start with a lowercase letter.
-   Every uppercase letter in the camel case string starts a new word.
-   Convert all letters to lowercase.
-   Separate words with an underscore (`_`).
    

If the given sentence meets any of the rules above, return  `"AI"`, otherwise, return  `"Human"`.
## My Thoughts
If there is a capital, place an underscore but and append the rest. 

## Solution (Python)
```python
def to_snake(camel):
	res = ''
	for i in camel:
		if i.isupper():
			res += "_"
		res += i.lower()
		
	return res
```
