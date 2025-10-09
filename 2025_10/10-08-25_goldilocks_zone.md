

#  Goldilocks Zone
## Prompt


For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

1.  Find the luminosity of the star by raising its mass to the power of 3.5.
2.  The start of the zone is 0.95 times the square root of its luminosity.
3.  The end of the zone is 1.37 times the square root of its luminosity.

-   Return the distances rounded to two decimal places.

For example, given  `1`  as a mass, return  `[0.95, 1.37]`.

## My Thoughts
I just had to do what was asked of me. At first I did it without rounding and tried to fstring the result. However that probably had a return type they didn't want, therefore I just rounded in the initial calculations.

## Solution (Python)
```python
def goldilocks_zone(mass):
	lum = mass ** 3.5
	start = round(0.95 * (lum ** 0.5),  2)
	end = round(1.37 * (lum ** 0.5),  2)

	return  [start, end]
```

