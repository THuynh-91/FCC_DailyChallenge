


# Pairwise
## Prompt


Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given  `[2, 3, 4, 6, 8]`  and  `10`, you will find two valid pairs:

-   `2`  and  `8`  (2 + 8 = 10), whose indices are  `0`  and  `4`
-   `4`  and  `6`  (4 + 6 = 10), whose indices are  `2`  and  `3`

Add all the indices together to get a return value of  `9`.

## My Thoughts
For this challenge we had to find the pair of values that add up to the target. We know that each element can only be used at most once. When we find a valid pair, we add the indices to a running total. We loop over the array and during that we loop again with the index j > i. This avoids duplicates and reusing the same index. If i and j == target, we add i+j, mark both indices as used and break.

## Solution (Python)
```python
def pairwise(arr, target):
	used = set()
	total = 0

	for i in  range(len(arr)):
		if i in used:
			continue

	for j in  range(i + 1,  len(arr)):
		if j in used:
			continue

		if arr[i] + arr[j] == target:
			total += i + j
			used.add(i)
			used.add(j)
			break
			
	return total
```
