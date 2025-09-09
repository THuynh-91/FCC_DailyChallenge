


# Unique Characters

## Prompt

Given a string, determine if all the characters in the string are unique.

-   Uppercase and lowercase letters should be considered different characters.

`all_unique("abc")`  should return  `True`.

`all_unique("aA")`  should return  `True`.
    
`all_unique("QwErTy123!@")`  should return  `True`.

`all_unique("~!@#$%^&*()_+")`  should return  `True`.
    
`all_unique("hello")`  should return  `False`.
    
`all_unique("freeCodeCamp")`  should return  `False`.
    
`all_unique("!@#*$%^&*()aA")`  should return  `False`.


## My Thoughts
This was quite simple. All I had to do was iterate through a string. If it was the first time I was checking that char append it to the seen list. Then if I see the char I return false, true otherwise.

## Solution (Python)
```python
def all_unique(s):
	seen = []
	for i in s:
		if i not  in seen:
			seen.append(i)
		else:
			return  False
	return  True
```
