



# Markdown Italic Parser
## Prompt
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

-   Italic text in Markdown is any text that starts and ends with a single asterisk (`*`) or a single underscore (`_`).
-   There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
-   Convert all italic occurrences to HTML  `i`  tags and return the string.

For example, given  `"*This is italic*"`, return  `"<i>This is italic</i>"`.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

## My Thoughts
I could have done this with the regex import, but I wanted to do it without. It took a lot more code but essentially we just check the beginning if they had `*` or `_`. We check the closing marker is the same as the beginning marker and no space at the end.

## Solution (Python)
```python
def parse_italics(s):
	result = []
	i = 0

	while i < len(s):
		char = s[i]
		if char in  "*_":
			marker = char
			j = i + 1

			if j < len(s)  and s[j] != " ":
				while j < len(s)  and s[j] != marker:
					j += 1

				if j < len(s):
					if s[j - 1] != " ":
						content = s[i + 1  : j]
						result.append(f"<i>{content}</i>")
						i = j + 1
						continue
						
		result.append(char)
		i += 1

	return  "".join(result)
```
