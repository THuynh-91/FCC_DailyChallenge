

#  Exoplanet Search
## Prompt

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

-   Luminosity readings only comprise of characters  `0-9`  and  `A-Z`  where each reading corresponds to the following numerical values:
-   Characters  `0-9`  correspond to luminosity levels  `0-9`.
-   Characters  `A-Z`  correspond to luminosity levels  `10-35`.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

## My Thoughts
The approach for this was this maps '0' onto 0, '9' onto 9, and 'A' onto 10. We then compute the average and check if any reading is less than the threshold.

## Solution (Python)
```python
def has_exoplanet(readings:  str) -> bool:

	if  not readings:
		return  False

	values = [int(c,  36)  for c in readings]
	avg = sum(values) / len(values)
	threshold = avg * 0.8

	return  any(v <= threshold for v in values)
```

