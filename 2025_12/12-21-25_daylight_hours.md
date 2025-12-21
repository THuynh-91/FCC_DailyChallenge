


# Daylight Hours
## Prompt


December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

## My Thoughts
We find the distance from a table latitude, then we find the key with the smallest distance. Handles negative values, ties, and edge cases as well.

## Solution (Python)
```python
def daylight_hours(latitude):

	table = {
		-90:  24,
		-75:  23,
		-60:  21,
		-45:  15,
		-30:  13,
		-15:  12,
		0:  12,
		15:  11,
		30:  10,
		45:  9,
		60:  6,
		75:  2,
		90:  0
	}

	closest_lat = min(table.keys(), key=lambda x:  abs(latitude - x))
	return table[closest_lat]
```
