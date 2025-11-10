

# Extension Extractor
## Prompt
Given a string representing a filename, return the extension of the file.

-   The extension is the part of the filename that comes after the last period (`.`).
-   If the filename does not contain a period or ends with a period, return  `"none"`.
-   The extension should be returned as-is, preserving case.

## My Thoughts
Really simple. Traverse the string backwards until I hit a `"."`. Once that happens I stop printing and reverse the string. 

## Solution (Python)
```python
def get_extension(filename):
	temp = True
	res = ""

	if filename[-1] == ".":
		return  "none"
	if  "."  not  in filename:
		return  "none"

	for ch in filename[::-1]:
		if ch == ".":
			temp = False
		if temp:
			res += ch
			
	return res[::-1]
```

