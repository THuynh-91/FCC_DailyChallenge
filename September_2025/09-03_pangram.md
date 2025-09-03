

# Base Check

## Prompt

Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

-   Ignore non-alphabetical characters in the word or sentence.
-   Ignore letter casing in the word or sentence.
  
  `is_pangram("hello", "helo")`  should return  `True`
    
`is_pangram("hello", "hel")`  should return  `False`<br>
    
 `is_pangram("hello", "helow")`  should return  `False`<br>
    
`is_pangram("hello world", "helowrd")`  should return  `True`<br>
    
 `is_pangram("Hello World!", "helowrd")`  should return  `True`<br>
    
`is_pangram("Hello World!", "heliowrd")`  should return  `False`<br>
    
`is_pangram("freeCodeCamp", "frcdmp")`  should return  `False`<br>
    
`is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz")`  should return  `True`

## My Thoughts
The first thought was to remove from `letters` onto `sentence`. This is where I used replace. Additionally I realized I had to take into account, what if `letters` had a char not in `sentence` that's when I created my first conditional to check if all the letters provided are in the sentence. Secondly, I realized that if the string contains a symbol it could still be true only if no other alphabetical chars, that is why I checked if it was not alpha.
```python
"!".isalpha() --> False
not "!".isalpha() --> True #What we are trying to check
```

## Solution (Python)
```python
def is_pangram(sentence, letters):
	str = sentence.lower()
	lett = letters.lower()

	for ch in lett:
		if ch not  in  str:
			return  False
		else:
			str = str.replace(ch,  "")
	return  not  str.strip().isalpha()
```
