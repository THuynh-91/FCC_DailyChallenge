

# Array Shift
## Prompt

Given an array and an integer representing how many positions to shift the array, return the shifted array.

-   A positive integer shifts the array to the left.
-   A negative integer shifts the array to the right.
-   The shift wraps around the array.

For example, given  `[1, 2, 3]`  and  `1`, shift the array 1 to the left, returning  `[2, 3, 1]`.

## My Thoughts
I just had to normalize the array then return the corrected shifts.

## Solution (Python)
```python
def shift_array(arr, n):
	k = len(arr)
	if k == 0:
		return arr
	n %= k
	return arr[n:] + arr[:n]
```

