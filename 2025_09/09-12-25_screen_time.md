

# Screen Time
## Prompt
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

-   If any single day has 10 hours or more, it's too much.
-   If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
-   If the average of the seven days is greater than or equal to 6 hours, it's too much.


## My Thoughts
Just check all three cases, nothing too crazy.


## Solution (Python)
```python
def too_much_screen_time(hours):
	if  sum(hours) / len(hours) >= 6:
		return  True
	if  any(h >= 10  for h in hours):
		return  True
	if  any((a + b + c) / 3 > 8  for a, b, c in  zip(hours, hours[1:], hours[2:])):
		return  True
	return  False
```
