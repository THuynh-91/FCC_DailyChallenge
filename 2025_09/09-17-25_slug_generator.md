

# Slug Generator
## Prompt



Given a string, return a URL-friendly version of the string using the following constraints:

-   All letters should be lowercase.
-   All characters that are not letters, numbers, or spaces should be removed.
-   All spaces should be replaced with the URL-encoded space code  `%20`.
-   Consecutive spaces should be replaced with a single  `%20`.
-   The returned string should not have leading or trailing  `%20`.

`generate_slug("helloWorld")`  should return  `"helloworld"`.
    
`generate_slug("hello world!")`  should return  `"hello%20world"`.
    
`generate_slug(" hello-world ")`  should return  `"helloworld"`.
    
`generate_slug("hello world")`  should return  `"hello%20world"`.
    
`generate_slug(" ?H^3-1*1]0! W[0%R#1]D ")`  should return  `"h3110%20w0r1d"`.

## My Thoughts
This was fun, because I have been working with regex. Anyways to do this I made it similar to alphanumeric: `alnum()`. However we also needed to preserve spaces, so I modify it to do so. Additionally we then make multiple spaces into just one. Then replace the single space with "%20". 


## Solution (Python)
```python
import re

def generate_slug(str_word):
	cleaned_text = re.sub(r'[^a-zA-Z0-9 ]',  '', str_word.strip().lower())
	cleaned_text = re.sub(r'\s+',  ' ', cleaned_text)
	result = cleaned_text.replace(" ",  "%20")
	return result
```
