



# Plant the Crop
## Prompt

Given an integer representing the size of your farm field, and  `"acres"`  or  `"hectares"`  representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

-   1 acre equals 4046.86 square meters.
-   1 hectare equals 10,000 square meters.

Here's a list of crops that will be given as input and how much space a single plant takes:

Crop

Space per plant

`"corn"`

1 square meter

`"wheat"`

0.1 square meters

`"soybeans"`

0.5 square meters

`"tomatoes"`

0.25 square meters

`"lettuce"`

0.2 square meters

Return the number of plants that fit in the field, rounded down to the nearest whole plant.

## My Thoughts
We are given the field size, unit and crop type. We just need to convert the field size into square meters. We check how much space one plant occupies and compute.

## Solution (Python)
```python
import math

def get_number_of_plants(size, unit, crop):
	
	if unit == "acres":
		area = size * 4046.86
	else:
		area = size * 10000

	crop_space = {
		"corn":  1,
		"wheat":  0.1,
		"soybeans":  0.5,
		"tomatoes":  0.25,
		"lettuce":  0.2
	}

	return math.floor(area / crop_space[crop])
```
