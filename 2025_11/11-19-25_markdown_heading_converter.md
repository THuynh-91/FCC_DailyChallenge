

# Markdown Heading Converter
## Prompt


Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

-   Start with zero or more spaces, followed by
-   1 to 6 hash characters (`#`) in a row, then
-   At least one space. And finally,
-   The heading text.

The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an  `h1`  tag, and six hash symbols correspond to an  `h6`  tag.

If the given string doesn't have the exact format above, return  `"Invalid format"`.

For example, given  `"# My level 1 heading"`, return  `"<h1>My level 1 heading</h1>"`.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

## My Thoughts
Essentially it was just a lot of restrictions we had to do. First strip the str then count the hashes and make sure the formatting was correct. 

## Solution (Python)
```python
def convert(s:  str) -> str:	
	trimmed = s.lstrip()
	i = 0
	
	while i < len(trimmed)  and trimmed[i] == '#':
		i += 1
		if i == 0  or i > 6:
			return  "Invalid format"

	if i >= len(trimmed)  or trimmed[i] != ' ':
		return  "Invalid format"

	text = trimmed[i+1:].lstrip()
	if  not text:
		return  "Invalid format"

	level = i
	return f"<h{level}>{text}</h{level}>"
```

