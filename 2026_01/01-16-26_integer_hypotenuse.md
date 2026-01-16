



# Integer Hypotenuse
## Prompt


Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2  + b2  = c2).

## My Thoughts
To approach this we find `c`. This is very standard, then we just check if it's an integer.

## Solution (Python)
```python
import math

def is_integer_hypotenuse(a, b):
	c_squared = a * a + b * b
	c = math.sqrt(c_squared)

	return c.is_integer()
```
