

# Spam Detector
## Prompt

Given a phone number in the format  `"+A (BBB) CCC-DDDD"`, where each letter represents a digit as follows:

-   `A`  represents the country code and can be any number of digits.
-   `BBB`  represents the area code and will always be three digits.
-   `CCC`  and  `DDDD`  represent the local number and will always be three and four digits long, respectively.

Determine if it's a spam number based on the following criteria:

-   The country code is greater than 2 digits long or doesn't begin with a zero (`0`).
-   The area code is greater than 900 or less than 200.
-   The sum of first three digits of the local number appears within last four digits of the local number.
-   The number has the same digit four or more times in a row (ignoring the formatting characters).

`is_spam("+0 (200) 234-0182")`  should return  `False`.
    
`is_spam("+091 (555) 309-1922")`  should return  `True`.
    
 `is_spam("+1 (555) 435-4792")`  should return  `True`.
    
`is_spam("+0 (955) 234-4364")`  should return  `True`.
    
`is_spam("+0 (155) 131-6943")`  should return  `True`.
    
`is_spam("+0 (555) 135-0192")`  should return  `True`.
    
`is_spam("+0 (555) 564-1987")`  should return  `True`.
    
`is_spam("+00 (555) 234-0182")`  should return  `False`.


## My Thoughts
This was a bit of a more challenging problem. The first task at hand was finding a way to separate the formatting into what we had wanted. I was able to split it into the 3 most important `country code`, `area code`, and `local number` with the split function. From there on I just had to undo the formatting a bit, and split the `local number` in two separate parts. Additionally I had to check if a digit was repeated 4 times consecutively. From there on I just had to check all the cases of a spam number.

## Solution (Python)
```python
def four_in_a_row(num_str):
	count = 1
	for i in  range(1,  len(num_str)):
		if num_str[i] == num_str[i-1]:
			count += 1
			if count >= 4:
				return  True
		else:
			count = 1
	return  False

def is_spam(number):
	c_code, a_code, l_num = (number[1:].split())
	a_code = a_code[1:-1]
	l_num1, l_num2 = l_num.split("-")
	x = sum(int(i)  for i in l_num1)

	num = ""
	for digit in number:
		if digit.isdigit():
			num += digit
	if  len(c_code) > 2  or c_code[0] != "0":
		return  True

	if  int(a_code) > 900  or  int(a_code) < 200:
		return  True
	if  str(x)  in l_num2:
		return  True
	if four_in_a_row(num):
		return  True

	return  False

```
