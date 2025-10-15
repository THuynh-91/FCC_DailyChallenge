

#  HTML Tag Stripper
## Prompt




Given a string of HTML code, remove the tags and return the plain text content.

-   The input string will contain only valid HTML.
-   HTML tags may be nested.
-   Remove the tags and any attributes.

For example,  `'<a href="#">Click here</a>'`  should return  `"Click here"`.

## My Thoughts
How this works essentially is keeping track of what are IN tags and what are not. When it is in tag we pay attention to the contents, if it's not we disregard.

## Solution (Python)
```python
def strip_tags(html:  str) -> str:
	out = []
	in_tag = False

	for ch in html:
		if ch == '<':
			in_tag = True
		elif ch == '>':
			in_tag = False
		else:
			if  not in_tag:
				out.append(ch)
	return  ''.join(out)
```

