

# Missing Numbers
## Prompt

Given an array of integers from 1 to  `n`, inclusive, return an array of all the missing integers between 1 and  `n`  (where  `n`  is the largest number in the given array).

-   The given array may be unsorted and may contain duplicates.
-   The returned array should be in ascending order.
-   If no integers are missing, return an empty array.

`find_missing_numbers([1, 3, 5])`  should return  `[2, 4]`.
    
`find_missing_numbers([1, 2, 3, 4, 5])`  should return  `[]`.
    
`find_missing_numbers([1, 10])`  should return  `[2, 3, 4, 5, 6, 7, 8, 9]`.
    
`find_missing_numbers([10, 1, 10, 1, 10, 1])`  should return  `[2, 3, 4, 5, 6, 7, 8, 9]`.
    
`find_missing_numbers([3, 1, 4, 1, 5, 9])`  should return  `[2, 6, 7, 8]`.
    
 `find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4])`  should return  `[11]`

## My Thoughts
This was surprisingly easy. Create a list of the range of the max value in the given array `1,2...max`. If the given array appeared in the range array, remove it from the range array then return it.


## Solution (Python)
```python
def find_missing_numbers(arr):
	lst = [i for i in  range(1,  max(arr))]
	for i in arr:
		if i in lst:
			lst.remove(i)
	return lst
```
