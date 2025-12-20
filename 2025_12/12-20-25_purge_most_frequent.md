


# Purge Most Frequent
## Prompt

Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

-   If multiple values are tied for most frequent, remove all of them.
-   Do not change any of the other elements or their order.

## My Thoughts
The first thing we do is count how often each value appears, meaning we have to take into account if multiple have the same most `max` frequency. From that we identify which values have that highest freq and then build the result through filtering. 

## Solution (Python)
```python
from collections import Counter
  
def purge_most_frequent(arr):
	counts = Counter(arr)
	max_freq = max(counts.values())
	to_remove = {val for val, freq in counts.items()  if freq == max_freq}

	res = []

	for item in arr:
		if item not  in to_remove:
			res.append(item)
	return res
```
