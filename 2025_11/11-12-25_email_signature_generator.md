

# Email Signature Generator
## Prompt
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

-   The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
    -   `A-I`: Use  `>>`  as the prefix.
    -   `J-R`: Use  `--`  as the prefix.
    -   `S-Z`: Use  `::`  as the prefix.
-   A comma and space (`,` ) should follow the name.
-   The title and company should follow the comma and space, separated by  `" at "`  (with spaces around it).

For example, given  `"Quinn Waverly"`,  `"Founder and CEO"`, and  `"TechCo"`  return  `"--Quinn Waverly, Founder and CEO at TechCo"`.

## My Thoughts
I checked the index of the first letter of their name to grab the prefix using the string import. I initially only checked upper until there was an edge case, so I had to resolve it. From that I just had to make the string builder to follow the correct format.

## Solution (Python)
```python
import string

alphabet = string.ascii_uppercase

def generate_signature(name, title, company):
	# Index 0-8 is >>
	# Index 9-17 os --
	# Rest is ::

	prefix_index = alphabet.index(name[0].upper())

	if prefix_index < 9:
		prefix = ">>"
	elif prefix_index < 18:
		prefix = "--"
	else:
		prefix = "::"

	return f'{prefix}{name}, {title} at {company}'
```

