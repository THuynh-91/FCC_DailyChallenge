

# Perfect Square
## Prompt



Given an integer, determine if it is a perfect square.

-   A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.

`is_perfect_square(9)`  should return  `True`.
    
`is_perfect_square(49)`  should return  `True`.
    
`is_perfect_square(1)`  should return  `True`.
    
`is_perfect_square(2)`  should return  `False`.
    
`is_perfect_square(99)`  should return  `False`.
    
`is_perfect_square(-9)`  should return  `False`.
    
`is_perfect_square(0)`  should return  `True`.
    
`is_perfect_square(25281)`  should return  `True`.


## My Thoughts
I was thinking about using the math import for sqrt, however I remember it was the same as power to the `1/2`. Then I just made the root an int, and if the square of that didn't match `n` then it wasn't the right solution. I also made a check to make sure the given was a positive number.


## Solution (Python)
```python
def is_perfect_square(n):
	if n < 0:
		return  False
	root = int(n ** 0.5)
	return root * root == n

  
```
