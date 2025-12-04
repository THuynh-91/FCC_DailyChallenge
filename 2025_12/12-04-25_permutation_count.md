


#  Permutation Count
## Prompt


Given a string, return the number of distinct permutations that can be formed from its characters.

-   A permutation is any reordering of the characters in the string.
-   Do not count duplicate permutations.
-   If the string contains repeated characters, repeated arrangements should only be counted once.
-   The string will contain only letters (`A-Z`,  `a-z`).

For example, given  `"abb"`, return  `3`  because there's three unique ways to arrange the letters:  `"abb"`,  `"bab"`, and  `"bba"`.
## My Thoughts
The first step was to understand the problem which was needing the # of **distinct permutations** of a string. If all characters were unique it would be the factorial of len(string). However if there were repeated characters that would mean some permutations were duplicate and we had to divide out the duplicates.

The formula to solve this would have been:
n! / (count of each repeated letter)!

We then just implement that.

## Solution (Python)
```python
from math import factorial
from collections import Counter

def count_permutations(s):
	n = len(s)
	freq = Counter(s)
	denom = 1
	for count in freq.values():
		denom *= factorial(count)

	return factorial(n) // denom
```
