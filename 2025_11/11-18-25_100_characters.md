

# 100 Characters
## Prompt

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
    -   The number of differing characters does not exceed 10% of the fingerprint length.

## My Thoughts
Essentially I floor divide by the length then I just attached the remainder on top of it.

## Solution (Python)
```python
def one_hundred(chars):
	x = len(chars)
	div = 100 // x
	res = chars * div
	
	if  len(res) != 100:
		rem = 100 - len(res)
		res += chars[:rem]
	return res
```

