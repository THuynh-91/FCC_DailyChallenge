


# Takeoff Fuel
## Prompt


Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

-   1 gallon equals 3.78541 liters.
-   If the airplane already has enough fuel, return  `0`.
-   You can only add whole gallons.
-   Do not include decimals in the return number.

## My Thoughts
Relatively simple solution. We compare the current to the required and iterate and keep track of how many gallons are added.

## Solution (Python)
```python
def fuel_to_add(current_gallons, required_liters):
	l = 3.78541
	res = 0

	while current_gallons * l < required_liters:
		current_gallons += 1
		res += 1

	return res
```
