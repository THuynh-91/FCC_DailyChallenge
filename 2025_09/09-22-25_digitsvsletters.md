

# Digits vs Letters
## Prompt

Given a string, return  `"digits"`  if the string has more digits than letters,  `"letters"`  if it has more letters than digits, and  `"tie"`  if it has the same amount of digits and letters.

-   Digits consist of  `0-9`.
-   Letters consist of  `a-z`  in upper or lower case.
-   Ignore any other characters.


## My Thoughts
This was relatively simple, I just had a counter and returned the state of that counter.


## Solution (Python)
```python
import string

def digits_or_letters(s):
letters = string.ascii_letters
digits = string.digits
count = 0

for ch in s:
	if ch in letters:
		count += 1
	if ch in digits:
		count -= 1
if count > 0:
	return  "letters"
elif count < 0:
	return  "digits"
else:
	return  "tie"

  
```
