



# Sorted Array?
## Prompt

Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

-   In ascending order (lowest to highest), return  `"Ascending"`.
-   In descending order (highest to lowest), return  `"Descending"`.
-   Not sorted in ascending or descending order, return  `"Not sorted"`.

## My Thoughts
The key idea is to check ascending. Every element must be less then the next element. Additionally we also have to check ascending. Otherwise it's not sorted. To do this we had 2 checkers `ascending` and `descending`. If those booleans were deemed false we moved on.

## Solution (Python)
```python
def is_sorted(arr):
	ascending = True
	descending = True

	for i in  range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			ascending = False
		if arr[i] < arr[i + 1]:
			descending = False
			
	if ascending:
		return  "Ascending"
	if descending:
		return  "Descending"
	return  "Not sorted"
```
