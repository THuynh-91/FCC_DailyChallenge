
# Fibonacci Sequence

## Prompt

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with  `0`  and  `1`, the first 10 numbers in the sequence are  `0`,  `1`,  `1`,  `2`,  `3`,  `5`,  `8`,  `13`,  `21`,  `34`.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

-   Your function should handle sequences of any length greater than or equal to zero.
-   If the length is zero, return an empty array.
-   Note that the starting numbers are part of the sequence.

## My Thoughts
I first tackled the edge cases: if `length = 0` return an empty array. Given that the `start_sequence` was an array of 2 numbers, meaning `len(start_sequence) = 2`, we can just slice if given `length <= 2`.

From that I just made a while loop that checked the length of `seq` was less than `length`. If it was still less then length, I appended the sum of the last 2 numbers in the sequence, also incrementing the length of `seq` by 1. Then returned `seq`.


## Solution (Python)
```python
def fibonacci_sequence(start_sequence, length):
	if length == 0:
		return  []
	seq = start_sequence[:]
	
	if length <= 2:
		return seq[:length]

	while  len(seq) < length:
		seq.append(seq[-1] + seq[-2])
		
	return seq
```
