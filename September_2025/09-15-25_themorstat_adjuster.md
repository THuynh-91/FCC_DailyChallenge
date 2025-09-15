

# Thermostat Adjuster
## Prompt

Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

-   Return "heat" if the current temperature is below the target.
-   Return "cool" if the current temperature is above the target.
-   Return "hold" if the current temperature is equal to the target.

## My Thoughts
Super easy, just check all 3 conditions.


## Solution (Python)
```python
def adjust_thermostat(temp, target):
	if temp < target:
		return  "heat"
	elif temp > target:
		return  "cool"
	else:
		return  "hold"
```
