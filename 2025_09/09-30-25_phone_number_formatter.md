

# Phone Number Formatter
## Prompt



Given a string of ten digits, return the string as a phone number in this format: `"+D (DDD) DDD-DDDD"`.

`format_number("05552340182")`  should return  `"+0 (555) 234-0182"`.
    
`format_number("15554354792")`  should return  `"+1 (555) 435-4792"`


## My Thoughts
Pretty simple, I just had to format the country code, area code, and local code.

## Solution (Python)
```python
def format_number(number):
	c_code = "+"+number[0]
	a_code = f"({number[1:4]})"
	l_code = f"{number[4:7]}-{number[7:]}"
	return  " ".join([c_code, a_code, l_code])
```
