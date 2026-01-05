



# The Pressure
## Prompt


Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

-   1 bar equal 14.5038 psi.

Return an array with the following values for each tire:

-   `"Low"`  if the tire pressure is below the minimum allowed.
-   `"Good"`  if it's between the minimum and maximum allowed.
-   `"High"`  if it's above the maximum allowed.

## My Thoughts
Relatively normal problem. We convert the `range_bar` to match the psi units. We iterate through the list and check the condition or the state of each psi corresponding to the range bar and append it to the resulting list.

## Solution (Python)
```python
def tire_status(pressures_psi, range_bar):
	range_bar = [i * 14.5038  for i in range_bar]
	res = []

	for _ in pressures_psi:
		if _ < range_bar[0]:
			res.append("Low")
		elif _ > range_bar[1]:
			res.append("High")
		else:
			res.append("Good")
			
	return res
```
