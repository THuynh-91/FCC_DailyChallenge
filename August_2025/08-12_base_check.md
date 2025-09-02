
# Base Check

## Prompt
Given a string, determine whether the number of vowels in the first half of the string equals the number of vowels in the second half.  
- Consider vowels: `a, e, i, o, u` (case-insensitive).  
- If the length is odd, ignore the middle character.  
- The string may contain any characters.Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

-   The string may contain integers, and uppercase or lowercase characters.
-   The check should be case-insensitive.
-   The base can be any number 2-36.
-   A number is valid if every character is a valid digit in the given base.
-   Example of valid digits for bases:
    -   Base 2: 0-1
    -   Base 8: 0-7
    -   Base 10: 0-9
    -   Base 16: 0-9 and A-F
    -   Base 36: 0-9 and A-Z

## My Thoughts
The first idea was to make a list of bases 2, 8, 10, 16, until I noticed base 17 and 20 in the tests. Therefore I realized I had to adapt to custom bases. The base of a number is basically the number previous of it.

- `Base2 = [0,1]`
- `Base8 = [0,1,2,3,4,5,6,7]`  

That means I can create a big base, and slice until the provided base. To do this I learned about the string import, and joined digits and the alphabet.
```python
import string
base = string.digits + string.ascii_lowercase
# 0-9 + a-z
```

All I had to do was check that each char in n was in the list of base. I decided to use the `all()` function as it returns True if all the iterations was true.

We then compare vowel counts in `left` vs `right`.

## Solution (Python)
```python
import string

def is_valid_number(n, base):
	base_36 = string.digits + string.ascii_lowercase
	is_valid_base = base_36[:base]

	return  (all(ch in is_valid_base for ch in n.lower()))
```
