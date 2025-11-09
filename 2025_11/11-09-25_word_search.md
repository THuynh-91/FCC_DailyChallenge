

# Word Search
## Prompt


Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

-   The given matrix will be filled with all lowercase letters (`a-z`).
-   The word to find will always be in the matrix exactly once.
-   The word to find will always be in a straight line in one of these directions:
    -   left to right
    -   right to left
    -   top to bottom
    -   bottom to top

For example, given the matrix:

```md
[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]

```

And the word  `"cat"`, return:

```md
[[0, 1], [2, 1]]

```

Where  `[0, 1]`  are the indices for the  `"c"`  (start of the word), and  `[2, 1]`  are the indices for the  `"t"`  (end of the word).

## My Thoughts
This was a very interesting problem. The solution was to scan every cell and then when it matches the FIRST letter of the word, we then try all directions. If all the letters match and stay in bounds, return the start and computed end coordinates.

## Solution (Python)
```python
def find_word(matrix, word):
	R, C = len(matrix),  len(matrix[0])
	L = len(word)
	directions = [(0,  1),  (0,  -1),  (1,  0),  (-1,  0)]

	for r in  range(R):
		for c in  range(C):
			if matrix[r][c] != word[0]:
				continue

	  

			for dr, dc in directions:
				er, ec = r + dr * (L - 1), c + dc * (L - 1)
				# End point must be within bounds
				if  not  (0 <= er < R and  0 <= ec < C):
					continue
					
				ok = True

				for k in  range(L):
					rr, cc = r + dr * k, c + dc * k
						if matrix[rr][cc] != word[k]:
							ok = False
							break

				if ok:
					return  [[r, c],  [er, ec]]
```

