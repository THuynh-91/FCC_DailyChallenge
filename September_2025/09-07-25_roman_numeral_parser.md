

# Roman Numeral Parser

## Prompt


Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:
-   Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.

|Symbol | Value |
| :-----:| :----:|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |


`parse_roman_numeral("III")`  should return  `3`.
    
`parse_roman_numeral("IV")`  should return  `4`.
    
`parse_roman_numeral("XXVI")`  should return  `26`.
    
 `parse_roman_numeral("XCIX")`  should return  `99`.
    
`parse_roman_numeral("CDLX")`  should return  `460`.
    
`parse_roman_numeral("DIV")`  should return  `504`.
    
`parse_roman_numeral("MMXXV")`  should return  `2025`.


## My Thoughts
This is one of those problems on how you just know how to do it, but implementing it was kind of tricky. There were a couple  specific things we had to check for. If the first value was less than the second value and placed before it would be subtracted from it. Ex: `IV ->  1|5 --> 5-1 -> 4 then VI -> 5|1 --> 5 + 1 -> 6`. This was interesting to code and overall fun to solve. 

## Solution (Python)
```python
def parse_roman_numeral(numeral):
	total = 0
	roman = {'I':1,  'V':5,  'X':10,  'L':50,  'C':100,  'D':500,  'M':1000}
	
	for index, char in  enumerate(numeral[:-1]):
		value = roman[char]
		second_value = roman[numeral[index+1]]

		if value < second_value:
			total -= value
		else:
			total += value

		total += roman[numeral[-1]]
		return total
```
