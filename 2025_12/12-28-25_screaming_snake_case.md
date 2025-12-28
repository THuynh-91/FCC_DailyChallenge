


# SCREAMING_SNAKE_CASE
## Prompt

Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

-   `camelCase`
-   `PascalCase`
-   `snake_case`
-   `kebab-case`

In the above formats, words are separated by an underscore (`_`), a hyphen (`-`), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

-   Make all letters uppercase
-   Separate words with an underscore (`_`)

## My Thoughts
This was a tricky solution, but in the end it just ended up breaking each test cases and addressing them individually.

## Solution (Python)
```python
def to_screaming_snake_case(variable_name):
	res = []
	if  '-'  in variable_name:
		res = variable_name.split('-')

	if  '_'  in variable_name:
		res = variable_name.split('_')

	temp = ''

	# Checks if a capital letter exist
	if  any(c.isupper()  for c in variable_name):
		for i in variable_name:
			if i.isupper():
				res.append(temp)
					temp = ''
				temp += i
		res.append(temp)

	if  not res:
		return variable_name.upper()

	# Filters res, removing empty string and upper everything
	upper_lst = [item.upper()  for item in res if item != '']

	return  "_".join(upper_lst).strip()
```
