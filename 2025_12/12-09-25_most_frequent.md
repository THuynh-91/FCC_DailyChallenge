


# Most Frequent
## Prompt

Given an array of elements, return the element that appears most frequently.

-   There will always be a single most frequent element.
## My Thoughts
I just had to use the collections import to retrieve the most common item. 

## Solution (Python)
```python
from collections import Counter

def most_frequent(arr):
	counts = Counter(arr)
	most_freq = counts.most_common(1)
	return most_freq[0][0]

```
