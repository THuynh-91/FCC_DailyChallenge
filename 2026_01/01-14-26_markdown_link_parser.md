# Markdown Link Parser
## Prompt

Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.

## My Thoughts
This was a relatively fun problem. The main concept was to check the formatting of the input. From that we parse through and grab the link and the reference for that link.
Given the uniformality of the link, I probably should have done it in a way to check for edge cases. 

## Solution (Python)
```python
def parse_link(markdown):
    caption = ''
    link = ''

    for _ in markdown[1:]:
        if _ == ']':
            break
        caption += _

    idx = markdown.index(']')

    for _ in markdown[idx + 2: -1]:
        link += _
    
    return f'<a href="{link}">{caption}</a>'
```
