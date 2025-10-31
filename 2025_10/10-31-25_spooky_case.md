

#  SpOoKy~CaSe
## Prompt



Given a string representing a variable name, convert it to "spooky case" using the following constraints:

-   Replace all underscores (`_`), and hyphens (`-`) with a tilde (`~`).
-   Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.

For example, given  `hello_world`, return  `HeLlO~wOrLd`.

## My Thoughts
I really enjoyed this problem. How I approached it was by mapping the replacements using replace. I had use a dict to do that. Following that I had an indicator telling me if it should be a capitalize char or not. Went through the list and done so accordingly. I was initially going to enumerate and only capitalize evenly, but then it wouldn't have been at the correct index with the symbols.

## Solution (Python)
```python
def spookify(boo):
	replace = {"_":"~",  "-":"~"}
	res = ""
	cap = True

	for old, new in replace.items():
		boo = boo.replace(old, new)

	for ch in boo:
		if  not ch.isalpha():
			res += ch

		elif ch.isalpha()  and cap:
			res += ch.upper()
			cap = False
		else:
			res += ch.lower()
			cap = True
	return res

```

