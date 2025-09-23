

# String Mirror
## Prompt


Given two strings, determine if the second string is a mirror of the first.

-   A string is considered a mirror if it contains the same letters in reverse order.
-   Treat uppercase and lowercase letters as distinct.
-   Ignore all non-alphabetical characters.

`is_mirror("helloworld", "helloworld")`  should return  `False`.
    
`is_mirror("Hello World", "dlroW olleH")`  should return  `True`.
    
`is_mirror("RaceCar", "raCecaR")`  should return  `True`.
    
`is_mirror("RaceCar", "RaceCar")`  should return  `False`.
    
`is_mirror("Mirror", "rorrim")`  should return  `False`.
    
`is_mirror("Hello World", "dlroW-olleH")`  should return  `True`.
    
`is_mirror("Hello World", "!dlroW !olleH")`  should return  `True`.


## My Thoughts
This was pretty simple as well. All I had to do was reverse the first string and remove the symbols, same with the second and compare them.


## Solution (Python)
```python
def is_mirror(str1, str2):
	string1 = [ch for ch in str1[::-1]  if ch.isalpha()]
	string2 = [ch for ch in str2 if ch.isalpha()]

	return  "".join(string1) == "".join(string2)

  
```
