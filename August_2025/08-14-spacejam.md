
# SPACEJAM

## Prompt

Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).<br>
 `space_jam("freeCodeCamp")`  should return  `"F R E E C O D E C A M P"`<br>
 `space_jam(" free Code Camp ")`  should return  `"F R E E C O D E C A M P"`.<br>
 `space_jam("Hello World?!")`  should return  `"H E L L O W O R L D ? !"`.<br>
 `space_jam("C@t$ & D0g$")`  should return  `"C @ T $ & D 0 G $"`.<br>
 `space_jam("allyourbase")`  should return  `"A L L Y O U R B A S E"`.<br>


## My Thoughts
This challenge was relatively simple and easy. I broke it down as: given a string, add `"  "` in between every character. Then uppercase the whole string. I didn't complicate it further then that and removed all `' '` in a string. From that I turned `"Hello World" --> "HelloWorld"`. From that I iterated through each char and added `"  "` to an empty string. Then returned uppercase version, and removed any trailing white spaces. 


## Solution (Python)
```python
def space_jam(s):
	strip_str = s.replace(" ",  "")
	empty_str = ""

	for i in strip_str:
		empty_str += i + " "
		
	return empty_str.upper().strip()
```
