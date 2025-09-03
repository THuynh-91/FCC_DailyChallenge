

# Anagram Checker

## Prompt


Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

-   Ignore casing and white space.

`are_anagrams("listen", "silent")`  should return  `true`.
    
`are_anagrams("School master", "The classroom")`  should return  `true`.
    
`are_anagrams("A gentleman", "Elegant man")`  should return  `true`.
    
`are_anagrams("Hello", "World")`  should return  `false`.
    
`are_anagrams("apple", "banana")`  should return  `false`.
    
`are_anagrams("cat", "dog")`  should return  `false`.

## My Thoughts
This problem was quite easy and straightforward. I knew that to be anagrams they had to have the same characters and same number of characters. Thankfully `Counter` does that for us. I just compared the Counter of str1, and str2 and checked if they were equal. Realized I had to replace the whitespaces and did so.

## Solution (Python)
```python
from collections import Counter

def are_anagrams(str1, str2):
	str1, str2 = (_.replace(" ",  "")  for _ in  (str1,str2))
	return Counter(str1.lower()) == Counter(str2.lower())
```
