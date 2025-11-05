

#  Matrix Builder
## Prompt
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (`0`) of the given size.

For example, given  `2`  and  `3`, return:

```json
[
  [0, 0, 0],
  [0, 0, 0]
]
```
-   Return the images in the same order they appear in the input array.

## My Thoughts
Really simple, I append empty arrays depending on how many rows there should be in the matrix. From that I fill those rows with the length of the columns. 

## Solution (Python)
```python
def build_matrix(rows, cols):
	res = []

	for i in  range(rows):
		res.append([])

	for i in res:
		for j in  range(cols):
			i.append(0)
	return res
```

