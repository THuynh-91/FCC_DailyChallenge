

#  Hex to Decimal
## Prompt


Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

-   `0-9`  represent values  `0`  through  `9`.
-   `A-F`  represent values  `10`  through  `15`.

## My Thoughts
I remembered they had a built in functions regarding this and just utilized it.

## Solution (Python)
```python
def hex_to_decimal(hex):	
	return  int(hex,16)
```

