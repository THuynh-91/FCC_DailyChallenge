


# Fwd:Fw:Count
## Prompt


Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

-   `"fw:"`
-   `"fwd:"`
-   `"re:"`

Return the total number of occurrences of these markers.

## My Thoughts
To solve this I used the regex import. First we count how many times the subject line contains the markers. From that I just lowercased everything to make it easier. We look for each marker and scan the string and count how many times they appear. 

## Solution (Python)
```python
import re

def email_chain_count(subject):
	pattern = r"(re:|fw:|fwd:)"
	return  len(re.findall(pattern, subject, re.IGNORECASE))
```
