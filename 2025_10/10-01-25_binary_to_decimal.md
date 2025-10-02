# Binary to Decimal
## Prompt

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits  `0`  and  `1`  to represent any number. To convert binary to decimal, multiply each digit by a power of  `2`  and add them together. Start by multiplying the rightmost digit by  `2^0`, the next digit to the left by  `2^1`, and so on. Once all digits have been multiplied by a power of  `2`, add the result together.

For example, the binary number  `101`  equals  `5`  in decimal because:


## My Thoughts
Really easy, use the built in conversion.

## Solution (Python)
```python
def to_decimal(binary):
	return  int(binary,2)
```

## Oher Solution (Python)
```python
def to_decimal(binary):
	total = 0
	for i,v in enumerate(lst_str):
		if v == "0":
		  continue
		else:
		  total += 2 ** int(i)
		return total
```
