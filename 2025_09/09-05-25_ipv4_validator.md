# IPv4 Validator

## Prompt

Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (`.`). Each number must satisfy the following conditions:

-   It is between 0 and 255 inclusive.
-   It does not have leading zeros (e.g. 0 is allowed, 01 is not).
-   Only numeric characters are allowed.

`is_valid_ipv4("192.168.1.1")`  should return  `True`.
    
`is_valid_ipv4("0.0.0.0")`  should return  `True`.
    
`is_valid_ipv4("255.01.50.111")`  should return  `False`.
    
`is_valid_ipv4("255.00.50.111")`  should return  `False`.
    
`is_valid_ipv4("256.101.50.115")`  should return  `False`.
    
`is_valid_ipv4("192.168.101.")`  should return  `False`.
    
`is_valid_ipv4("192168145213")`  should return  `False`.


## My Thoughts
The first thing that came to my mind was splitting the string `split.('.')` to gather the parts. Secondly I wanted to target the cases, if there were not 4 integers in the address, it would be false. Additionally if it had a preceding 0 when it wasn't supposed to. I checked if the length of that part of the string was greater than 1, and if the value of the `str[0]` was `'0'` then it had to be false.

## Solution (Python)
```python
def is_valid_ipv4(ipv4):
	parts = (ipv4.split("."))

	if  len(parts) != 4:
		return  False

	for num in parts:
		if  len(num) == 0:
			return  False
			
		elif  len(num) > 1  and num[0] == '0':
			return  False
			
		elif  int(num) < 0  or  int(num) > 255:
		return  False
		
	return  True
```
