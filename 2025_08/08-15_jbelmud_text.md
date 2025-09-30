# Jbelmud Text

## Prompt
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

-   The first and last letters of the words remain in place
-   All letters between the first and last letter are sorted alphabetically.
-   The input strings will contain no punctuation, and will be entirely lowercase.

 `jbelmu("hello world")`  should return  `"hello wlord"`. <br>
  `jbelmu("i love jumbled text")`  should return  `"i love jbelmud text"`.<br>
 `jbelmu("freecodecamp is my favorite place to learn to code")` should return  `"faccdeeemorp is my faiortve pacle to laern to cdoe"`.<br>
  `jbelmu("the quick brown fox jumps over the lazy dog")`  should return  `"the qciuk borwn fox jmpus oevr the lazy dog"`.


## My Thoughts
I first decided to separate each word into a list using `split`. From that I wanted to modify each word in the list. There were some base lines we had to set first. 
We know that the first and last letter of the char had to remain in the same spot. `'ba' --> 'ba' not 'ab'`. 
Knowing that, that also means the middle char had to stay in the same spot if the end chars are locked. 
Therefore if the `len(string) < 4` we returned the original string. However if `len(string)` was greater then 4. 
I just join the end chars and the in-between with sorted. <br>

--> `mid = ''.join(sorted(i[1:-1]))`. <br>
This essentially sorts the inside into a list, then joins the list together into a string.
From that I just combined it, and appended to result.


## Solution (Python)
```python
def jbelmu(text):
	split_text = text.split()
	result = ""

	for i in split_text:
		if  len(i) < 4:
			result += "{} ".format(i)
	else:
		mid = ''.join(sorted(i[1:-1]))
		result += "{}{}{} ".format(i[0], mid, i[-1])
		
	return result.strip()
