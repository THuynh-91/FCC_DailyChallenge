
# Markdown Inline Code Parser
## Prompt
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.

Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.

Return the given string with all code blocks converted to HTML code tags.

For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

## My Thoughts
The strategy to this approach we set the `in_code` to False. We parse through the string and check the current status of `in_code` and substitute appropriately.

## Solution (Python)
```python
def parse_inline_code(text):
    result = []
    in_code = False

    for ch in text:
        if ch == "`":
            if in_code:
                result.append("</code>")
            else:
                result.append("<code>")
            in_code = not in_code
        else:
            result.append(ch)

    return "".join(result)

```
