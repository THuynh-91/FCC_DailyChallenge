

# Decimal to Binary
## Prompt


Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits  `0`  and  `1`  to represent any number. To convert a decimal number to binary, repeatedly divide the number by  `2`  and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert  `12`  to binary:


## My Thoughts
Really easy, use the built in conversion.

## Solution (Python)
```python
def to_binary(decimal):
	return  bin(decimal)[2:]
```

