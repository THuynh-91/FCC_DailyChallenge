

# 2nd Largest
## Prompt

Given an array, return the second largest distinct number.

`second_largest([1, 2, 3, 4])`  should return  `3`.
    
`second_largest([20, 139, 94, 67, 31])`  should return  `94`.
    
`second_largest([2, 3, 4, 6, 6])`  should return  `4`.
    
`second_largest([10, -17, 55.5, 44, 91, 0])`  should return  `55.5`.
    
`second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0])`  should return  `0`.


## My Thoughts
Set of an arr, removes all duplicates and return a dictionary, we then call sorted to make it a sorted list, then return the 2nd last digit.


## Solution (Python)
```python
def second_largest(arr):	
	return  sorted(set(arr))[-2]
```
