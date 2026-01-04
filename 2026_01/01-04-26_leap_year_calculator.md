



# Leap Year Calculator
## Prompt


Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

-   The year is evenly divisible by 4, and
-   The year is not evenly divisible by 100, unless
-   The year is evenly divisible by 400.

## My Thoughts
Nothing too complicated with this, I just had to have a condition for each case.


## Solution (Python)
```python
def is_leap_year(year):
	if year % 400 == 0:
		return  True

	if year % 100 == 0:
		return  False
		
	return year % 4 == 0
```
