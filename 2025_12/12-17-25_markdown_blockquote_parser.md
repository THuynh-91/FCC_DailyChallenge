


# Markdown Blockquote Parser
## Prompt


Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

-   Starts with zero or more spaces
-   Followed by a greater-than sign (`>`)
-   Then, one or more spaces
-   And finally, the blockquote text.

Return the blockquote text surrounded by opening and closing HTML  `blockquote`  tags.

For example, given  `"> This is a quote"`, return  `<blockquote>This is a quote</blockquote>`.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

## My Thoughts
I had a string builder of the beginning and the end `blockquote`. From that I had to make sure that there was `>` featured, then I stripped the white space following that symbol and added the beginning and end blocks to it.

## Solution (Python)
```python
def parse_blockquote(markdown):
	start = "<blockquote>"
	end = "</blockquote>"
	
	markdown = markdown.strip()

	if markdown[0] == '>':
		new_str = markdown[1:].strip()
	return f"{start}{new_str}{end}"

  

```
