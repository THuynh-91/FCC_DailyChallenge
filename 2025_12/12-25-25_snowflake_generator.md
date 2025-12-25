


# Snowflake Generator
## Prompt


Given a multi-line string that uses newline characters (`\n`) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

-   Mirror a line by reversing all of its characters, including spaces.

For example, given  `"* \n *\n* "`, which logs to the console as:

```sh
* 
 *
* 

```

Return  `"* *\n ** \n* *"`, which logs to the console as:

```sh
*  *
 ** 
*  *

```

Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them.

## My Thoughts
We first split the string into lines. Then process each line: to do that we reverse all characters, including spaces. Concat preserves spacing perfectly and rejoin with `\n`.

## Solution (Python)
```python
def generate_snowflake(s):
	lines = s.split("\n")
	mirrored_lines = []

	for line in lines:
		mirrored_lines.append(line + line[::-1])

	return  "\n".join(mirrored_lines)

```
