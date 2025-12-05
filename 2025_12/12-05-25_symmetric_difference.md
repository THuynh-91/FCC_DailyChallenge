


#  Symmetric Difference
## Prompt

Given two arrays, return a new array containing the symmetric difference of them.

-   The symmetric difference between two sets is the set of values that appear in either set, but not both.
-   Return the values in the order they first appear in the input arrays.
## My Thoughts
I had two for loops. In the first loop I checked whatever was unique in arr1 and added it to `res`. In the second loop I checked whatever was unique in arr2 and added it to `res`.

## Solution (Python)
```python
def difference(arr1, arr2):
	res = []
	for i in arr1:
		if i not  in arr2:
			res.append(i)
	for i in arr2:
		if i not  in arr1:
			res.append(i)

	return res
```
