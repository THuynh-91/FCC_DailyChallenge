


# Markdown Image Parser
## Prompt

Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format:  `"![alt text](image_url)"`. Where:

-   `alt text`  is the description of the image (the  `alt`  attribute value).
-   `image_url`  is the source URL of the image (the  `src`  attribute value).

Return a string of the HTML  `img`  tag with the  `src`  set to the image URL and the  `alt`  set to the alt text.

For example, given  `"![Cute cat](cat.png)"`  return  `'<img src="cat.png" alt="Cute cat">'`;

-   Make sure the tag, order of attributes, spacing, and quote usage is the same as above.

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.

## My Thoughts
This was a fun problem. The syntax for the input is always the same so we parse and grab the caption name first. We start by indexing through until we find the closer: `']'`. We also do the same for the link: `')'`. From that we build the string.

## Solution (Python)
```python
def parse_image(markdown):
	alt = ''
	src = ''

	idx = markdown.index('(')

	for i in markdown[2:]:
		if i == ']':
			break
		alt += i

	for i in markdown[idx + 1:]:
		if i == ')':
			break
		src += i

	return f'<img src="{src}" alt="{alt}">'


```
