

#  HTML Attribute Extractor
## Prompt


Given a string of a valid HTML element, return the attributes of the element using the following criteria:

-   You will only be given one element.
-   Attributes will be in the format:  `attribute="value"`.
-   Return an array of strings with each attribute property and value, separated by a comma, in this format:  `["attribute1, value1", "attribute2, value2"]`.
-   Return attributes in the order they are given.
-   If no attributes are found, return an empty array.

## My Thoughts

We’re looking for all attribute-value pairs in the form  
`attribute="value"`  
from a single valid HTML tag.

1.  Use a regex to find all matches of that pattern.
    
2.  Extract the attribute and value parts.
    
3.  Format them as `"attribute, value"`.
    
4.  Return them in order.

## Solution (Python)
```python
import re

def extract_attributes(html:  str):
	matches = re.findall(r'(\w+)="([^"]*)"', html)
	return  [f"{attr}, {val}"  for attr, val in matches]
```

